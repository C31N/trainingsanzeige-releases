#!/usr/bin/env python3
"""Rev B0.9: shorter ANT feed, near-feed GND vias; prototype only, no RF compliance claim."""
import json
import re
import sys
import uuid
from pathlib import Path

root=Path(sys.argv[1]).resolve()
k=root/'kicad'
for p in [k/'buzzer-revb-stx883pro-ROUTED-V3-EXPERIMENT.kicad_pcb',
          k/'buzzer-revb-stx883pro-PLACEMENT-ONLY.kicad_pcb']:
    s=p.read_text(encoding='utf-8')
    old='(footprint "WFD-RevB:HEADER_1x01" (version 20240108) (generator "pcbnew") (layer "F.Cu") (at 24.0 3.2 0)'
    assert s.count(old)==1,(p,'expected exactly one antenna connector')
    s=s.replace(old,old.replace('24.0 3.2 0','19.73 3.2 0'))
    if 'ROUTED' in p.name:
        regex=r'\(segment\s+\(start ([\d.]+) ([\d.]+)\) \(end ([\d.]+) ([\d.]+)\) \(width ([\d.]+)\) \(layer F\.Cu\) \(net 2\) \(uuid "[^"]+"\)\)'
        removed=[]
        def rm(m):
            a=[float(m.group(i)) for i in range(1,6)]
            assert all(18.5<=x<=24 for x in (a[0],a[2]))
            assert all(2.5<=y<=7 for y in (a[1],a[3]))
            removed.append(a)
            return ''
        s=re.sub(regex,rm,s)
        assert len(removed)==10,(p,len(removed))
        segment_count=s.count('(segment ')
        uid=str(uuid.uuid5(uuid.NAMESPACE_URL,'wfd-revb-b09-ant-short-feed'))
        extras=[f'\n(segment (start 19.7300 3.2000) (end 19.7300 6.4000) (width 0.8) (layer F.Cu) (net 2) (uuid "{uid}"))']
        for side,x in [('left',17.5),('right',21.95)]:
            uid=str(uuid.uuid5(uuid.NAMESPACE_URL,'wfd-revb-b09-antenna-return-via-'+side))
            extras.append(f'\n(via (at {x:.4f} 3.7500) (size 0.75) (drill 0.35) (layers "F.Cu" "B.Cu") (net 12) (uuid "{uid}"))')
        s=s.rstrip()[:-1]+''.join(extras)+'\n)\n'
        assert s.count('(segment ')==segment_count+1
        assert s.count('(via ')==46
    p.write_text(s,encoding='utf-8')
script=root/'make_design.py'
s=script.read_text(encoding='utf-8')
old="A('J3','433MHz_ANT_50OHM','HEADER_1x01',{'1':'ANT'},[24.0,3.2],kind='hand')"
assert s.count(old)==1
script.write_text(s.replace(old,old.replace('[24.0,3.2]','[19.73,3.2]')),encoding='utf-8')
meta=root/'design.json'
d=json.loads(meta.read_text(encoding='utf-8'))
j=[p for p in d['parts'] if p['ref']=='J3']
assert len(j)==1 and j[0]['xy']==[24.0,3.2]
j[0]['xy']=[19.73,3.2]
d['revision']='B0.9-ANTENNA-SHORT-FEED-PROTOTYPE'
d['status']='NATIVE_KICAD_REVALIDATION_PENDING_NO_SERIES_FAB_RELEASE'
meta.write_text(json.dumps(d,indent=2,ensure_ascii=False),encoding='utf-8')
validation=root/'validation'
validation.mkdir(exist_ok=True)
(validation/'B09_RF_SHORT_FEED.json').write_text(json.dumps({
    'from':'B0.8','connector_J3_mm':[19.73,3.2],'prior_rf_length_mm':5.37,
    'new_rf_length_mm':3.2,'trace_width_mm':0.8,
    'removed_ant_segments':10,'added_ant_segments':1,
    'added_gnd_vias_mm':[[17.5,3.75],[21.95,3.75]],
    'nominal_9v_battery_measured_by_user':True,
    'battery_under_load_verified':False,
    'jlc_c3001517_landpattern_verified':False,
    'rf_50ohm_verified':False,
    'fabrication_release':False
},indent=2,ensure_ascii=False),encoding='utf-8')
with (root/'README.md').open('a',encoding='utf-8') as f:
    f.write('\n\n## B0.9 prototype antenna-feed update\n'
        'Moved J3 into direct alignment with STX883PRO pin 4. ANT feed is now '
        'one 3.2-mm x 0.8-mm segment instead of ten 0.25-mm segments over 5.37 mm; '
        'two grounded return vias near the feed. Exact characteristic impedance, '
        'JLC pad geometry, antenna and real battery under-load operation NOT VERIFIED. '
        'This is an engineering prototype; NO SERIES FABRICATION RELEASE.\n')
print('B0.9 patch complete: 3.2mm RF path, 2 GND vias, copper routing otherwise unchanged')
