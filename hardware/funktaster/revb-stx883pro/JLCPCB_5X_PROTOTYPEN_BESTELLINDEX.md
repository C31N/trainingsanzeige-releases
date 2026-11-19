> **Aktuell für die neun B0.10-S2-Buzzer: V2-N9.1 / Anleitung D4.** [Firmware, Programmierung und Genauigkeitsangaben](README.md). Vier Pakete: ein erstes und drei Neuner-Wiederholungsrunden. U1/HOLD und Empfänger diamex-5 bleiben unverändert. Ältere Fünfer-Slotbeschreibungen unten gelten für die bisherige Firmware. Hallenprüfung folgt durch den Nutzer.

# Aktueller Bestellstand: B0.10-S2, neun PCBA

Am 19.11.2026 wurde der Bestellverlauf geprüft: zehn Leiterplatten, davon neun Standard-PCBA, aktuelle S2-Beschriftung und finale B010-CPL. [PDF, Firmware IDs 1-9 und exakte Fertigungsdateien](dokumentation-b10-d2/README.md). Die folgenden älteren Fünferangaben sind historisch und keine neue Bestellgrundlage. Musterabnahme bleibt offen.

---

# JLCPCB: Bestellpaket für fünf Rev-B0.9-Prototypen

**Nur Prototypenfertigung – keine Serien- oder Funkfreigabe.** Dieses Dokument ist der dauerhafte Verweis auf den reproduzierbaren Fertigungsdatenexport.

## Verifizierter Export
- GitHub Actions: https://github.com/C31N/trainingsanzeige-releases/actions/runs/44295672022 (Run #42, SUCCESS)
- GitHub-Artefakt: https://github.com/C31N/trainingsanzeige-releases/actions/runs/44295672022/artifacts/14423023781 (`revb-b09-jlcpcb-prototype-preview-not-approved`; zeitlich begrenzte Aufbewahrung)
- Reproduzierbarer Export: `tools/export_jlcpcb_b09_prototype.py`, aufgerufen aus `.github/workflows/revb-native-kicad-preflight.yml`. Originalquelle B0.3 + reproduzierbare Patchskripte bis B0.9.
- Native KiCad 8: **0 DRC-Verstöße, 0 ERC-Verstöße, 0 Unconnected, 0 Schaltplan-/PCB-Paritätsabweichungen**.
- Stücklistenprüfung: 35 SMD-Referenzen, 19 unterschiedliche LCSC-Teilenummern, genau die 35 Top-CPL-Positionen.
- Gerber: F.Cu, B.Cu, F.Paste, F.Mask, B.Mask, Silkscreen, Edge.Cuts und Excellon. Die 30 × 70 mm Platine besitzt zwei NPTH-Befestigungslöcher.

## JLCPCB-Einstellungen
1. Nur das innere `01_JLCPCB_GERBER_30x70_2L_PROTO.zip` beim Gerber-Upload verwenden (nicht das gesamte Dokumentationsarchiv).
2. PCB 5 Stück, **30 × 70 mm**, FR4, 2 Lagen, 1,6 mm, 1 oz, Standard-Lötstopplack.
3. `PCB Assembly` einschalten, **Economic PCBA** falls JLCPCB diese Teilebestückung zulässt; 5 bestückte Platinen, Top Side.
4. `02_JLCPCB_BOM_35_SMD.csv` und `03_JLCPCB_CPL_35_SMD.csv` importieren.
5. Für alle 19 LCSC-Teilenummern Preis/Verfügbarkeit/Extended-Gebühren und die tatsächliche Maschinenbestückbarkeit prüfen. In der Vorschau speziell STX883PRO (C3001517, Pads 1–4), ATtiny13A, ATtiny402, U2/U3, D1/D2, Transistoren und alle polarisierten Teile überprüfen.
6. J1–J5 **nicht maschinell bestücken**: Handmontage/Verkabelung nach Lieferung. H1/H2 sind mechanisch, nicht bestücken.
7. JLCPCB liefert Mikrocontroller ohne separat beauftragtes Flashing gewöhnlich **unprogrammiert**: 1× ATtiny402 HOLD-Firmware pro Board; 1× ID1–ID5 Firmware für ATtiny13A, jeweils eindeutige ID.

## Kostenstatus
- Nachkalkuliertes, **nicht verbindliches** Modell: **142,51 EUR** einschließlich angenommener Versandkosten nach Deutschland, 19 % Einfuhrumsatzsteuer und Abwicklungsgebühr.
- Budget **150–200 EUR** für Economic PCBA; bei Standard PCBA grob 180–260 EUR. Endpreis nur im JLCPCB-Warenkorb.
- Teilkomponenten und Header/Batterie/Antenne, sofern nachzukaufen, Programmierung und mögliche Nacharbeiten sind nicht enthalten.
- Rechenweg: `BESTELLUNG_5X_PREIS_UND_AKKU_MODELL.md`; Excel-Kosten-/Akku-Modell wird im generierten Bestellpaket mitgeliefert.

## Unverhandelbare technische Hinweise
- Der **selbst abgeleitete** STX883PRO-Footprint wurde anhand Hersteller-Rastermaß auf 2,54 mm geändert, aber **nicht** gegen das original JLCPCB-C3001517-Landpattern/Bestückungsrotation verifiziert (öffentlicher EasyEDA-Endpunkt lieferte HTTP 403).
- Der 3,2 mm lange, 0,8 mm breite Antennenleiterzug mit GND-Vias hat **keinen HF-Impedanz-/50-Ohm-Abnahmenachweis**.
- 9 V am VERICO-Ausgang sind vom Nutzer gemessen, nicht jedoch Ruhestrom, Lastverhalten, automatische Boost-Abschaltung oder LDO-Erwärmung.
- Funksendeleistung der bisherigen Geräte wurde im Gehäuse je Buzzer zehnmal und laut Nutzer ungefähr 10 % unter dem gesetzlichen Grenzwert gemessen. Dies ist **nicht** für den neuen STX883PRO übertragbar.
- **Keine Einsatzerlaubnis für alle fünf Geräte ohne erfolgreiche Musterprüfung** von Sender-ID, Impulsdauer, 9-V-Betrieb, RF-Spektrum, Duty Cycle und ERP im endgültigen Gehäuse.
- Erzeugung der Daten ist eine **technische Bestellvorbereitung für Prototypen**, nicht eine bereits abgeschlossene JLCPCB-Bestellung und keine Garantie für ein fertiges Plug-and-Play-Gerät.

**Projekt-Gates:** `cad_preflight=pass`, `prototype_export=pass`, `jlc_component_landing_review=pending`, `antenna_rf=unverified`, `battery_under_load=unverified`, `firmware_programming=pending`, `series_fabrication_release=false`.


## Aktualisierung B0.9-D1 vom18.11.2026

[Neue Dokumentation und PDF](dokumentation-b09-d1/README.md) haben Vorrang. Genehmigte Ersatztypen und Bildbeleg sind gesichert. Die finale numerische Live-CPL nach den Viewer-Korrekturen fehlt. Die oben genannten ursprünglichen BOM/CPL-Dateien sind keine unverändert wiederverwendbare finale Bestückung. Keine Fertigungsfreigabe, bis der numerische Abgleich und der metrische STX883PRO-Landpattern-Nachweis vorliegen.
