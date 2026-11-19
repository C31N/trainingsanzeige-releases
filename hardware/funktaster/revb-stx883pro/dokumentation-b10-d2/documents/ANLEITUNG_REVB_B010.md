# Buzzer Rev B0.10 - B0.10-D2

01  Buzzer Rev B0.10


## Buzzer Rev B0.10

Beschreibung, Anschluss, Programmierung und Erstprüfung

Wasserfreunde Dalum | Dokumentation B0.10-D2 | 19.11.2026

Bestellter Prototypenstand

Neun bestückte Prototypen bestellt; Musterabnahme steht aus. Die native CAD-Prüfung und der metrische C3001517-Abgleich sind bestanden. Die finale numerische Bestückungsdatei wurde erneut importiert und alle35 Referenzen wurden visuell geprüft. Nach diesem Import wurden keine Drehungen oder Positionen im Viewer geändert. Schaltung, Akku und Funk müssen nach Lieferung am Muster geprüft werden.

Merkmal | Stand

Platine | 30 x70 mm, FR4, 1,6 mm, 2 Lagen, 1 oz

Bestellter Auftrag | 10 PCBs, davon9 Top-Standard-PCBA;1 unbestückt

Bestückung | 35 SMD-Referenzen, 19 LCSC-Typen

Controller U1 | ATtiny402: Impulsverlängerung, UPDI

Sendersteuerung U4 | ATtiny13A: V2-Firmware, IDs1-9, ISP

Funkmodul U5 | STX883PRO-433MHz, Versorgung3,3 V

Lieferzustand | Unprogrammiert; J1-J5, Taster, Antenne und Akku manuell

Was gegenüber V5 anders ist

Rev B integriert den bisherigen Sender und die Rev-A-Impulsverlängerung auf einer Platine. Statt STX882 und R-78E werden STX883PRO und ein zweiter TPS70933 verwendet. Vorhandene V2-IDs1-9 bleiben vorgesehen; die neue Funkhardware muss trotzdem am realen Gerät geprüft werden.

Der Taster liefert nur einen potentialfreien Kontakt gegen Masse. U1 hält den Sender nominal1000 ms eingeschaltet, sperrt weitere Drücke und ermöglicht danach Entladung und erneute Freigabe. Ein sicher erfasster1-ms-Druck ist weiterhin ein Messziel.

02  Bauteile und Anschlüsse


## Bauteile und Anschlüsse

Anschlussbelegung

Anschluss | Belegung

J1 Akku | 1 BAT_FUSED (+ nach externer Sicherung),2 GND

J2 Taster | 1 BUTTON_RAW (NO),2 GND (COM); NC bleibt frei

J3 Antenne | 1 ANT; externe passende433-MHz-Antenne

J4 UPDI / U1 | 1 UPDI,2 Controller3V3,3 GND

J5 ISP / U4 | 1 MISO,2 TX3V3,3 SCK,4 MOSI,5 RESET,6 GND

03  Verdrahtung und Versorgung


## Verdrahtung und Versorgung

Orientierung anhand der Fertigungsdaten

Koordinaten in Millimetern: Ursprung oben links, X nach rechts und Y nach unten. Gerber verwendet hierfür negative Y-Werte. Diese Tabelle stammt direkt aus den Gerber-X2-Padzuordnungen.

Anschluss | Pin und Netz | X | Y unten

J1 | 1 BAT_FUSED | 5.20 | 64.00

J1 | 2 GND | 5.20 | 66.54

J2 | 1 BUTTON_RAW | 13.00 | 64.00

J2 | 2 GND | 13.00 | 66.54

J3 | 1 ANT | 19.73 | 3.20

J4 | 1 UPDI | 20.50 | 63.20

J4 | 2 3V3 | 20.50 | 65.74

J4 | 3 GND | 20.50 | 68.28

J5 | 1 MISO | 5.00 | 35.00

J5 | 2 TX3V3 | 7.54 | 35.00

J5 | 3 SCK | 5.00 | 37.54

J5 | 4 MOSI | 7.54 | 37.54

J5 | 5 RESET | 5.00 | 40.08

J5 | 6 GND | 7.54 | 40.08

Anschließen

