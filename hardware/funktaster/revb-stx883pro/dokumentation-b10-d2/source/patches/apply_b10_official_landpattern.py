#!/usr/bin/env python3
"""Replace the experimental U5 lands with the inspected C3001517 library geometry.

Source: JLCEDA/EasyEDA Official Library, https://lceda.cn/ https://easyeda.com
No inference about JLC machine placement, physical hardware or RF acceptance.
"""
import csv
import hashlib
import json
import re
import sys
import uuid
from pathlib import Path

root = Path(sys.argv[1]).resolve()
source = Path(__file__).resolve().parents[1] / 'validation/b10-footprint/C3001517_EasyEDA_Official_Library.json'
data = json.loads(source.read_text(encoding='utf-8'))
assert data['head']['uuid'] == 'a9205db4edc6417e8063158c3dd307e5'
raw = {}
for shape in data['shape']:
    fields = shape.split('~')
    if fields[0] == 'PAD':
        assert fields[1] == 'RECT' and fields[6] == '1'
        raw[fields[8]] = [float(v) for v in fields[2:6]]
assert set(raw) == {'1', '2', '3', '4'}
# EasyEDA Standard internal coordinate unit = 10 mil = 0.254 mm.
# Anchor pad 2 at the existing PCB position; do not move the power pin or module ref.
origin = raw['2'][:2]
new = {}
for pin, (x, y, width, height) in raw.items():
    new[pin] = [round((x-origin[0])*.254, 6), round(7.1+(y-origin[1])*.254, 6),
                round(width*.254, 4), round(height*.254, 4)]
assert new['1'] == [-2.54, 7.1, 1.9, 2.7]
assert new['3'] == [2.54, 7.1, 1.9, 2.7]
assert abs(new['4'][0]-4.73) < .0001
assert new['4'][2:] == [2.0, 2.5]
old = {'1':[-2.54,7.1,1.7,2.5], '2':[0,7.1,1.7,2.5],
       '3':[2.54,7.1,1.7,2.5], '4':[4.73,-6.1,1.8,2.2]}

def change_pads(text):
    for pin, expected in old.items():
        pattern = (r'(\(pad "'+pin+r'" smd )roundrect( \(at )'
                   r'([-\d.]+) ([-\d.]+)(\) \(size )([-\d.]+) ([-\d.]+)'
                   r'(\) \(layers "F.Cu" "F.Paste" "F.Mask"\))'
                   r' \(roundrect_rratio 0\.15\)')
        def replace(match):
            actual = [float(match.group(i)) for i in [3,4,6,7]]
            assert actual == expected, (pin, actual, expected)
            x,y,w,h = new[pin]
            return f'{match[1]}rect{match[2]}{x:g} {y:g}{match[5]}{w:g} {h:g}{match[8]}'
        text, count = re.subn(pattern, replace, text)
        assert count == 1, (pin, count)
    # Body envelope from the official library outline, aligned to pad 2.
    text = text.replace('(start -7.06 -7.335) (end 7.06 7.335)',
                        '(start -7.06 -6.765111) (end 7.06 7.904889)')
    text = text.replace('(start -7.4 -7.7) (end 7.4 7.7)',
                        '(start -7.4 -7.1) (end 7.4 8.7)')
    return text

def end_sexp(text, start):
    depth=0; quoted=False; escaped=False
    for index in range(start,len(text)):
        char=text[index]
        if quoted:
            if escaped: escaped=False
            elif char=='\\': escaped=True
            elif char=='"': quoted=False
        elif char=='"': quoted=True
        elif char=='(': depth+=1
        elif char==')':
            depth-=1
            if depth==0: return index+1
    raise ValueError('Unclosed footprint')

