# Wasserfreunde Dalum – Funktaster Rev B0.7 (STX883PRO-433MHz)

**ENTWURF / NICHT BESTELLEN.** Erstes integriertes KiCad-8-Layout mit 35 SMD-Positionen, fünf externen Anschlussgruppen und zwei Montagebohrungen. Schaltplan und Bauteilpositionen sind vorhanden. **Es gibt noch keinen bestätigten vollständig gerouteten, unabhängigen DRC-sauberen PCB-Stand. Gerber sind absichtlich nicht enthalten.**

## Aktueller technischer Stand (18.11.2026)

**PROTOTYP, KEINE FERTIGUNGSFREIGABE.** Der aktuelle Entwicklungsstand B0.7 wird aus der originalen B0.3-ZIP und den Skripten `tools/apply_b04_fixes.py`, `tools/apply_b05_schematic_fix.py`, `tools/apply_b06_parity_fix.py` und `tools/apply_b07_nc_nets.py` reproduzierbar aufgebaut. Das Native-KiCad-8-CI-Ergebnis des neuesten Standes liegt unter https://github.com/C31N/trainingsanzeige-releases/actions/runs/44285300239 . Das historische B0.3-Layout bleibt als Experiment archiviert.

- Native KiCad Rev B0.5: DRC 0, Unconnected 0, ERC 0, aber 110 Paritätsabweichungen.
- Rev B0.6: 108 Netzpräfix- und 2 Montagebohrungsabweichungen korrigiert; 7 NC-Pin-Abweichungen verbleiben.
- Rev B0.7: den sieben nicht angeschlossenen Pins eindeutige KiCad-Pseudonetze zugewiesen; nativer KiCad-8-Nachweis folgt im laufenden Workflow.
- HF-Bauteil/Landpattern und Antennenimpedanz sind **nicht freigegeben**. Siehe `HF_ANTENNENFUEHRUNG_GATING.md`: ca. 5,37 mm ANT-Leitung, bisher 0,25 mm Breite.
- Keine Gerber oder Bestellfreigabe für JLCPCB, keine fünf Sender anfertigen, bevor die KiCad-Freigabe und anschließend die HF-/Hardwareprüfungen erfolgt sind.

## Ziel
Fünf identische neu hergestellte Senderplatinen anstelle der selbst verdrahteten Lochrasterplatinen V5 + Rev-A-Zusatzmodul. Alle 5 sollen sich allein durch die geflashte ATtiny13A-V2-Firmware (Sender-ID 1–5) unterscheiden.

## Technischer Aufbau
- Mechanik **30 × 70 mm / 1,6 mm / FR4 / 2 Lagen** zunächst vom V5-Prototyp übernommen. Gehäuse, Akkufach, Höhe und Montagebohrungen noch *am Originalgehäuse messen*.
- **J1**: abgesicherter VERICO-9-V-Akku (+ nach externer T250-mA-Sicherung, GND); **D2 SS14** als Verpolschutz, Schottky-Spannungsabfall zu berücksichtigen.
- **J2**: vorhandener großer Buzzer als potentialfreier Schließer (NO/COM gegen Masse), keine 9 V am Tastereingang.
- **U1 ATtiny402 + U2 TPS70933 + Q1–Q4**: Original-Impulsverlängerung Rev A, nominell 1000 ms Sender an, 100 ms Entladung, 20 ms stabil losgelassen. Die vorhandene Firmware wird unverändert übernommen.
- **U3 TPS70933**: zweiter 3,3-V-LDO aus dem geschalteten Rohspannungszweig (SWVIN). Statt des bisherigen steckbaren R-78E wird ein kompakter SMD-Regler verwendet. RF-Modul sowie ATtiny13A laufen ausschließlich mit **3,3 V**, nicht direkt mit 9 V.
- **U4 ATtiny13A-SSU**: V2-Protokoll aus dem originalen DIAMEX-Paket, Pin 2 / PB3 = DATA; unveränderte Sender-IDs 1–5, vorhandener Pi-Empfänger bleibt. **J5**: bisheriges DIAMEX-ISP-Pinout, unbestückt.
- **U5 STX883PRO-433MHz, JLCPCB C3001517**: SMD-Sender, Pins **1 GND, 2 VCC, 3 DATA, 4 ANT**, 433,92 MHz nominal, 10 dBm bei 3,3 V. **J3**: externer 50-Ω-Antennenanschluss/Lötpunkt; Antenne wird manuell montiert und im Gehäuse vermessen.
- **J4**: UPDI / Controller-3,3 V / Masse, selbst anschließen; J5: MISO / VCC / SCK / MOSI / RESET / GND; unter keinen Umständen mehrere Versorgungen gleichzeitig verbinden.
- Senderversorgung wird über R15=330 Ω entladen; Stabilität / vollständiger Reset sind in der realen Schaltung zu messen.