Akku abziehen. Vorhandene T250-mA-Sicherung vor die gesamte Elektronik setzen. Sicherungsausgang an J1/1, Akku-Minus an J1/2. Taster-NO an J2/1 und COM an J2/2. An J2 keine9 V anlegen. Antenne an J3 anschließen und Leitungen mechanisch sichern.

Zwei getrennte3,3-V-Bereiche

J4/2 versorgt U1 und heißt /3V3. J5/2 versorgt U4 und U5 und heißt /TX3V3. Diese Anschlüsse sind nicht austauschbar. Für jeden Programmierschritt Akku abziehen, nur eine geregelte3,3-V-Quelle verwenden und den jeweils anderen Programmer entfernen. Kein5 V und keine Hochvolt-UPDI-Impulse einspeisen.

04  ATtiny402 über UPDI


## ATtiny402 über UPDI

Alle neun Platinen erhalten dieselbe Datei ATtiny402_HOLD_RevA.hex. Die Datei ist bytegleich zur Rev-A-Controllerfirmware. Die Übernahme belegt noch keinen erfolgreichen Betrieb auf Rev B.

Vorbereitung und Anschluss

- Akku, ISP-Programmer und externe Versorgungen entfernen. Strombegrenzte3,3-V-Quelle vorbereiten.

- 3,3-V-kompatiblen SerialUPDI-Adapter an J4 anschließen: UPDI an1,3,3 V an2, GND an3. Ein reiner VTREF-Anschluss liefert keine Versorgung.

- Spannung an U1/1 gegen U1/8 vor Verbindung prüfen. COM7 in den Beispielen durch den echten Adapterport ersetzen.

Schreiben und prüfen

```powershell
py -m pip install pymcuprog
pymcuprog ping -t uart -u COM7 -d attiny402
pymcuprog read -t uart -u COM7 -d attiny402 -m fuses
pymcuprog write -t uart -u COM7 -d attiny402 -f firmware/ATtiny402_HOLD_RevA.hex --erase --verify
```

Die lange Schreibzeile ist ein einziger Befehl. Wird eine Signatur, Versorgung oder Fuseeinstellung anders als erwartet gemeldet: stoppen und Ursache klären. Kein erzwungenes Überschreiben unbekannter Geräte.

Fuse / Offset | Sollwert | Bedeutung

WDTCFG /0 | 0x00 | Watchdog von Firmware gesteuert

BODCFG /1 | 0x56 | 2,6-V-BOD laut Referenzprojekt

OSCCFG /2 | 0x7e | 20-MHz-Oszillator; Firmware teilt auf5 MHz

SYSCFG0 /5 | 0xf6 | UPDI bleibt aktiv

SYSCFG1 /6 | 0xff | Referenzwert

APPEND /7; BOOTEND /8 | 0x00;0x00 | Referenzwerte

Fuses zuerst rücklesen. Beispiel für die bestätigte BOD-Abweichung:

```powershell
pymcuprog write -t uart -u COM7 -d attiny402 -m fuses -o 1 -l 0x56 --verify
pymcuprog read -t uart -u COM7 -d attiny402 -m fuses
```

Weitere Abweichungen kontrolliert mit Microchip-Dokumentation und ATtiny402_fuses.json klären. Keine Lockbits setzen, UPDI nicht als GPIO umschalten. Zum Schluss Adapter und Versorgung entfernen.

05  ATtiny13A über DIAMEX-ISP


## ATtiny13A über DIAMEX-ISP

Jede der neun Platinen bekommt eine eindeutige Sender-ID1-9. ID ist keine Bahnnummer; die Zuordnung erfolgt im Adminmenü. Empfänger diamex-5 muss installiert sein. IDs6-9 unter Admin - Funktaster als eigenen Sender neu anlernen; die bisherigen IDs1-5 behalten ihre Zuordnung.

Platine / Beschriftung | Datei

Buzzer 1 | ATtiny13A_V2_ID1.hex

Buzzer 2 | ATtiny13A_V2_ID2.hex

Buzzer 3 | ATtiny13A_V2_ID3.hex

Buzzer 4 | ATtiny13A_V2_ID4.hex

