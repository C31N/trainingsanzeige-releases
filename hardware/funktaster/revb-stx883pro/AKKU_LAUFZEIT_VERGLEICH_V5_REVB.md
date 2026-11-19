# Akkuverbrauch: vorhandene V5 + Rev A vs. integrierte Rev B0.9

**Stand 18.11.2026, nur technische Abschätzung, KEINE gemessene Laufzeit.**

## Quellen
- VERICO LoopEnergy PP3 4500: 9 V konstant, 500 mAh / 4500 mWh laut Hersteller: https://www.vericoglobal.com/en/products/loopenergy-pp3-4500/
- NiceRF STX882: 34 mA @ 3,3 V, 15 dBm (nur TX-Phase): https://www.nicerf.com/ask-modules/433mhz-ask-transmitter-module-stx882.html
- NiceRF STX883PRO: typisch 9,2 mA @ 3,3 V, 10 dBm, Modulherstellerdatenblatt; max. laut Webseite <20 mA: https://www.nicerf.com/ask-modules/ask-transmitter-module-stx883pro.html
- Alter R-78E3.3-0.5: Schaltregler, je nach Last ca. 75–88 % Wirkungsgrad: https://recom-power.com/de/rec-p-R-78E3.3-0.5.html
- Neuer TPS70933: Linearregler, 3,3 V bei 9 V Eingang; typischer IQ nur ~1 µA, aber Verlustleistung = (9 V – 3,3 V) × Laststrom: https://www.ti.com/product/TPS709
- Die V5- und Rev-B-Schaltungen enthalten jeweils einen 330-Ω-Entladewiderstand an 3,3 V. Solange 3,3 V anliegt, zieht dieser 10 mA (P=33 mW).
- Gemessene 9 V am vom Nutzer verwendeten VERICO-Block bestätigen Spannung, **nicht** seine Laufzeit, Ruhestrom oder Belastbarkeit.

## Entscheidend ist die Ruhephase

**Alt V5 allein ohne Rev-A-Halteplatine:** Hauptplatine war direkt durch den Taster stromlos geschaltet. Die Elektronik benötigte zwischen Betätigungen im Wesentlichen keinen Strom; trotzdem bleibt die Eigenaufnahme der im Akku eingebauten 9-V-Elektronik.

**Alt V5 mit Rev-A-Zusatzplatine:** ATtiny402 und TPS70933 laufen auch in Ruhe, sonst wäre die 1-ms-Erkennung nicht möglich. Vergleichbar zur neuen Rev-B-Schaltung: gleiche Controller-Standby-Architektur, aber genaue Firmware-Ruheleistungsaufnahme nicht gemessen.

**Neu Rev B0.9:** Standby-Controller U1 + LDO U2 immer versorgt; Funkteil U3/U4/U5 nur für nominal 1 Sekunde eingeschaltet. Es ist nicht belegt, ob der ATtiny402 korrekt im tiefen Schlafmodus arbeitet; Akku-Boost-Standby-Strom und Unterlastabschaltung ebenfalls unbekannt.

## Realistische Vergleichsrechnung (nur veranschaulichendes Modell)

Annäherung: 9-V-Output 500 mAh nutzbar, 100 Tastendrücke/Tag, neue Schaltung pro Tastendruck 1 Sekunde lang **20 mA aus dem 9-V-Akku** (kein Messwert!). Nutzungsbeitrag: 100 × 1 s × 20 mA / 3600 = **0,556 mAh pro Tag**.

| Gemessener/simulierte 9-V-Ruhestrom | 9-V-Ruheaufnahme pro Tag | Modellierte theoretische Gesamtlaufzeit |
| --- | ---: | ---: |
| 0,05 mA | 1,2 mAh | 285 Tage |
| 0,10 mA | 2,4 mAh | 169 Tage |
| 0,50 mA | 12 mAh | 40 Tage |
| 1,00 mA | 24 mAh | 20 Tage |
| 2,00 mA | 48 mAh | 10 Tage |

Formel: `tage = 500 / (24 * I_ruhe_mA + tastendruecke_pro_tag * I_aktiv_mA * t_aktiv_s / 3600)`.

**Keine Laufzeitgarantie:** Nennenergie, tatsächliche nutzbare Kapazität, Boost-Wirkungsgrad, Akku-Eigenverbrauch, Alterung und Unterlastabschaltung sind nicht eingerechnet. Der Ausgangsstrom bei 9 V muss gemessen werden. In Ruhe kann die Akku-Boost-Schaltung den Verbrauch dominieren. Die tatsächlichen Laufzeiten können wesentlich kürzer ausfallen.

## Wieso weniger Funkstrom keine 4× Laufzeit bedeutet

STX883PRO braucht beim Senden deutlich weniger Strom als STX882 (9,2 gegenüber 34 mA typisch bei unterschiedlichen HF-Ausgangsleistungen). Jedoch ersetzt ein **9-V->3,3-V-LDO** den **energieeffizienten DC/DC-Schaltregler** der alten Platine. Gleichzeitig liegt der 330-Ω-Entladewiderstand mit 10 mA auf der 3,3-V-Schiene während des Einschaltfensters. Die Nettobilanz der **gesamten Batterieaufnahme** ist ohne TX-/Ruhemessungen nicht sicher berechenbar.

## Messplan (vor 5-teiliger JLCPCB-Prototypenbestellung empfohlen)

1. 9-V-Akkustrom **in Serie** messen – Multimeter nie direkt über den Akku im Strommessmodus anschließen (Kurzschluss!).
2. **Betriebszustände vergleichen:** Alt V5 direkt, Alt V5 + Rev A, Neu Rev B0.9.
3. Aufzeichnung: Ruhestrom nach 30 Sekunden und 30 Minuten, Startimpuls, RF-aktiv während 1000 ms, Entladephase, nach Rückkehr in Ruhe.
4. Zeitaufgelöste Strommessung verwenden, da ein normales Multimeter den 1-Sekunden-Peak mittelt.
5. Akku voll und teilweise entladen testen; dokumentieren, ob USB-C-Boost bei Mikrolast abschaltet.
6. Vor Serienfreigabe reale Dauerzyklen und 5-teilige Funktionsprüfung dokumentieren.

**Freigabe**: battery_9v_confirmed=true (Nutzermessung), idle_current_verified=false, active_current_verified=false, capacity_verified=false, runtime_claim_approved=false, fabrication_release=false.
