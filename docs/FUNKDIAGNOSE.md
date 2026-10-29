# Funktaster prüfen und Fernbedienungen verwalten

Ab Version **2.20.5** enthält **Administration → Funktaster** drei aufklappbare
Bereiche. Sie stehen lokal am Pi und über die gekoppelte Online-App zur Verfügung.
Für alle Bereiche ist eine Admin-Anmeldung erforderlich.

## Fernbedienungen und Buzzer

1. Unter **Fernbedienungen und Buzzer** einen Namen eingeben, zum Beispiel
   „Trainer“, und **Fernbedienung anlegen** wählen.
2. Bei jeder zugehörigen Taste diese Fernbedienung auswählen und **Speichern**
   drücken. Vier Tasten einer Trainerfernbedienung können unterschiedliche
   Funktionen haben; die Anzahl der Tasten ist nicht auf vier begrenzt.
3. Einzelne Bahnbuzzer behalten die Auswahl **Einzelner Buzzer**. Jede Taste
   hat weiterhin ihren eigenen Namen, Funkcode und ihre Bahn- oder Trainerfunktion.
4. Eine Taste lässt sich durch eine andere Auswahl verschieben. **Gruppe auflösen**
   entfernt nur die Zusammenfassung; die Tasten und ihre Funktionen bleiben bestehen.

Neue Sender weiterhin mit **Sender anlernen** erfassen. Eine Gruppierung ändert
weder die Firmware noch den Funkcode. Bestehende Zuordnungen bleiben beim Update erhalten.

Ab 2.20.13 bleibt die gespeicherte Fernbedienungszuordnung auch beim erneuten
Öffnen korrekt sichtbar, wenn die Fernbedienungsliste langsamer geladen wird als
die Tasten. Währenddessen erscheint kurz „Fernbedienung wird geladen …“.
Bereits gespeicherte Zuordnungen müssen nicht erneut angelegt werden.

## Empfang live

**Empfang live** öffnen und den gewünschten Taster einmal drücken. Die neueste
Aufzeichnung steht oben. Die Tabelle zeigt die Zeit, erkannte Taste, Fernbedienung,
Protokoll, Kennung, Signalstärke, erfasste Dauer und das Ergebnis der Verarbeitung.

- **dBm:** stärkster zeitnah erfasster Signalstärkewert innerhalb der Aufzeichnung.
  Ein weniger negativer Wert bedeutet ein stärkeres Empfangssignal. Fehlt ein
  zuordenbarer Messwert, steht dort **nicht erfasst**. Das ist keine Reichweitengarantie.
- **MHz:** eingestellte Empfangsfrequenz, normalerweise **433,92 MHz**. Das Gerät
  ermittelt damit nicht die genaue Sendefrequenz eines unbekannten Senders.
- **Dauer:** aufgezeichneter Abschnitt einschließlich erfasster Pausen. Er ist
  nicht automatisch identisch mit der Zeit, die der Knopf gedrückt gehalten wurde.
- **Code und Telegramminhalt:** erkannte Kennung beziehungsweise auslesbare
  Telegrammbytes. Ein **Fingerabdruck** ist nur ein Vergleichswert für ein unbekanntes
  Impulsmuster und kein entschlüsselter Telegramminhalt.
- **Verarbeitung:** eine erkannte Wiederholung löst nicht nochmals dieselbe Aktion
  aus. „Von der Anwendung angenommen“ bestätigt die Übergabe; die Wirkung hängt
  zusätzlich vom aktuellen Training, Spiel oder Quiz ab.

Mit **Details** den Impulsverlauf, Pegel und Impulszeiten in Mikrosekunden sowie
die Prüfsummenprüfung ansehen. Nicht jedes Funkprotokoll enthält eine Prüfsumme.
Die Filter zeigen bekannte Tasten, unbekannte Signale oder Fehler.

**Ansicht pausieren** hält ausschließlich die Darstellung an. Der Empfang und die
Bedienung laufen weiter. **Diagnose exportieren** speichert die aktuell gelisteten
Messwerte und Ergebnisse als JSON-Datei auf dem Bediengerät.

Der Verlauf ist flüchtig: höchstens 200 Aufzeichnungen mit jeweils 2.048 Impulsen.
Ältere Einträge werden ersetzt; Lücken und abgeschnittene Aufzeichnungen werden
angezeigt. Nach einem Funkdienst-Neustart beginnt ein neuer Verlauf. In der Cloud
kann die Anzeige verzögert sein. Zeitstempel und Verbindungsmeldung beachten;
alte Daten gelten nicht als aktueller Empfangsnachweis.

