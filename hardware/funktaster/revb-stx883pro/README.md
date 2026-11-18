# Wasserfreunde Dalum - Buzzer Rev B0.9

**Prototyp / keine Fertigungs- oder Einsatzfreigabe.** Aktueller Dokumentationsstand: B0.9-D1, 18.11.2026.

Rev B integriert ATtiny402-Impulsverlängerung, ATtiny13A-V2-Sendersteuerung und STX883PRO auf einer 30 x70-mm-Zweilagenplatine. Fünf identische PCBA sind vorbereitet; die Sender unterscheiden sich nach Programmierung durch IDs1-5. Beide Controller werden unprogrammiert geliefert.

## Aktuelles Paket
- [Eigene PDF: Anschluss, Programmierung, Erstprüfung](dokumentation-b09-d1/documents/Buzzer_RevB_B09_Anleitung_Programmierung.pdf)
- [Archivübersicht und Änderungen](dokumentation-b09-d1/README.md)
- [Vollständiges Dokumentationsarchiv](Buzzer_RevB_B09_Dokumentation_D1_NICHT_FERTIGUNGSFREIGEGEBEN.zip)
- [Prüfstatus](dokumentation-b09-d1/validation/RELEASE_GATES.json)

## Was belegt ist
Native KiCad8.0.9: DRC0 / ERC0 / Unconnected0 / Parität0, CI-Lauf44295672022. 35 SMD-Referenzen und19 LCSC-Gruppen abgeglichen. Die drei genehmigten Ersatztypen sowie ein JLCPCB-Bildexport und35 visuelle Prüfvermerke sind gesichert. D1/D2 wurden im Viewer um180 Grad korrigiert; Kathoden links.

## Was vor der Bestellung noch fehlt
Die finale numerische Live-CPL nach manuellen Viewer-Korrekturen ließ sich über die verfügbare Oberfläche nicht exportieren. Die archivierten Original- und Y-negativ-CPLs sind **keine reproduzierbare finale Bestückung**. Erst finale numerische Koordinaten/Winkel sichern und gegen Gerberpads und Hersteller-Landpatterns, besonders STX883PRO, abgleichen. Das Projekt bleibt bis dahin `fabrication_release=false`.

Hardware-, Akku-, Programmier-, Gehäuse- und Funkabnahmen sind weiterhin offen. Erst ein Muster prüfen. Die visuelle Vorschau garantiert weder die tatsächliche Bestückung noch die Funktion.

## Programmierung beachten
ATtiny402: J4/UPDI, Controller3V3. ATtiny13A: J5/ISP, TX3V3. Diese Versorgungsschienen nicht verbinden. Für den neuen integrierten Aufbau genügt Gedrückthalten des Buzzers nicht; die Impulsverlängerung schaltet nach etwa1 s ab. Die PDF beschreibt die getrennte3,3-V-Programmierversorgung und die Fuse-Rücklesung.

## Historische Dateien
B0.2/B0.3-ZIPs, ältere BOM/CPL-Entwürfe und frühere Abnahmedokumente bleiben als Verlauf erhalten. Ihr früherer Status kann veraltet sein. Für den aktuellen Freigabestand gelten ausschließlich diese Übersicht und dokumentation-b09-d1/validation/RELEASE_GATES.json. Keine ältere Gerber-/CPL-Datei ungeprüft für eine neue Bestellung verwenden.
