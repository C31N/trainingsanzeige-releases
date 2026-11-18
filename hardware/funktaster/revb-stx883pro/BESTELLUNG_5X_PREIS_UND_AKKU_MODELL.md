# Fünf STX883PRO-Funktaster Rev B0.9 – JLCPCB und Akkurechnung

**Stand 18.11.2026.** Modellwerte, kein echter JLCPCB-Warenkorb. Für Rev B0.9 ist der native KiCad-8-DRC/ERC/Paritätslauf #33 grün. **Dieser CAD-Nachweis ist keine Freigabe von RF, fertigem Gerät, Programmierung oder externem JLC-Landpattern.** Der Nutzer hat 9 V am VERICO-Akku gemessen; der Strom ist nicht gemessen. Stückzahl **5 PCB und 5 PCBA**, jeweils **35 SMD-Teile**, **19 LCSC-Gruppen**, alle oben. Handmontage J1–J5 separat.

## Akku: Wie viele Tastendrücke?

Quelle Hersteller: https://www.vericoglobal.com/de/products/loopenergy-pp3-4500/ → 9 V, 500 mAh, 4500 mWh.

Quelle NiceRF V1.3: https://www.nicerf.com/pdf/stx883pro-ce-fcc-certified-ask-transmitter-module-v1.3.pdf → 9,2 mA typisch bei 3,3 V / 10 dBm; das Modul zieht im ungünstigen Bereich mehr Strom (auf der Webseite unter 20 mA).

**Schaltungsdaten:** R15=330 Ω zwischen TX3V3 und GND → 3,3 V / 330 Ω = **10,0 mA** während eingeschaltet. ATtiny13A plus Daten-Eingang/Regler grob weitere 3–6 mA; zur veranschaulichenden Rechnung wird **25 mA mittlerer Strom am 9-V-Akkuausgang während 1,0 s** angenommen. Dies ist **kein Messwert**. ATtiny402-Versorgung bleibt im Standby aktiv; Firmware `source_reva/firmware/main.c` verwendet `SLEEP_MODE_PWR_DOWN` im bewaffneten Zustand, aber Akkubooster-Eigenstrom ist unbekannt.

- `Q_je_Druck_mAh = I_aktiv_mA * t_s / 3600 = 25/3600 = 0,006944 mAh`.
- Bei der Hersteller-Nennkapazität **500 mAh** ohne Ruhestrom: theoretisch **72.000 Tastendrücke**.
- Modell mit **80 % nutzbarer Kapazität = 400 mAh**: theoretisch **57.600 Tastendrücke**, ohne verstrichene Ruhezeit.
- `Tage = 400 / (24 * I_ruhe_mA + 100 * 25/3600)`; `Tastendrücke = 100 * Tage`.

| Angenommener **gesamter 9-V-Akku-Ruhestrom** | Modell-Laufzeit mit 100 Tastendrücken/Tag | Tastendrücke gesamt |
| --- | ---: | ---: |
| 0,02 mA | 340,6 Tage | ca. 34.100 |
| 0,05 mA | 211,1 Tage | ca. 21.100 |
| 0,10 mA | 129,3 Tage | ca. 12.900 |
| 0,20 mA | 72,8 Tage | ca. 7.300 |
| 0,50 mA | 31,5 Tage | ca. 3.200 |

Dazu mögliche Betriebsprobleme: USB-C-9-V-Boost-Unterlasterkennung/automatische Abschaltung; real verfügbare Kapazität und Temperatur. Keine der Tabellenzeilen ist eine Messung oder Garantie.

## Kosten für 5 maschinell SMD-bestückte, unprogrammierte Prototyp-Platinen

JLCPCB-Konditionen 22.10.2026: https://jlcpcb.com/help/article/pcb-assembly-price → Economic PCBA Setup **8,18 USD**, Schablone **1,53 USD**, Extended Feeder **3,07 USD pro zusätzlicher Bauteilgruppe**, SMT 0,0016 USD je Lötstelle, Bestückungskontrolle **0,45 USD**. PCB-Aktionspreis ab **2 USD für 5 2-Lagen-PCB <= 100 × 100 mm** (nur wenn Auftragsvoraussetzungen erfüllt): https://jlcpcb.com/help/article/how-do-i-place-an-order. JLCPCB JLC C3001517 STX883PRO: https://jlcpcb.com/partdetail/gnicerf-STX883PRO433MHz/C3001517 .

### Nachvollziehbares Kostenszenario (Economic PCBA)

