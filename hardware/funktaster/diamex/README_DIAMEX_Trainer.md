# Funktaster mit DIAMEX programmieren

Diese Anleitung gilt für das aktuelle Downloadpaket mit V5-Aufbau und V2-Firmware.
Bereits funktionierende V2-Sender benötigen wegen eines Anwendungs- oder
Dokumentationsupdates keine erneute Programmierung.

## 1. Vorbereiten

Benötigt werden Windows-PC, DIAMEX USB ISP, 6-poliges ISP-Kabel und der vollständig
aufgebaute Taster nach [Lochrasterplan V5](../Lochrasterplan_Funktaster_V5_Rueckseitenverdrahtung.pdf).
Der ATtiny13A arbeitet mit 3,3 V, STX882-DATA liegt an PB3 / Pin 2.

Zuerst auf dem Pi unter **Admin → Funktaster** Empfängerstand **diamex-5** prüfen.
V2-Sender können mit älteren Empfängern nicht verwendet werden. Die
[technische V2-Anleitung](README_V2.md) erklärt Zeitübernahme und Grenzen.

## 2. Stromversorgung und Stecker prüfen

**Beide Target-Versorgungsschalter am DIAMEX bleiben OFF.** Der fertige Taster
versorgt sich bei gedrücktem großen Taster selbst mit etwa 3,3 V. Den Taster
während des gesamten Programmierens gedrückt halten. Niemals DIAMEX-5-V-Versorgung
anlegen oder Akku und Fremdversorgung zusammenschalten. Keine lose COM/NO-Brücke.

ISP-Belegung am Taster:

```text
1 MISO    2 VCC
3 SCK     4 MOSI
5 RESET   6 GND
```

Pin 1 am echten Stecker kontrollieren. Ein verdrehter Stecker ist kein
Softwareproblem; vor dem Anschließen die Orientierung klären.

## 3. Windows-Werkzeug öffnen

1. `DIAMEX_Funktaster.zip` vollständig in einen neuen Ordner entpacken.
2. DIAMEX per USB anschließen, beide Versorgungsschalter OFF kontrollieren.
3. ISP-Kabel korrekt anschließen.
4. `START_Funktaster_Programmer.cmd` doppelklicken.
5. Falls AVRDUDE fehlt, **AVRDUDE installieren** wählen. Das Werkzeug bezieht die
   festgelegte offizielle Version 8.3 und prüft deren SHA-256 vor dem Entpacken.
6. Großen Taster gedrückt halten, COM-Port auswählen und **Verbindung testen**.

## 4. Gewünschte Firmware schreiben

1. **V2 – Zeitstempel / Kollisionsminderung** wählen und die vorherige Einrichtung
   von **diamex-5** bestätigen.
2. Richtige ID über **Buzzer 1 … 5 programmieren** oder **Eigene ID** auswählen.
   Jede physische Taste braucht eine andere ID von 1 bis 255. ID ist keine Bahnnummer.
3. Taster weiter gedrückt halten und Programmierung starten.
4. Flash- und Prüfergebnis abwarten. Erst nach **ERFOLGREICH** loslassen.
5. ISP-Kabel abziehen, mindestens drei Sekunden warten und Taste einzeln testen.
6. Nächste Taste erst danach anschließen.

Fuses: **HFUSE 0xFB / LFUSE 0x76**. Korrekte Werte werden nur geprüft. Kein `-F`
zum Übergehen einer falschen Signatur, RESET/SPIEN nicht abschalten und keine
zusätzlichen Lockbits setzen. Bei Fehlern anhalten, Versorgung und Verkabelung
prüfen und das Protokoll auswerten, bevor erneut geschrieben wird.

## 5. Im Hallensystem zuordnen

Unter **Admin → Funktaster → Sender anlernen** drücken, Code prüfen, Namen und
Bahn beziehungsweise Trainerfunktion wählen und speichern. IDs 1–5 behalten
bestehende Zuordnungen. Kein automatisches Anlernen durch das Programmierwerkzeug.

Jeden Sender aus den üblichen Positionen mit geschlossenem Gehäuse prüfen.
Kurze Drücke, Halten, erneutes Drücken und mehrere Sender gemeinsam testen.
Je Betätigung darf genau eine passende Aktion entstehen. Die vollständige
Funk- und Zeitmessabnahme am Hallenstandort steht noch aus.

## 6. Fehler und Rückfall

- Kein COM-Port: USB-Verbindung und Windows-Geräteerkennung prüfen.
- Keine Signatur: Taster gedrückt halten, 3,3 V und ISP-Pin 1 kontrollieren.
- Schreib-/Prüffehler: nicht übergehen; Versorgung, Kabel und Protokoll prüfen.
- Programmierung erfolgreich, aber kein Empfang: Empfängerstand, ID, Batterie
  und Funkdiagnose prüfen. Erfolg beim Flashen ist keine Funkabnahme.

Für IDs 1–5 kann bewusst **V1** gewählt werden. Die fünf bisherigen HEX-Dateien
liegen unter `firmware/`, V2 unter `firmware/v2/`. Der aktuelle Pi-Empfänger
unterstützt beide. IDs ab 6 haben keinen V1-Rückfall im Paket. Vor Rücksetzen
auf einen alten Pi-Empfänger müssen sämtliche V2-Sender passend umgestellt werden.
