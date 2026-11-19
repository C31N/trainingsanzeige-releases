#!/usr/bin/env python3
"""Read-only consistency check. A pass is not a hardware acceptance test."""
from pathlib import Path
import hashlib,json,csv,zipfile
root=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
catalog=root/'SHA256SUMS.txt'
entries={}
for line in catalog.read_text(encoding='utf-8').splitlines():
    digest,name=line.split('  ',1); p=root/name
    assert p.resolve().is_relative_to(root.resolve()),name
    assert p.is_file() and sha(p)==digest,('checksum',name)
    entries[name]=digest
assert set(entries)=={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p!=catalog},'Uncatalogued files'
mf=root/'manufacturing'; rows=list(csv.DictReader((mf/'02_JLCPCB_BOM_35_SMD.csv').open(encoding='utf-8-sig')))
refs={};expected_sub={'C3':'C76639','C6':'C76639','C8':'C6119932','R13':'C114523'}
for r in rows:
    for ref in r['Designator'].split(','):
        assert ref not in refs;refs[ref]=r['LCSC Part #']
assert len(rows)==19 and len(refs)==35 and len(set(refs.values()))==19
assert all(refs[r]==code for r,code in expected_sub.items())
cpl=list(csv.DictReader((mf/'03_JLCPCB_REVB_B010_FINAL.csv').open(encoding='utf-8-sig')))
assert len(cpl)==35 and {r['Designator'] for r in cpl}==set(refs)
for r in cpl:
    ref=r['Designator'];want=270 if ref in {'U1','U4'} else 180 if ref in {'U2','U3','Q1','Q2','Q3','Q4'} else 0
    assert r['Layer']=='Top' and float(r['Rotation'])==want
    assert float(r['Mid Y'].removesuffix('mm'))<0
    if ref=='U5':
        assert abs(float(r['Mid X'].removesuffix('mm'))-16.095019)<.000002
        assert abs(float(r['Mid Y'].removesuffix('mm'))+13.022416)<.000002
assert sha(mf/'03_JLCPCB_REVB_B010_FINAL.csv')=='06aec6b7b8c08d75b3b32cdc685a7b8cb93175f4464b8c948ca27276c23004f9'
with zipfile.ZipFile(root/'source/DIAMEX_Funktaster.zip') as z:
    for i in range(1,10):assert (root/f'firmware/ATtiny13A_V2_ID{i}.hex').read_bytes()==z.read(f'firmware/v2/buzzer{i}.hex')
hexes=list((root/'firmware').glob('*.hex'));assert len(hexes)==19
for p in hexes:
    eof=False;count=0
    for line in p.read_text().splitlines():
        assert line.startswith(':'); raw=bytes.fromhex(line[1:]);assert len(raw)==raw[0]+5 and sum(raw)%256==0
        assert not eof,'Data after EOF'
        if raw[3]==0:count+=raw[0]
        if raw[3]==1:eof=True
    assert eof and count>0,p.name
n9=json.loads((root/'validation/FIRMWARE_N9.json').read_text())
assert [i['id'] for i in n9['images']]==list(range(1,10))
for item in n9['images']:
    assert sha(root/f"firmware/ATtiny13A_V2_N9_ID{item['id']}.hex")==item['sha256_hex']
    assert item['flash_bytes']<=1024
    assert all(m['max_timestamp_error_us']<2000 and m['last_edge_us']*1.25<975000 for m in item['models'])
drc=json.loads((root/'validation/native-drc.json').read_text());erc=json.loads((root/'validation/native-erc.json').read_text())
assert drc['kicad_version']=='8.0.9'
assert all(drc[k]==[] for k in ['violations','unconnected_items','schematic_parity'])
assert erc['sheets'] and all(s['violations']==[] for s in erc['sheets'])
gates=json.loads((root/'validation/RELEASE_GATES.json').read_text())
assert gates['pcba_qty_ordered']==9 and gates['pcb_qty_ordered']==10
assert gates['hardware_tested'] is False and gates['series_fabrication_release'] is False
assert gates['placement_from_archived_input'] is True and gates['manual_viewer_changes_after_import']==[]
ledger=json.loads((root/'validation/PLACEMENT_REVIEW.json').read_text())
assert {r['Designator'] for r in ledger['references']}==set(refs)
print(f'PASS: {len(entries)} file checksums; 35 placements / 19 BOM types; 19 valid HEX files (10 historical originals, 9 compiled N9); native CAD 0/0/0/0. Hardware acceptance remains open.')
