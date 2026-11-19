# Buzzer Rev B0.10 - Dokumentation D3

Stand 19.11.2026: Die beschriftete Revision **B0.10-S2** ist laut sichtbarem JLCPCB-Bestellverlauf bestellt: zehn Leiterplatten, davon **neun Standard-PCBA**, eine unbestückt. Die PDF und Firmware gelten für IDs 1-9. Beide Controller sind nach Lieferung selbst zu programmieren. Erst eine Platine vollständig prüfen.

## Benutzen
1. documents/Buzzer_RevB_B010_Anleitung_Programmierung.pdf lesen.
2. Archiv mit `python tools/verify_archive.py` prüfen.
3. U1 über J4/UPDI, U4 über J5/ISP programmieren. Versorgung jeweils geregelte 3,3 V; J4 und J5 sind getrennte Schienen. Akku und jeweils anderen Programmer abziehen.
4. Pro physischem Sender eine eindeutige ID vergeben. IDs 6-9 im Empfänger diamex-5 neu anlernen; bestehende ID-Zuordnungen nicht doppelt vergeben.
5. Nach erfolgreicher Programmierung die ID im freien Feld auf der Platine markieren und die Musterprüfung protokollieren.

## Fertigungsstand
manufacturing/ enthält die tatsächlich hochgeladenen S2-Gerber, die genehmigte BOM und die finale neu importierte numerische CPL. Diese ersetzt die historische B0.9-Bestückung. U1/U4: 270 Grad; U2/U3/Q1-Q4: 180 Grad; alle übrigen: 0 Grad. U5 enthält den JLC-Bibliotheksversatz. Keine manuellen Viewer-Änderungen nach dem letzten Import. Aufdruck vorne und hinten: **Buzzer Rev B0.10** (kleines v).

Native KiCad-8.0.9-Prüfung im CI-Lauf 44374130631: DRC, ERC, Unconnected und Schaltplanparität jeweils 0. Die S2-Änderung ergänzt Aufdruck ohne Kupfer- oder Bestückungsänderung. Das ist keine elektrische oder Funkabnahme. Reale Programmier-, Versorgungs-, Akku-, Gehäuse- und Funkprüfungen bleiben offen; siehe validation/RELEASE_GATES.json.

## Herkunft und Wiederherstellung
source/Buzzer_RevB_STX883PRO_Entwurf_B0.10_S2.zip enthält den vollständigen nativen CAD-Stand. source/ enthält außerdem die B0.3-Basis, Patchskripte, Workflow, Rev-A-Controllerquelle und unveränderte DIAMEX-Firmwarequelle. Die CI-Datei dokumentiert die Patchreihenfolge und KiCad-Version. Die Quellskripte stammen aus dem Sechser-Prototypenexport; dessen Mengenmetadaten sind historisch. Maßgeblich für die tatsächlich bestellte Menge ist evidence/BESTELLSTAND.json. Die zusätzliche Firmware für IDs 7-9 stammt bytegleich aus DIAMEX_Funktaster.zip, firmware/v2/buzzer7.hex bis buzzer9.hex.

Offizielle U5-Landpatternquelle: **JLCEDA/EasyEDA Official Library**, https://lceda.cn/ und https://easyeda.com/ . Originalquelle und Lizenzangabe stehen unter source/validation/b10-footprint/. Keine fremde Bibliothek als eigene Arbeit ausgegeben.

## Belege und Datenschutz
Der vollständige Bildexport zeigt alle 35 SMD-Referenzen. Der BOM-Beleg wurde während der Sechservorbereitung gesichert und belegt Typen/Zuordnung, nicht die endgültigen Verbrauchsmengen für neun. Der Bestellverlauf bestätigt neun PCBA und dieselben Dateinamen; nachträgliche nicht sichtbare Änderungen können daraus nicht ausgeschlossen werden. Private Adresse, Telefonnummer, Bestellnummer, Konto- und Zahlungsdaten werden nicht veröffentlicht. Der öffentlich dokumentierte Gesamtbetrag ist 192,22 USD inklusive angezeigter Versandkosten und Abgaben; ein tatsächlicher Gutscheinanteil war nicht separat sichtbar.

Das historische dokumentation-b09-d1 bleibt unverändert. Es ist keine aktuelle Bestellgrundlage. SHA256SUMS.txt erfasst alle Dateien dieses Pakets; eine erfolgreiche Prüfung ist keine Hardwarefreigabe.

## Bestelltes Zubehör und aktuelle Arbeitsanleitungen

Adafruit High Voltage UPDI Friend5893 und ein10-Pack433-MHz-Federantennen (Angabe5mm) sind bestellt.

- [Friend5893 Schritt für Schritt](documents/UPDI_FRIEND_5893.md)
- [Federantennen montieren](documents/ANTENNE_433MHZ.md)

Die PDF wurde auf zwölf Seiten ergänzt. Der Ordnername dokumentation-b10-d2 bleibt für bestehende Links erhalten; inhaltlicher Stand ist D3. Platine, Fertigungsdateien und Firmware bleiben unverändert.
