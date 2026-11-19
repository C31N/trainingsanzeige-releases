from pathlib import Path
import csv,json,re,hashlib,shutil,zipfile,html
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,Image,Preformatted,KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader
STAGE=Path(__file__).resolve().parents[1]
OUT=STAGE/'documents'
PDF=OUT/'Buzzer_RevB_B010_Anleitung_Programmierung.pdf'
source=STAGE/'manufacturing'
with zipfile.ZipFile(source/'01_JLCPCB_REVB_B010_S2_30x70_2L.zip') as z:
 g=z.read(next(n for n in z.namelist() if n.endswith('F_Cu.gtl'))).decode()
pads={}
for m in re.finditer(r'%TO\.P,([^,]+),([^*]+)\*%\s*%TO\.N,([^*]*)\*%\s*X(-?\d+)Y(-?\d+)D03\*',g):
 ref,pin,net,x,y=m.groups();pads.setdefault(ref,{})[pin]={'net':net,'x_mm':int(x)/1e6,'gerber_y_mm':int(y)/1e6,'top_y_down_mm':-int(y)/1e6}
bom=list(csv.DictReader((source/'02_JLCPCB_BOM_35_SMD.csv').open(encoding='utf-8-sig')))
sub=[['C3,C6','C415536','C76639'],['C8','C2835529','C6119932'],['R13','C2889503','C114523']]
fontroot=Path(r'C:/Windows/Fonts');pdfmetrics.registerFont(TTFont('Guide',str(fontroot/'arial.ttf')));pdfmetrics.registerFont(TTFont('GuideBold',str(fontroot/'arialbd.ttf')))
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyG',fontName='Guide',fontSize=10,leading=14,spaceAfter=8,textColor=colors.HexColor('#223344')))
styles.add(ParagraphStyle(name='H1G',fontName='GuideBold',fontSize=22,leading=26,spaceAfter=14,textColor=colors.HexColor('#125780')))
styles.add(ParagraphStyle(name='H2G',fontName='GuideBold',fontSize=12,leading=16,spaceBefore=10,spaceAfter=6,textColor=colors.HexColor('#125780')))
styles.add(ParagraphStyle(name='SmallG',fontName='Guide',fontSize=8,leading=11,spaceAfter=5))
styles.add(ParagraphStyle(name='CodeG',fontName='Courier',fontSize=7.1,leading=10,backColor=colors.HexColor('#eef4f8'),borderPadding=6,spaceAfter=8))
story=[]; md=[]
def p(t,style='BodyG'):story.append(Paragraph(t,styles[style]));md.append(re.sub('<[^>]+>','',t)+'\n')
def h(t):p(t,'H2G')
def title(n,t):
 if story:story.append(PageBreak())
 p(f'{n:02d}  {t}','H1G');md.append('\n## '+t+'\n')
def table(data,widths=None,small=False):
 sty=styles['SmallG'] if small else styles['BodyG']
 cells=[[Paragraph(html.escape(str(x)).replace('\n','<br/>'),sty) for x in row] for row in data]
 t=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT');t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dcebf3')),('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#c8d5de')),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),4)]));story.append(t);story.append(Spacer(1,8));md.extend([' | '.join(map(str,row))+'\n' for row in data])
def code(t):
 import textwrap
 lines=[]
 for line in t.splitlines():
  parts=textwrap.wrap(line,width=100,break_long_words=False,break_on_hyphens=False) or ['']
  lines.extend(part+(' `' if i<len(parts)-1 else '') for i,part in enumerate(parts))
 rendered='\n'.join(lines);story.append(Preformatted(rendered,styles['CodeG']));md.append('```powershell\n'+rendered+'\n```\n')
