# Infotafel – Informationen & Werbung

Der Start-PIN **654323** öffnet am normalen Anmeldeschirm
einen getrennten Infotafel-Zugang. Er gewährt keine Trainer- oder Adminrechte.
Administratoren ändern ihn unter **Zugang & PINs → Infotafel-PIN**. Bereits
geänderte PINs bleiben bei Updates erhalten. Eine Sitzung endet nach acht Stunden.

## 1. Bilder vorbereiten

Empfohlen: **Querformat 16:9, 1920 × 1080 Pixel**, für 4K auch
**3840 × 2160 Pixel**. Höchstens **5 MB pro Datei**, insgesamt **30 Bilder**.
Erlaubt sind statische JPG-, PNG- und WebP-Dateien bis 40 Megapixel. PDFs,
SVGs, GIFs, Videos und animierte Bilder werden nicht unterstützt.

Das Bild bleibt vollständig sichtbar. Hochformat und andere Seitenverhältnisse
erhalten schwarze Ränder. Transparente Flächen werden schwarz hinterlegt.
Bezeichnung, Aktivierung, Reihenfolge und Dauer lassen sich je Bild einstellen:
voreingestellt 15 Sekunden, zulässig 5–300 Sekunden. Ein einzelnes aktives Bild
bleibt stehen; mehrere wechseln in einer Endlosschleife. Löschen muss bestätigt werden.

### Bahnhofsuhr zwischen Werbebildern

Unter **Bilder & Uhr → Bahnhofsuhr hinzufügen** wird die laufende Bahnhofsuhr
mit dem aktuellen Vereinslogo als eigener Eintrag hinzugefügt. Mit **Uhr in
Bildfolge anzeigen** lässt sie sich aktivieren oder aussetzen. **Reihenfolge**
bestimmt ihren Platz zwischen den Bildern, **Dauer (Sekunden)** die Einblendzeit
(5–300 Sekunden, Vorgabe 15 Sekunden). Änderungen mit **Bild speichern** übernehmen.
Die Uhr läuft live und beginnt beim nächsten Einblenden nicht wieder bei null.
Sie benötigt keine Bilddatei und zählt nicht zu den maximal 30 hochgeladenen Bildern.
Es gibt höchstens einen Uhreintrag; bei Bedarf lässt er sich entfernen und erneut
hinzufügen. Ohne aktive Bilder bleibt die Bahnhofsuhr weiterhin die Leerlaufanzeige.

### Sponsor links unten bei der Bahnhofsuhr

Nur Administratoren sehen neben **Bahnhofsuhr hinzufügen** die Schaltfläche
**Sponsor**. Dafür mit dem Admin-PIN anmelden und die Infotafel-Verwaltung öffnen;
der getrennte Infotafel-PIN gewährt keine Sponsor-Verwaltungsrechte.

Vorbelegt ist die vom Betreiber bereitgestellte Grafik **Mikroförderung LAGFA
Niedersachsen**. Sie erscheint vollständig und proportional links unten –
**ausschließlich bei der Bahnhofsuhr innerhalb der aktivierten Infotafel**, auch
wenn ohne aktive Bilder nur die Uhr läuft. Über Werbebildern, Training,
Lernvideos, Spielen, Musik, IPTV, Miracast und der normalen Uhr außerhalb der
Infotafel wird sie nicht eingeblendet.

Im Sponsorfenster kann der Admin eine eigene SVG-, EPS-, JPG-, PNG- oder WebP-Datei bis
5 MB hochladen, die Grafik deaktivieren/aktivieren oder nach Bestätigung
entfernen. Änderungen erscheinen ohne Seitenneuladen; online gespeicherte
Grafiken werden erst nach vollständiger Übertragung auf dem TV freigegeben.
Deaktivieren und Entfernen bleiben nach Neustart und Updates erhalten.
Die Grafik verbraucht keinen der 30 Plätze der Bildfolge und verändert deren
Dauer nicht. Sponsoränderungen aktivieren keine zuvor deaktivierte Infotafel.

Illustrator-EPS-Dateien mit binärem Vorschaukopf und
SVG-Ebenennamen werden ebenfalls akzeptiert. Die Dateiendung allein entscheidet nicht über das Format.

Das Sponsorfenster zeigt eine Uhr-Vorschau. **Größe** skaliert
proportional von 25 bis 200 Prozent der Standardgröße. **Horizontal** und
**Vertikal** bestimmen die Position im verfügbaren Bereich. Alternativ das Logo
mit Maus oder Finger in der Vorschau ziehen. Das Bild bleibt vollständig
innerhalb der kalibrierten TV-Ränder. Änderungen gelten auf dem TV nach
**Speichern**; ungespeicherte Eingaben bleiben beim Statusabgleich erhalten.
Ein Grafikwechsel behält Größe und Position bei.

