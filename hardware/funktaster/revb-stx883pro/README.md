> **Aktuell: Firmware V2-N9.1 / Dokumentation D4.** Für die neun neuen Geräte die U4-Dateien mit **N9** im Namen verwenden. U1/HOLD bleibt unverändert. Vier Pakete mit drei Neuner-Zeitplatzrunden; kein Empfängerupdate bei diamex-5 erforderlich. Hallenprüfung steht aus.

# Wasserfreunde Dalum - Buzzer Rev B0.10

Aktueller Stand **B0.10-S2 / Dokumentation D3**, 19.11.2026. Beschriftung: **Buzzer Rev B0.10** mit kleinem v, Komponentenreferenzen, Pinmarkierungen und ausführlicher Rückseitenlegende.

Laut geprüftem Bestellverlauf sind **zehn Leiterplatten, davon neun Standard-PCBA**, bestellt. Beide Controller werden unprogrammiert geliefert. Eine Platine zuerst elektrisch, mechanisch und im Funkbetrieb abnehmen.

- [PDF: Anschluss, Programmierung und Erstprüfung](dokumentation-b10-d2/documents/Buzzer_RevB_B010_Anleitung_Programmierung.pdf)
- [Vollständiges Paket und Herkunft](dokumentation-b10-d2/README.md)
- [Download: CAD, Fertigung, Firmware IDs 1-9 und Anleitung](Buzzer_RevB_B010_S2_9x_Dokumentation.zip)
- [Prüfstatus](dokumentation-b10-d2/validation/RELEASE_GATES.json)
- [Gesicherter Bestellstand ohne private Kundendaten](dokumentation-b10-d2/evidence/BESTELLSTAND.json)

Rev B integriert ATtiny402-Impulsverlängerung, ATtiny13A-V2-Sendersteuerung und STX883PRO auf 30 x 70 mm. Native KiCad8.0.9: DRC0/ERC0/Unconnected0/Parität0, CI44374130631. U5-Lands sind mit der offiziellen JLCEDA/EasyEDA-Bibliothek abgeglichen. Die tatsächlich importierte finale CPL ist reproduzierbar archiviert; der frühere B0.9-CPL-Blocker ist für diesen Stand behoben. Keine manuellen Viewer-Änderungen nach dem finalen Import.

Programmierung: U1 an J4/UPDI mit Controller3V3; U4 an J5/ISP mit TX3V3. Getrennte Schienen nicht verbinden. Akku und jeweils anderen Programmer entfernen; extern geregelte 3,3 V, DIAMEX-Targetversorgung aus. Gedrückthalten des Buzzers genügt wegen der Abschaltung nach etwa 1 s nicht. Pro physischem Sender eine eindeutige ID verwenden; IDs 6-9 neu anlernen.

Hardware-, Akku-, Programmier-, Gehäuse- und Funkabnahmen bleiben offen. Die Dateiprüfung ist keine Funktionsgarantie oder Serienfreigabe. Historische B0.2-B0.9-Dateien bleiben als Verlauf erhalten; aktuelle Bestellgrundlage ist ausschließlich dokumentation-b10-d2/manufacturing.

## Bestelltes Zubehör und aktuelle Arbeitsanleitungen

Adafruit High Voltage UPDI Friend5893 und ein10-Pack433-MHz-Federantennen (Angabe5mm) sind bestellt.

- [Friend5893 Schritt für Schritt](dokumentation-b10-d2/documents/UPDI_FRIEND_5893.md)
- [Federantennen montieren](dokumentation-b10-d2/documents/ANTENNE_433MHZ.md)

Die PDF ist auf14Seiten aktualisiert. Der Ordnername dokumentation-b10-d2 bleibt für bestehende Links erhalten; inhaltlicher Stand ist D3. Platine, Fertigungsdateien und Firmware bleiben unverändert.

[Theoretische Genauigkeit für einen und mehrere Buzzer](dokumentation-b10-d2/documents/GENAUIGKEIT_N9.md). Die PDF umfasst jetzt14Seiten. D3-Angaben zur bisherigen U4-Firmware sind historisch.

Die aktuellen HEX heißen ATtiny13A_V2_N9_ID1.hex bis ID9.hex und liegen im Gesamtarchiv unter firmware/. Dateien ohne N9 sind historischer Rückfall. Quelle und reproduzierbarer Build liegen unter source/firmware-nine-slot/; im Repository zusätzlich unter firmware-nine-slot/.
