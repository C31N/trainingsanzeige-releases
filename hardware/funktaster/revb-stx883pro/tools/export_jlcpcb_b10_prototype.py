#!/usr/bin/env python3
"""Rev B0.10 six-PCBA JLCPCB prototype export. Strict BOM/CPL/PCB reconciliation."""
import csv,hashlib,json,sys,zipfile
from collections import defaultdict
from pathlib import Path
import pcbnew
root,out=map(lambda x:Path(x).resolve(),sys.argv[1:3])
out.mkdir(parents=True,exist_ok=True)
board=pcbnew.LoadBoard(str(root/'kicad/buzzer-revb-stx883pro.kicad_pcb'))
items=list(csv.DictReader((root/'BOM_JLC_Entwurf_NICHT_FREIGEGEBEN.csv').open(encoding='utf-8-sig')))
entries={r['Designator']:r for r in items if r['Population']=='smd'}
assert len(entries)==35 and len({r['LCSC Part #'] for r in entries.values()})==19
assert {r['Designator'] for r in items if r['Population']=='hand'}=={'J1','J2','J3','J4','J5'}
assert {r['Designator'] for r in items if r['Population']=='mechanical'}=={'H1','H2'}
orig={r['Designator']:r for r in csv.DictReader((root/'CPL_JLC_Entwurf_NICHT_FREIGEGEBEN.csv').open(encoding='utf-8-sig'))}
assert set(entries)==set(orig)
fp={p.GetReference():p for p in board.GetFootprints()}
assert set(fp)=={r['Designator'] for r in items},(set(fp),{r['Designator'] for r in items})
bycode=defaultdict(list)
for ref,r in entries.items():bycode[r['LCSC Part #']].append(ref)
with (out/'02_JLCPCB_BOM_35_SMD.csv').open('w',encoding='utf-8-sig',newline='') as fh:
 w=csv.writer(fh);w.writerow(['Comment','Designator','Footprint','LCSC Part #'])
 for lcsc,refs in sorted(bycode.items()):
  data=[entries[ref] for ref in refs]
  assert len({r['Footprint'] for r in data})==1,(lcsc,'footprint conflict')
  # U2 and U3 have distinct functional labels but the same verified LCSC part.
  # LCSC code is the assembly identity, not the functional Comment.
  val=data[0]['Comment']
  if len({r['Comment'] for r in data})>1:
   val=val.split(' ')[0]
  w.writerow([val,','.join(refs),data[0]['Footprint'].split(':')[-1],lcsc])
with (out/'03_JLCPCB_CPL_35_SMD.csv').open('w',encoding='utf-8-sig',newline='') as fh:
 w=csv.writer(fh);w.writerow(['Designator','Mid X','Mid Y','Layer','Rotation'])
 for ref in sorted(entries):
  f=fp[ref];x=pcbnew.ToMM(f.GetPosition().x);y=pcbnew.ToMM(f.GetPosition().y);rot=f.GetOrientationDegrees()
  v=orig[ref]
  assert abs(float(v['Mid X'].removesuffix('mm'))-x)<0.01,(ref,x)
  assert abs(float(v['Mid Y'].removesuffix('mm'))-y)<0.01,(ref,y)
  assert abs(float(v['Rotation'])-rot)<0.001 and v['Layer']=='Top'
  assert 0<x<30 and 0<y<70
  jlc_rot=270 if ref in {'U1','U4'} else 180 if ref in {'U2','U3','Q1','Q2','Q3','Q4'} else rot
  # C3001517 library origin offset, verified by the clean viewer re-import.
  if ref=='U5': x+=1.095019; y+=0.522416
  w.writerow([ref,f'{x:.6f}mm',f'{-y:.6f}mm','Top',f'{jlc_rot:g}'])
g=out/'gerbers'
assert g.is_dir()
files=list(g.iterdir())
assert any('Edge_Cuts' in x.name for x in files)
assert sum(x.suffix=='.drl' for x in files)>=1
assert len(files)>=9,(len(files),[x.name for x in files])
with zipfile.ZipFile(out/'01_JLCPCB_GERBER_30x70_2L_PROTO.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(files):
  if p.is_file():z.write(p,p.name)
(out/'04_NICHT_SMD_BESTUECKEN.txt').write_text('J1 J2 J3 J4 J5: manuell verkabeln / programmieren\nH1 H2: 2.2-mm-Befestigungsbohrungen\n9V-Akku, externe T250mA-Sicherung, Taster und 433MHz-Antenne nicht Bestandteil der PCBA.\n')
(out/'RELEASE_GATES.json').write_text(json.dumps({
 'revision':'B0.10','board_mm':[30,70],'pcb_qty':10,'pcba_qty':6,'assembly_type':'Standard',
 'smd_ref_qty':35,'unique_lcsc':19,
 'jlc_c3001517_library_lands_matched':True,'placement_file_reimport_visually_reviewed':True,'unlogged_viewer_edits':False,'fabrication_release':False,'rf_erp_confirmed':False,
 'battery_under_load_confirmed':False,'firmware_preprogrammed':False,
 'prototype_only':True,'series_fabrication_release':False,'hardware_tested':False
},indent=2))
(out/'SHA256SUMS.txt').write_text(''.join(
 f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(out)}\n'
 for p in sorted(out.rglob('*')) if p.is_file() and p.name!='SHA256SUMS.txt'))
print('JLC B0.10 candidate package: 35 SMD, 19 LCSC groups, board centroid coords, Gerbers/drills')
