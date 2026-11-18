#!/usr/bin/env python3
"""Add readable manufacturing silkscreen without changing copper or placements."""
import json
import math
import re
import sys
import uuid
from pathlib import Path

root=Path(sys.argv[1]).resolve()

def parse(text):
    stack=[]; result=[]; cursor=result
    for token in re.findall(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+',text):
        if token=='(':
            child=[];cursor.append(child);stack.append(cursor);cursor=child
        elif token==')':cursor=stack.pop()
        else:cursor.append(json.loads(token) if token.startswith('"') else token)
    assert not stack
    return result[0]

def fields(items,key):return [x for x in items if isinstance(x,list) and x[0]==key]
def field(items,key):return fields(items,key)[0][1:]
def intersects(a,b,gap=0):
    return a[0]<b[2]+gap and a[2]>b[0]-gap and a[1]<b[3]+gap and a[3]>b[1]-gap

for name in ['buzzer-revb-stx883pro-ROUTED-V3-EXPERIMENT.kicad_pcb',
             'buzzer-revb-stx883pro-PLACEMENT-ONLY.kicad_pcb']:
    path=root/'kicad'/name; source=path.read_text(encoding='utf-8'); board=parse(source)
    footprints={next(p[2] for p in fields(fp,'property') if p[1]=='Reference'):fp
                for fp in fields(board,'footprint')}
    boxes={}
    for ref,fp in footprints.items():
        origin=list(map(float,field(fp,'at')[:2])); coords=[]
        assert len(field(fp,'at'))<3 or float(field(fp,'at')[2])==0
        for pad in fields(fp,'pad'):
            x,y=map(float,field(pad,'at')[:2]);w,h=map(float,field(pad,'size')[:2])
            coords.extend([(x-w/2,y-h/2),(x+w/2,y+h/2)])
        for shape in fp:
            if isinstance(shape,list) and shape and shape[0] in ['fp_rect','fp_line']:
                if field(shape,'layer')[0] in ['F.Fab','F.SilkS']:
                    coords.extend([tuple(map(float,field(shape,key)[:2])) for key in ['start','end']])
        assert coords,ref
        boxes[ref]=(origin[0]+min(x for x,y in coords)-.12,origin[1]+min(y for x,y in coords)-.12,
                    origin[0]+max(x for x,y in coords)+.12,origin[1]+max(y for x,y in coords)+.12)
    extra=[]; occupied=[]; entries=[]
    def text(label,x,y,size=.8,back=False,role='legend'):
        # Conservative stroke-font box for packing; native KiCad DRC is a separate gate.
        width=sum(.42 if c in '1 Iil.,:' else .80 for c in label)*size+.16
        height=size+.20
        box=(x-width/2,y-height/2,x+width/2,y+height/2)
        assert .35<=box[0] and box[2]<=29.65 and .35<=box[1] and box[3]<=69.65,(label,box)
        layer='B.SilkS' if back else 'F.SilkS'
        uid=str(uuid.uuid5(uuid.NAMESPACE_URL,f'wfd:b10:silk:{layer}:{role}:{label}:{x}:{y}'))
        mirror=' (justify mirror)' if back else ''
        extra.append(f'(gr_text {json.dumps(label)} (at {x:.4f} {y:.4f} 0) (layer "{layer}") '
                     f'(uuid "{uid}") (effects (font (size {size} {size}) (thickness 0.12)){mirror}))')
        entries.append({'text':label,'xy_mm':[x,y],'size_mm':size,'layer':layer,'role':role})
        if not back:occupied.append(box)
        return box

    text('Buzzer Rev B0.10',14.0,1.15,.95)
    text('ANT',24,1.3,.8)
    # Front header labels identify the actual holes; the back provides full net names.
    for ref,x,y in [('J1',5.2,61.8),('J2',13,61.8),('J4',20.5,60.7),('J5',6.27,32.7),('J3',24,5.2)]:
        text(ref,x,y,.85,role='reference')
    for label,x,y in [('1+',3.1,64),('2-',3.1,66.54),('1',11.25,64),('2',11.25,66.54),
                      ('1',18.75,63.2),('2',18.75,65.74),('3',18.75,68.28),
                      ('1',3.25,35),('3',3.25,37.54),('5',3.25,40.08),
                      ('2',9.25,35),('4',9.25,37.54),('6',9.25,40.08),('1',18,3.2)]:
        text(label,x,y,.7,role='connector_pin')
    # Place all 35 SMD references outside component/pad envelopes, close to their part.
    refs=[ref for ref in footprints if ref[0] in 'RCDQU']
    assert len(refs)==35
    refs.sort(key=lambda ref:-(boxes[ref][2]-boxes[ref][0])*(boxes[ref][3]-boxes[ref][1]))
    for ref in refs:
        a=boxes[ref]; ox,oy=map(float,field(footprints[ref],'at')[:2]);size=.8
        width=sum(.42 if c in '1 Iil.,:' else .80 for c in ref)*size+.16;h=size+.20
        candidates=[]
        for distance in [0,.25,.5,.75,1,1.5,2,2.5,3]:
            candidates.extend([(ox,a[1]-.28-h/2-distance),(ox,a[3]+.28+h/2+distance),
                               (a[0]-.28-width/2-distance,oy),(a[2]+.28+width/2+distance,oy)])
        chosen=None
        for x,y in candidates:
            b=(x-width/2,y-h/2,x+width/2,y+h/2)
            if b[0]<.4 or b[2]>29.6 or b[1]<.4 or b[3]>69.6:continue
            if any(intersects(b,v,.20) for v in boxes.values()):continue
            if any(intersects(b,v,.18) for v in occupied):continue
            chosen=(x,y);break
        assert chosen,(ref,'No readable silkscreen reference location')
        text(ref,*chosen,size,role='reference')
    # Back legend is mirrored in CAD, so it reads normally when viewing the back.
    back=[('Buzzer Rev B0.10',15,7.2,1.1),('ID: ______',15,10.3,1.15),
          ('RUECKSEITE - ANT oben',15,13,.8),('Pin 1 = markierte Ecke',15,15,.8),
          ('J1 AKKU: 1 +9V / 2 GND',15,18,.8),
          ('J2 TASTER: 1 NO / 2 GND',15,20,.8),
          ('J3: ANT / 433 MHz',15,22,.8),
          ('J4 UPDI: 1 UPDI / 2 CTRL3V3 / 3 GND',15,25,.75),
          ('J5 ISP: 1 MISO / 2 TX3V3',15,28,.8),
          ('3 SCK / 4 MOSI / 5 RESET / 6 GND',15,30,.75),
          ('U5: 1 GND / 2 TX3V3 / 3 DATA / 4 ANT',15,32,.7),
          ('U2/U3: 1 IN / 2 GND / 3,4 NC / 5 OUT',17,33.7,.65),
          ('Q1/Q3: 1 G / 2 S / 3 D',19,35.5,.75),
          ('Q2/Q4: 1 B / 2 E / 3 C',19,37.3,.75),
          ('D1/D2: K links (von oben)',19,39.1,.7),
          ('U1 ATtiny402',8,43.0,.8),('U4 ATtiny13A',22,43.0,.8),
          ('Keine 5V an J4/J5!',15,60.5,.85)]
    for label,x,y,size in back:text(label,x,y,size,True)
    labels={'/3V3':'CTRL3V3','/TX3V3':'TX3V3','/POWER':'POWER','/BUTTON':'BUTTON',
            '/UPDI':'UPDI','/DISCHARGE':'DISCH','/GND':'GND','/RESET':'RESET',
            '/MCU_DATA':'DATA','/MOSI':'MOSI','/MISO':'MISO','/SCK':'SCK'}
    for ref,x in [('U1',8),('U4',22)]:
        pads={pad[1]:pad for pad in fields(footprints[ref],'pad')}
        for pin in range(1,9):
            net=field(pads[str(pin)],'net')[1]
            label='NC' if net.startswith('unconnected-') else labels[net]
            text(f'{pin} {label}',x,45.3+(pin-1)*1.7,.75,True,role='controller_pin')
    # Pin 1 and cathode marks already present in the original footprints are retained.
    output=source.rstrip()[:-1]+'\n'+'\n'.join(extra)+'\n)\n'
    assert output[:len(source.rstrip())-1]==source.rstrip()[:-1]
    path.write_text(output,encoding='utf-8')
    (root/'validation/B10_SILKSCREEN.json').write_text(json.dumps({
        'revision':'B0.10-S2','title':'Buzzer Rev B0.10','copper_changed':False,
        'placement_changed':False,'smd_reference_count':len(refs),
        'native_drc_pending':True,'texts':entries},indent=2),encoding='utf-8')
    print(name,len(extra),'silkscreen texts; 35 SMD references, connector pins and back legend')