Buzzer 5 | ATtiny13A_V2_ID5.hex

Buzzer 6 | ATtiny13A_V2_ID6.hex

Buzzer 7 | ATtiny13A_V2_ID7.hex

Buzzer 8 | ATtiny13A_V2_ID8.hex

Buzzer 9 | ATtiny13A_V2_ID9.hex

Rev B nicht wie den alten V5-Aufbau programmieren

Gedrückthalten des Buzzers genügt nicht: U1 schaltet die Senderversorgung nach nominal1000 ms ab. Für ISP den Akku abziehen und /TX3V3 dauerhaft extern mit geregelten3,3 V über J5/2 versorgen. GND an J5/6. Beide Target-Versorgungsschalter des DIAMEX bleiben AUS. UPDI-Adapter und J4-Versorgung entfernen.

J5 von oben: erste Reihe1 MISO /2 TX3V3; zweite Reihe3 SCK /4 MOSI; dritte Reihe5 RESET /6 GND. Kabelorientierung vor Anschluss per Durchgangsmessung prüfen.

Beispiel mit AVRDUDE

Im entpackten Paket arbeiten. AVRDUDE muss installiert und im Suchpfad sein. COM8 ist nur ein Beispiel. Vor Änderungen Fuses sichern. -B50 entspricht dem bestehenden DIAMEX-Projekt.

```powershell
avrdude -p t13a -c stk500v2 -P COM8 -B 50 -U lfuse:r:lfuse.txt:h -U hfuse:r:hfuse.txt:h
avrdude -p t13a -c stk500v2 -P COM8 -B 50 -U flash:w:firmware/ATtiny13A_V2_ID1.hex:i
```

Jede Zeile ist ein Befehl. ID1 im zweiten Befehl durch die passende ID ersetzen. AVRDUDE-Verifikation muss erfolgreich sein; -V und -F nicht verwenden. Flashen kann vorhandene EEPROM-Ereigniszähler zurücksetzen.

Fuse | Soll

LFUSE | 0x76

HFUSE | 0xFB

Nur bei bestätigter Abweichung die vorgesehenen Werte schreiben und rücklesen. RESET und SPIEN nicht deaktivieren, keine zusätzlichen Lockbits setzen. Danach ISP und3,3-V-Quelle entfernen; erst dann Akku anschließen. Ein tatsächlicher Flashvorgang an Rev B wurde noch nicht nachgewiesen.

06  Erstprüfung am Prototyp


## Erstprüfung am Prototyp

Zuerst eine der neun Platinen vollständig prüfen. Die übrigen erst nach erfolgreicher Musterprüfung in Betrieb nehmen. Die folgenden Punkte sind Abnahmekriterien, keine bereits gemessenen Ergebnisse.

Prüfung | Soll / Dokumentation

Sicht- und Durchgangsprüfung | Keine Brücken; D1/D2-Kathode links; Versorgungsnetze gegen Gerber abgleichen

Strombegrenzter Erststart | Zuerst nominal9 V; Stromaufnahme und beide3,3-V-Rails beobachten; bei Erwärmung/Einbruch sofort aus

Programmierung | U1-Fuses rückgelesen; U4-Fuses korrekt; beide Flash-Verifikationen erfolgreich

Einschalten / Reset | Kein Phantomereignis, auch mit gehaltenem Taster oder bei Unterspannung

Kurze Kontakte | 1/2/5/10/20/50 ms einzeln erzeugen und Empfang protokollieren

Sendefenster | Nominal1000 ms; V2-Burst vollständig; lang halten löst nur einmal aus

Entladung / Neustart | 100 ms Entladung +20 ms stabile Freigabe; TX-Rail vor Neustart unter0,3 V als Abnahmeziel

Drücke in Sperrzeit | Kein Nachspeichern und kein verspätetes Auslösen

Akku | VERICO unter Last und nach langer Ruhe; Auto-off, Ruhestrom, Erwärmung prüfen

Pi / Anwendung | Richtige ID und genau eine Aktion in Training, Quiz und Spielen

Mehrere Buzzer | Einzeln, zu zweit und gemeinsam; verlorene Funkereignisse dokumentieren