SVG benötigt eine gültige `viewBox` und darf keine Skripte, externen Bilder,
Dateiverweise oder aktiven Inhalte enthalten. Es gilt dieselbe geprüfte
Element-/Attributauswahl wie beim Vereinslogo. Nicht unterstützte SVGs bitte
als PNG exportieren. EPS benötigt einen EPSF-Kopf und eine gültige BoundingBox;
allgemeine PostScript-Dateien, PDFs und Animationen gehören nicht zu den
freigegebenen Formaten. Transparente Grafikflächen bleiben transparent.

SVG/EPS werden ausschließlich auf dem Pi in WebP-Anzeigedateien umgewandelt.
Die Online-App speichert Originale privat, führt sie nicht aus und stellt
sie nicht als aktive Browserinhalte dar. Bis zur vollständigen Verarbeitung
bleibt der letzte gültige TV-Stand erhalten; bei Offlinebetrieb wartet die
Übertragung. Eine noch fehlende Vorschau wird zeitlich begrenzt erneut geladen.
Neue und aktualisierte Installationen prüfen `librsvg2-bin`, `ghostscript`,
`bubblewrap` und `python3-pil`. EPS benötigt die zusätzliche Namespace-Sandbox;
ohne diese gibt es ausdrücklich keinen unsandboxierten Ersatz.

