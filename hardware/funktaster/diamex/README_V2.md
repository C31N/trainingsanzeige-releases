# Buzzer-Firmware V2 – weniger Kollisionen, bessere Zeitübernahme

Für den aktuellen Empfänger **diamex-5**. Installation und Buzzer-Programmierung
erfolgen bewusst manuell. Bereits programmierte V2-Buzzer benötigen wegen der
Dokumentationsüberarbeitung kein neues Flashen. Die vollständige Funk- und
Zeitmessabnahme am Hallenstandort steht noch aus.

Der Lochrasteraufbau **V5 bleibt unverändert**: ATtiny13A, STX882, DATA an
PB3/Pin 2. Keine neue Lötarbeit. Die Firmware wird mit dem DIAMEX USB ISP
übertragen. Das Paket enthält die bisherigen fünf V1-Dateien als Rückfall und
fertige V2-Dateien für IDs 1–255; auf dem Windows-PC ist kein Compiler nötig.

## Reihenfolge: zuerst Empfänger, dann Buzzer

1. Anwendungsupdate mit Empfänger **diamex-5** auf dem Pi installieren.
   Unter **Admin → Funktaster** steht die Empfängerkennung in der Diagnose.
   Alte V1-Buzzer und EV1527-Fernbedienungen funktionieren damit weiter.
2. Kein Training/Spiel laden. Aktuelles `DIAMEX_Funktaster.zip` vollständig in
   einen neuen Ordner entpacken und `START_Funktaster_Programmer.cmd` starten.
3. COM-Port wählen und Verbindung prüfen. Fertiger Buzzer: Akku eingesetzt,
   großen Taster bis zum Ende der Programmierung gedrückt halten. Beide
   Target-Versorgungsschalter am DIAMEX **AUS**. Niemals 5 V in die fertige
   3,3-V-Schaltung einspeisen oder Akku und Fremdversorgung zusammenschalten.
4. **V2 – Zeitstempel / Kollisionsminderung** wählen und erst nach Schritt 1
   „Pi-Empfänger diamex-5 vorher installiert“ bestätigen.
5. Richtigen Button „Buzzer 1 … 5 programmieren“ drücken. Andere IDs unter
   „Eigene ID“ auswählen. Jede physische Taste braucht eine eigene ID!
   Eine ID ist keine Bahnnummer; die Bahn wird weiterhin im Adminmenü zugeordnet.
6. Erfolg/Flashprüfung abwarten, Taster loslassen, ISP-Kabel abziehen.
   Mindestens drei Sekunden warten und einzeln testen. IDs 1–5 behalten ihre
   bisherigen Funkcodes und Bahnzuordnungen; andere IDs einmal anlernen.
7. Erst danach den nächsten Buzzer programmieren. V1 und V2 dürfen während
   der Umstellung gemeinsam betrieben werden; nur V2 bietet die Zeitkorrektur.

Fuses bleiben **HFUSE 0xFB / LFUSE 0x76**; bereits korrekte Werte werden nur
ausgelesen und nicht erneut geschrieben. Kein `-F`, keine Abschaltung von
RESET oder SPIEN, keine zusätzlichen Lockbit-Schreibbefehle. Fehler müssen vor dem nächsten
Programmierschritt geklärt werden. Es wird nichts automatisch geflasht.

## Empfangstest vor dem Training

- Jede Taste mehrfach einzeln drücken: richtige Bahn, genau eine Aktion.
- Dann zwei und anschließend alle vorhandenen Tasten gemeinsam testen.
- Am realen Aufstellort mit geschlossenem Gehäuse, neuer/geladener Batterie,
  eingeschaltetem TV und normal positionierter Empfangsantenne wiederholen.
- Kurz drücken und länger halten: Halten darf keine weitere Aktion auslösen.
  Bei sehr kurzem Druck kann die Stromversorgung spätere Wiederholungen
  abschneiden. Zum ersten Vergleich etwa **250 ms** drücken; danach auch die
  im Betrieb üblichen kurzen Drücke prüfen.
- Diagnose zeigt Protokoll, Ereignisnummer, Zeitkorrektur und Zeit bis Aktion.
  Eine größere Zeitkorrektur bedeutet einen später erfolgreich empfangenen
  Wiederholungsframe, nicht automatisch einen stockenden Pi.

## Funkformat und Zeitübernahme

V2 sendet `D3 6D ID EVENT REPEAT AGE_H AGE_L CRC16_H CRC16_L`
(9 Byte, CRC-16/XMODEM, Polynom 0x1021, Initialwert 0).
Ein Druck erhält vor dem Senden eine gespeicherte 8-Bit-Ereignisnummer.
Die Nummer läuft nach 255 auf 0; Empfangssperren gelten nur zwei Sekunden.
32 EEPROM-Einträge mit Wert/Gegenwert verteilen die Schreibzugriffe und
lassen abgebrochene Einträge erkennen. Ein Speicherfehler ist dadurch nicht
ausgeschlossen; dieser Mechanismus ist keine Sicherheitszertifizierung.

Timer0 misst seit Firmwarestart mit nominal 26⅔ µs je Tick (9,6 MHz /256).
Überläufe werden ohne Interrupts geprüft, damit die Funkpulse nicht durch
Interrupts verschoben werden. Der Empfänger berücksichtigt die gemessene
Präambelgeschwindigkeit und die Telegrammdauer. V1/EV1527 erhalten weiterhin
ihren Empfangszeitstempel, aber keine behauptete Sendezeitkorrektur.
Dabei bleiben die GPIO-Zeitstempel unterhalb einer Mikrosekunde erhalten;
die Schleifen-/GPIO-Takte der kompilierten Präambel werden mitberücksichtigt.
Der Build prüft die verwendeten 2887 CPU-Takte je Präambelpaar. Ein anderer
Compiler mit abweichendem Timing benötigt eine erneute Prüfung dieser Konstante.

