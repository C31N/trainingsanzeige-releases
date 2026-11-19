# Buzzer Rev B0.9 - B0.9-D1

01  Buzzer Rev B0.9


## Buzzer Rev B0.9

Beschreibung, Anschluss, Programmierung und Erstprüfung

Wasserfreunde Dalum | Dokumentation B0.9-D1 | 18.11.2026

Status vor Bestellung

Prototyp. Noch keine Fertigungs- oder Einsatzfreigabe. Die CAD-Prüfung ist bestanden. Die Bestückung wurde im JLCPCB-Viewer visuell kontrolliert und D1/D2 wurden gedreht. Ein numerischer Export des nachbearbeiteten Live-Bestückungsstands fehlt. Deshalb ist das Archiv noch kein vollständig reproduzierbares Bestellpaket.

Merkmal | Stand

Platine | 30 x70 mm, FR4, 1,6 mm, 2 Lagen, 1 oz

Auftrag vorbereitet | 5 identische PCBs, 5 Top-Economic-PCBA

Bestückung | 35 SMD-Referenzen, 19 LCSC-Typen

Controller U1 | ATtiny402: Impulsverlängerung, UPDI

Sendersteuerung U4 | ATtiny13A: V2-Firmware, IDs1-5, ISP

Funkmodul U5 | STX883PRO-433MHz, Versorgung3,3 V

Lieferzustand | Unprogrammiert; J1-J5, Taster, Antenne und Akku manuell

Was gegenüber V5 anders ist

Rev B integriert den bisherigen Sender und die Rev-A-Impulsverlängerung auf einer Platine. Statt STX882 und R-78E werden STX883PRO und ein zweiter TPS70933 verwendet. Vorhandene V2-IDs1-5 bleiben vorgesehen; die neue Funkhardware muss trotzdem am realen Gerät geprüft werden.

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

Alle fünf Platinen erhalten dieselbe Datei ATtiny402_HOLD_RevA.hex. Die Datei ist bytegleich zur Rev-A-Controllerfirmware. Die Übernahme belegt noch keinen erfolgreichen Betrieb auf Rev B.

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

Jede Platine bekommt eine eindeutige Sender-ID. ID ist keine Bahnnummer; die Zuordnung erfolgt weiterhin im Adminmenü. Empfänger diamex-5 muss vor dem V2-Betrieb installiert sein.

Platine / Beschriftung | Datei

Buzzer 1 | ATtiny13A_V2_ID1.hex

Buzzer 2 | ATtiny13A_V2_ID2.hex

Buzzer 3 | ATtiny13A_V2_ID3.hex

Buzzer 4 | ATtiny13A_V2_ID4.hex

Buzzer 5 | ATtiny13A_V2_ID5.hex

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

Zuerst eine der fünf Platinen vollständig prüfen. Die übrigen erst nach erfolgreicher Musterprüfung in Betrieb nehmen. Die folgenden Punkte sind Abnahmekriterien, keine bereits gemessenen Ergebnisse.

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

07  Bestellstand und offene Freigaben


## Bestellstand und offene Freigaben

Gesichert und abgeglichen

- Originaler B0.9-CI-Export unverändert archiviert; dessen Firmwareprüfsummen stimmen. KiCad8.0.9: DRC0, ERC0, Unconnected0, Parität0.

- 19 BOM-Gruppen und35 Referenzen passen zum gespeicherten JLCPCB-Warenkorb. Die Ersatztypen sind in der genehmigten BOM enthalten.

Referenz | Original | Ersatz

C3,C6 | C415536 | C76639

C8 | C2835529 | C6119932

R13 | C2889503 | C114523

- D1 und D2 wurden relativ zur importierten CPL im Viewer um180 Grad gedreht. Der gespeicherte Bildexport zeigt die Kathoden links. U1/U4, U2/U3, Q1-Q4, U5 sowie sämtliche Passivteile wurden visuell betrachtet.

Was das Archiv ausdrücklich nicht enthält

Keine bestätigte finale numerische Live-CPL. JLCPCB exportiert über die verfügbare Viewer-Schaltfläche ein PNG, nicht die nachbearbeiteten Koordinaten/Rotationen. Die archivierten Original- und Y-negativ-CPLs enthalten die manuellen Dreh-/Lagekorrekturen nicht. Sie sind nur Referenzdateien und dürfen nicht ungeprüft wieder hochgeladen werden.

