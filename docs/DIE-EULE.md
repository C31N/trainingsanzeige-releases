# Die Eule & das Schwimmen

Ab Anwendung **2.20.36** und Lernbibliothek **swim-eule-20261112-1** steht unter
**Lernen → Die Eule & das Schwimmen** ein eigener, zunächst geschlossener Bereich
bereit. Der bestehende Lernzugang gilt weiter. Alle Inhalte funktionieren nach
vollständigem Laden lokal ohne Internet.

## Einstieg wählen

- **So funktioniert die Eule:** Einführung, Auswahl des Einstiegs und die fünf Phasen.
- **Schritt für Schritt lernen:** Rot → Gelb → Grün → Türkis → Blau. Jede Phase
  nennt ihr Ziel, Voraussetzungen, passende Aufgaben und den nächsten Übergang.
- **Lernstand anschauen:** Basis-Check mit fünf Aufgaben, Schwimm-Check Blaue Bahn
  und zwölf Aufgaben für den Detailblick.
- **Material für die Unterrichtenden:** alle Original-PDFs zum Öffnen, Speichern
  und Drucken, einschließlich der vollständigen Praxisunterlagen.

Die Lehrperson entscheidet anhand der tatsächlichen Ausführung über den Einstieg
und den nächsten Schritt. Das System legt keine Kinderakten an und speichert
keine persönlichen Bewertungen. Ein angesehenes Video ist keine bestandene
Prüfung. Die Phasen werden nicht mit Schwimmabzeichen gleichgesetzt.

## Eine Aufgabe verwenden

1. Phase oder Check aufklappen und die Aufgabe öffnen.
2. **Auftrag für das Kind** lesen. Unter **Durchführung und Beobachtung** stehen
   die vollständigen Originalbeschreibungen und Kriterien für die Lehrperson.
3. **Video zeigen**, **Aufgabe erklären** oder **Originalbild zeigen** wählen.
   Am Fernseher erscheinen das Video mit kurzen Merkpunkten, lesbare Textkarten
   beziehungsweise die Originalillustration. Vorhandene deutsche Untertitel
   sind enthalten. Ausführliche Beobachtungshinweise bleiben am Handy.
4. Mit **Zurück / Weiter** ausdrücklich umschalten. Lange Kinderaufträge haben
   mehrere Karten. Eulen-Videos wiederholen sich zunächst nicht und wechseln
   am Filmende auch nicht selbstständig zur nächsten Aufgabe. Wiedergabe,
   Lautstärke, Zeitlupe und eine bewusst eingeschaltete Schleife bleiben bedienbar.
5. Mit **Lernmodus beenden** zurückkehren. Bei überlagertem Training heißt die
   Rückkehr **Zurück zum Training**. Die Fernsehtaste beendet den angezeigten
   Inhalt entsprechend dem normalen Ablauf.

Unter **Originalbilder und Druckvorlagen** lassen sich weitere Bilder auswählen
und die zugehörigen PDFs am Handy öffnen. Die Blaue Bahn bietet dort ihre
Gesamtübersicht und die neun Schritte in Originalreihenfolge. Die Original-PDFs
bleiben vollständig erhalten; ihre Bildschirmfassungen sind eigene Bilddateien.

Geöffnete Bereiche bleiben bei Statusaktualisierungen offen. Die Handyansicht ist
einspaltig und scrollbar. Derselbe Lernbefehl wird lokal und online verwendet.

## Vorbereitete Lernfolgen

Jede der fünf Phasen hat **Lernfolge starten**. Zusätzlich gibt es **Basis-Check
erklären** und **Blaue Bahn erklären**. Die sieben vorgegebenen Folgen gehören
zum signierten Katalog und werden getrennt von eigenen Lernfolgen verwaltet.
Vorhandene eigene Folgen bleiben unverändert.

Die Phasenfolgen zeigen nacheinander Kinderauftrag und Originalvideo jeder
Aufgabe. Der Basis-Check enthält Taucher, Astronaut, Seestern, Flugzeug und
Seehund. Wenn eine Voraussetzung noch nicht gelingt, beendet die Lehrperson
den Check und wählt passende Übungen; es gibt keine automatische Bewertung.
Die Folge zur Blauen Bahn enthält Erklärung, Video, Gesamtbild und neun Schritte.
In Blau führen zusätzliche Schaltflächen zu den vorhandenen Schwimmtechnik-Themen.

Trainer-Funktaster verwenden ihre bestehenden Lernfunktionen für Weiter, Zurück,
Wiedergabe/Pause und Stummschaltung. Bahn-Buzzer bewerten keine Eulen-Aufgabe.
Ein überlagertes Training behält seine normale Bahnsteuerung. Die vorhandenen
Sperren für Spiele und Funksendungen sowie die Wechselbestätigung bei IPTV und
Spiegelung gelten weiter.

## Update auf einer bestehenden Anlage

Anwendungsupdate und große Mediendateien sind getrennte Pakete. Die
Veröffentlichung installiert nichts auf dem Hallen-Pi.

1. Im Ruhezustand eine private Sicherung erstellen. Anschließend über
   **Administration → Sicherung & Updates → Trainingssystem** mindestens 2.20.36
   installieren. Der bestehende Updateweg aktualisiert Pi und gekoppelte Online-App.
