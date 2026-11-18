# HF-Vergleichsmessung: bestehende V5-Funktaster vs. neue STX883PRO Rev B

**Stand: 18. November 2026. Kein Messprotokoll beigefügt; Nutzerangabe, noch keine unabhängige Verifikation.**

## Vorliegende Nutzermessung – bestehende fertig montierte Geräte

- Bestehende, selbst gelötete V5-Senderplatinen wurden **im vollständig eingebauten Zustand** funktechnisch geprüft.
- Pro Buzzer wurden **10 Einzelmessungen** ausgeführt.
- **Jede** dieser Messungen lag laut Nutzerangabe rund **10 % unter der für die verwendete Messart zugrunde gelegten gesetzlichen Höchstgrenze**.
- Akku: Beim vorhandenen VERICO-9-V-Block wurden am Ausgang **9 V** gemessen (Messbedingungen/Last noch unbekannt).
- Noch nicht dokumentiert: Einzelmesswerte, Einheit (ERP/EIRP/Feldstärke/leitungsgebundene Leistung), Frequenz, Antennentyp, Abstand/Kalibrierung, Messunsicherheit, Duty-Cycle-Prüfung, Akkuladezustand und Prüfgerät/-labor.

**Daraus folgt NICHT, dass Rev B mit STX883PRO bereits gesetzeskonform ist.** Ein anderes RF-Modul, veränderte Antennenführung, Gehäuseeinbau und Antenne können die abgestrahlte Leistung ändern.

## Regulatorischer Arbeitspunkt Deutschland

Die [Bundesnetzagentur, Allgemeinzuteilung SRD Vfg. 91/2025](https://www.bundesnetzagentur.de/DE/Fachthemen/Telekommunikation/Frequenzen/Allgemeinzuteilungen/_DL/vfg91_2025.pdf?__blob=publicationFile&v=3), Tabelle 2, Zeile **44b** sieht für Geräte geringer Reichweite 433,05–434,79 MHz **10 mW ERP** und Arbeitszyklus **≤ 10 %** vor. Zeile 44a gestattet 1 mW ERP ohne diese Arbeitszyklusbeschränkung. Die konkret verwendbare Zeile und alle weiteren Anforderungen sind zum Endgerät passend auszuwählen.

NiceRF spezifiziert den [STX883PRO](https://www.nicerf.com/ask-modules/ask-transmitter-module-stx883pro.html) mit **10 dBm Sender-Ausgangsleistung bei 3,3 V**. Das sind **10 mW am Senderausgang** (typischer Datenblattwert), **nicht automatisch 10 mW ERP** an der fertigen Gehäuse-/Antennenanordnung. Antennengewinn, Verluste, Aufbau und Messunsicherheit verändern die ERP.

Eine Messung mit ca. 90 % des ERP-Limits entspräche bei tatsächlicher Anwendung der 10-mW-ERP-Regel etwa 9 mW ERP. Die bisherigen Einzelwerte und ihre Einheit sind unbekannt; diese Zahl ist nur eine theoretische Umrechnung, kein gemessener V5-Wert.

## Abnahmekriterien für fünf neue Rev-B-Sender

1. Erst vollständige Layout-, JLC-Bestückungs-, Footprint- und 3,3-V-Versorgungsabnahme; 9-V-Leerlaufmessung allein genügt nicht.
2. **Alle fünf neuen Buzzer vollständig montieren**, mit endgültiger Antenne, dem vorgesehenen Gehäuse, Akku und identischem Messaufbau wie bei den V5-Geräten.
3. **10 HF-Einzelmessungen je Buzzer**, alle Einzelwerte mit Einheiten und zulässiger Messunsicherheit dokumentieren. Keine Mittelwertprüfung statt Einzelwertprüfung.
4. Grenzwertabhängige Bewertung: **jede** relevante Einzelmessung einschließlich Messunsicherheit muss den für die Einsatzklasse zutreffenden ERP-Grenzwert einhalten. Zielwert ist mindestens der dokumentierte V5-Pegel, sofern genügend Messreserve und zuverlässige Funkreichweite bestehen; gegebenenfalls niedrigere Ausgangsleistung/Antennengewinn oder Anpassnetzwerk auslegen.
5. Frequenz, Modulationsbandbreite, Oberwellen, Duty-Cycle (mit 1000-ms-Haltezeit plus Telegrammwiederholungen) und Empfangssicherheit unter realer Nutzung nachweisen.
6. Gerät bei vollem und schwachem Akkustand unter Sendelast prüfen; 9-V-Boost-Ausgang, Ruhestrom, Reset und DC-DC/LDO-Erwärmung messen.
7. Ergebnis in prüfbarer Tabelle (Sender-ID, Gerät/Seriennr., zehn Einzelwerte, Maximalwert, Messunsicherheit, Antenne, Akku-Zustand, Datum, Freigabeentscheidung).

## Ampel-/Release-Entscheidung

- Bestandsmessung V5: **vom Nutzer als bestanden gemeldet**, Nachweisunterlagen/Einzelwerte noch offen.
- Rev B: **FUNKFREIGABE NEIN** bis fünf Einbau-Messserien und Norm-/Frequenzprüfung vorliegen.
- Kein Ausreizen der Obergrenze aufgrund bloßer Modul-Datenblattangabe von 10 dBm.
- Keine finalen Gerber oder JLCPCB-Massenbestellung, solange der neue STX883PRO-Footprint C3001517, RF-Anpassung und prototypische Prüfung offen sind.
