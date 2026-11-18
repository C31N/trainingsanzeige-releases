# Rev B0.9 – KiCad-8-Abnahme des Prototyp-Entwurfs

**Native CAD-Prüfung erfolgreich. Keine elektrische/HF-Freigabe und keine Gerber-Fertigungsfreigabe.**

- GitHub Actions: https://github.com/C31N/trainingsanzeige-releases/actions/runs/44290645317
- CI Run #33: `native-kicad8` SUCCESS.
- Verifiziert: PCB native Zone-Fill SUCCESS; **0 violations**, **0 unconnected items**, **0 schematic parity issues**.
- `kicad-cli sch erc`: **0 violations**.
- `ZONE_FILL=0`, `DRC=0`, `ERC=0`, `JSON_GATE=0`.
- Native Nachweise: GitHub-Actions-Artefakt `revb-b09-native-kicad8-preflight`, Artifact-ID `14420664669`.
- Rev B0.9 wurde aus dem B0.3-Archiv mit den Skripten B0.4 bis B0.9 reproduziert.
- ANT-Route vom STX883PRO U5/4 nach J3 verkürzt auf einen **3,2-mm-Leiterzug, 0,8 mm breit**, mit zwei Masse-Vias in unmittelbarer Nähe. Das ist **keine** nachgewiesene 50-Ω-Leitung: Die tatsächliche Antennenimpedanz und Rückstromführung benötigen unabhängigen Stack-up-/HF-Nachweis.
- Öffentliche EasyEDA-C3001517-API gab beim Zugriff aus GitHub Actions HTTP **403** zurück. Der Runner markiert dies bewusst nur als fehlenden externen Landpattern-Nachweis; der Job war technisch erfolgreich, aber **JLC-Footprint nicht bestätigt**.

## Messungen bestehender Funktaster

Nutzerangabe vom 18.11.2026: **10 einzelne Funkmessungen je eingebautem Buzzer** und **alle Messungen etwa 10 % unter der gesetzlichen Höchstgrenze**. Details/Einzelmesswerte und Messunsicherheit liegen nicht vor. Dokumentiert unter `HF_REFERENZMESSUNG_V5_UND_REV_B_ABNAHME.md`. Dies ist ein Vergleichsmaßstab für die neuen fünf Rev-B-Sender, ersetzt aber nicht deren eigene Funkmessung.

Die derzeit einschlägige Bundesnetzagentur-Vfg. 91/2025 nennt für 433,05–434,79 MHz bei Zeile 44b **10 mW ERP mit Arbeitszyklus ≤ 10 %**. Modul-Datenblatt NiceRF STX883PRO gibt **10 dBm bei 3,3 V** an; conducted RF-Ausgangsleistung darf **nicht** als fertige abgestrahlte ERP ausgegeben werden.

## Sperren

`design_erc_drc_verified=true`; `rf_erp_measured=false`; `jlc_stx883pro_landpattern_verified=false`; `battery_load_test_passed=false`; `fabrication_release=false`.