def bullet(t):p('- '+t)
title(1,'Buzzer Rev B0.10')
p('Beschreibung, Anschluss, Programmierung und ErstprÃ¼fung')
p('Wasserfreunde Dalum | Dokumentation B0.10-D2 | 19.11.2026','SmallG')
h('Bestellter Prototypenstand')
p('<b>Neun bestÃ¼ckte Prototypen bestellt; Musterabnahme steht aus.</b> Die native CAD-PrÃ¼fung und der metrische C3001517-Abgleich sind bestanden. Die finale numerische BestÃ¼ckungsdatei wurde erneut importiert und alle35 Referenzen wurden visuell geprÃ¼ft. Nach diesem Import wurden keine Drehungen oder Positionen im Viewer geÃ¤ndert. Schaltung, Akku und Funk mÃ¼ssen nach Lieferung am Muster geprÃ¼ft werden.')
table([['Merkmal','Stand'],['Platine','30 x70 mm, FR4, 1,6 mm, 2 Lagen, 1 oz'],['Bestellter Auftrag','10 PCBs, davon9 Top-Standard-PCBA;1 unbestÃ¼ckt'],['BestÃ¼ckung','35 SMD-Referenzen, 19 LCSC-Typen'],['Controller U1','ATtiny402: ImpulsverlÃ¤ngerung, UPDI'],['Sendersteuerung U4','ATtiny13A: V2-Firmware, IDs1-9, ISP'],['Funkmodul U5','STX883PRO-433MHz, Versorgung3,3 V'],['Lieferzustand','Unprogrammiert; J1-J5, Taster, Antenne und Akku manuell']], [120,385])
h('Was gegenÃ¼ber V5 anders ist')
p('Rev B integriert den bisherigen Sender und die Rev-A-ImpulsverlÃ¤ngerung auf einer Platine. Statt STX882 und R-78E werden STX883PRO und ein zweiter TPS70933 verwendet. Vorhandene V2-IDs1-9 bleiben vorgesehen; die neue Funkhardware muss trotzdem am realen GerÃ¤t geprÃ¼ft werden.')
p('Der Taster liefert nur einen potentialfreien Kontakt gegen Masse. U1 hÃ¤lt den Sender nominal1000 ms eingeschaltet, sperrt weitere DrÃ¼cke und ermÃ¶glicht danach Entladung und erneute Freigabe. Ein sicher erfasster1-ms-Druck ist weiterhin ein Messziel.')
title(2,'Bauteile und AnschlÃ¼sse')
photo=Image(str(STAGE/'evidence/JLCPCB_Bestueckungsansicht_20261118.png'),width=145,height=342)
legend=Paragraph('Blick auf die BestÃ¼ckungsseite, Antennenanschluss oben. Die Abbildung ist der exportierte JLCPCB-Viewer-Stand. Sie belegt die sichtbare Orientierung, keine Funktions- oder Funkabnahme.<br/><br/>U5: Funkmodul<br/>U4: ATtiny13A<br/>U1: ATtiny402<br/>U2/U3:3,3-V-Regler<br/>D1: Gate-Begrenzung<br/>D2: Verpolschutz<br/>J5: ISP links mittig<br/>J1/J2/J4: unten<br/><br/>Nicht nach der Unterseitenansicht verdrahten. Anschlussnummern anhand der Gerber-Koordinaten und durch Durchgangsmessung kontrollieren. Die Silkscreen-Ecken allein sind keine hinreichende Pin-1-Kennzeichnung.',styles['BodyG'])
story.append(Table([[photo,legend]],colWidths=[175,330],style=[('VALIGN',(0,0),(-1,-1),'TOP')]))
h('Anschlussbelegung')
table([['Anschluss','Belegung'],['J1 Akku','1 BAT_FUSED (+ nach externer Sicherung),2 GND'],['J2 Taster','1 BUTTON_RAW (NO),2 GND (COM); NC bleibt frei'],['J3 Antenne','1 ANT; externe passende433-MHz-Antenne'],['J4 UPDI / U1','1 UPDI,2 Controller3V3,3 GND'],['J5 ISP / U4','1 MISO,2 TX3V3,3 SCK,4 MOSI,5 RESET,6 GND']], [105,400],True)
title(3,'Verdrahtung und Versorgung')
h('Orientierung anhand der Fertigungsdaten')
p('Koordinaten in Millimetern: Ursprung oben links, X nach rechts und Y nach unten. Gerber verwendet hierfÃ¼r negative Y-Werte. Diese Tabelle stammt direkt aus den Gerber-X2-Padzuordnungen.')
table([['Anschluss','Pin und Netz','X','Y unten'],*[[ref,f'{pin} {d["net"].lstrip("/")}',f'{d["x_mm"]:.2f}',f'{d["top_y_down_mm"]:.2f}'] for ref in ['J1','J2','J3','J4','J5'] for pin,d in pads[ref].items()]], [60,245,100,100],True)
h('AnschlieÃŸen')
p('Akku abziehen. Vorhandene T250-mA-Sicherung vor die gesamte Elektronik setzen. Sicherungsausgang an J1/1, Akku-Minus an J1/2. Taster-NO an J2/1 und COM an J2/2. An J2 keine9 V anlegen. Antenne an J3 anschlieÃŸen und Leitungen mechanisch sichern.')
h('Zwei getrennte3,3-V-Bereiche')
p('J4/2 versorgt U1 und heiÃŸt /3V3. J5/2 versorgt U4 und U5 und heiÃŸt /TX3V3. Diese AnschlÃ¼sse sind nicht austauschbar. FÃ¼r jeden Programmierschritt Akku abziehen, nur eine geregelte3,3-V-Quelle verwenden und den jeweils anderen Programmer entfernen. Kein5 V und keine Hochvolt-UPDI-Impulse einspeisen.')
title(4,'ATtiny402 Ã¼ber UPDI')
p('Alle neun Platinen erhalten dieselbe Datei <b>ATtiny402_HOLD_RevA.hex</b>. Die Datei ist bytegleich zur Rev-A-Controllerfirmware. Die Ãœbernahme belegt noch keinen erfolgreichen Betrieb auf Rev B.')
h('Vorbereitung und Anschluss')
bullet('Akku, ISP-Programmer und externe Versorgungen entfernen. Strombegrenzte3,3-V-Quelle vorbereiten.')
bullet('3,3-V-kompatiblen SerialUPDI-Adapter an J4 anschlieÃŸen: UPDI an1,3,3 V an2, GND an3. Ein reiner VTREF-Anschluss liefert keine Versorgung.')
bullet('Spannung an U1/1 gegen U1/8 vor Verbindung prÃ¼fen. COM7 in den Beispielen durch den echten Adapterport ersetzen.')
h('Schreiben und prÃ¼fen')
code('py -m pip install pymcuprog\npymcuprog ping -t uart -u COM7 -d attiny402\npymcuprog read -t uart -u COM7 -d attiny402 -m fuses\npymcuprog write -t uart -u COM7 -d attiny402 -f firmware/ATtiny402_HOLD_RevA.hex --erase --verify')
p('Die lange Schreibzeile ist ein einziger Befehl. Wird eine Signatur, Versorgung oder Fuseeinstellung anders als erwartet gemeldet: stoppen und Ursache klÃ¤ren. Kein erzwungenes Ãœberschreiben unbekannter GerÃ¤te.')
table([['Fuse / Offset','Sollwert','Bedeutung'],['WDTCFG /0','0x00','Watchdog von Firmware gesteuert'],['BODCFG /1','0x56','2,6-V-BOD laut Referenzprojekt'],['OSCCFG /2','0x7e','20-MHz-Oszillator; Firmware teilt auf5 MHz'],['SYSCFG0 /5','0xf6','UPDI bleibt aktiv'],['SYSCFG1 /6','0xff','Referenzwert'],['APPEND /7; BOOTEND /8','0x00;0x00','Referenzwerte']], [150,80,275],True)
p('Fuses zuerst rÃ¼cklesen. Beispiel fÃ¼r die bestÃ¤tigte BOD-Abweichung:','SmallG')
code('pymcuprog write -t uart -u COM7 -d attiny402 -m fuses -o 1 -l 0x56 --verify\npymcuprog read -t uart -u COM7 -d attiny402 -m fuses')
p('Weitere Abweichungen kontrolliert mit Microchip-Dokumentation und ATtiny402_fuses.json klÃ¤ren. Keine Lockbits setzen, UPDI nicht als GPIO umschalten. Zum Schluss Adapter und Versorgung entfernen.','SmallG')
title(5,'ATtiny13A Ã¼ber DIAMEX-ISP')
p('Jede der neun Platinen bekommt eine eindeutige Sender-ID1-9. ID ist keine Bahnnummer; die Zuordnung erfolgt im AdminmenÃ¼. EmpfÃ¤nger diamex-5 muss installiert sein. IDs6-9 unter Admin - Funktaster als eigenen Sender neu anlernen; die bisherigen IDs1-5 behalten ihre Zuordnung.')
table([['Platine / Beschriftung','Datei'],*[ [f'Buzzer {i}',f'ATtiny13A_V2_ID{i}.hex'] for i in range(1,10)]],[160,345])
h('Rev B nicht wie den alten V5-Aufbau programmieren')
p('<b>GedrÃ¼ckthalten des Buzzers genÃ¼gt nicht:</b> U1 schaltet die Senderversorgung nach nominal1000 ms ab. FÃ¼r ISP den Akku abziehen und /TX3V3 dauerhaft extern mit geregelten3,3 V Ã¼ber J5/2 versorgen. GND an J5/6. Beide Target-Versorgungsschalter des DIAMEX bleiben AUS. UPDI-Adapter und J4-Versorgung entfernen.')
p('J5 von oben: erste Reihe1 MISO /2 TX3V3; zweite Reihe3 SCK /4 MOSI; dritte Reihe5 RESET /6 GND. Kabelorientierung vor Anschluss per Durchgangsmessung prÃ¼fen.')
h('Beispiel mit AVRDUDE')
p('Im entpackten Paket arbeiten. AVRDUDE muss installiert und im Suchpfad sein. COM8 ist nur ein Beispiel. Vor Ã„nderungen Fuses sichern. -B50 entspricht dem bestehenden DIAMEX-Projekt.')
code('avrdude -p t13a -c stk500v2 -P COM8 -B 50 -U lfuse:r:lfuse.txt:h -U hfuse:r:hfuse.txt:h\navrdude -p t13a -c stk500v2 -P COM8 -B 50 -U flash:w:firmware/ATtiny13A_V2_ID1.hex:i')
p('Jede Zeile ist ein Befehl. ID1 im zweiten Befehl durch die passende ID ersetzen. AVRDUDE-Verifikation muss erfolgreich sein; -V und -F nicht verwenden. Flashen kann vorhandene EEPROM-EreigniszÃ¤hler zurÃ¼cksetzen.')
table([['Fuse','Soll'],['LFUSE','0x76'],['HFUSE','0xFB']],[130,375])
p('Nur bei bestÃ¤tigter Abweichung die vorgesehenen Werte schreiben und rÃ¼cklesen. RESET und SPIEN nicht deaktivieren, keine zusÃ¤tzlichen Lockbits setzen. Danach ISP und3,3-V-Quelle entfernen; erst dann Akku anschlieÃŸen. Ein tatsÃ¤chlicher Flashvorgang an Rev B wurde noch nicht nachgewiesen.')
title(6,'ErstprÃ¼fung am Prototyp')
p('Zuerst eine der neun Platinen vollstÃ¤ndig prÃ¼fen. Die Ã¼brigen erst nach erfolgreicher MusterprÃ¼fung in Betrieb nehmen. Die folgenden Punkte sind Abnahmekriterien, keine bereits gemessenen Ergebnisse.')
table([['PrÃ¼fung','Soll / Dokumentation'],['Sicht- und DurchgangsprÃ¼fung','Keine BrÃ¼cken; D1/D2-Kathode links; Versorgungsnetze gegen Gerber abgleichen'],['Strombegrenzter Erststart','Zuerst nominal9 V; Stromaufnahme und beide3,3-V-Rails beobachten; bei ErwÃ¤rmung/Einbruch sofort aus'],['Programmierung','U1-Fuses rÃ¼ckgelesen; U4-Fuses korrekt; beide Flash-Verifikationen erfolgreich'],['Einschalten / Reset','Kein Phantomereignis, auch mit gehaltenem Taster oder bei Unterspannung'],['Kurze Kontakte','1/2/5/10/20/50 ms einzeln erzeugen und Empfang protokollieren'],['Sendefenster','Nominal1000 ms; V2-Burst vollstÃ¤ndig; lang halten lÃ¶st nur einmal aus'],['Entladung / Neustart','100 ms Entladung +20 ms stabile Freigabe; TX-Rail vor Neustart unter0,3 V als Abnahmeziel'],['DrÃ¼cke in Sperrzeit','Kein Nachspeichern und kein verspÃ¤tetes AuslÃ¶sen'],['Akku','VERICO unter Last und nach langer Ruhe; Auto-off, Ruhestrom, ErwÃ¤rmung prÃ¼fen'],['Pi / Anwendung','Richtige ID und genau eine Aktion in Training, Quiz und Spielen'],['Mehrere Buzzer','Einzeln, zu zweit und gemeinsam; verlorene Funkereignisse dokumentieren'],['Funk / Mechanik','Antenne, Frequenz, Spektrum, Sendeleistung, Duty-Cycle, GehÃ¤use und Feuchtigkeit fachlich prÃ¼fen']], [140,365],True)
h('Messblatt fÃ¼hren')
p('FÃ¼r jedes GerÃ¤t notieren: Serienkennzeichnung, Sender-ID, Datum, Firmware-PrÃ¼fsummen, Akku, Spannungen, Ruhestrom, maximale Temperatur, Impulsdauer, Resetspannung und Empfangsergebnis. Oszilloskop/Logikanalysator fÃ¼r kurze VorgÃ¤nge verwenden; ein Multimeter allein reicht dafÃ¼r nicht.')
p('Neue STX883PRO-GerÃ¤te benÃ¶tigen eigene Funkmessungen. Die Messungen der alten V5-GerÃ¤te sind kein Nachweis fÃ¼r Rev B. Keine Genauigkeits- oder Wettkampfzulassung aus der CAD-PrÃ¼fung oder TimerauflÃ¶sung ableiten.')
title(7,'GeprÃ¼fter Bestellstand')
h('CAD, Footprint und Aufdruck')
bullet('KiCad8.0.9: DRC0 / ERC0 / Unconnected0 / ParitÃ¤t0. Die vier U5-Lands stimmen mit der JLCEDA/EasyEDA Official Library fÃ¼r C3001517 Ã¼berein. Quelle: https://lceda.cn/ und https://easyeda.com/.')
bullet('U5-Pads1-3:1,90 x2,70 mm; Pad4:2,00 x2,50 mm. Die TX3V3-Leiterbahn neben Pad1 wurde mit unverÃ¤ndertem0,20-mm-Mindestabstand angepasst.')
bullet('Aufdruck auf beiden Seiten: Buzzer Rev B0.10. Vorne35 SMD-Referenzen und Stecker-Pinnummern; hinten Pinlegenden und freies ID-Feld. Neue Schrift mindestens1,0 mm hoch bei0,15-mm-Strichen; native PrÃ¼fung auf Masken- und RandÃ¼berschneidungen bestanden.')
h('Finale numerische BestÃ¼ckung')
p('03_JLCPCB_REVB_B010_FINAL.csv ist die tatsÃ¤chlich neu importierte Datei. U1/U4:270 Grad. U2/U3 und Q1-Q4:180 Grad. D1/D2 und alle Ã¼brigen Referenzen:0 Grad. Negative Gerber-Y-Koordinaten. U5 verwendet den JLC-Bibliotheksversatz: X16,095019 / Y-13,022416 mm im CPL; das ist kein verschobener PCB-Footprint. Die physische Padreihe bleibt bei Y19,600 mm.')
p('Nach dem finalen Import keine manuellen Viewer-Ã„nderungen. Pin1 oben links, Diodenkathoden links, alle Anschlussreihen und das Funkmodul visuell auf den zugehÃ¶rigen Pads geprÃ¼ft. Das Archiv enthÃ¤lt die numerische Datei und ihren SHA-256. Die frÃ¼here B0.9-CPL ist keine Bestellgrundlage.')
table([['Referenz','Original','Genehmigter Ersatz'],*[r[:3] for r in sub]], [110,190,205],True)
h('Kosten und Gutscheine')
p('Bestellverlauf am19.11.2026 geprÃ¼ft: zehn Leiterplatten, davon neun Standard-PCBA. Dateiname: B010_S2; BOM und finale CPL wie im Archiv. Waren143,13 USD + Versand18,41 USD + Abgaben30,68 USD =192,22 USD. Auftrag zeigt In Produktion; Einzelpositionen noch Datenaufbereitung. Montage3-4 Tage laut Auftrag.')
p('Die Bestellung wurde vom Nutzer ausgelÃ¶st. Eine separate Gutscheinabrechnung und die endgÃ¼ltige Versandart wurden in dieser Ansicht nicht angezeigt. FrÃ¼here Sechserangebote und Coupon-SchÃ¤tzungen sind nicht der tatsÃ¤chliche Endpreis.')
h('Offen bleibt die Musterabnahme')
p('Beide Controller kommen unprogrammiert. Reale Versorgungs-, Akku-, Programmier-, GehÃ¤use- und FunkprÃ¼fungen sind nicht bestanden erklÃ¤rt. Erst ein Muster vollstÃ¤ndig abnehmen. IDs1 und6 teilen sich in der unverÃ¤nderten V2-Firmware die erste Wiederholungs-Zeitgruppe; den gleichzeitigen Betrieb aller neun deshalb ausdrÃ¼cklich testen.')

