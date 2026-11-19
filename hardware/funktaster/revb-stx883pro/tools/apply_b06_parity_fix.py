#!/usr/bin/env python3
"""Rev B0.6: match local KiCad schematic net names with PCB nets; fix H1/H2 BOM.
Does not reroute copper. Experimental only, no fabrication release.
"""
from pathlib import Path
import json
import re
import sys
root = Path(sys.argv[1]).resolve()
lib = root / "kicad"
nets = set(json.loads((root / "design.json").read_text())["nets"])
assert len(nets) >= 15
net_re = re.compile(r'(\(net\s+\d+\s+")([^"\n]+)("\))')
zone_re = re.compile(r'(\(net_name\s+")([^"\n]+)("\))')
report = {}
for path in sorted(lib.glob("*.kicad_pcb")):
    original = path.read_text()
    counts = [0, 0]
    def modify(m, index):
        name = m.group(2)
        if name in nets:
            counts[index] += 1
            return m.group(1)+"/"+name+m.group(3)
        if name.startswith("/") and name[1:] in nets:
            return m.group(0)
        raise ValueError(f"{path}: unrecognized net {name}")
    edited = net_re.sub(lambda m: modify(m, 0), original)
    edited = zone_re.sub(lambda m: modify(m, 1), edited)
    assert counts[0] >= len(nets), (path, counts)
    assert {m.group(2) for m in net_re.finditer(edited)} == {"/"+n for n in nets}
    # Confirm every changed byte is ONLY a leading slash added to a net name.
    assert edited.replace('"/', '"') == original, path
    path.write_text(edited)
    report[path.name] = dict(net_rewrites=counts[0], zone_rewrites=counts[1])
for filename in ["buzzer-revb-stx883pro.kicad_sch", "WFD-RevB.kicad_sym"]:
    path = lib / filename
    text = original = path.read_text()
    for ref in ("H1", "H2"):
        if filename.endswith(".kicad_sch"):
            regexes = [
                r'(\(symbol\s+\"WFD-RevB:'+ref+r'\"\s+\(pin_names\s+\(offset\s+0\.5\)\)\s+\(in_bom\s+)yes(\))',
                r'(\(symbol\s+\(lib_id\s+\"WFD-RevB:'+ref+r'\"\)\(at\s+[^)]*\)\(unit\s+1\)\(in_bom\s+)yes(\))'
            ]
        else:
            regexes = [r'(\(symbol\s+\"'+ref+r'\"\s+\(pin_names\s+\(offset\s+0\.5\)\)\s+\(in_bom\s+)yes(\))']
        for pat in regexes:
            text,n = re.subn(pat,r'\g<1>no\2',text)
            assert n == 1, (filename, ref, n)
    assert text != original
    path.write_text(text)
    report[filename] = "H1/H2 BOM-excluded"
meta_path = root / "design.json"
meta = json.loads(meta_path.read_text())
meta["revision"] = "B0.6-NETPARITY-EXPERIMENT"
meta["status"] = "NATIVE_KICAD_DRC_ERC_PARITY_PENDING_NO_FABRICATION"
meta_path.write_text(json.dumps(meta,indent=2,ensure_ascii=False))
validation = root / "validation"
validation.mkdir(exist_ok=True)
(validation/"B06_NETPARITY_PATCH.json").write_text(json.dumps(report,indent=2))
with (root/"README.md").open("a") as f:
    f.write("\n\n## Rev B0.6 net/schematic parity\n"
            "All PCB local nets carry the root-sheet / prefix, matching the schematic. "
            "H1/H2 excluded from BOM in schematic and library. "
            "Copper unchanged. Independent KiCad ERC/DRC/parity pending. "
            "NO FABRICATION RELEASE.\n")
print(json.dumps(report,indent=2))
