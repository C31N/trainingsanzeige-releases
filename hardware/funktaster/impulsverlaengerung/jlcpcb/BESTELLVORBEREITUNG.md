# JLCPCB-Bestellvorbereitung – Buzzer-Hold Rev A (18.11.2026)

**STATUS: ORIGINAL-RELEASE-DATEN ERMITTELT UND KONSISTENZ GEPRÜFT; HARDWARE WEITER PROTOTYP.** Die reine Git-Tag-Quellcodeversion enthält nur Dokumentation, aber der [GitHub-Hardware-Release](https://github.com/C31N/trainingsanzeige-releases/releases/tag/buzzer-hold-revA-0.1.0) enthält separate Assets `Gerber_RevA_Prototyp.zip` und `WFD_Buzzer_Impulsverlaengerung_RevA_Prototyp.zip`. Die Dateien wurden über GitHub Actions geladen. Original-BOM und original CPL enthalten dieselben 26 Refdes, die veröffentlichte KiCad-Geometriedatei stimmt mit allen 22 SMD-Koordinaten überein. Alle 64 Release-Checksummen waren korrekt; das veröffentlichte Projekt meldet null ERC/DRC/Unconnected. Eine unabhängige erneute KiCad-8-Prüfung wurde in Actions ergänzt. Die reale Hardwareabnahme und finale JLCPCB-Vorschau bleiben offen.

## Zielauftrag
- 5 Stück, 30 x 25 mm, 2 Lagen, FR4, 1,6 mm, 1 oz, Lötstopp, Oberseite bestückt, Economic PCBA soweit verfügbar.
- Nur 22 SMD-Bauteile pro Platine; J1/J2/J3 (je 2 Pins) und J4 (3 Pins) **NICHT** bestücken, Anschlussleitungen später direkt anlöten oder optional Stiftleisten selbst montieren.
- Die `JLCPCB_BOM_RevA_SMD_PRECHECK.csv` enthält 13 Gruppeneinträge mit insgesamt 22 SMD-Positionen. Die Dateien `JLCPCB_BOM_SMD_Release_RevA.csv` und `JLCPCB_CPL_SMD_Release_RevA.csv` in diesem Verzeichnis wurden aus dem Original-Release geprüft erstellt. Die unveränderte Fertigungsdatei `Gerber_RevA_Prototyp.zip` befindet sich in den offiziellen Release-Anhängen. **Alle drei** Dateien gehören zusammen.
- **U1 kommt unprogrammiert**. Der ATtiny402 muss anschließend per UPDI mit `firmware/buzzer-hold.hex` und geprüften Fuse-Einstellungen aus dem zugehörigen Hardwarepaket programmiert werden.
- Mit dem VERICO-Akku: Der 9-V-Ausgang ist grundsätzlich im designierten Eingangsspannungsbereich 6–12 V. Ein Akku-/Ruhestrom-/Einschaltversuch am echten Prototyp steht noch aus.

## Ersetzte / prüfbedürftige Komponenten
- **C1,C4**: ursprünglicher `GRM21BR71C104KA01L` (nicht mehr zuverlässig erhältlich) durch `CL21B104KBCNNNC` (C1711, 100 nF, 50 V, X7R, 0805) ersetzt. Mechanik elektrisch gleichwertig plausibel; noch am PCB überprüfen.
- **C3**: ursprünglicher `GRM21BR71A475KA73L` (abgekündigt) durch `GRM21BR71A475KE51L` (C415536, 4,7 µF, 10 V, X7R, ±10 %, 0805) ersetzt. DC-Bias und Mindestkapazität gegen TPS70933-Datenblatt prüfen.
- **U1**: C1339884 `ATTINY402-SSN` statt `ATTINY402-SSNR` (Packungsvariante). Pinout, Bestückungsseite und Pin-1-Auszeichnung prüfen.
- **Q2,Q4**: C7422625 `MMBT3904LT1G` bei anderem Anbieter. B/E/C-Pinout und 200-mA-/Spannungsgrenzen vergleichen.
- **D1**: C2103 `BZT52C10` anderer Anbieter statt `BZT52C10-7-F`. 10-V-Zenerspannung, SOD-123-Kathodenrichtung und Schutzfunktion prüfen.
- Keine weiteren Teile ohne elektrische / geometrische Rückprüfung austauschen.

## Pflichtprüfungen vor Checkout
1. **Erledigt:** Original-Hardware-Release mit Gerber/Excellon, CPL, KiCad-PCB und Firmware separat abgerufen, 64 Checksummen korrekt. Git-Tag-Source-ZIP weiterhin nur Dokumentation.
2. KiCad ERC/DRC 0 und Gerber-Vorschau; Netze `BAT`, `SWVIN`, `3V3`, `GND`, `POWER`, `DISCHARGE` und alle Transistorpads kontrollieren.
3. BOM/CPL 1:1 vergleichen (22 SMD-Refdes); J1–J4 nicht bestücken, keine fehlenden Komponenten.
4. JLCPCB-Vorschau: U1-Pin 1, U2 (TPS70933-DBVR PIN 1/2/3/4/5), D1-Kathode, Q1/Q3 G-S-D, Q2/Q4 B-E-C visuell verifizieren.
5. JLCPCB-Bauteil- und Lagerbestand **zum Bestellzeitpunkt** erneut kontrollieren. Die C-Teilenummern sind Bestellvorschläge, keine garantierten Warenkorbreservierungen.
6. Ohne Firmware und reale Messungen **nicht** in fünf Sendern einsetzen; zunächst ein 9-V-Prototyp mit Labornetzteil/VERICO, Scope und gemessener V5-Resetkurve abnehmen.
7. Sendezeit nominal 1000 ms, danach 100 ms Entladung, 20 ms losgelassener Taster. Insbesondere unter 0,3 V auf V5-VIN und V5-3V3 messen, andernfalls Entladung technisch neu auslegen statt die Zeit blind zu ändern.

## Referenzen
- Original `hardware/funktaster/impulsverlaengerung/README.md`, `BOM.csv`, `documents/*.pdf`.
- Getrenntes Release: https://github.com/C31N/trainingsanzeige-releases/releases/tag/buzzer-hold-revA-0.1.0
- Bestückung: https://jlcpcb.com/pcb-assembly
- Erforderliche BOM / CPL / Gerber: https://jlcpcb.com/help/article/pcb-assembly-faqs
- `U1`: https://jlcpcb.com/partdetail/MicrochipTech-ATTINY402SSN/C1339884
- `U2`: https://jlcpcb.com/partdetail/TPS70933DBVR/C89347
- `R11`: https://jlcpcb.com/partdetail/VishayIntertech-CRCW2512100RFKEG/C844884
- `C3`: https://jlcpcb.com/partdetail/408030-GRM21BR71A475KE51L/C415536

**Ein verbindlicher Preis sowie die Freigabe der maschinellen Bestückungsorientierungen sind erst nach dem JLCPCB-Upload und der tatsächlichen Bauteilzuordnung möglich. Die elektrisch geprüfte Hardwarefunktion fehlt weiter.**

## Original-Release-Check (18.11.2026)

- Zwei Asset-ZIPs aus dem taggenauen GitHub-Release heruntergeladen; unverändertes Gerber-Archiv bytegleich in beiden Assets.
- 26 BOM- und 26 CPL-Referenzen identisch, vier Steckverbinder als THT aus Assembly ausgeschlossen.
- BOM 13 Teilegruppen / 22 SMD-Referenzen, CPL exakt 22 Top-Positionen. Y-Koordinaten **negativ** belassen, da die ursprünglichen Gerber-Koordinaten Y=0 bis Y=-25 mm verwenden.
- Intel HEX-Prüfsummen gültig und 738 Flash-Bytes deckungsgleich mit Original-BIN; Host-Zustandsmaschinentests unabhängig kompiliert und PASS.
- Hardware-Abnahme und mögliche JLCPCB-Automatikrotationen bleiben unverändert offen.