k=root/'kicad'
path=k/'WFD-RevB.pretty/STX883PRO.kicad_mod'
path.write_text(change_pads(path.read_text(encoding='utf-8')),encoding='utf-8')
for name in ['buzzer-revb-stx883pro-PLACEMENT-ONLY.kicad_pcb',
             'buzzer-revb-stx883pro-ROUTED-V3-EXPERIMENT.kicad_pcb']:
    path=k/name; text=path.read_text(encoding='utf-8')
    start=text.index('(footprint "WFD-RevB:STX883PRO"'); end=end_sexp(text,start)
    block=text[start:end]
    assert '(at 15.0 12.5 0)' in block
    text=text[:start]+change_pads(block)+text[end:]
    if 'ROUTED' in name:
        oldtrack='(start 19.7300 3.2000) (end 19.7300 6.4000) (width 0.8)'
        assert text.count(oldtrack)==1
        text=text.replace(oldtrack,f'(start 19.7300 3.2000) (end 19.7300 {12.5+new["4"][1]:.6f}) (width 0.8)')
        # The larger GND pad reduces clearance to the adjacent TX3V3 diagonal.
        # Shift this diagonal outward by 0.25 mm, preserving the 0.20-mm rule.
        oldtrack='(start 7.5000 27.7500) (end 7.5000 27.2500) (width 0.25)'
        assert text.count(oldtrack)==1
        text=text.replace(oldtrack,oldtrack.replace('27.2500','27.5000'))
        oldtrack='(start 7.5000 27.2500) (end 14.7500 20.0000) (width 0.25)'
        assert text.count(oldtrack)==1
        text=text.replace(oldtrack,'(start 7.5000 27.5000) (end 14.7500 20.2500) (width 0.25)')
        uid=str(uuid.uuid5(uuid.NAMESPACE_URL,'wfd:revb:b10:tx3v3-clearance-dogleg'))
        text=text.rstrip()[:-1]+f'\n(segment (start 14.7500 20.2500) (end 14.7500 20.0000) (width 0.25) (layer F.Cu) (net 23) (uuid "{uid}"))\n)\n'
    path.write_text(text,encoding='utf-8')
# Keep the generator consistent with the patched library.
path=root/'make_design.py'; text=path.read_text(encoding='utf-8')
for pin,(x,y,w,h) in old.items():
    token=f'smd_pad({pin},{x:g},{y:g},{w:g},{h:g})'
    assert text.count(token)==1,token
    nx,ny,nw,nh=new[pin]
    text=text.replace(token,f'smd_pad({pin},{nx:g},{ny:g},{nw:g},{nh:g})')
# Generator helper emits roundrect; use an exact rectangular override for U5 only.
text=text.replace('(start -7.06 -7.335) (end 7.06 7.335)',
                  '(start -7.06 -6.765111) (end 7.06 7.904889)')
text=text.replace('(start -7.4 -7.7) (end 7.4 7.7)',
                  '(start -7.4 -7.1) (end 7.4 8.7)')
# Apply the rectangular shape to the generated U5 body without changing other packages.
start=text.index("custom('STX883PRO',f'''"); end=text.index("''')",start)+4
block=text[start:end]
for pin,(x,y,w,h) in new.items():
    token='{'+f'smd_pad({pin},{x:g},{y:g},{w:g},{h:g})'+'}'
    block=block.replace(token, f'(pad "{pin}" smd rect (at {x:g} {y:g}) (size {w:g} {h:g}) (layers "F.Cu" "F.Paste" "F.Mask"))')
text=text[:start]+block+text[end:]
path.write_text(text,encoding='utf-8')
# Retain the three substitutions explicitly approved for the current order.
substitutions={'C415536':'C76639','C2835529':'C6119932','C2889503':'C114523'}
for path in [root/'BOM_JLC_Entwurf_NICHT_FREIGEGEBEN.csv', root/'make_design.py',
             *k.glob('*.kicad_sch'), *k.glob('*.kicad_pcb'), *k.glob('*.kicad_sym')]:
    text=path.read_text(encoding='utf-8')
    for before,after in substitutions.items(): text=text.replace(before,after)
    path.write_text(text,encoding='utf-8')
path=root/'design.json'; meta=json.loads(path.read_text(encoding='utf-8'))
for part in meta['parts']:
    part['lcsc']=substitutions.get(part['lcsc'],part['lcsc'])
meta['revision']='B0.10-C3001517-LIBRARY-LANDS'
meta['status']='NATIVE_KICAD_PENDING_JLC_PLACEMENT_UNVERIFIED_NO_FABRICATION'
path.write_text(json.dumps(meta,indent=2,ensure_ascii=False),encoding='utf-8')
report={'revision':'B0.10','source':'JLCEDA/EasyEDA Official Library',
        'source_urls':['https://lceda.cn/','https://easyeda.com/',
          'https://jlcpcb.com/partdetail/gnicerf-STX883PRO433MHz/C3001517'],
        'source_uuid':data['head']['uuid'],
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'library_unit_mm':.254,'anchor':'U5 pad 2 remains at (15,19.6) mm',
        'old_pads_local_mm':old,'corrected_pads_local_mm':new,
        'pad_shape':'rect','antenna_trace_length_mm':round(12.5+new['4'][1]-3.2,6),
        'tx3v3_clearance_diagonal_shift_mm':.25,
        'library_lands_compared':True,'live_numeric_cpl_verified':False,
        'approved_lcsc_substitutions':substitutions,
        'hardware_verified':False,'fabrication_release':False}
(root/'validation/B10_OFFICIAL_LANDPATTERN.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('B0.10: four U5 lands matched to C3001517 library, pending native CAD and live placement checks')
