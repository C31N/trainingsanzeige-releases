# Bewertung einer einzigen Senderplatine statt Zusatzplatine (Entwurfsentscheidung)

**Für die ersten fünf vorhandenen V5-Sender: Rev-A-Zusatzplatine bevorzugen, nicht sofort integrieren.**

## Warum?
- Bisheriger V5-Funktaster: ATtiny13A, 433-MHz-STX882, R-78E3.3-0.5, Akku und Taster auf Lochraster. Das Rev-A-Modul erhält unverändert Firmware, Funkcode, ID und vorhandenes Sender-Hardwaremodul.
- Voll integrierte Trägerplatine mit ATtiny402 + ATtiny13A + STX882 + Regler spart Kabel und Montagefläche, benötigt aber neues Layout und Abnahme der Reset-, HF-, Antennen-, EMV- und Reichweiteneigenschaften sowie Gehäuseprüfung.
- Der ursprüngliche STX882 ist nicht als maschinell bestückbares JLCPCB-Lagerbauteil nachgewiesen. Das RF-Modul sowie ein etwaiger THT-Regler/Anschlüsse können zusätzliche Handbestückung erfordern; **vollbestückt** ist daher nicht gesichert.
- Ein bestückbares SMD-Alternativmodul, STX883PRO-433MHz (C3001517), ist am JLC-Katalog gelistet, sendet aber mit anderen Leistungsdaten. Austausch gegen STX882 ohne Funk- und Zulassungs-/Reichweitenprüfung nicht empfehlen.
- Eine Einzel-MCU-Architektur, die V2-Protokoll und Impulsverlängerung zusammenführt, braucht neue Firmware mit EEPROM/ID-Migration und Nachweis der Ereignisfolge. Für fünf Stück ist das erheblich aufwendiger als die vorhandene Rev-A-Ergänzung.

## Empfehlung
1. Einen Rev-A-Prototyp fertigen/bestücken, UPDI programmieren und reale Messungen + Funktests durchführen.
2. Nach Freigabe die restlichen vier gleichen Platinen bestücken lassen oder bei Einmalauftrag fünf bestellen und nur eine zuerst in Betrieb nehmen.
3. Eine integrierte Rev B separat als **Neuentwicklung** planen (inkl. Schaltplan und KiCad-PCB, 433-MHz-RF-Layout, fertigungsgerechtem Modul, Gehäuse, Sicherung und programmierfähigen Testpads). Keine ungeprüfte Gerberdatei als bestellbereit behandeln.

Quellen: `hardware/funktaster/Lochrasterplan_Funktaster_V5_Rueckseitenverdrahtung.pdf`, Rev-A-README/BOM und https://jlcpcb.com/partdetail/GNiceRF-STX883PRO433MHz/C3001517
