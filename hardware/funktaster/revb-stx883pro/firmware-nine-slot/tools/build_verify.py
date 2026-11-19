"""Build and instruction-model all nine images; never opens a programmer."""
import argparse,hashlib,json,subprocess,statistics
from pathlib import Path
from avr_waveform import AVR
from receiver_diamex5_reference import DiamexStreamDecoder,diamex_code,DIAMEX_V2_PREAMBLE_PAIR_CYCLES
ROOT=Path(__file__).resolve().parents[1]
def build(tc, ids):
 out=ROOT/'images';out.mkdir(exist_ok=True);report=[]
 def tool(n):return str(tc/(n+'.exe' if (tc/(n+'.exe')).exists() else n))
 for i in ids:
  base=out/f'ATtiny13A_V2_N9_ID{i}';elf=base.with_suffix('.elf')
  subprocess.run([tool('avr-gcc'),'-mmcu=attiny13a','-Os','-std=gnu99','-Wall','-Wextra','-Werror','-ffunction-sections','-fdata-sections','-Wl,--gc-sections',f'-DBUTTON_ID={i}',str(ROOT/'source/funktaster_v2_nine_slot.c'),'-o',str(elf)],check=True)
  subprocess.run([tool('avr-objcopy'),'-O','ihex','-R','.eeprom',str(elf),str(base.with_suffix('.hex'))],check=True)
  subprocess.run([tool('avr-objcopy'),'-O','binary','-R','.eeprom',str(elf),str(base.with_suffix('.bin'))],check=True)
  listing=subprocess.check_output([tool('avr-objdump'),'-d',str(elf)],text=True).replace(str(elf),'buzzer.elf')
  size=len(base.with_suffix('.bin').read_bytes());assert size<=1024
  traces=[]
  for event in ([0,1,127,255] if i==1 else [0]):
   # A valid previous event record causes next_event() to produce this event.
   ee=bytearray(b'\xff'*64);ee[0]=(event-1)%256;ee[1]=ee[0]^255
   model=AVR(listing,eeprom=ee).run();assert model.slept and model.min_sp>=0x70 and model.edges[-1][1]==0
   pair=round(statistics.median(model.edges[n+2][0]-model.edges[n][0] for n in [8,10,12,14])*9.6)
   assert pair==DIAMEX_V2_PREAMBLE_PAIR_CYCLES
   # Independently decode actual compiled GPIO transitions, including ages and CRC.
   max_error=0
   for scale in [.8,1.,1.25]:
    dec=DiamexStreamDecoder();packets=[]
    for n in range(1,len(model.edges)):
     delta=(model.edges[n][0]-model.edges[n-1][0])*scale
     code=dec.feed(delta)
     if code:
      assert code==diamex_code(i);assert dec.last_event['event_id']==event
      offset=dec.last_event['offset_us'];end=model.edges[n][0]*scale
      max_error=max(max_error,abs(offset-end))
      assert abs(offset-end)<2000,(i,event,scale,offset,end)
      packets.append(dict(dec.last_event))
    assert [p['repeat'] for p in packets]==[0,1,2,3],(i,event,scale,packets)
   assert model.edges[-1][0]*1.25<975000,'Insufficient reserve before 1-second hold cutoff'
   traces.append({'event':event,'last_edge_us':round(model.edges[-1][0],3),'minimum_stack_pointer':model.min_sp,'max_timestamp_error_us':round(max_error,3)})
  base.with_suffix('.lst').write_text(listing,encoding='utf-8');elf.unlink()
  report.append({'id':i,'flash_bytes':size,'sha256_hex':hashlib.sha256(base.with_suffix('.hex').read_bytes()).hexdigest(),'models':traces})
 # All nine get distinct slots in every round; the slot permutation changes.
 rounds=[[(i*m)%9 for i in range(9)] for m in [1,2,4]]
 assert all(sorted(r)==list(range(9)) for r in rounds)
 result={'version':'V2-N9.1','packet_format_unchanged':True,'receiver_required':'diamex-5','receiver_source_sha256':hashlib.sha256((ROOT/'tools/receiver_diamex5_reference.py').read_bytes()).hexdigest(),'compiler':subprocess.check_output([tool('avr-gcc'),'--version'],text=True).splitlines()[0],'source_sha256':hashlib.sha256((ROOT/'source/funktaster_v2_nine_slot.c').read_bytes()).hexdigest(),'round_slots_by_id':rounds,'hfuse':'0xfb','lfuse':'0x76','hardware_tested':False,'loss_rate_measured':False,'images':report}
 (ROOT/('verification.json' if len(ids)==9 else 'verification_'+str(ids[0])+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(f'PASS: IDs {ids}; instruction models and receiver decodes passed',flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--toolchain',type=Path,required=True);p.add_argument('--ids',type=int,nargs='+',default=list(range(1,10)));a=p.parse_args();build(a.toolchain.resolve(),a.ids)
