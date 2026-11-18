#!/usr/bin/env python3
"""B0.8 experiment: correct U5 bottom-pad pitch per NiceRF Rev1.1 drawing.
No certified JLC landpattern or RF impedance; NO FABRICATION.
"""
from pathlib import Path
import json,re,sys,uuid
root=Path(sys.argv[1]).resolve()
k=root/"kicad"
p=k/"WFD-RevB.pretty"/"STX883PRO.kicad_mod"
s=p.read_text()
def move(s,pin,old,new):
    pat=r'(\(pad "'+pin+r'" smd roundrect \(at )'+re.escape(old)+r'( 7\.1\))'
    edited,n=re.subn(pat,r'\g<1>'+new+r'\2',s)
    assert n==1,(pin,old,n)
    return edited
p.write_text(move(move(s,"1","-4.25","-2.54"),"3","4.25","2.54"))
def end_sexp(s,i):
    quote=False;esc=False;dep=0
    for j in range(i,len(s)):
        ch=s[j]
        if quote:
            if esc:esc=False
            elif ch=="\\":esc=True
            elif ch=='"':quote=False
        elif ch=='"':quote=True
        elif ch=="(":dep+=1
        elif ch==")":
            dep-=1
            if dep==0:return j+1
    raise ValueError("unclosed footprint")
for name in ("buzzer-revb-stx883pro-PLACEMENT-ONLY.kicad_pcb",
             "buzzer-revb-stx883pro-ROUTED-V3-EXPERIMENT.kicad_pcb"):
    path=k/name
    src=path.read_text()
    at=src.index('(footprint "WFD-RevB:STX883PRO"')
    end=end_sexp(src,at)
    block=src[at:end]
    block=move(move(block,"1","-4.25","-2.54"),"3","4.25","2.54")
    out=src[:at]+block+src[end:]
    if "ROUTED-V3" in name:
        net=re.search(r'\(net (\d+) "/RF_DATA"\)',out)
        assert net and net.group(1)=="19"
        assert '(start 19.2500 19.6000) (end 19.5000 20.0000)' in out
        uid=str(uuid.uuid5(uuid.NAMESPACE_URL,"wfd:revb:b08:stx883pro:RF_DATA:newPad3ToOldEscape"))
        track=(f'\n(segment (start 17.5400 19.6000) (end 19.2500 19.6000) '
               f'(width 0.25) (layer F.Cu) (net {net.group(1)}) (uuid "{uid}"))\n')
        assert uid not in out
        out=out.rstrip()[:-1]+track+')\n'
    path.write_text(out)
genfile=root/"make_design.py"
gen=genfile.read_text()
for old,new in (
 ("smd_pad(1,-4.25,7.1,1.7,2.5)","smd_pad(1,-2.54,7.1,1.7,2.5)"),
 ("smd_pad(3,4.25,7.1,1.7,2.5)","smd_pad(3,2.54,7.1,1.7,2.5)")):
    assert old in gen
    gen=gen.replace(old,new)
genfile.write_text(gen)
for name in ("buzzer-revb-stx883pro-ROUTED-EXPERIMENT.kicad_pcb",
             "buzzer-revb-stx883pro-ROUTED-V2-EXPERIMENT.kicad_pcb"):
    (k/name).unlink(missing_ok=True)
meta=root/"design.json"
data=json.loads(meta.read_text())
data["revision"]="B0.8-STX883PRO-PAD-PITCH-EXPERIMENT"
data["status"]="NATIVE_KICAD_PENDING_RF_LANDPATTERN_UNVERIFIED_NO_FABRICATION"
meta.write_text(json.dumps(data,indent=2,ensure_ascii=False))
(root/"validation"/"B08_RF_FOOTPRINT_PATCH.json").write_text(json.dumps(
 {"source":"NiceRF STX883PRO Rev 1.1 mechanical diagram","new_pitch_mm":2.54,
  "pad_refs":["U5.1","U5.3"],"rf_data_escape_added_mm":1.71,
  "manufacturer_landpattern_verified":False,"fab_release":False},indent=2))
with (root/"README.md").open("a") as f:
    f.write("\n\n## B0.8 mechanical experiment\n"
            "U5 bottom-pad centers adjusted to 2.54-mm pitch per manufacturer diagram; "
            "RF_DATA 1.71-mm trace completes pad3 connection. "
            "JLC footprint, 50-ohm RF trace and actual hardware remain unverified. "
            "NO FABRICATION RELEASE.\n")
print("B0.8 pad pitch corrected as experiment, no fabrication release")
