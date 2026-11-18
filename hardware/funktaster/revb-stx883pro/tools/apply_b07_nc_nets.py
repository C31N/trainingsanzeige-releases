#!/usr/bin/env python3
"""B0.7: give seven explicit no-connect pads KiCad's one-pad pseudo-net names.
Never changes copper geometry. NO FABRICATION RELEASE.
"""
from pathlib import Path
import json,re,sys
root=Path(sys.argv[1]).resolve()
k=root/"kicad"
nc=[("U1","2"),("U1","3"),("U2","3"),("U2","4"),("U3","3"),("U3","4"),("U4","3")]
def endblock(s,start):
    depth=0;quoted=False;escaped=False
    for i in range(start,len(s)):
        ch=s[i]
        if quoted:
            if escaped:escaped=False
            elif ch=="\\":escaped=True
            elif ch=='"':quoted=False
        elif ch=='"':quoted=True
        elif ch=="(":depth+=1
        elif ch==")":
            depth-=1
            if depth==0:return i+1
    raise ValueError("unclosed S-expression")
report={}
for file in sorted(k.glob("*.kicad_pcb")):
    src=file.read_text()
    first=src.find("(footprint ")
    existing={int(i):n for i,n in re.findall(r'\(net\s+(\d+)\s+"([^"]*)"\)',src[:first])}
    assert max(existing)==24,(file,max(existing))
    names={(ref,p):(25+i,f"unconnected-({ref}-Pad{p})") for i,(ref,p) in enumerate(nc)}
    blocks=[];cursor=0;attached=[]
    while True:
        start=src.find("(footprint ",cursor)
        if start<0:
            blocks.append(src[cursor:]);break
        blocks.append(src[cursor:start])
        stop=endblock(src,start)
        chunk=src[start:stop]
        m=re.search(r'\(property "Reference" "([A-Z]+\d+)"',chunk)
        assert m, file
        ref=m.group(1)
        for r,p in nc:
            if r!=ref:continue
            at=chunk.find(f'(pad "{p}"')
            assert at>=0,(file,r,p)
            j=endblock(chunk,at)
            pad=chunk[at:j]
            assert "(net " not in pad,(file,r,p)
            number,name=names[(r,p)]
            chunk=chunk[:at]+pad[:-1]+f' (net {number} "{name}"))'+chunk[j:]
            attached.append((r,p))
        blocks.append(chunk)
        cursor=stop
    assert sorted(attached)==sorted(nc)
    dst="".join(blocks)
    insert=dst.find("(footprint ")
    declarations="\n".join(f'  (net {i} "{n}")' for i,n in names.values())+"\n"
    dst=dst[:insert]+declarations+dst[insert:]
    for kind in ("segment","via","zone"):
        assert dst.count("("+kind+" ")==src.count("("+kind+" "),kind
    file.write_text(dst)
    report[file.name]={"added_nc_nets":len(nc),"pads":len(attached),"segments_unchanged":src.count("(segment ")}
meta_file=root/"design.json";meta=json.loads(meta_file.read_text())
meta["revision"]="B0.7-NC-NET-PARITY-EXPERIMENT"
meta["status"]="NATIVE_KICAD_DRC_ERC_PARITY_PENDING_NO_FABRICATION"
meta_file.write_text(json.dumps(meta,indent=2,ensure_ascii=False))
(root/"validation"/"B07_NC_NETS.json").write_text(json.dumps(report,indent=2))
with (root/"README.md").open("a") as f:
    f.write("\n\n## B0.7 NC-pin parity correction\n"
            "Seven unconnected pads assigned individual schematic pseudo-nets. "
            "No physical copper modified. Native KiCad DRC/ERC/parity is mandatory. "
            "NO FABRICATION RELEASE.\n")
print(json.dumps(report,indent=2))