## Dateien
- `kicad/buzzer-revb-stx883pro.kicad_sch`: funktionaler KiCad-Schaltplan mit Netznamen.
- `kicad/buzzer-revb-stx883pro-PLACEMENT-ONLY.kicad_pcb`: **nur** mechanische Bestückungsplatzierung ohne geroutete Verbindungen.
- `kicad/WFD-RevB.pretty`: lokale Footprints. **Wichtig:** RF-Modul-Footprint auf Basis der Hersteller-Abmessungen abgeleitet, noch nicht mit JLC/Original-EasyEDA-Landpattern abgeglichen.
- `kicad/buzzer-revb-stx883pro-ROUTED-EXPERIMENT.kicad_pcb`: **nicht freigegebenes, nur algorithmisches Routingexperiment** (Leiterbahnkollisionen vorhanden). Nicht zur Bestellung verwenden.
- `design.json`, `NETLIST.csv`: elektrische Netze, Bauteile, Maße und Stückliste.
- `BOM_JLC_Entwurf_NICHT_FREIGEGEBEN.csv`, `CPL_JLC_Entwurf_NICHT_FREIGEGEBEN.csv`: Beschaffungs-/Positionierungsentwürfe, ohne JLC-Komponentenzuordnungsgarantie.
- `firmware/`: fünf geprüfte Original-V2-Sender-HEX-Dateien (IDs 1–5) plus Original-Rev-A-Firmware für den Controller. Nicht ungeprüft auf die neuen PCB übertragen.
- `docs/Layout_Uebersicht.png`: anschauliche Bauteilplatzierung, keine geroutete Leiterplatte.

## Kostenrelevante JLCPCB-Entscheidung
- Die Stückliste enthält nach der Vorprüfung für alle 35 SMD-Bauteile Kandidaten-Codes. **Keiner dieser Codes stellt eine Bestands-, Geometrie- oder Freigabebestätigung dar.** Die drei zuletzt ergänzten Kandidaten sind R13 150 Ohm C2889503, R15 330 Ohm C105878 und C8 10 uF C2835529; insbesondere DC-Bias, Spannungsfestigkeit und Footprint von C8 vor der Bestellung verifizieren.
- Automatische Bestückung gilt ausschließlich für 35 SMD-Bauteile. J1-J5, externe Sicherung, VERICO-Akku, Taster und Antenne werden später manuell montiert. Die beiden Controller kommen ab Werk **unprogrammiert**.
- Eine realistische JLCPCB-Kalkulation ist erst nach DRC-bereinigtem Routing, verifiziertem RF-Footprint und Bauteilzuordnung möglich.

## Abnahme-Gates vor Gerber/JLCPCB
1. STX883PRO-Footprint von Hersteller/EasyEDA C3001517 mit Lötflächen 1–4 und Polarität vergleichen; Datenblatt liefert überwiegend **Modulmaße**, nicht verbindlich empfohlene Platinenpads.
2. Eigenen Rev-B-Schaltplan gegen Original Rev-A-Schaltplan + V5-Verdrahtung **unabhängig** prüfen; insbesondere U3 TPS70933 Pin 3/EN, D2, Q1–Q4 und 6-polige ISP-Pinorientierung.
3. F.Cu/B.Cu voll entflech­ten; echte KiCad-8 ERC/DRC **0 Fehler, 0 Warnungen und 0 Unconnected**, flächig geschlossene Masse, HF-Führung mit 50-Ω-Impedanzbewertung und ausreichendem Antennenabstand.
4. JLCPCB-AOI/Bestückungsansicht: Pin1 für U1/U4/U5 und D1/D2; alle 35 SMD-Positionen; alle Bauteile verfügbar.
5. Ein reales Muster mit Labornetzteil und anschließend VERICO-Block: Ruhestrom und Abschaltverhalten des Akku-Boosters, 3,3-V-LDO-Temperatur, V5-Resetzeit unter 0,3 V, 1-ms-Tastendruck, vollständige V2-Funksendefolge.
6. 433-MHz-Spektrum, Frequenz, Antenne, Reichweite, ERP und Duty Cycle am fertigen Gerät für Deutschland prüfen. Eine Modul-CE-Erklärung ist kein automatischer Endgeräte-Freibrief.
7. Gehäuse, Feuchtigkeitsschutz und Befestigungen am echten Taster abnehmen.

## Funk- und Datenblattquellen
- [NiceRF STX883PRO Produkt/Datenblatt](https://www.nicerf.com/ask-modules/ask-transmitter-module-stx883pro.html)
- [JLCPCB STX883PRO C3001517](https://jlcpcb.com/partdetail/GNiceRF-STX883PRO433MHz/C3001517)
- [LCSC ATtiny13A-SSU C14075](https://www.lcsc.com/de/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATTINY13A-SSU_C14075.html)
- [TI TPS70933 C89347](https://jlcpcb.com/partdetail/TPS70933DBVR/C89347)
- [Bundesnetzagentur SRD Vfg. 91/2025](https://www.bundesnetzagentur.de/DE/Fachthemen/Telekommunikation/Frequenzen/Allgemeinzuteilungen/start.html)
- Originalprojekte: [V5 + RevA](https://github.com/C31N/trainingsanzeige-releases/releases/tag/buzzer-hold-revA-0.1.0)