# WFD Games mit vier Funktastern

Unter **Aktiv** öffnet die zusätzliche Pille **Spiele** die Spielauswahl für Trainer und Administratoren. Ein geladenes Training muss vor dem Laden eines Spiels beendet werden. Die Spiele benötigen keinen weiteren PIN.

### Hallenbad Dalum

Laut Hallenangaben beträgt das Becken 16,66 × 8 Meter. Der Hubboden ermöglicht eine variable Wassertiefe von 0,90 bis 2,00 Metern. Die Spiele verwenden Länge und Breite für die Streckenberechnung; sie erkennen oder steuern den Hubboden nicht. Die tatsächliche Tiefe muss vor Ort geprüft werden. Die Beckenbreite wird unter **Admin → Spiele** auf **8 m** eingestellt; die Länge bleibt in der Halleneinrichtung bearbeitbar.

## Einmal einrichten

1. Unter **Admin → Spiele** die Beckenbreite eingeben. Die Länge stammt aus der Halleneinrichtung.
2. Vier unterschiedliche aktive Funktaster den Stationen Nord, Ost, Süd und West zuweisen. Die Bezeichnungen beschreiben die Skizze; eine Ausrichtung nach dem tatsächlichen Kompass ist nicht erforderlich.
3. Die Buzzer jeweils mittig an der entsprechenden Beckenseite aufstellen. Beschriftung und Farbe müssen zum tatsächlichen Buzzer passen. Die ursprünglichen Zuordnungen zu Trainingsbahnen bleiben erhalten.
4. Maße und Positionen bestätigen und speichern. Ohne geladenes Training oder Spiel **Buzzer 30 Sekunden testen** starten und jede Taste einmal drücken. Die erkannte Station wird angezeigt.
5. Lautstärke, Sprachansagen und die vier Spielklänge einstellen. Eigene Klänge aus der vorhandenen Klangbibliothek können ausgewählt werden.

Der Aktivierungsschalter blendet die Spiele bei Trainern und Administratoren aus. Während eines geladenen Spiels erfordert das Deaktivieren die Bestätigung, dass der laufende Durchgang beendet wird.

## WFD-Run

Zwei Spieler starten an den gegenüberliegenden Stationen 1 und 3. Nach der Zielansage und dem Countdown schwimmen sie jeweils zu einer benachbarten Station und drücken ihren Zielbuzzer. Die Ziele sind stets um 180 Grad gespiegelt. Beide schwimmen pro Etappe dieselbe direkte Strecke: `sqrt((Beckenlänge / 2)² + (Beckenbreite / 2)²)`. Gegenkurse zur gegenüberliegenden Beckenseite sind ausgeschlossen.

Der schnellere Anschlag erhält einen Punkt. Innerhalb von 0,01 Sekunden erhalten beide einen Punkt. Nach beiden Anschlägen folgen die nächste Zielansage und der Countdown. Standard sind sechs Etappen; möglich sind drei bis zwölf. Bei Punktgleichheit entscheidet die summierte Schwimmzeit.

Nach 90 Sekunden ohne beide Ziele pausiert das Spiel. Für eine Wiederholung müssen beide Spieler an die Startpositionen der aktuellen Etappe zurückkehren. Falsche Buzzer verändern die Wertung nicht.

## WFD-Cup

Team 1 pendelt zwischen Station 1 und 2, Team 2 zwischen Station 3 und 4. Jeder korrekte Anschlag räumt einen virtuellen Becher ab und schaltet auf die andere eigene Station um. Beide Teams schwimmen damit dieselbe Gesamtstrecke. Das zuerst fertige Team gewinnt; nahe Zieleinläufe werden anhand der Empfangszeitstempel verglichen.

Sechs Becher sind voreingestellt; alternativ sind zehn möglich. Einzelduell und Staffel funktionieren mit denselben Regeln. Bei einer Staffel erfolgt die Übergabe am jeweils erreichten Ziel. Echte Becher oder Bälle werden nicht benötigt.

## Reaktionsduell

Zwei bis vier Spieler bleiben jeweils an ihrem eigenen Buzzer. Nach der Bereitschaftsansage folgt eine zufällige Wartezeit von 1,5 bis vier Sekunden. Erst bei **GO** drücken. Ein zu früher Druck ist für diesen Spieler in der Runde ungültig. Die schnellste gültige Reaktion gewinnt einen Punkt. Nach drei Sekunden endet eine Runde auch ohne alle Anschläge.

Standard sind zehn Runden; fünf bis zwanzig sind möglich. Bei Punktgleichheit entscheidet die mittlere gültige Reaktionszeit. Die Zeit basiert auf dem lokalen Funkempfang des vollständigen Telegramms.

## Anzeige, Musik und Ergebnisse

Die Hallenanzeige bestätigt Bild- und Klangbereitschaft, bevor sich das Spiel starten lässt. Alle Sprachclips werden lokal vorgehalten. Die Lautstärke der Spielsignale und die Musiklautstärke sind getrennt einstellbar. Bestehende Bluetooth- oder Webradio-Wiedergabe kann weiterlaufen.

Eine geschlossene Handyansicht beendet das Spiel nicht. **Spiel beenden** oder **Zur Spielauswahl** gibt die Anzeige wieder frei: Bei weiterlaufender Musik erscheint die Musikansicht, sonst die Uhr mit Standby-Countdown. Ergebnisse schließen nach zwei Minuten automatisch; eine unbediente Vorbereitung oder Pause endet nach zehn Minuten.

Ergebnisse liegen auf dem Raspberry und werden für die angemeldete Online-App gespiegelt. Bestenlisten gruppieren nach Spiel, Rundenzahl, Teilnehmerzahl und Beckenmaßen. Gespeichert werden höchstens 500 Durchgänge. Admins können einzelne Ergebnisse oder alle Bestenlisten löschen. Anwendungssicherungen enthalten Spieleinstellungen und Ergebnisse, jedoch kein automatisch fortzusetzendes Spiel.

Nach einem Neustart wird ein unterbrochenes Spiel nicht fortgesetzt. Anwendungs- und Systemupdates sind während eines geladenen Spiels gesperrt.
