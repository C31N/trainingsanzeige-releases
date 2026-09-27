# Trainingssignale einstellen

Öffnen Sie als Admin **Trainingssignale → Klangbibliothek & Bahntöne öffnen**.

## Töne je Bahn wählen

Für jede eingerichtete Bahn gibt es drei Felder: **Start**, **Countdown** und
**Abschluss**. Wählen Sie einen Klang, den bisherigen Piepton oder **Kein Ton**.
Drücken Sie anschließend **Bahnzuordnung speichern**. Die Auswahl gilt für alle
Trainings. Beim Entfernen einer Bahn behalten die übrigen Bahnen ihre Tonslots.

Der Startton gehört zum Beginn eines Schwimmabschnitts, nicht zum Hochfahren
des Geräts. Beim Fortsetzen einer angehaltenen Bahn gibt es keinen neuen Startton.
Eine eigene Countdown-Datei wird vollständig abgespielt und endet bei null.
Ein sechs Sekunden langer Klang beginnt also sechs Sekunden vor dem Nullpunkt
der jeweiligen rückwärts laufenden Bahnuhr. Ist die verbleibende Zeit kürzer als
die Datei oder die Datei noch nicht geladen, entfällt dieser Countdown; die
Trainingszeit wird niemals verlängert. Eine Pause ohne feste Dauer hat keinen
Countdown. Die bisherigen Pieptöne bleiben in den letzten drei Sekunden.
Der Abschlusston ertönt beim vollständigen Abschluss der jeweiligen Bahn.

## Weitere Klänge

Geben Sie im Bereich **Klangbibliothek** einen Namen ein, wählen Sie eine Datei
und drücken Sie **Hochladen**. Erlaubt sind MP3, WAV und OGG mit höchstens 5 MB
und 15 Sekunden je Datei. Die gesamte Bibliothek einschließlich aufbereiteter
Dateien darf 100 MB umfassen (höchstens 100 Klänge).

- **Hier anhören** spielt eine Vorschau auf Ihrem Handy oder Computer.
- **Hallenanzeige testen** sendet den Klang an die geöffnete Hallenanzeige.
- **Original herunterladen** sichert die unveränderte hochgeladene Datei.
- **Name speichern** benennt einen Klang um.
- **Löschen** fragt zuerst nach. Noch zugewiesene Klänge sind geschützt.

Die fünf für Wasserfreunde Dalum gelieferten MP3-Dateien werden nur in dieser
Installation hinterlegt, nicht als Dateien in das öffentliche Release gepackt.
Neue Installationen beginnen mit den bisherigen Pieptönen und einer leeren Bibliothek.

## Lautstärke, Internet und Sicherungen

Der vorhandene Regler **Trainingssignale** steuert die Signallautstärke unabhängig
von Spotify oder Webradio. Musik wird durch Signale nicht unterbrochen oder
abgesenkt. Bei gleichzeitig gleichen Signalen mehrerer Bahnen erklingt der Klang
nur einmal, unterschiedliche Klänge werden gleichzeitig gemischt.

Änderungen und Hallentests benötigen online einen verbundenen Pi. Bestätigte
Downloads bleiben auch bei getrenntem Pi verfügbar. Neue Dateien benötigen kurz
Zeit für die Übertragung zur Online-App; eine noch nicht übertragene Datei wird
dort entsprechend als nicht verfügbar gemeldet. Die lokale Hallenanzeige ist
von dieser Übertragung unabhängig. Fehlende Wiedergabedateien führen zum kurzen
Standardton und blockieren weder Training noch Taster.

JSON-Sicherungen ab Format 10 enthalten alle Originale, Wiedergabedateien und
Zuordnungen. Ältere Sicherungen bleiben importierbar und ändern die Klangbibliothek
nicht. Lokale Sicherungen enthalten zusätzlich ein Archiv des Klangordners.
