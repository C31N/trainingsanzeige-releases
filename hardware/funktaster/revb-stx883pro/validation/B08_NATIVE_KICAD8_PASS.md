# Rev B0.8 – unabhängiger KiCad-8-DRC/ERC-/Parity-Check

**Natives CAD-Gate BESTANDEN; Hardware-/HF-/JLC-Fertigungsfreigabe WEITER GESPERRT.**

- Workflow: https://github.com/C31N/trainingsanzeige-releases/actions/runs/44287207148 (Run #24)
- Branch-Commit des Prüfworkflows: `0c87e43acc7ef80a1f44d2d22ccb3edc2ca99182`
- Eingabe: B0.3-ZIP + `apply_b04_fixes.py` bis `apply_b08_rf_module_pitch.py`
- KiCad **8.0.9**, native Zone Fill erfolgreich
- Leiterplatten-DRC: **0 violations**
- Unconnected: **0**
- Schaltplan-/PCB-Parität: **0**
- Schaltplan-ERC: **0 violations**
- Prozessstatus: **ZONE_FILL=0, DRC=0, ERC=0, JSON_GATE=0**
- Artefakt: `revb-b08-native-kicad8-preflight` (speichert Quellprojekt und Original-Berichte, GitHub-Aufbewahrung begrenzt).

## Wichtige verbleibende Gates

1. STX883PRO-Pads: Rastermaß unten auf 2,54 mm angepasst (Herstellerbild Rev1.1), aber JLC/EasyEDA-Landpattern C3001517 inklusive Pinorientierung und der genauen Anlandemaße noch **nicht** verglichen.
2. Antennen-RF: bisher `ANT` ca. 5,37 mm auf F.Cu bei 0,25 mm Leiterbahnbreite. Hersteller fordert eine 50-Ω-Antenne; die Stripline-/Coplanar-Impedanz und Rückstromfläche sind **nicht** verifiziert.
3. Mechanik: 30 × 70 mm, 2,2-mm-Montagebohrungen, Akku-/Buzzer-/Antenne-Anschluss und Gehäusehöhe an tatsächlichem Funktaster noch nicht abgenommen.
4. Versorgung/Timing: VERICO-Ausgang, Ruhestrom/Boost-Autoabschaltung, 9 V auf 3,3 V, 1-ms-Buzzer, 1000-ms-Haltezeit, Entladung, 1,12-s-Sperrphase und fünf DIAMEX-Funkkennungen noch nicht auf echter neuer Hardware nachgewiesen.
5. HF-Funkrecht: Antennengewinn, Ausgangsleistung/ERP, Duty-Cycle und Spektrum vor realem Einsatz prüfen.

**Kein Gerberexport, `fabrication_release=false`.** 0 CAD-Verstöße beweisen keine physische Bestückbarkeit oder Funkkonformität.