Die EPS-Umwandlung nutzt den [SAFER-Modus von Ghostscript](https://ghostscript.readthedocs.io/en/latest/Use.html)
zusätzlich zur Sandbox ohne Netzwerk und ohne Zugriff auf Anwendungsdaten.

Eigene Sponsor-Uploads werden privat übertragen und mit den Infotafelmedien
gesichert. Nur die ausdrücklich als Standard beauftragte LAGFA-Grafik ist
Bestandteil von GitHub und dem Updatepaket; sie ist keine private Werbefolie.

Sponsor-Schreibzugriffe: nur Admin, mit CSRF und erwarteter Inhaltsrevision:
`POST/PUT/DELETE /api/v1/municipal/sponsor`.

Die Originaldateien liegen privat. Der Pi richtet Fotos nach ihren EXIF-Daten
aus, entfernt Metadaten aus den Anzeigedateien und erzeugt Vorschauen. Diese
Arbeit läuft in einem begrenzten, niedrig priorisierten Prozess, nicht im
Trainings-/Tasterprozess. Voraussetzung ist System-Python mit Pillow/WebP;
die Installation beziehungsweise Updatevorbereitung prüft `python3-pil`.

## 2. Einschaltzeiten

Montag bis Sonntag können mehrere Zeitfenster hinterlegt werden. Überlappungen
werden zusammengefasst. Ein Ende vor dem Beginn bedeutet „am Folgetag“;
identische Beginn-/Endzeiten bedeuten 24 Stunden. Maßgeblich ist die Zeitzone
der Halle einschließlich Sommer-/Winterzeit. Die Dalumer Öffnungszeiten sind
als bearbeitbare Vorgabe eingetragen:

| Tag | Zeiten |
| --- | --- |
| Montag | Geschlossen |
| Dienstag | 06:15–07:30 und 15:30–21:00 |
| Mittwoch | 06:15–07:30 und 15:30–21:00 |
| Donnerstag | 15:30–21:00 |
| Freitag | Geschlossen |
| Samstag | 14:00–18:00 |
| Sonntag | 08:00–13:00 |

Die Wochenübersicht zeigt sieben Tageskarten wie die Trainingszeiten. **Zeit
hinzufügen** ergänzt ein Fenster direkt beim jeweiligen Wochentag. Jedes
Zeitfenster hat einen eigenen **Aktiv**-Schalter. Änderungen anschließend
mit **Einschaltzeiten speichern** übernehmen. Inaktive Zeiten bleiben gespeichert,
halten den Bildschirm aber nicht eingeschaltet. Alle Zeiten lassen sich ändern,
ergänzen und löschen. Bereits selbst gespeicherte Pläne bleiben bei Updates erhalten.

Während eines Zeitfensters wird das Display über den bestehenden HDMI-/CEC-Weg
eingeschaltet und bleibt an. Ein bestätigter anderer HDMI-Eingang wird nicht
übernommen. Bewusstes manuelles Standby bleibt bis zum nächsten Zeitfenster
erhalten, auch nach einem Pi-Neustart; manuelles Einschalten hebt die Pause auf.
Ein durchgehend belegter Wochenplan hat keinen nächsten Beginn: Hier ist zum
Aufheben der Pause manuelles Einschalten erforderlich.

Außerhalb dieser Zeiten gilt die normale Leerlauf-Standbyfrist. Ein Upload,
die Anmeldung oder der Bildwechsel weckt das Display nicht. Beim Ende des
letzten aktiven Zeitfensters beginnt die Standbyfrist neu. Der Countdown ist
in der Infotafel nicht sichtbar.

Im bestätigten Standby lauscht der CEC-Monitor nur auf Ereignisse; auch eine
bereits vorgemerkte regelmäßige Statusabfrage wird abgesagt. Ein ausdrücklicher
Einschaltbefehl aktiviert die Bestätigungsabfragen wieder. Zeigt ein Display
beim Einschalten mit seiner Fernbedienung keinerlei CEC-Ereignis, kann der
App-Status bis zur nächsten ausdrücklichen Steueraktion beim letzten
bestätigten Stand verbleiben.

## 3. Vorschau, Aktivierung und Vorrang

Ein erfolgreicher Upload oder das Speichern von Bildern beziehungsweise
Einschaltzeiten gibt die Infotafel direkt frei. Es gibt keinen zusätzlichen
Einrichtungsschritt und keine dauerhafte Aktivierungsbox. Im Adminmenü unter
**Infotafel** lässt sich die Anzeige bei Bedarf pausieren oder wieder freigeben.
Ein Update allein aktiviert sie nicht automatisch. Im Leerlauf erscheinen anschließend
die aktiven Bilder, ohne aktive Bilder die gewohnte Bahnhofsuhr mit Vereinslogo – ohne
Bereit-Pille, Verbindungsstatus oder Standby-Text.

Geladene Trainings, Spiele, Musikmodus, IPTV, Spiegelung, Wartung und
Kalibrierung haben Vorrang. Danach beginnt die Bildfolge wieder mit dem ersten
aktiven Bild. Die Vorschau zeigt den vom Pi bestätigten Stand; bei offline
gespeicherten Änderungen kann sie deshalb noch den bisherigen Inhalt zeigen.

## Online speichern und Konflikte

Bilder und Einschaltzeiten können auch bei nicht erreichbarem Pi online
gespeichert werden. **Online gespeichert – noch nicht auf dem Display**
unterscheidet sich ausdrücklich von **Übernommen**. Zeiten werden unabhängig
von großen Bilddateien abgeglichen. Der letzte gültige Bildbestand bleibt
aktiv, bis alle benötigten Bilder vollständig übertragen, geprüft und verarbeitet sind.

Gleichzeitige lokale und Onlineänderungen erzeugen einen sichtbaren Konflikt.
Beide Stände lassen sich vergleichen und ausdrücklich auswählen. Kein Stand
wird still überschrieben. Bei Speicherfehlern bleiben die Eingaben erhalten.

## Daten, Sicherungen und Schnittstellen

Auf dem Pi: SQLite-Tabellen `municipal_documents` und `municipal_sessions`,
private Medien unter `/var/lib/trainingsanzeige/municipal`. Online liegen
Dokumente, getrennte Sitzungen und nicht ausführbare Bild-BLOBs in eigenen
`ta_municipal_*`-Tabellen. Die ergänzenden Migrationen sind wiederholbar;
die Online-Healthprüfung bestätigt die benötigten Tabellen vor Updatefreigabe.

Die normalen Datenbanksicherungen und der JSON-Export (Format 11) enthalten
die Inhalte der Infotafel. Tägliche Pi-Sicherungen enthalten zusätzlich das
Medienverzeichnis. Nicht mehr referenzierte Bilder werden erst nach bestätigtem
Abgleich und einer Schonfrist bereinigt. **Bilder der Infotafel und Originaldateien
gehören niemals in Git, Standardmedien oder Anwendungspakete.** Ausnahme ist
die oben ausdrücklich als auszuliefernder Standard beauftragte Sponsor-Grafik.

Editor-API, jeweils Infotafel-/Adminberechtigung, schreibend mit CSRF-Token:

- `GET /api/v1/municipal/status`, `GET /api/v1/municipal/session`
- `GET/PUT /api/v1/municipal/settings`
- `GET/POST /api/v1/municipal/slides`
- `PUT/DELETE /api/v1/municipal/slides/{id}` (mit erwarteter Inhaltsrevision)
- `GET /api/v1/municipal/slides/{id}/preview`
- `GET/PUT /api/v1/municipal/schedule`
- `POST /api/v1/municipal/resolve`, `POST /api/v1/municipal/logout`
- nur Admin: `POST /api/v1/auth/change-municipal-pin`

Nur freigegebene, normalisierte Anzeigebilder sind über
`GET /api/v1/municipal/display/{sha256}` öffentlich abrufbar. Der getrennte
HMAC-geschützte Geräteabgleich `/device/v1/municipal` überträgt höchstens eine
Bilddatei je Durchlauf; Änderungen an Einschaltzeiten haben Vorrang.
