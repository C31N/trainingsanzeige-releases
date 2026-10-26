# Funkempfänger und Abnahme

Der aktuelle Empfängerstand heißt **diamex-5**. Er unterstützt DIAMEX V1,
DIAMEX V2 und vorhandene EV1527-Sender. V2 benötigt diesen Empfängerstand;
vor einer Senderprogrammierung unter **Admin → Funktaster** prüfen.

## Bestehende Sender übernehmen

Codes und gespeicherte Zuordnungen bleiben bei Updates erhalten. DIAMEX-IDs 1–5
behalten ihre Kennungen auch beim Wechsel von V1 zu V2. Weitere V2-IDs werden
als eigene Sender angelernt. Für jeden physischen Sender eine andere ID verwenden.

| ID | Zuordnungscode |
| --- | --- |
| 1 | D36C019C |
| 2 | D36C0295 |
| 3 | D36C0392 |
| 4 | D36C0487 |
| 5 | D36C0580 |

## Prüfstand und Grenzen

CRC, Wiederholungsfilter, Ereignisnummern, Zeitübernahme und Übergabe zur
Anwendung sind softwareseitig geprüft. Doppelte GPIO-Meldungen werden vor der
Dekodierung gefiltert. Diagnoseabfragen dürfen die Übergabe nicht blockieren.
Die Decodergrenzen werden dafür nicht aufgeweicht.

Frühere Einzelversuche bestätigten einzelne empfangene Sender; sie ersetzen
keine vollständige Freigabe am Montageort. Insbesondere kurze Drücke aller
verwendeten V2-Sender, Überschneidungen und die bestehende EV1527-Fernbedienung
sind noch gemeinsam am Standort zu prüfen. Auffällige Versorgung oder Kontakte
müssen hardwareseitig geklärt werden.

STX882 sendet ohne Empfangsbestätigung. Sehr kurze Betätigungen können spätere
Wiederholungen abschneiden; gleichzeitig sendende Geräte können kollidieren.
Zeitkorrektur bezieht sich auf den Firmwarestart. Sie ist keine zugesicherte
Genauigkeit am mechanischen Taster und keine Wettkampfzulassung.

## Zuordnung und Standorttest

1. Stromversorgung und Aufbau nach [V5-Plan](Lochrasterplan_Funktaster_V5_Rueckseitenverdrahtung.pdf) prüfen.
2. Unter **Admin → Funktaster → Sender anlernen** einmal drücken.
3. Erkannten Code, Namen und gewünschte Bahn oder Trainerfunktion kontrollieren und speichern.
4. Jede Taste mit geschlossenem Gehäuse und geladener Batterie aus den üblichen Positionen testen.
5. Kurze Drücke, Halten, Loslassen und erneutes Drücken sowie zwei und mehrere Sender prüfen.
6. Pro Betätigung genau eine Aktion erwarten. Fehlende oder verzögerte Aktionen
   mit Zeitpunkt und Funkdiagnose dokumentieren; nicht als bestanden markieren.

Die gemeinsame [Hallenabnahme](../../docs/ABNAHME.md) ist die maßgebliche Checkliste.
Technische Einzelheiten: [V2-Anleitung](diamex/README_V2.md).

## Softwareprüfung ohne Funkbetrieb

```powershell
python hardware/funktaster/verify_package.py
python hardware/funktaster/check_receiver_compatibility.py
python -m pytest tests/test_radio_diamex.py tests/test_radio.py tests/test_radio_delivery.py -q
```
