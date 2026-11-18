# Nachweis: KiCad 8 Rev-A-GitHub-Lauf #9 (18.11.2026)

**Ergebnis: PASS (native Softwareprüfung), keine reale Hardwareabnahme.**

- GitHub Actions: https://github.com/C31N/trainingsanzeige-releases/actions/runs/44232889454
- Ausgeführter Quellstand: `dd505b1d12f996c6825f1b18866767b061ddf18f`
- Hardwarequelle: veröffentlichtes GitHub-Release `buzzer-hold-revA-0.1.0`, ZIP `WFD_Buzzer_Impulsverlaengerung_RevA_Prototyp.zip`
- KiCad: **8.0.9**, von `ppa:kicad/kicad-8.0-releases` auf Ubuntu 24.04
- Unabhängiger `kicad-cli pcb drc --schematic-parity`: **0 violations**
- Unabhängiger `kicad-cli sch erc`: **0 violations**
- Beide CLI-Befehle und JSON-Ergebnisprüfung: Exitcode 0
- Actions-Job `download-hardware-release`: SUCCESS
- Artefakt `reva-kicad-8-native-preflight`: `board-drc.json`, `schematic-erc.json`, `kicad-version.txt` (GitHub-Retention 1 Tag)
- Hinweis: ERC meldet als Zusatzhinweis `You must first configure the library table to include all footprint libraries not included with KiCad.`. Die im Hardware-Release mitgelieferten lokalen WFD-Bibliotheken sind in `kicad/fp-lib-table` und `kicad/sym-lib-table` referenziert; Meldung zukünftig durch gesonderte Konfiguration gegenprüfen. Das gemeldete 0/ERC ist kein elektrischer Praxistest.

## Vergleich zur vorherigen Fehlermeldung
- Lauf #7: fehlgeschlagen, weil Ubuntu aus Standard-Repositories KiCad 7.0.11 installierte und CLI-Optionen der 8er-Version nicht unterstützt.
- Commit `dd505b1d`: KiCad-8-PPA, Version-Gate, strikte Fehler-/Warnungsprüfung eingebaut.
- Lauf #9 bestätigt die Korrektur.

## JLCPCB-Datensatz
- `02_JLCPCB_BOM_SMD.csv`: 13 Bauteilgruppen / 22 SMD-Referenzen
- `03_JLCPCB_CPL_SMD.csv`: 22 auf Top gelegene SMD-Referenzen, aus Original-Geometrie abgeglichen
- J1, J2, J3 und J4 sind absichtlich ausgelassen und werden vom Nutzer selbst montiert
- Die unveränderten **Original-Gerber** liegen im Hardware-Release: https://github.com/C31N/trainingsanzeige-releases/releases/tag/buzzer-hold-revA-0.1.0
- JLCPCB-Bauteilverfügbarkeit, Footprint/Pin-1/Polarität und Bestückungsvorschau müssen beim Checkout noch unabhängig geprüft werden. 9-V-VERICO-Ruhestrom, reale V5-Resetkurve, 1-ms-Auslösung und HF-Tests stehen aus.
- Status: **Prototyp; keine Freigabe für Serienfertigung/Einbau in alle fünf Funktaster ohne Messung.**