title(8,'Bauteilliste und PrÃ¼fstand')
table([['Referenzen','Wert / Funktion','LCSC'],*[[r['Designator'],r['Comment'],r['LCSC Part #']] for r in bom]],[190,195,120],True)
p('J1-J5 werden nicht maschinell bestÃ¼ckt. H1/H2 sind mechanische Bohrungen. Alle Firmwaredateien und Fertigungsreferenzen liegen im Archiv. Die Mess- und Freigabefelder bleiben bewusst offen.','SmallG')
h('Freigabevermerk')
p('Datei- und visuelle BestÃ¼ckungsprÃ¼fung:18.11.2026, archiviert.<br/>Metrischer C3001517-Abgleich:18.11.2026, archiviert.<br/>Muster elektrisch / Akku abgenommen: ______________________<br/>Funk / GehÃ¤use abgenommen: ______________________________<br/>PrÃ¼fer / verwendete GerÃ¤te: ______________________________')
title(9,'Dateien und Nachvollziehbarkeit')
table([['Ordner','Inhalt'],['documents/','Diese PDF sowie die textliche Anleitung'],['manufacturing/','GeprÃ¼fte S2-Gerber, genehmigte BOM und tatsÃ¤chlich importierte finale CPL'],['firmware/','Neun V2-HEX-Dateien, HOLD-HEX, PrÃ¼fsummen und Referenz-Fuses'],['evidence/','Gespeicherter JLCPCB-Bildexport und gelesener BOM-Beleg'],['validation/','Original-CAD-Berichte, Gerber-Padkoordinaten,35 EinzelprÃ¼fvermerke und offene Gates'],['source/','VollstÃ¤ndiger B0.10-S2-CAD-Stand, B0.3-Basis und Patchskripte'],['tools/','PrÃ¼fskript; keine automatische GerÃ¤teprogrammierung']], [115,390],True)
h('Originalstand')
p('GitHub-Repository: C31N/trainingsanzeige-releases<br/>Entwurfs-PR:#2<br/>Quellstand:B0.10-S2, finale JLC-CPL und zehn HEX-Dateien<br/>CI-Lauf:44374130631; native KiCad-Version8.0.9','SmallG')
h('Firmware verifizieren')
p('SHA256SUMS.txt unter firmware/ enthÃ¤lt die zehn originalen HEX-PrÃ¼fsummen. tools/verify_archive.py kontrolliert zusÃ¤tzlich die Archivdateien, BOM/CPL-Mengen und die dokumentierten PrÃ¼fstatus. Ein erfolgreicher Archivtest bedeutet keine Hardwarefreigabe.')
code('python tools/verify_archive.py')
h('Technische Quellen')
for s in ['https://github.com/C31N/trainingsanzeige-releases/pull/2','https://github.com/C31N/trainingsanzeige-releases/releases/tag/buzzer-hold-revA-0.1.0','https://github.com/microchip-pic-avr-tools/pymcuprog/blob/main/help.md','https://www.microchip.com/en-us/product/ATTINY402','https://www.ti.com/lit/ds/symlink/tps709.pdf','https://www.nicerf.com/ask-modules/ask-transmitter-module-stx883pro.html']:
 p(s,'SmallG')