2. Die Technik lädt das neue Medienpaket aus demselben
   [GitHub-Release](https://github.com/C31N/trainingsanzeige-releases/releases/tag/trainingsanzeige-v2.20.36)
   und stellt die geprüfte Bibliothek auf dem eingerichteten Webhosting bereit
   (siehe unten). Der Katalog auf dem Webhosting und auf dem Pi muss dieselbe
   Version haben. Ein reines Anwendungsupdate ergänzt die großen Medien nicht.
3. Unter **Administration → Schwimmen lernen** die Lernbibliothek laden. Strom
   und Netzwerk verbunden lassen. Ein unterbrochener Download kann erneut
   gestartet werden; vorhandene Dateien werden geprüft und wiederverwendet.
   Training oder Präsentation pausieren den Download.
4. Erst **swim-eule-20261112-1**, **409 verfügbare Inhalte** und vollständige
   Offline-Verfügbarkeit bestätigen den neuen Bestand. Er umfasst **251 Dateien**.
   Fehlende Videos, Bilder, PDFs oder Untertitel verhindern diese Kennzeichnung.
5. Lokal und online eine Aufgabe öffnen, eine Folge starten und beenden. Danach
   Bild, Ton, Untertitel, erste/schnelle Trainer-Tastendrücke und Offlinebetrieb
   am Hallengerät prüfen. Diese tatsächlichen Standortprüfungen bleiben offen.

## Medien auf dem Webhosting bereitstellen – Technik

Benötigt werden `trainingsanzeige-media-swim-eule-20261112-1.zip`, das
Installationspaket 2.20.36 mit `tools/media-package.py`, der unabhängig bestätigte
öffentliche Prüfschlüssel sowie `installation.json` und `installation.sig`.
Die Installationssignatur schützt auch die Prüfsumme des Medien-ZIPs. Die
Prüfschritte stehen in der [Neuinstallation](NEUINSTALLATION-LG-UND-CLOUD.md).

Auf einem Verwaltungsrechner mit Python und OpenSSL in ein **neues** Verzeichnis
entpacken und alle Dateiprüfsummen und die Katalogsignatur prüfen:

```bash
python kit/tools/media-package.py --key kit/release-signing.pub install --archive trainingsanzeige-media-swim-eule-20261112-1.zip --destination /NEUES/VERZEICHNIS/learning-library
```

Unter Windows einen passenden absoluten Zielpfad und gegebenenfalls
`--openssl "C:/Program Files/Git/usr/bin/openssl.exe"` vor `install` angeben.
Die Platzreserve beträgt auch beim Entpacken mindestens 6 GiB.

Auf dem Webhosting zuerst die bisherigen Dateien von
`/trainingsanzeige/learning-library` sichern. Neue Dateien aus `assets/` unter
demselben Namen hochladen, die bisherigen Dateien stehen lassen. Danach
`catalog.json` und `catalog.sig` unter temporären Namen hochladen und beide
im Wartungsfenster auf ihre endgültigen Namen umbenennen. Während dieses kurzen
Wechsels keinen Mediendownload starten. Bei einem abgebrochenen Katalogwechsel
beide bisherigen Katalogdateien gemeinsam wiederherstellen und erneut versuchen.
Dateien und Signatur nicht bearbeiten. Danach den Katalog vom eingerichteten
HTTPS-Webhosting mit dem Medienwerkzeug erneut vollständig prüfen oder im
Adminbereich laden und dessen vollständige Prüfung abwarten.

`config.php`, Kopplung, Datenbank und Benutzerdateien werden dabei nicht ersetzt.
Für eine neue Anlage und den direkten Offline-Import auf einen Pi gelten die
[Installationsschritte](NEUINSTALLATION-LG-UND-CLOUD.md). Ein vorhandenes Pi-
Medienverzeichnis nicht über eine Neuinstallation überschreiben.

## Quellen, Umfang und Freigabe

Stand des Quellenabgleichs: **12.11.2026**. Grundlage sind
[Mediathek](https://www.dieeuleunddasschwimmen.de/mediathek/),
[Unterrichtsmodell](https://www.dieeuleunddasschwimmen.de/unterrichten/),
[Lernstand](https://www.dieeuleunddasschwimmen.de/lernstand/) und die dort
verlinkten 18 Aufgabenseiten. Urheberzuordnung: **Die Eule & das Schwimmen,
Deutsche Sporthochschule Köln**, mit den weiteren Hinweisen in den Originalen.

Die 30 vorgefundenen PDF-Verweise enthalten 28 tatsächliche Dateien und zwei
fehlerhafte Dateinamen-Links bei Taucher und Schatzsucher. Beide Illustrationen
sind daneben korrekt verlinkt und enthalten. Es fehlen deshalb keine dieser
Vorlagen. Enthalten sind 18 Originalvideos, 18 deutsche Untertiteldateien,
28 Original-PDFs und 27 Bildschirmillustrationen. Gleiche Dateien werden anhand
ihrer SHA-256-Prüfsumme nur einmal gespeichert. Alle bisherigen 318 Inhalte und
160 Dateien bleiben unverändert; 91 Inhalte und 91 Dateien kommen hinzu.

Der Auftraggeber hat die Freigabe für Übernahme, Bearbeitung, Offline-Nutzung und
öffentliche Weitergabe im Projektgespräch bestätigt. Das ist eine dokumentierte
projektbezogene Bestätigung, keine behauptete allgemeine Lizenz der Website.
Quellen und Originalhinweise bleiben zugeordnet. Das signierte Medienverzeichnis
enthält Quelleninventar, Abrufstand, Herkunft, Prüfsummen und Freigabehinweis.

Alle Videos wurden vollständig mit Tonspur dekodiert und in ihrer höchsten
veröffentlichten Auflösung übernommen. Das ersetzt keine Hörprüfung im Hallenbad.
Wassertiefen, Können und örtliche Sicherheitsregeln sind bei jeder Übung zu beachten.
