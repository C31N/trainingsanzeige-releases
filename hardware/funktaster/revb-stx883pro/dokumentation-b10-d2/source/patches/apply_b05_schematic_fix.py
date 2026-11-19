#!/usr/bin/env python3
"""B0.5: fix overlapping schematic cells and include two mounting-hole symbols.
Do not change PCB copper. Not a fabrication release.
"""
from pathlib import Path
import json
import subprocess
import sys

root = Path(sys.argv[1]).resolve()
source = root / "make_design.py"
code = source.read_text(encoding="utf-8")
overlap = "    if y>270:x=31.75+(ix%6)*63.50;y=25.40+(ix//6)*25.40"
assert overlap in code, "Expected B0.4 schematic wrap not found"
code = code.replace(overlap,
                    "    # A2 page: all 40 electrical symbols fit on a 4x10 grid; do not wrap.")
no_mount = "    if not p['pins']:continue"
assert no_mount in code, "Expected omitted mounting symbols not found"
code = code.replace(no_mount,
                    "    # Include H1/H2 no-pin schematic symbols for footprint parity.")
source.write_text(code, encoding="utf-8")
kicad = root / "kicad"
copper = {p.name:p.read_bytes() for p in kicad.glob("*ROUTED*pcb")}
subprocess.run([sys.executable,str(source)],cwd=root,check=True)
for name,original in copper.items():
    assert (kicad/name).read_bytes() == original, f"Copper modified: {name}"
meta_file = root / "design.json"
meta = json.loads(meta_file.read_text())
meta.update(revision="B0.5-SCHEMATIC-PARITY-EXPERIMENT",
            status="NATIVE_KICAD_ERC_DRC_REVALIDATION_PENDING_NO_FABRICATION")
meta_file.write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
with (root / "README.md").open("a",encoding="utf-8") as f:
    f.write("\n\n## B0.5 schematic parity correction\n"
            "Remove overlap of schematic symbol groups: 4x10 unique A2 cells. "
            "Include H1/H2 symbols for footprint parity. Copper routing unchanged. "
            "Native KiCad ERC/DRC pending; NOT FABRICATION APPROVED.\n")
print("B0.5 schematic regenerated; existing copper preserved.")