Das Bild ist keine Quelle für Fertigungskoordinaten. Der metrische Abgleich des JLCPCB-STX883PRO-Landpatterns bleibt offen. Ebenso fehlen reale Versorgungs-, Akku-, Programmier- und Funkabnahmen.

Nächster notwendiger Schritt vor Bestellung

Den finalen numerischen Pick-and-Place-Stand vom JLCPCB-Entwurf beschaffen oder die Platzierung aus verifizierten Hersteller-Landpatterns reproduzierbar neu aufbauen. Danach alle35 Referenzen erneut mit Gerberpads, Pin1 und Polarität vergleichen. Erst dann eine Prototypenfertigung bewusst freigeben. Der bestehende Entwurf bleibt bis dahin gesperrt.

Kostenmomentaufnahme

Browserstand18.11.2026: PCB+PCBA102,39 USD, Global Standard Direct Line9,87 USD, ausgewiesene Abgaben26,89 USD, zusammen139,15 USD vor Gutscheinen. Ein SMT-Neukundengutschein über10 USD war hinterlegt, aber nicht angewendet. Preise sind keine Garantie; Kontaktdaten und Checkout-Zugänge gehören nicht in dieses öffentliche Archiv.

08  Bauteilliste und Prüfstand


## Bauteilliste und Prüfstand

Referenzen | Wert / Funktion | LCSC

R15 | 330R | C105878

U1 | ATtiny402-SSN | C1339884

U4 | ATtiny13A V2 | C14075

Q1 | AO3407A HS | C15155

C1,C4,C7,C9 | 100n | C1711

Q3 | AO3400A | C20917

D1 | BZT52C10 | C2103

D2 | SS14 Reverse | C2480

C8 | 10u | C6119932

R13 | 150R | C114523

U5 | STX883PRO-433MHz | C3001517

C3,C6 | 4.7u | C76639

Q2,Q4 | MMBT3904 | C7422625

C2,C5 | 1u | C77080

R1,R4,R5,R7,R9,R12,R14 | 10k | C84376

R11 | 100R | C844884

U2,U3 | TPS70933 | C89347

R2 | 1k | C95781

R3,R6,R8,R10 | 100k | C96346

J1-J5 werden nicht maschinell bestückt. H1/H2 sind mechanische Bohrungen. Alle Firmwaredateien und Fertigungsreferenzen liegen im Archiv. Die Mess- und Freigabefelder bleiben bewusst offen.

Freigabevermerk

Numerische Bestückung geprüft: __________  Datum: __________Landpattern geprüft: __________________  Datum: __________Muster elektrisch / Akku abgenommen: ______________________Funk / Gehäuse abgenommen: ______________________________Prüfer / verwendete Geräte: ______________________________

09  Dateien und Nachvollziehbarkeit


## Dateien und Nachvollziehbarkeit

Ordner | Inhalt

documents/ | Diese PDF sowie die textliche Anleitung

manufacturing/ | Unveränderte Gerber, genehmigte BOM, zwei ausdrücklich unvollständige CPL-Referenzen

firmware/ | Fünf V2-HEX-Dateien, HOLD-HEX, Prüfsummen und Referenz-Fuses

evidence/ | Gespeicherter JLCPCB-Bildexport und gelesener BOM-Beleg

validation/ | Original-CAD-Berichte, Gerber-Padkoordinaten,35 Einzelprüfvermerke und offene Gates

source/ | B0.3-Quellarchiv und unveränderter B0.9-CI-Prototypenexport

tools/ | Prüfskript; keine automatische Geräteprogrammierung

Originalstand

GitHub-Repository: C31N/trainingsanzeige-releasesEntwurfs-PR:#2Basis-Commit:09f80822e131fa1d7f6cef4a08b638c0d64b4231CI-Lauf:44295672022 (Run42)CI-Artefakt:14423023781

Firmware verifizieren

SHA256SUMS.txt unter firmware/ enthält die sechs originalen HEX-Prüfsummen. tools/verify_archive.py kontrolliert zusätzlich die Archivdateien, BOM/CPL-Referenzmengen und die bewusst offenen Freigaben. Ein erfolgreicher Archivtest bedeutet keine Hardwarefreigabe.

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

Diese Anleitung dokumentiert B0.9-D1. Ältere B0.2/B0.3-Archive und die Anleitung für die separate Rev-A-Platine sind keine austauschbaren Bestell- oder Verdrahtungsanleitungen.