p('Diese Anleitung dokumentiert B0.10-D2. Ã„ltere B0.2/B0.3-Archive und die Anleitung fÃ¼r die separate Rev-A-Platine sind keine austauschbaren Bestell- oder Verdrahtungsanleitungen.','SmallG')
title(10,'Bedruckte RÃ¼ckseite')
p('Ansicht von hinten, Antennenseite oben. Die Pinbezeichnungen entsprechen denselben physischen Kontakten wie auf der Vorderseite. Die Abbildung zeigt die tatsÃ¤chlich exportierte Beschriftung; keine Anschlussleitung wird allein aus einer Seitenansicht abgeleitet.')
story.append(Image(str(STAGE/'evidence/silkscreen-back.png'),width=240,height=560))
p('ID1-9 erst nach erfolgreicher Programmierung im freien Feld markieren. Die1-mm-Schrift wird weiÃŸ auf grÃ¼ner LÃ¶tstoppmaske gedruckt.','SmallG')

def footer(c,doc):
 c.saveState();c.setStrokeColor(colors.HexColor('#b6cbd8'));c.line(44,40,551,40);c.setFont('Guide',8);c.setFillColor(colors.HexColor('#486070'));c.drawString(44,27,'WFD | Rev B0.10 / D2 | Prototyp - Musterabnahme offen');c.drawRightString(551,27,str(doc.page));c.restoreState()
doc=SimpleDocTemplate(str(PDF),pagesize=(595.28,841.89),rightMargin=45,leftMargin=45,topMargin=42,bottomMargin=55,title='Buzzer Rev B0.10 - Beschreibung und Programmierung',author='Wasserfreunde Dalum')
OUT.mkdir(parents=True,exist_ok=True)
doc.build(story,onFirstPage=footer,onLaterPages=footer)
# PDF already written into documents/
(STAGE/'documents/ANLEITUNG_REVB_B010.md').write_text('# Buzzer Rev B0.10 - B0.10-D2\n\n'+'\n'.join(md),encoding='utf-8')
reader=PdfReader(str(PDF)); print('PDF pages:',len(reader.pages));assert len(reader.pages)==10,'Unexpected pagination: inspect layout'
print('STAGE',STAGE);print('PDF',PDF)