## Signal senden

Training, Lernen, Quiz und Spiele zuerst beenden. Ein pausiertes oder nur geladenes
Training zählt weiterhin als aktiv. Die Sperre gilt auch für den bisherigen
Lernsender zum Vorbereiten einer Universalfernbedienung.

### Ein empfangenes Signal wiederholen

1. In **Empfang live → Details** eine vollständige, sendbare Aufzeichnung benennen
   und **Aufzeichnung speichern** wählen.
2. **Signal senden** öffnen, **Gespeicherte Aufzeichnung wiederholen** wählen und
   die gewünschte Aufzeichnung auswählen.
3. Frequenz und Wiedergabeeinstellung prüfen und **Ausgewähltes Signal senden** drücken.

Die Wiederholung unterstützt geeignete OOK-Impulsfolgen im bestehenden Bereich
433,05 bis 434,79 MHz. Abgeschnittene Aufzeichnungen, beschädigte Prüfsummen,
ungültige Impulszeiten und zu große Aufzeichnungen können nicht gesendet werden.
Wechselnde und verschlüsselte Codes lassen sich durch eine Aufnahme nicht
zuverlässig nachbilden. Ein empfangenes DIAMEX2-Telegramm enthält außerdem eine
Ereigniskennung: Seine Wiederholung ist kein neu erzeugter Tastendruck.

### Einen Tastencode eingeben

**EV1527-Tastencode eingeben** wählen und sechs Hex-Zeichen zwischen **100000** und
**FFFFFF** eintragen, beispielsweise **A1B2C3**. Das Feld erzeugt ausschließlich ein
EV1527-Signal; andere Protokolle werden dadurch nicht automatisch unterstützt.

Standardmäßig wird einmal gesendet. **Zeitlich begrenzt wiederholen** erlaubt eine
Sendedauer bis zwölf Sekunden. Danach gilt eine Sendepause von zehn Sekunden.
**Senden abbrechen** beendet einen laufenden Auftrag. Während des Sendens kann der
Funkbaustein keine Buzzer empfangen. Anschließend schaltet er automatisch zurück;
die Oberfläche zeigt Empfangsbereitschaft oder eine Störung an. Nach unklarer
Verbindungsunterbrechung bleibt der Start einer Anwendung kurz gesperrt, bis der
maximale mögliche Sendezeitraum abgelaufen ist.

Cloud-Sendebefehle verfallen nach fünf Sekunden und werden nicht automatisch
wiederholt. Eine verlorene Bestätigung ist kein Anlass für eine automatische
erneute Sendung. Ein angenommener Sendeauftrag bestätigt keinen Gegenempfang:
Diesen immer am vorgesehenen Empfangsgerät prüfen.

## Sicherung und Prüfung am Standort

Fernbedienungsgruppen, Tasten und gespeicherte Aufzeichnungen sind Bestandteil der
vollständigen privaten Pi-Sicherung nach [Wiederherstellung](WIEDERHERSTELLUNG.md).
Der flüchtige Diagnoseverlauf und laufende Sendeaufträge werden nicht wieder aktiviert.
Der normale Trainings-JSON-Export ersetzt diese vollständige Gerätesicherung nicht.

Am tatsächlichen Standort jede Taste einzeln, mehrmals schnell und während einer
Quizfrage testen – insbesondere den ersten Druck des roten Buzzers. Dabei die
Diagnose öffnen und Ergebnis sowie sichtbare Reaktion vergleichen. Anschließend
den Gegenempfang eines Testsignals und die Rückkehr zum Buzzerempfang prüfen.
Diese Hardwareprüfungen erst nach Durchführung in der [Abnahmeliste](ABNAHME.md) bestätigen.

## Mobile Ansicht und Aufräumen ab 2.20.7

Empfangseinträge, Fernbedienungen und Buzzer lassen sich aufklappen. Einträge
können einzeln gelöscht oder mit „Empfangsverlauf leeren“ für alle Bediengeräte
entfernt werden. Neue Signale werden weiterhin empfangen. Gespeicherte
Aufzeichnungen werden separat gelöscht; Tasten und Trainings bleiben erhalten.

Eindeutig erkannte unbekannte Codes lassen sich ignorieren und unter
„Ignorierte Signale verwalten“ wieder zulassen. Zugeordnete Tasten sind geschützt.
Ignorierte Codes werden standardmäßig ausgeblendet, bleiben aber über den Filter
sichtbar. Die Ignorierliste gehört zur privaten Datenbanksicherung. Eine Sperre
unterdrückt Softwareaktionen; sie beseitigt keine physische Funkstörung.