| Kostenbestandteil | Modellansatz USD |
| --- | ---: |
| 5 nackte zweilagige PCB (Aktionspreis) | 2,00 |
| Einrichtung | 8,18 |
| Lötpastenschablone | 1,53 |
| 17 von 19 LCSC-Gruppen als kostenpflichtig Extended (Schätzung) | 52,19 |
| 35 SMD-Bauteile je PCB × 5 (7,20 USD/PCB geschätzt) | 36,00 |
| Maschinelle Bestückung | 2,00 |
| Bestückungspositionen prüfen | 0,45 |
| Versand nach Deutschland | 22,00 |
| **Zwischensumme** | **124,35 USD** |

Währungsumrechnung **0,909 EUR je USD** (18.11.2026) = **113,03 EUR**; + 19 % Einfuhrumsatzsteuer (**21,48 EUR**) + angenommene Gebühren für Zoll-/Versandabwicklung **8,00 EUR** = **142,51 EUR Gesamtmodell** für fünf SMD-PCBA, also **28,50 EUR pro Platine**. Reale Teilepreise, Bestückbarkeitsklasse, Fracht und Kurs sind nicht fixiert.

**Budgetempfehlung**: rund **150 EUR**, zweckmäßiger Reserve-/Angebotskorridor **120–200 EUR** für fünf SMD-PCBA. Falls JLCPCB aufgrund der Modulverpackung, Bauteile oder Panelisierung Standard-PCBA verlangt: möglicherweise **180–260 EUR** (unverbindliche Szenarioabschätzung). Nicht doppelt Umsatzsteuer zahlen, falls sie schon beim Checkout eingezogen wurde. Zollbefreiung unter 150 EUR entfiel in Deutschland Juli 2026: https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Zoll/wegfall-der-150-euro-zollfreigrenze.html .

**Nicht enthalten**: Akkus, Taster und Antennen (vorhandene weiterverwenden), externe T250-mA-Sicherung, manuelle J1–J5-Verdrahtung, UPDI-/ISP-Programmierhardware/-dienstleistung, zwei Controller mit 6 Firmware-HEX-Dateien programmieren, Messtechnik und Gehäusemontage. JLCPCB bestückt Bauteile – ohne separat vereinbarten Dienst **werden die ATtiny-Chips unprogrammiert geliefert**.

## Bestellablauf nach fertigem, verifiziertem Export

1. `01_JLCPCB_GERBER_30x70_2L_PROTO.zip` bei JLCPCB als **einzige Gerber-Datei** hochladen.
2. 30 × 70 mm, zwei Lagen, FR4, 1,6 mm, 1 oz, 5 Stück PCB.
3. Economic PCBA, Oberseite/Top, **5 Stück PCBA**, 35 SMD-Positionen. Ggf. `Panel by JLCPCB` auswählen, keine Eigenpanelisierung ohne erneute Gerber/CPL-Kontrolle.
4. `02_JLCPCB_BOM_35_SMD.csv` und `03_JLCPCB_CPL_35_SMD.csv` hochladen.
5. Alle 19 LCSC-Codes auf Preis/Verfügbarkeit prüfen; im Vorschaufenster Orientierung von U1/U4, U5 (Pins 1–4), U2/U3, Q1–Q4, D1/D2 **manuell prüfen**.
6. J1–J5 und H1/H2 **nicht bestücken**; Anschlüsse später selbst.
7. **Freigabegrenze**: Das anhand der NiceRF-Maßzeichnung gezeichnete U5-Landpattern ist trotz bestandenen KiCad-DRC noch nicht mit den JLC-/EasyEDA-Fertigungsdaten verglichen. Der 3,2 mm lange, 0,8 mm breite ANT-Abschnitt hat keinen unabhängigen 50-Ω-Impedanznachweis. **Bestellung als fünf Prototypen erfolgt auf dieses Risiko, keine Serienfreigabe.**
8. Pro Platine ATtiny402 HOLD Rev A flashen; ATtiny13A auf **einzigartige ID 1 bis 5** flashen; Fuses, elektrische 3,3-V-Programmierschnittstellen, Akku unter Last und Funk im Gehäuse abnehmen.
9. Vor Einsatz je Gerät 10 HF-Einzelmessungen und Funktelegramm-/Duty-Cycle-/Leistungsprüfung. Altgeräte lagen nach Nutzerangabe je 10 Messungen ca. 10 % unter dem Grenzwert; das gilt nicht automatisch für Rev B.

## Status

- `cad_drc_erc_parity=pass` (native KiCad 8, Run #33)
- `jlc_footprint_landpattern_confirmed=false`
- `erp_and_rf_compliance_new_board=false`
- `9v_battery_voltage_user_measured=true`
- `battery_standby_and_tx_current_measured=false`
- `firmware_programmed=false`
- `manufacturing_status=prototype_only`
- `series_fabrication_release=false`
