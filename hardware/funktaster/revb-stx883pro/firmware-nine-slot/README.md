# Senderfirmware V2-N9.1 für Buzzer Rev B0.10-S2

Für die neun neu bestückten Buzzer IDs1-9. U1/HOLD bleibt bei1000ms unverändert. U4 mit images/ATtiny13A_V2_N9_ID1.hex bis ID9.hex programmieren; LFUSE76, HFUSEFB wie bisher. Diese Dateien ersetzen die bisherigen U4-HEX im aktuellen Programmierablauf. Alter und neuer Sender mit derselben ID dürfen nicht gleichzeitig betrieben werden.

## Verhalten
Erstes Paket etwa15ms nach Firmwarestart. Danach drei vollständige Runden mit neun Zeitplätzen,27ms Abstand: Basen45/288/531ms. Slot=((ID-1)*Faktor)%9; Faktoren1/2/4. Jede Runde ist eine andere Permutation. Vier Pakete statt fünf: drei vollständig getrennte Neuner-Runden passen in das bestehende HOLD-Fenster; eine vierte Neuner-Runde hätte zu wenig Reserve. Nominales Ende vor775ms; Softwaremodell prüft Ende bei1,25-facher Zeitskalierung unter975ms. Keine Erhöhung der Einschalt- oder Funkdauer. Neue Firmware ist auf IDs1-9 begrenzt.

Das Funkformat D3 6D, CRC, EEPROM-Ereigniszähler und Sendercodes bleiben erhalten. Empfänger diamex-5 akzeptiert Repeat0-3 und die Alterswerte; kein Empfängerupdate erforderlich, wenn dieser Stand bereits installiert ist. Kein Update am Pi wurde ausgelöst. Gesicherte Empfängerquelle: C31N/wasserfreunde-dalum.de, lokaler Quellstand680b65339491c9b83e72e403116da32f35fe081e, trainingsanzeige/app/radio_protocol.py. Hash und unveränderte Referenz unter tools/.

## Prüfung und Grenzen
Build mit AVR-GCC7.3.0, Warnungen als Fehler;1024-Byte-Flashgrenze. Der mitgelieferte Instruktionssimulator prüft jede kompilierte ID, Ereignisse0/1/127/255 für ID1 und Ereignis0 für IDs2-9, Stapel, Schlafzustand, Präambeltakte und spätestes Ende. Die resultierenden Flanken werden mit dem echten diamex-5-Decoder bei Taktskalierung0,8/1/1,25 gelesen und auf IDs, CRC, Wiederholungen, Ereignisse und Zeitkorrektur geprüft. verification.json enthält die Ergebnisse. Das Modell setzt ideale Versorgung und skalierte Flanken voraus; es simuliert keine reale Funkstrecke oder gemessene Oszillatoren.

Kein bestätigter Verlustquotenwert. Bei identischen Takten und gleichzeitigem Start sind die Wiederholungen nominal zeitlich getrennt. Unterschiedliche Takte und versetzte Drücke können trotzdem kollidieren; echte Senderbestätigung fehlt. Erst die spätere Hallenabnahme bewertet Empfangsquote und Zeitfehler.

## Reproduzieren
`python tools/build_verify.py --toolchain PFAD_ZU_AVR_GCC_BIN`

Dieser Befehl kompiliert und simuliert, öffnet keinen COM-Port und programmiert kein Gerät. Der modellierte Empfänger ist als Referenz beigefügt und wird nicht installiert. Alte V2-HEX bleiben im D4-Gesamtarchiv als historischer Rückfall enthalten. Firmwarequelle und Prüfsummen gehören zu diesem Paket.
