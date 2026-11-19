# Buzzer Rev B0.9 - Dokumentation B0.9-D1

**ARCHIV / PROTOTYP - NICHT ZUR FERTIGUNG FREIGEGEBEN.**

Stand 18.11.2026. Dieses Paket sichert Gerber, Firmware, genehmigte Ersatzteile, den JLCPCB-Bildexport und das visuelle Prüfprotokoll. Es enthält eine eigene neunseitige Anleitung für Rev B. Es enthält **keine bestätigte finale numerische Live-CPL**. Die beiden CPL-Dateien sind ausdrücklich nur Referenzen vor den manuellen Live-Korrekturen. Nicht unverändert zur Wiederbestellung hochladen.

## Einstieg
- [PDF: Beschreibung, Anschluss, Programmierung und Erstprüfung](documents/Buzzer_RevB_B09_Anleitung_Programmierung.pdf)
- [Textfassung](documents/ANLEITUNG_REVB_B09.md)
- [Aktueller JLCPCB-Bildexport](evidence/JLCPCB_Bestueckungsansicht_20261118.png)
- [Offene Freigaben](validation/RELEASE_GATES.json)
- [Prüfvermerke für alle 35 Referenzen](validation/BESTUECKUNGSPRUEFUNG_35_REFERENZEN.json)

## Im Warenkorb abgeglichene Änderungen
- C3/C6: C415536 -> TDK C76639, 4,7 uF / 10 V / X7R / 10 % / 0805.
- C8: C2835529 -> HRE C6119932, 10 uF / 25 V / X7R / 10 % / 0805.
- R13: C2889503 -> Yageo C114523, 150 Ohm / 0,125 W / 1 % / 0805.
- D1/D2 im Viewer relativ zur importierten Datei um 180 Grad gedreht; Kathode jeweils links in Bestückungsansicht.
- Pin 1 / Gehäuseorientierung von U1/U4, U2/U3, Q1-Q4 und U5 sowie alle Passivteile visuell betrachtet. Dies ist keine numerische Maschinenbestückungsfreigabe.

## Wichtiger Unterschied beim Programmieren
U1 (ATtiny402) wird über J4/UPDI versorgt und programmiert; U4 (ATtiny13A) über J5/ISP. Beim neuen integrierten Aufbau reicht Gedrückthalten des Tasters **nicht**: die Senderversorgung endet nach etwa einer Sekunde. Akku abziehen und den jeweils richtigen 3,3-V-Bereich extern und allein versorgen. Keine Versorgungsschienen zusammenschalten. Details und geprüfte Anschlusskoordinaten stehen in der PDF.

## Vor Bestellung erforderlich
1. Finale numerische Pick-and-Place-Datei des gespeicherten JLCPCB-Stands beschaffen oder die Platzierung aus verifizierten Hersteller-Landpatterns neu reproduzieren.
2. Koordinaten, Winkel, Pin 1 und alle Anschlüsse gegen Gerberpads vergleichen; speziell STX883PRO metrisch prüfen.
3. Aktualisiertes Paket mit neuen Prüfsummen sichern und erst dann eine Prototypenbestellung freigeben.
4. Nach Lieferung zunächst ein Muster programmieren und elektrisch, am Akku, im Gehäuse und per Funk prüfen.

**Ein grüner Archivtest oder eine plausible 3D-Vorschau ersetzt diese Schritte nicht.**

## Archiv prüfen
```text
python tools/verify_archive.py
```
Das Skript liest nur Dateien und programmiert kein Gerät. Die erwartete Ausgabe enthält PASS für Dateiintegrität und ausdrücklich BLOCKED FOR FABRICATION für die offenen technischen Gates.

## Herkunft
Basis-Commit `09f80822e131fa1d7f6cef4a08b638c0d64b4231`, PR #2 in C31N/trainingsanzeige-releases; nativer KiCad-8-Lauf #42 / 44295672022. Unveränderter B0.9-CI-Export und B0.3-Quellarchiv unter source/. Die Patchskripte B0.4-B0.9 und der damalige Workflow sind beigelegt. Die Firmwarequellen der Impulsverlängerung liegen im vollständigen Rev-A-Referenzarchiv. ATtiny13A-V2 bleibt die Original-Firmware mit IDs 1-5.

Die Dokumentationsrevision D1 ändert keine Leiterbahnen und erklärt keinen Hardwaretest als bestanden. Kontaktdaten, Adresse, Telefonnummer, Kontozugänge und persönliche Checkout-URLs sind nicht Bestandteil dieses Archivs.