Funk / Mechanik | Antenne, Frequenz, Spektrum, Sendeleistung, Duty-Cycle, Gehäuse und Feuchtigkeit fachlich prüfen

Messblatt führen

Für jedes Gerät notieren: Serienkennzeichnung, Sender-ID, Datum, Firmware-Prüfsummen, Akku, Spannungen, Ruhestrom, maximale Temperatur, Impulsdauer, Resetspannung und Empfangsergebnis. Oszilloskop/Logikanalysator für kurze Vorgänge verwenden; ein Multimeter allein reicht dafür nicht.

Neue STX883PRO-Geräte benötigen eigene Funkmessungen. Die Messungen der alten V5-Geräte sind kein Nachweis für Rev B. Keine Genauigkeits- oder Wettkampfzulassung aus der CAD-Prüfung oder Timerauflösung ableiten.

07  Geprüfter Bestellstand


## Geprüfter Bestellstand

CAD, Footprint und Aufdruck

- KiCad8.0.9: DRC0 / ERC0 / Unconnected0 / Parität0. Die vier U5-Lands stimmen mit der JLCEDA/EasyEDA Official Library für C3001517 überein. Quelle: https://lceda.cn/ und https://easyeda.com/.

- U5-Pads1-3:1,90 x2,70 mm; Pad4:2,00 x2,50 mm. Die TX3V3-Leiterbahn neben Pad1 wurde mit unverändertem0,20-mm-Mindestabstand angepasst.

- Aufdruck auf beiden Seiten: Buzzer Rev B0.10. Vorne35 SMD-Referenzen und Stecker-Pinnummern; hinten Pinlegenden und freies ID-Feld. Neue Schrift mindestens1,0 mm hoch bei0,15-mm-Strichen; native Prüfung auf Masken- und Randüberschneidungen bestanden.

Finale numerische Bestückung

03_JLCPCB_REVB_B010_FINAL.csv ist die tatsächlich neu importierte Datei. U1/U4:270 Grad. U2/U3 und Q1-Q4:180 Grad. D1/D2 und alle übrigen Referenzen:0 Grad. Negative Gerber-Y-Koordinaten. U5 verwendet den JLC-Bibliotheksversatz: X16,095019 / Y-13,022416 mm im CPL; das ist kein verschobener PCB-Footprint. Die physische Padreihe bleibt bei Y19,600 mm.

Nach dem finalen Import keine manuellen Viewer-Änderungen. Pin1 oben links, Diodenkathoden links, alle Anschlussreihen und das Funkmodul visuell auf den zugehörigen Pads geprüft. Das Archiv enthält die numerische Datei und ihren SHA-256. Die frühere B0.9-CPL ist keine Bestellgrundlage.

Referenz | Original | Genehmigter Ersatz

C3,C6 | C415536 | C76639

C8 | C2835529 | C6119932

R13 | C2889503 | C114523

Kosten und Gutscheine

Bestellverlauf am19.11.2026 geprüft: zehn Leiterplatten, davon neun Standard-PCBA. Dateiname: B010_S2; BOM und finale CPL wie im Archiv. Waren143,13 USD + Versand18,41 USD + Abgaben30,68 USD =192,22 USD. Auftrag zeigt In Produktion; Einzelpositionen noch Datenaufbereitung. Montage3-4 Tage laut Auftrag.

Die Bestellung wurde vom Nutzer ausgelöst. Eine separate Gutscheinabrechnung und die endgültige Versandart wurden in dieser Ansicht nicht angezeigt. Frühere Sechserangebote und Coupon-Schätzungen sind nicht der tatsächliche Endpreis.

Offen bleibt die Musterabnahme

Beide Controller kommen unprogrammiert. Reale Versorgungs-, Akku-, Programmier-, Gehäuse- und Funkprüfungen sind nicht bestanden erklärt. Erst ein Muster vollständig abnehmen. IDs1 und6 teilen sich in der unveränderten V2-Firmware die erste Wiederholungs-Zeitgruppe; den gleichzeitigen Betrieb aller neun deshalb ausdrücklich testen.

08  Bauteilliste und Prüfstand


## Bauteilliste und Prüfstand

Referenzen | Wert / Funktion | LCSC

