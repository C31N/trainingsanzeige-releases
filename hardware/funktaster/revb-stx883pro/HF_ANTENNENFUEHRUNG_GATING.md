# Rev B: HF-Leitung und Antennenanschluss – Fertigungsgate

**Status: OFFEN / NICHT FERTIGUNGSFREIGEGEBEN.** Native KiCad-DRC/ERC und die Schaltplanparität sind notwendig, aber keine Hochfrequenzabnahme.

## Quantitativer Befund (B0.6/B0.7-Routingkandidat)

- STX883PRO-433MHz (JLC C3001517), nominal 433,92 MHz, ANT-Pin 4, vom Hersteller erwartete Antennenimpedanz: **50 Ω**.
- Bestehende `ANT`-Verbindung zwischen U5 Pin 4 und J3: 10 Segmente auf F.Cu, zusammen ca. **5,37 mm**, Leiterbahnbreite durchgehend **0,25 mm**.
- Trägerplatine: zwei Kupferlagen, FR4, 1,6 mm; auf F.Cu und B.Cu sind GND-Zonen vorgesehen. Der tatsächliche HF-Rückstromweg nach dem Zonenfüllen ist noch nicht unabhängig modelliert.
- Eine 0,25-mm-Leiterbahn über einer 1,6-mm-FR4-Massefläche entspricht **nicht ohne Weiteres** einer 50-Ω-Mikrostreifenleitung. Als reine Microstrip-Näherung ohne seitliche Masse liegt die Impedanz deutlich über 50 Ω. Die nahe F.Cu-Masse und Lötstopplack ändern den Wert; daher nicht blind 3 mm als endgültige Leiterbahnbreite setzen.
- Das Stück ist kurz, die Gesamtanpassung muss dennoch mit realem PCB-Stackup und Antenne bewertet werden. Die bisherige geometrische 0,20-mm-Kupferabstandsprüfung überprüft **keine** HF-Impedanz.

## Erforderliche Entscheidung für Rev B0.8

1. **Antenne festlegen:** Original-STX883PRO-Federantenne, externe 50-Ω-Koaxverbindung oder externe Antenne; die Antennenposition, der zugehörige Masseanschluss und der Abstand zu Akku/Gehäuse sind zu vermessen.
2. JLCPCB-Typ (2 Lagen, 1,6 mm, 1 oz) und die tatsächlich gewählte HF-Führung vorgeben: Microstrip oder geerdeter Coplanar Waveguide; Breite/Gap im JLCPCB-Rechner berechnen und dokumentieren.
3. F.Cu-Abstände und B.Cu-Referenz unter dem ANT-Leiterzug überprüfen; F.Cu-GND-Zone gegebenenfalls mit definiertem Rückstromweg und Stitching koppeln.
4. Footprint U5 anhand der bei JLC hinterlegten EasyEDA-C3001517-Landpattern-/Pick-and-Place-Information prüfen. Vorher keine SMD-Bestellung.
5. Echten 433-MHz-Funkversuch mit Spektrummessung/ERP/Duty-Cycle, Antenne, dem realen VERICO-9-V-Akku sowie fünf Sendern durchführen.

Keine Änderung an der Kupfergeometrie durch die reinen Rev-B0.6/B0.7-Paritätskorrekturen.

Referenzen:
- Hersteller https://www.nicerf.com/ask-modules/ask-transmitter-module-stx883pro.html
- Hersteller-PDF https://atta.szlcsc.com/upload/public/pdf/source/20220425/A5DE282F31CC427808FF7DA9A0756AC1.pdf
- JLC-Teilenummer https://jlcpcb.com/partdetail/GNiceRF-STX883PRO433MHz/C3001517
- JLC Impedanzrechner https://jlcpcb.com/pcb-impedance-calculator/
