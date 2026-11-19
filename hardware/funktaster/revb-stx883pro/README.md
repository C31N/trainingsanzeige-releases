# Wasserfreunde Dalum - Buzzer Rev B0.10

Aktueller Stand **B0.10-S2 / Dokumentation D2**, 19.11.2026. Beschriftung: **Buzzer Rev B0.10** mit kleinem v, Komponentenreferenzen, Pinmarkierungen und ausführlicher Rückseitenlegende.

Laut geprüftem Bestellverlauf sind **zehn Leiterplatten, davon neun Standard-PCBA**, bestellt. Beide Controller werden unprogrammiert geliefert. Eine Platine zuerst elektrisch, mechanisch und im Funkbetrieb abnehmen.

- [PDF: Anschluss, Programmierung und Erstprüfung](dokumentation-b10-d2/documents/Buzzer_RevB_B010_Anleitung_Programmierung.pdf)
- [Vollständiges Paket und Herkunft](dokumentation-b10-d2/README.md)
- [Download: CAD, Fertigung, Firmware IDs 1-9 und Anleitung](Buzzer_RevB_B010_S2_9x_Dokumentation.zip)
- [Prüfstatus](dokumentation-b10-d2/validation/RELEASE_GATES.json)
- [Gesicherter Bestellstand ohne private Kundendaten](dokumentation-b10-d2/evidence/BESTELLSTAND.json)

Rev B integriert ATtiny402-Impulsverlängerung, ATtiny13A-V2-Sendersteuerung und STX883PRO auf 30 x 70 mm. Native KiCad8.0.9: DRC0/ERC0/Unconnected0/Parität0, CI44374130631. U5-Lands sind mit der offiziellen JLCEDA/EasyEDA-Bibliothek abgeglichen. Die tatsächlich importierte finale CPL ist reproduzierbar archiviert; der frühere B0.9-CPL-Blocker ist für diesen Stand behoben. Keine manuellen Viewer-Änderungen nach dem finalen Import.

Programmierung: U1 an J4/UPDI mit Controller3V3; U4 an J5/ISP mit TX3V3. Getrennte Schienen nicht verbinden. Akku und jeweils anderen Programmer entfernen; extern geregelte 3,3 V, DIAMEX-Targetversorgung aus. Gedrückthalten des Buzzers genügt wegen der Abschaltung nach etwa 1 s nicht. Pro physischem Sender eine eindeutige ID verwenden; IDs 6-9 neu anlernen.

Hardware-, Akku-, Programmier-, Gehäuse- und Funkabnahmen bleiben offen. Die Dateiprüfung ist keine Funktionsgarantie oder Serienfreigabe. Historische B0.2-B0.9-Dateien bleiben als Verlauf erhalten; aktuelle Bestellgrundlage ist ausschließlich dokumentation-b10-d2/manufacturing.
