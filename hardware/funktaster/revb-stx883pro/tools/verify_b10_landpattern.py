#!/usr/bin/env python3
"""Read-only independent KiCad pad comparison with the saved official library."""
import hashlib
import json
import re
import sys
from pathlib import Path

board_path = Path(sys.argv[1])
source = Path(__file__).resolve().parents[1]/'validation/b10-footprint/C3001517_EasyEDA_Official_Library.json'
library=json.loads(source.read_text(encoding='utf-8'))
tokens=re.findall(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+',board_path.read_text(encoding='utf-8'))
stack=[]; root=[]; cursor=root
for token in tokens:
    if token=='(':
        child=[]; cursor.append(child); stack.append(cursor); cursor=child
    elif token==')': cursor=stack.pop()
    else: cursor.append(json.loads(token) if token.startswith('"') else token)
assert not stack
footprint=next(x for x in root[0] if isinstance(x,list) and x[:2]==['footprint','WFD-RevB:STX883PRO'])
pads={x[1]:x for x in footprint if isinstance(x,list) and x[0]=='pad'}
def field(items,key):
    return next(x[1:] for x in items if isinstance(x,list) and x[0]==key)
reference={f[8]:list(map(float,f[2:6])) for f in
           [s.split('~') for s in library['shape'] if s.startswith('PAD~')]}
assert set(pads)==set(reference)=={'1','2','3','4'}
anchor=list(map(float,field(pads['2'],'at')[:2]))
origin=reference['2']; nets={'1':'/GND','2':'/TX3V3','3':'/RF_DATA','4':'/ANT'}
rows=[]
for pin,pad in sorted(pads.items()):
    at=list(map(float,field(pad,'at')[:2])); size=list(map(float,field(pad,'size')[:2]))
    expected=[anchor[i]+.254*(reference[pin][i]-origin[i]) for i in range(2)]
    errors=[at[i]-expected[i] for i in range(2)]+[size[i]-.254*reference[pin][i+2] for i in range(2)]
    assert max(map(abs,errors))<.00005,(pin,'geometry mismatch',errors)
    assert pad[2:4]==['smd','rect'],(pin,'shape',pad[2:4])
    assert field(pad,'net')[1]==nets[pin],(pin,'net mismatch')
    rows.append({'pin':pin,'net':nets[pin],'pcb_local_xy_mm':at,'pcb_size_mm':size,'source_error_mm':errors})
result={'revision':'B0.10','source':'JLCEDA/EasyEDA Official Library',
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'board_sha256':hashlib.sha256(board_path.read_bytes()).hexdigest(),
        'max_allowed_geometry_error_mm':.00005,'pads':rows,
        'live_placement_verified':False,'fabrication_release':False}
if len(sys.argv)>2:
    Path(sys.argv[2]).write_text(json.dumps(result,indent=2),encoding='utf-8')
print('PASS: 4 U5 pads match official library geometry, rectangular shape and pin/net map')
