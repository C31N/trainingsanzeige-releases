#!/usr/bin/env python3
"""Reproducible B0.4 correction of KiCad-8 zone syntax and schematic grid/library.
NO FABRICATION RELEASE. Requires a clean extraction of the B0.3 design ZIP."""
import json
from pathlib import Path
import subprocess
import sys

root=Path(sys.argv[1]).resolve()
script=root/'make_design.py'
code=script.read_text()
old='x=30+(ix%4)*95;y=28+(ix//4)*29\n    if y>270:x=30+(ix%6)*64;y=28+(ix//6)*26'
new='x=31.75+(ix%4)*95.25;y=25.4+(ix//4)*30.48\n    if y>270:x=31.75+(ix%6)*63.50;y=25.40+(ix//6)*25.40'
assert old in code, 'Unexpected old schematic grid generator'
code=code.replace(old,new)
old="(OUT/'sym-lib-table').write_text('(sym_lib_table)',encoding='utf-8')"
new='''# Project-local schematic symbol library generated from the same embedded symbols.
(OUT/'WFD-RevB.kicad_sym').write_text(
    '(kicad_symbol_lib (version 20231120) (generator "kicad_symbol_editor") '+
    ' '.join(S).replace('(symbol "WFD-RevB:', '(symbol "')+')',encoding='utf-8')
(OUT/'sym-lib-table').write_text(
    '(sym_lib_table (lib (name "WFD-RevB")(type "KiCad")'+
    '(uri "${KIPRJMOD}/WFD-RevB.kicad_sym")(options "")'+
    '(descr "Self-contained WFD Rev B schematic symbols")))',encoding='utf-8')'''
assert old in code, 'Symbol table generation changed unexpectedly'
code=code.replace(old,new)
script.write_text(code)

router=root/'route_board_v2.py'
r=router.read_text()
assert '(connect_pads (type solid) (clearance 0.3))' in r, 'Unexpected zone format'
router.write_text(r.replace('(connect_pads (type solid) (clearance 0.3))','(connect_pads yes (clearance 0.3))'))
for pcb in (root/'kicad').glob('*ROUTED*pcb'):
    s=pcb.read_text()
    pcb.write_text(s.replace('(connect_pads (type solid) (clearance 0.3))','(connect_pads yes (clearance 0.3))'))
# Re-generate schematic, project-local library, footprint table, and placement BOM.
# DO NOT touch the routed copper geometry.
subprocess.run([sys.executable,str(script)],cwd=root,check=True)
meta=json.loads((root/'design.json').read_text())
meta.update(revision='B0.4-EXPERIMENT',status='ROUTED_CANDIDATE_UNVERIFIED_NO_FABRICATION')
(root/'design.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
with (root/'README.md').open('a',encoding='utf-8') as f:
    f.write('\n\n## B0.4 syntax/library repair\nKiCad 8 zone syntax; grid-aligned schematic and local symbol library. Copper routing unchanged from B0.3; NOT FABRICATION APPROVED.\n')
print('B0.4 generated: KiCad-8 board zone syntax and schematic grid/library repaired')
