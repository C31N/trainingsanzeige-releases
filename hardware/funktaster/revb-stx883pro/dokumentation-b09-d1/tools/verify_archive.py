#!/usr/bin/env python3
"""Read-only archive checks. A PASS is not a fabrication/hardware release."""
from pathlib import Path
import csv,hashlib,json,sys
root=Path(__file__).resolve().parents[1]
checks=0
for line in (root/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
    expected,name=line.split('  ',1)
    p=root/name
    assert p.is_file(),name
    assert hashlib.sha256(p.read_bytes()).hexdigest()==expected,name
    checks+=1
for line in (root/'firmware/SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
    expected,name=line.split('  ',1)
    assert hashlib.sha256((root/'firmware'/name).read_bytes()).hexdigest()==expected,name
bom=list(csv.DictReader((root/'manufacturing/02_JLCPCB_BOM_35_SMD_APPROVED_SUBSTITUTIONS.csv').open(encoding='utf-8-sig')))
refs={ref for row in bom for ref in row['Designator'].split(',')}
assert len(bom)==19 and len(refs)==35
for filename in ['03_CPL_ORIGINAL_OHNE_LIVE_KORREKTUREN.csv','03_CPL_Y_NEGATIV_OHNE_LIVE_KORREKTUREN.csv']:
    rows=list(csv.DictReader((root/'manufacturing'/filename).open(encoding='utf-8-sig')))
    assert len(rows)==35 and {r['Designator'] for r in rows}==refs
live=json.loads((root/'evidence/JLCPCB_BOM_Beleg_20261118.json').read_text(encoding='utf-8'))
for row in bom:
    assert any(row['Designator'] in s and row['LCSC Part #'] in s for s in live),row
ledger=json.loads((root/'validation/BESTUECKUNGSPRUEFUNG_35_REFERENZEN.json').read_text(encoding='utf-8'))
assert {r['ref'] for r in ledger}==refs
assert all(r['final_numeric_rotation_deg'] is None for r in ledger)
gates=json.loads((root/'validation/RELEASE_GATES.json').read_text(encoding='utf-8'))
assert gates['fabrication_release'] is False
assert gates['live_numeric_cpl_export_available'] is False
assert gates['live_numeric_cpl_matches_archive'] is False
drc=json.loads((root/'validation/native-drc.json').read_text(encoding='utf-8'))
assert all(drc[k]==[] for k in ['violations','unconnected_items','schematic_parity'])
erc=json.loads((root/'validation/native-erc.json').read_text(encoding='utf-8'))
assert all(s['violations']==[] for s in erc['sheets'])
print(f'PASS: {checks} archive files, six HEX checksums, 19 BOM groups / 35 refs, live BOM match, CAD 0/0/0/0')
print('BLOCKED FOR FABRICATION: final live numeric CPL and metric STX883PRO landpattern evidence missing.')
