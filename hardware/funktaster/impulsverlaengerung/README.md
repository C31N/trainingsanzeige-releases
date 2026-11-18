# Buzzer-Impulsverlängerung Rev A

Das vollständige Paket einschließlich KiCad, Fertigungsdaten und Firmware steht im [Hardware-Release](https://github.com/C31N/trainingsanzeige-releases/releases/tag/buzzer-hold-revA-0.1.0).

**PROTOTYP – NOCH NICHT AM REALEN BUZZER FREIGEGEBEN.**

Bestellunterlagen, Firmware und Softwareprüfungen sind vorbereitet. Elektrische
Messungen, Akkutest und Funkabnahme stehen aus. Ein zuverlässig erkannter
1-ms-Kontakt ist ein Abnahmeziel, noch kein nachgewiesener Hardwaremesswert.

## Funktion

Der V5-Taster unterbricht beim Loslassen die Versorgung der gesamten Senderplatine.
Die Zusatzplatine erfasst den ersten gefilterten Schließkontakt und schaltet den
vorhandenen Sender unabhängig von der Druckdauer für nominal **1.000 ms** ein.
ATtiny13A, Senderfirmware, EEPROM, Funkcode und STX882 bleiben erhalten.

Während der Sendefolge bleiben weitere Drücke gesperrt. Sie werden nicht
gespeichert oder verspätet ausgeführt. Danach folgen **100 ms Entladung** und
**20 ms durchgehend losgelassener Taster**. Der nächste Druck ist damit frühestens
nach etwa 1,12 s möglich, zuzüglich Taktabweichung und Schaltreserve. Lang halten
sendet einmal. Beim Anschließen mit gedrücktem Taster wird zunächst nichts gesendet.

Die Platine ist für den bestätigten VERICO-Akku und **6–12 V Eingang** vorgesehen.
Sie schaltet vor dem vorhandenen R-78E3.3-0.5. Ein eigener TPS70933 versorgt den
ATtiny402 mit 3,3 V. Funkübertragungen bleiben unquittiert; Funkstörungen und
Kollisionen lassen sich durch eine Impulsverlängerung allein nicht ausschließen.

## Dateien und Bestellung

- `documents/Anleitung_RevA.pdf`: Anschluss, Programmierung und Abnahme.
- `documents/Bestueckung_RevA.pdf`: Oberseite und Anschlussbelegung.
- `documents/Schaltplan_RevA.pdf`: pinbeschrifteter Funktionsschaltplan.
- `kicad/buzzer-hold.kicad_pro`, `.kicad_sch`, `.kicad_pcb`: KiCad-8-Projekt.
- `kicad/WFD.kicad_sym`, `kicad/WFD.pretty`: lokale Symbole und Footprints.
- `manufacturing/`: Gerber X2, Excellon-Bohrdaten, Positionen und Fertigungs-ZIP.
- `BOM.csv`: Einzelpositionen mit Bestellbezeichnungen.
- `firmware/`: C-Quellen, HEX/BIN, Fusewerte und Buildmanifest mit Prüfsummen.
- `validation/`: tatsächlich durchgeführte Softwareprüfungen und offene Hardwareabnahme.

Bestellvorgabe: **30 × 25 mm**, zwei Lagen, FR4 1,6 mm, 35 µm Kupfer, Lötstopp
beidseitig, Bestückungsdruck oben, durchkontaktierte Bohrungen. Vor Bestellung
Gehäuseplatz, Bauhöhe und Drahtführung messen. Die Platine hat keine
Befestigungsbohrungen: mit isolierendem Halter befestigen. Zunächst einen
Prototyp bestücken und messen. Ersatztypen erfordern erneuten Pin- und Gehäuseabgleich.

## Schaltung und Orientierung

U2 **TPS70933DBVR**: Pin 1 IN, 2 GND, 3 EN offen, 4 NC, 5 OUT. EN ist intern
aktiviert; die Batteriespannung darf nicht an EN gelegt werden. C2 ist der
1-µF-Eingangskondensator, C3 der 4,7-µF-Ausgangskondensator und C1 die lokale
100-nF-Abblockung. Das abweichende Pinout anderer TPS709-Varianten beachten.

PA1 schaltet Q2 über R5. Q2 zieht das Gate des P-Kanal-MOSFETs Q1 über R4 herunter.
R3 hält Q1 bei Reset aus; D1 begrenzt dessen Gate-Source-Spannung. Masse bleibt
verbunden, nur der Pluspol wird geschaltet.

Q3 **AO3400A** entlädt den Ausgang über R11 **100 Ω / 1 W**. R7/R8 definieren
das Gate. Q4 blockiert die Entladung hardwareseitig, solange POWER aktiv ist.
Die Firmware schaltet vor dem Einschalten die Entladung aus; beim Ausschalten
wartet sie zusätzlich 1 ms vor dem Entladen. R11 ist für den kurzen Entladeimpuls
vorgesehen, nicht als Dauerlast bei eingeschaltetem Ausgang.

R1 (10 kΩ), R2 (1 kΩ) und C4 (100 nF) filtern den Tastereingang.
Die fallende Flanke wird damit im Bereich von etwa 0,1 ms geglättet. Die erste Flanke löst aus; nachfolgendes
Prellen bleibt bis zur stabilen Freigabe gesperrt. U1 PA2 ist der asynchron
aufweckbare Eingang. PA6/PA7 bleiben frei, PA0 bleibt UPDI.

Bei Blick auf die Bestückungsseite kennzeichnet das quadratische Pad jeweils
Pin 1. J1/J2/J3 haben Pin 1 oben, Pin 2 darunter. J4 hat Pin 1 oben, Pin 3 unten.
U1-Pin 1, D1-Kathode und Transistoranschlüsse nach Bestückungsplan und
Herstellerdatenblatt kontrollieren. Die Unterseite ist spiegelverkehrt.

## Anschluss an die vorhandene V5-Platine

1. Akku und DIAMEX abziehen. COM/NO durchmessen; NC bleibt frei.
2. Bisherige Verbindungen Sicherung → Taster COM und Taster NO → V5 09-A lösen.
3. Sicherungsausgang an **J1 Pin 1 BAT+**, Akku-Minus an **J1 Pin 2 GND**.
4. Taster NO an **J2 Pin 1 KEY**, COM an **J2 Pin 2 GND**. Hier ausschließlich
   den potentialfreien Kontakt anschließen, keine Akkuspannung.
5. **J3 Pin 1 OUT+ an V5 09-A/VIN**, **J3 Pin 2 GND an V5 07-A/GND**.
6. R-78E3.3-0.5, Kondensatoren und den 330-Ω-Widerstand der V5-Platine belassen.
   Den V5-Widerstand nicht mit R4 dieser Zusatzplatine verwechseln.
7. Leitungen kurz, isoliert und zugentlastet führen; Abstand zur Antenne halten.
   Bestehende Sicherung vor der gesamten Elektronik belassen.
8. Erst mit strombegrenztem Labornetzteil prüfen, dann den Akku anschließen.

J1, J3 und J4 dienen zugleich als Messpunkte für Akku, geschalteten Ausgang,
3,3-V-Rail, UPDI und GND. Zusätzliche Messungen erfolgen an den dokumentierten
Bauteilanschlüssen. Ein Multimeter allein erfasst kurze Einbrüche nicht zuverlässig.

## ATtiny402 programmieren

Der vorhandene DIAMEX-ISP-Programmer programmiert weiterhin den ATtiny13A;
für den ATtiny402 wird ein **3,3-V-kompatibler SerialUPDI-Adapter** oder ein
Microchip-UPDI-Programmer benötigt. Dessen Pinbelegung vor Anschluss prüfen.

Akku und Senderplatine zum Programmieren abziehen. Eine einzige geregelte
3,3-V-Quelle an **J4 Pin 2**, GND an **Pin 3**, UPDI-Daten an **Pin 1** anschließen.
Keine 5 V, keine parallelen Versorgungen und keine 12-V-Hochvolt-UPDI-Impulse.
Ein Programmer mit reinem VTREF-Eingang benötigt eine separate 3,3-V-Versorgung.

Beispiel für SerialUPDI an COM7, im entpackten Paket:

```powershell
py -m pip install pymcuprog
pymcuprog ping -t uart -u COM7 -d attiny402
pymcuprog read -t uart -u COM7 -d attiny402 -m fuses
pymcuprog write -t uart -u COM7 -d attiny402 -f firmware/buzzer-hold.hex --erase --verify
pymcuprog write -t uart -u COM7 -d attiny402 -m fuses -o 1 -l 0x56 --verify
pymcuprog read -t uart -u COM7 -d attiny402 -m fuses
```

Fusewerte gegen `firmware/fuses.json` rücklesen: BODCFG **0x56** für 2,6-V-BOD,
OSCCFG **0x7e** für 20 MHz, SYSCFG0 **0xf6** mit aktivem UPDI und WDTCFG **0x00**.
Andere vorgefundene Einstellungen zuerst kontrolliert korrigieren. Keine
Lockbits setzen und UPDI niemals als GPIO/Reset umkonfigurieren. Die Firmware
teilt den Takt durch vier auf 5 MHz. Der Watchdog läuft während aktiver Phasen
mit nominal 2 s und wird vor dauerhaftem Schlaf deaktiviert.

Ein Softwarehänger führt über den Watchdog-Reset zum vorgegebenen AUS-Zustand.
Die normale 1.000-ms-Zeit ist keine unabhängige Hardware-Zeitbegrenzung.
Nach dem Programmieren Programmer und 3,3-V-Quelle entfernen, anschließend
Sender und Akku anschließen. Der ATtiny13A wird nicht neu geflasht.

## Hardwareabnahme – noch offen

Mit strombegrenztem Netzteil bei 6, 7,4, 9 und 12 V beginnen. Erst ohne Sender
3,3-V-Rail und Ausgang prüfen, danach die V5-Platine anschließen. Mit Oszilloskop
oder Logikanalysator messen:

- Keine Phantomdrücke bei Einschalten, gehaltenem Taster, Reset und Unterspannung.
- Kontaktimpulse 1/2/5/10/20/50 ms erzeugen jeweils eine vollständige Sendefolge.
- Nominal 1.000 ms Einschaltung und keine Überschneidung mit aktiver Entladung.
- Einschaltstrom, Spannungseinbruch, Gatepegel und Erwärmung sind unauffällig.
- V5 VIN und dessen 3,3-V-Rail fallen vor erneutem Start in den sicheren
  Resetbereich; Abnahmeziel am Ende der Entladung **unter 0,3 V**.
- Alle fünf Funktelegramme liegen an V5 DATA an; der nächste freigegebene Druck
  erzeugt eine neue Ereigniskennung. Oszillatortoleranzen berücksichtigen.
- Prellen, langes Halten und Drücke während der Sperrzeit lösen nicht mehrfach aus.
- Nach 20 ms stabiler Freigabe und Ende der Entladung funktioniert der nächste Druck.
- Ruhestrom, längere Ruhephase und Wiederanlauf am tatsächlichen VERICO-Akku prüfen.
  Dessen Ausgang darf bei kleiner Ruhelast nicht unbemerkt abschalten.
- Watchdog-Reset bei künstlichem Softwarehänger und UPDI-Fuse-Rücklesung prüfen.

Danach Empfangsprotokoll und sichtbare Reaktion in Training, Quiz und Spielen
vergleichen, einschließlich gleichzeitig betätigter Buzzer. Reichweite und
Kollisionen separat prüfen. Messaufbau, Datum, Spannung und Revision in
`validation/HARDWARE-ABNAHME.md` dokumentieren. Bis dahin bleibt Rev A Prototyp.

## Build und Nachvollziehbarkeit

`tools/build_firmware.py --toolchain <AVR-bin> --dfp <Microchip-ATtiny_DFP>` baut
mit GCC 7.3.0 und ATtiny_DFP 3.4.278. `tests/controller_test.c` testet die echte
Firmware-Zustandslogik auf dem PC, nicht den AVR-Interruptpfad oder die Hardware.
KiCad 8.0.9/pcbnew und Freerouting 2.1.0 erzeugen das dokumentierte Layout.
`tools/build_design.py` erstellt Schaltplan/Platzierung; `tools/finish_board.py`
importiert die SES-Datei und prüft DRC sowie Netzgleichheit zum Schaltplan.
Fertigungsdateien werden aus der abschließend geprüften Platine exportiert.

## Quellen und Rechte

Die bereitgestellte ProjektARES-Lasercontroller-Anleitung vom 7.2.2016 dient
als Funktionsreferenz. Ihr Layout und ihre Firmware werden nicht übernommen;
die fremde PDF wird nicht öffentlich weiterveröffentlicht.

- https://www.microchip.com/en-us/product/ATTINY402
- https://packs.download.microchip.com/
- https://www.ti.com/lit/ds/symlink/tps709.pdf
- https://www.aosmd.com/sites/default/files/res/data_sheets/AO3407A.pdf
- https://www.aosmd.com/sites/default/files/res/data_sheets/AO3400A.pdf
- https://github.com/microchip-pic-avr-tools/pymcuprog/blob/main/help.md
- https://www.kicad.org/libraries/license/
- https://github.com/freerouting/freerouting/releases/tag/v2.1.0

Standard-Footprints behalten die KiCad-Lizenz CC-BY-SA-4.0 mit Bibliotheksausnahme.
Eigene Quellen und Dokumentation dieses Unterordners stehen unter MIT; siehe
LICENSE und THIRD-PARTY-LICENSES.txt. Herstellerprogramme und Datenblätter liegen
dem öffentlichen Paket nicht bei.