R15 | 330R | C105878

R13 | 150R | C114523

U1 | ATtiny402-SSN | C1339884

U4 | ATtiny13A V2 | C14075

Q1 | AO3407A HS | C15155

C1,C4,C7,C9 | 100n | C1711

Q3 | AO3400A | C20917

D1 | BZT52C10 | C2103

D2 | SS14 Reverse | C2480

U5 | STX883PRO-433MHz | C3001517

C8 | 10u | C6119932

Q2,Q4 | MMBT3904 | C7422625

C3,C6 | 4.7u | C76639

C2,C5 | 1u | C77080

R1,R4,R5,R7,R9,R12,R14 | 10k | C84376

R11 | 100R | C844884

U2,U3 | TPS70933 | C89347

R2 | 1k | C95781

R3,R6,R8,R10 | 100k | C96346

J1-J5 werden nicht maschinell bestückt. H1/H2 sind mechanische Bohrungen. Alle Firmwaredateien und Fertigungsreferenzen liegen im Archiv. Die Mess- und Freigabefelder bleiben bewusst offen.

Freigabevermerk

Datei- und visuelle Bestückungsprüfung:18.11.2026, archiviert.Metrischer C3001517-Abgleich:18.11.2026, archiviert.Muster elektrisch / Akku abgenommen: ______________________Funk / Gehäuse abgenommen: ______________________________Prüfer / verwendete Geräte: ______________________________

09  Dateien und Nachvollziehbarkeit


## Dateien und Nachvollziehbarkeit

Ordner | Inhalt

documents/ | Diese PDF sowie die textliche Anleitung

manufacturing/ | Geprüfte S2-Gerber, genehmigte BOM und tatsächlich importierte finale CPL

firmware/ | Neun V2-HEX-Dateien, HOLD-HEX, Prüfsummen und Referenz-Fuses

evidence/ | Gespeicherter JLCPCB-Bildexport und gelesener BOM-Beleg

validation/ | Original-CAD-Berichte, Gerber-Padkoordinaten,35 Einzelprüfvermerke und offene Gates

source/ | Vollständiger B0.10-S2-CAD-Stand, B0.3-Basis und Patchskripte

tools/ | Prüfskript; keine automatische Geräteprogrammierung

Originalstand

GitHub-Repository: C31N/trainingsanzeige-releasesEntwurfs-PR:#2Quellstand:B0.10-S2, finale JLC-CPL und zehn HEX-DateienCI-Lauf:44374130631; native KiCad-Version8.0.9

Firmware verifizieren

SHA256SUMS.txt unter firmware/ enthält die zehn originalen HEX-Prüfsummen. tools/verify_archive.py kontrolliert zusätzlich die Archivdateien, BOM/CPL-Mengen und die dokumentierten Prüfstatus. Ein erfolgreicher Archivtest bedeutet keine Hardwarefreigabe.

```powershell
python tools/verify_archive.py
```

Technische Quellen

https://github.com/C31N/trainingsanzeige-releases/pull/2

https://github.com/C31N/trainingsanzeige-releases/releases/tag/buzzer-hold-revA-0.1.0

https://github.com/microchip-pic-avr-tools/pymcuprog/blob/main/help.md

https://www.microchip.com/en-us/product/ATTINY402

https://www.ti.com/lit/ds/symlink/tps709.pdf

https://www.nicerf.com/ask-modules/ask-transmitter-module-stx883pro.html

Diese Anleitung dokumentiert B0.10-D2. Ältere B0.2/B0.3-Archive und die Anleitung für die separate Rev-A-Platine sind keine austauschbaren Bestell- oder Verdrahtungsanleitungen.

10  Bedruckte Rückseite


## Bedruckte Rückseite

Ansicht von hinten, Antennenseite oben. Die Pinbezeichnungen entsprechen denselben physischen Kontakten wie auf der Vorderseite. Die Abbildung zeigt die tatsächlich exportierte Beschriftung; keine Anschlussleitung wird allein aus einer Seitenansicht abgeleitet.

ID1-9 erst nach erfolgreicher Programmierung im freien Feld markieren. Die1-mm-Schrift wird weiß auf grüner Lötstoppmaske gedruckt.
