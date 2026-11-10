# Trainingssignale einstellen

Öffnen Sie als Admin **Trainingssignale → Klangbibliothek & Bahntöne öffnen**.

## Töne je Bahn wählen

Für jede eingerichtete Bahn gibt es drei Felder: **Start**, **Countdown** und
**Abschluss**. Wählen Sie einen Klang, den bisherigen Piepton oder **Kein Ton**.
Drücken Sie anschließend **Bahnzuordnung speichern**. Die Auswahl gilt für alle
Trainings. Beim Entfernen einer Bahn behalten die übrigen Bahnen ihre Tonslots.

Der Startton gehört zum Beginn eines Schwimmabschnitts. Beim ersten Start
bleibt die Trainingszeit während des Vorlaufs stehen. Der vollständige Klang
endet am geplanten Zeitstart. Hinzu kommen 500 ms Übertragungsreserve.
**Alle starten** nutzt für neu startende Bahnen denselben Zeitstart, auch bei
unterschiedlich langen Klängen. Stumm, Lautstärke null und **Kein Ton** verursachen
keinen eigenen Vorlauf. Fortsetzen nach manuellem Pausieren erzeugt keinen neuen
Startton.

Automatische Startklänge werden vor dem feststehenden Abgang eingeplant. Sie
enden am Abgang; die Abgangszeit wird nicht verschoben. Der Countdown liegt
davor und überlappt den Startklang nicht. Eigene Dateien und der dreifache
Standard-Countdown werden nur vollständig eingeplant. Fehlt ausreichend Zeit
oder ist eine Datei noch nicht decodiert, entfällt das betreffende Signal.
Es wird weder verspätet noch verkürzt oder durch einen Ersatzton abgespielt.
Eine Pause ohne anschließenden Start, insbesondere die letzte Pause, erhält
keinen Abgangston. Pausieren, Ausblenden, Zurücksetzen und Beenden brechen noch
vorgemerkte Signale ab.

Die hörbare Abstimmung mit der sichtbaren Uhr muss nach Installation am
Hallenfernseher bestätigt werden. Die Softwareplanung ersetzt diesen Hörtest
mit der tatsächlichen HDMI- und Fernsehverzögerung nicht.

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

Neue Standardinstallationen erhalten die freigegebenen 14 Trainingssounds mit
Originalen, Wiedergabedateien und Bahnzuordnungen. Vorhandene Bibliotheken werden
nicht überschrieben. Weitere eigene Klänge bleiben privat, solange sie nicht
ausdrücklich als neue Standardausstattung freigegeben werden. Siehe
[Standardausstattung](STANDARD-AUSSTATTUNG.md).

## Lautstärke, Internet und Sicherungen

Der vorhandene Regler **Trainingssignale** steuert die Signallautstärke unabhängig
von Spotify oder Webradio. Musik wird durch Signale nicht unterbrochen oder
abgesenkt. Bei gleichzeitig gleichen Signalen mehrerer Bahnen erklingt der Klang
nur einmal, unterschiedliche Klänge werden gleichzeitig gemischt.

Änderungen und Hallentests benötigen online einen verbundenen Pi. Bestätigte
Downloads bleiben auch bei getrenntem Pi verfügbar. Neue Dateien benötigen kurz
Zeit für die Übertragung zur Online-App; eine noch nicht übertragene Datei wird
dort entsprechend als nicht verfügbar gemeldet. Die lokale Hallenanzeige ist
von dieser Übertragung unabhängig. Fehlende Wiedergabedateien blockieren weder Training noch Taster. Für geplante
Start- und Countdown-Signale entfällt der Klang, statt verspätet zu erklingen.

Aktuelle JSON-Sicherungen enthalten alle Originale, Wiedergabedateien und
Zuordnungen. Ältere Sicherungen bleiben importierbar und ändern die Klangbibliothek
nicht. Lokale Sicherungen enthalten zusätzlich ein Archiv des Klangordners.