Das erste Telegramm beginnt nominal nach derselben 15-ms-Beruhigungszeit wie
bisher. Die EEPROM-Schreibvorgänge liegen normalerweise innerhalb dieser Zeit.
Danach folgen vier versetzte Wiederholungen mit wechselnder Slotreihenfolge.
Die späteren Wiederholungen variieren zusätzlich mit Ereignisnummer und ID,
damit unterschiedliche RC-Takte nicht immer wieder dieselbe Kollision erzeugen.
Das ist deterministische Zeitvariation, keine behauptete echte Zufallsquelle.
IDs 1–5 haben verschiedene Erholungsslots; IDs 6–255 teilen sich diese fünf
Slotklassen. Es gibt **keine Garantie für 255 gleichzeitig sendende Geräte**.
Der gesamte Burst endet nach höchstens etwa 0,75 Sekunden nominal und die Taste
schläft danach bis zur nächsten Stromunterbrechung. Kein Dauersenden.

Der Empfänger führt einen Druck nur einmal aus. Die Übergabeprüfung verwendet
das Alter seit Empfang, nicht das bereits korrigierte Alter des Drucks.

### Zeitauflösung ist nicht Gesamtgenauigkeit

Die 26⅔ µs sind die interne Timerauflösung, keine bestätigte Genauigkeit am
mechanischen Knopf. Die Tests der kompilierten Firmware verlangen bei nominalem
Takt weniger als 1,5 ms Abweichung beim Rückrechnen auf den **Firmwarestart**;
bei den getesteten Taktskalierungen 0,8 bis 1,25 entsprechend unter 1,9 ms.
Die gespeicherten Modelle für Buzzer 1–4 ergeben nominal etwa 0,1 ms Restversatz.
Das sind simulierte Werte, keine mit einer Referenzzeitmessanlage gemessenen
Betätigungszeiten. Einschalt-/Resetverhalten, Kontakte, Versorgung und reale
Funkverzerrung sind damit nicht als Gesamtfehler bestimmt.

Spätere erfolgreiche Wiederholungen werden zeitlich zurückgerechnet. Das
verhindert, dass die gesamte Funk-/App-Laufzeit als Schwimmzeit gezählt wird;
ein verlorener Tastendruck kann jedoch nicht rekonstruiert werden. Die sichtbare
Reaktion der Anzeige darf später kommen als der verwendete Ereigniszeitpunkt.
Eine Anzeige von Hundertsteln ist keine zugesicherte Genauigkeit von ±0,01 s.
Für eine belastbare praktische Genauigkeitsangabe ist eine gemeinsame Messung
mit elektrischer Kontakt-/Referenzzeit und allen verwendeten Buzzern erforderlich.
Eine 80-ms-Entprellung gilt weiterhin je Buzzer, gemessen an den korrigierten
Zeitpunkten; andere Buzzer werden dadurch nicht gesperrt. Instabile Versorgung
mit wiederholten echten Neustarts muss trotzdem an der Hardware behoben werden.
Trainingstimer verwenden den korrigierten Zeitpunkt statt der HTTP-Ankunft.
Ältere Eingaben dürfen keine neuere manuelle Bedienung, einen neuen Plan oder
einen bereits weitergeschalteten Trainingsabschnitt rückwirkend verändern.

## Grenzen und Rückfall

STX882 ist ein Einweg-Sender: keine Empfangsbestätigung, kein gesicherter
Kollisionsschutz. Regleranlauf, Tasterprellen, Reset-/Fuse-Anlauf und der interne
RC-Takt bleiben reale Unsicherheiten. Die Korrektur bezieht sich auf den
Firmwarestart – sie ist **keine garantierte millisekundengenaue Anschlagmessung**.
Echte Funk-/Zeitmessungen und ein Vergleich gegen eine Referenz sind noch nötig.
Simulatorprüfungen ersetzen weder den Hallentest noch eine Wettkampfzulassung.
Ein weiterer Druck benötigt weiterhin eine echte Stromunterbrechung/Reset.
Extrem kurzes Loslassen kann bei geladenen Stützkondensatoren dafür zu kurz sein.

Rückfall: im Programmer V1 wählen und die bisherige ID 1–5 programmieren.
Die neue Empfängersoftware kann installiert bleiben. Vor einem Rücksetzen der
Pi-Software alle V2-Tasten wieder auf V1 bringen; alte Empfänger verstehen V2
nicht. Eigene IDs ab 6 besitzen in diesem Paket keinen V1-Rückfall.

## Reproduzierbarer Build (Entwicklung)

Die folgenden Entwicklungsskripte liegen im Repository unter
`trainingsanzeige/hardware/funktaster`, nicht im Endnutzer-Downloadpaket.

`python build_firmware_v2.py --toolchain PFAD_ZU_AVR_GCC_BIN`
erstellt HEX/BIN und SHA-256-Katalog für alle IDs. `avr_waveform.py` modelliert
die tatsächlich kompilierten Instruktionen inklusive Timer, Stack und EEPROM;
unbekannte Instruktionen führen zum Fehler. Die gespeicherten Wellenformen sind
**Simulationsdaten**, keine aufgenommenen Funksignale.

`python build_package_v5.py` erzeugt das aktuelle V7-Downloadpaket; der historische
Skriptname bleibt für vorhandene Abläufe erhalten. `python verify_package.py`
prüft Archiv, V1-Rückfall, V2-Dateien und Prüfsummen, ohne zu programmieren.
