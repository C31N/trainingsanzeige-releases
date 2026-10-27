# Administration und Betrieb

Mit der eingerichteten Admin-PIN anmelden und unten **Admin** öffnen. Der
öffentliche Erstwert ist **136542**. Die Administration umfasst auch die
Trainingsbedienung. Medienzugänge sind eigene, begrenzte Berechtigungen.

## Einrichtung und PINs

- Unter **Verein & Erscheinungsbild** Vereinsdaten und Grafiken pflegen.
- Unter **Halle** Beckenlänge, Bahnen, Tasterposition und Zeitzone kontrollieren.
- Unter **Trainingszeiten** Gruppen und Termine verwalten.
- Unter **Zugang & PINs** die sieben getrennten Zugänge einrichten oder ändern.
  Die vollständige Tabelle mit Erklärungen steht unter [Start-PINs](STANDARD-AUSSTATTUNG.md).

Bereits geänderte PINs werden durch Updates nicht ersetzt. Keine Zugangsliste
öffentlich ablegen. Ein PIN-Wechsel ist keine Neuinstallation und erfordert
keine neue Cloudidentität.

## Netzwerk und Online-Verbindung

Unter **System & Kiosk** stehen Hostname und aktuelle lokale Adressen. Diese
Adressen für die Übergabe verwenden. Unter **Netzwerk & Systemdienste** mit
**WLANs suchen** das Hallennetz auswählen, Kennwort eingeben und verbinden.
Ein WLAN-Wechsel kann die Online-Verbindung kurz unterbrechen.

Ohne bekanntes WLAN stellt der Pi seinen geschützten Notfall-Hotspot bereit.
Nach Verbindung ist `http://10.42.0.1:8080/control` erreichbar. Das individuelle
Kennwort vertraulich aufbewahren; es ist keine der öffentlichen PINs.

Online bedeutet **Verbunden**, dass der Pi aktuell erreichbar ist. Vorbereitete
Änderungen werden gespeichert und abgeglichen. **Wird zum Gerät übertragen**
verschwindet nach der Bestätigung des Pi. Bei Konflikten bewusst den gewünschten
Stand auswählen. Direkte Geräteaktionen werden bei **Getrennt** nicht vorgemerkt.

Die vorhandene Cloud-Verbindung beibehalten. Eine zweite Anlage darf nicht
parallel dieselbe Geräteidentität nutzen. Es sind keine Internet-Portfreigaben
zum Pi erforderlich. Details: [Cloudbetrieb](../cloud/README.md).

## Display, Wartungsdesktop und Ton

Unter **System & Kiosk → Bildausgabe** erkanntes Display, Auflösung und Anschluss
prüfen. **Bild kalibrieren** verwenden, alle vier Ecken prüfen und Testbild
anschließend schließen. Displayprofile werden je erkanntem Bildschirm gespeichert.

**Wartungsdesktop öffnen** beendet den Kiosk vorübergehend. Über das Desktopsymbol
**Trainingsanzeige starten** zurückkehren; nach 60 Minuten kehrt der Kiosk
automatisch zurück. **Kiosk neu starten** lädt nur die Anzeige neu.
Im Uhrmodus öffnet längeres Drücken auf die Uhr die PIN-geschützte Notfallbedienung.
Nach bestätigter Admin-PIN zeigt **Notfall-WLAN** den gespeicherten Hotspot-Namen,
die Notfall-Adresse und das individuelle Hotspot-Kennwort. Diese Angaben werden
erst nach der PIN-Prüfung geladen. Bei deaktiviertem Hotspot erscheint ein Hinweis;
ein noch nicht verfügbares Kennwort wird ausdrücklich als solches angezeigt.
Mit dem Handy zuerst diesem WLAN beitreten und dann die angezeigte Adresse öffnen.
Mit **Hotspot jetzt aktivieren** lässt sich der Hotspot sofort einschalten.
Die Bestätigung weist darauf hin, dass dabei die WLAN-Verbindung des Pi zum
Hallennetz getrennt wird. Danach mit dem Handy das angezeigte Hotspot-WLAN wählen
und die Notfall-Adresse öffnen. **Hotspot ist aktiv** bestätigt die Aktivierung.
Am Handy über **Admin → Netzwerk & Systemdienste → WLANs suchen** wieder
mit dem Hallen-WLAN verbinden. Gespeicherte WLAN-Zugänge
und das vorhandene Hotspot-Kennwort bleiben erhalten. Die direkte Aktivierung
ändert nicht die Einstellung für den automatischen Notfall-Hotspot.

Die Online-Adresse kann dieses lokale Wartungsfenster nicht freischalten.


Unter **Leerlaufanzeige & Energiesparen** Uhr und automatische Standbyfrist
festlegen. Die Standbyautomatik berücksichtigt laufende Inhalte, Einschaltzeiten
und den bestätigten HDMI-Eingang. Ein anderer oder unbekannter Eingang darf
nicht automatisch ausgeschaltet werden. Bei Unsicherheit Automatik deaktivieren
und [Eingangskontrolle](input-guard.md) prüfen.

Am Pi 5 HDMI-Ton verwenden oder eine ausdrücklich eingerichtete Alternative.
Musik, Trainingssignale, Spiele, Lernvideo und IPTV haben getrennte Pegel.
**Hallenanzeige testen** muss in der Halle hörbar sein; **Hier anhören** ist nur
eine Vorschau am Bediengerät. [Trainingssignale](TRAININGSSIGNALE.md) und
[Musik](MUSIK.md) beschreiben Auswahl und Prüfung.

## Funktaster

1. **Admin → Funktaster** öffnen und Empfängerstatus prüfen.
2. **Sender anlernen** wählen und den gewünschten Sender einmal drücken.
3. Namen und Bahn oder Trainerfunktion wählen; **Zuordnung speichern**.
4. Jede Zuordnung einzeln am tatsächlichen Standort testen.

DIAMEX-Sender mit **Sender anlernen** zuordnen. **Leere Universalfernbedienung
vorbereiten** ist für passende lernfähige Fernbedienungen bestimmt: Lernsender
bewusst starten, Taste nach Herstelleranleitung anlernen und anschließend
prüfen. Erst der erkannte Prüfdruck bestätigt die Zuordnung.

Ein Bahntaster arbeitet abhängig vom Trainingszustand. Die Trainerfunktion
**Fernseher ein / Standby** beendet zuerst Inhalte, archiviert ein Training und
führt zur Uhr; erst der nächste Druck schaltet in Standby. Offene oder
fehlgeschlagene Übergänge in der Funkdiagnose prüfen.

Für Bau, Firmware und Programmierung gilt die [Funktaster-Anleitung](../hardware/funktaster/README.md).
Ein Anwendungsupdate programmiert keine Handsender.

## Medien, Lernen und Spiele verwalten

- **Bluetooth & Webradio**: Namen, Ausgabegerät und freigegebene Streams pflegen.
- **IPTV**: Funktion, Senderliste und einzelne Sender verwalten.
- **Infotafel**: Bilder, Uhr und Einschaltzeiten pflegen; Sponsorverwaltung nur als Admin.
- **Schwimmen lernen – Swim & Improve**: Bibliothek aktivieren, laden und prüfen.
  Mindestens 6 GiB frei lassen; Downloads pausieren während Training oder Präsentation.
- **Spiele**: Beckenmaße und vier Buzzer prüfen; Highscores erst nach Kontrolle löschen.
- **Bildschirmspiegelung**: Hardware prüfen und zunächst 720p/30 Hz verwenden.

Die jeweiligen Fachanleitungen sind über die [Systemübersicht](../README.md) erreichbar.
Lernvideos werden separat geladen. Private Infotafelbilder gehören nicht ins
Anwendungsrelease. Schließen der Handy-App beendet keine TV-Wiedergabe.

## Sicherung und Wiederherstellung

1. Unter **Sicherung & Updates** einen manuellen Export erstellen und auf einem
   zweiten Gerät ablegen. Die Sicherung kann persönliche Daten enthalten.
2. Täglichen Sicherungstimer und lesbare Sicherungen unter
   `/var/lib/trainingsanzeige/backups` prüfen. Nicht nur auf demselben Datenträger sichern.
3. Vor einer Wiederherstellung den aktuellen Stand zusätzlich sichern und
   Training/Medien beenden. Importfunktion mit der vorgesehenen Sicherung verwenden.
4. Nach dem Import Profile, Pläne, Archiv, Grafiken und Medien kontrollieren.
   Ein zuvor laufendes Training darf nur pausiert zurückkommen.
5. Den Wiederherstellungsweg auf einem getrennten Testsystem prüfen.

Die laufende SQLite-Datei nicht einfach kopieren. Für Gerätetausch zusätzlich
Systemabbild, geschützte Konfiguration und eigene Cloud-Datenbanksicherung vorsehen.
Die herunterladbare Lernvideobibliothek kann anhand ihres signierten Katalogs
wiederhergestellt werden und wird nicht in jede Updatesicherung kopiert.

## Updates und Fernwartung

[Anwendungsupdates](ANWENDUNGSUPDATES.md) aktualisieren Pi und gekoppelte Online-App
zusammen. Betriebssystemupdates sind ein eigener Vorgang. Außerhalb des Betriebs
arbeiten, sichern und freie Anzeige sicherstellen. Paketentfernungen benötigen
eine bewusste Einzelfreigabe; siehe [Systemupdates](SYSTEMUPDATES-MIT-PAKETWECHSEL.md).

Unter **Fernwartung** zuerst **Gerät erreichbar** und die Dienstzustände prüfen.
Protokolle, Sicherung und fest vorgegebene Neustarts sind nach erneuter
Adminbestätigung verfügbar. Offline werden diese Aktionen nicht gespeichert.
Es gibt keine frei verwendbare Kommandozeile. Ein Neustart unterbricht die Anzeige.

Bei Fehlern Zeitpunkt und betroffene Funktion notieren, passende Protokolle
sichern und vor Weitergabe persönliche Daten sowie Zugangsdaten entfernen.
Die [Abnahmeliste](ABNAHME.md) führt alle Prüfungen am Hallengerät zusammen.


## Funktaster gezielt prüfen

Unter **Admin → Funktaster → Letzte Tastendrücke prüfen** stehen die letzten
acht Übergaben an die Steuerung, neueste zuerst. Sendername, bei V2 der
Tastenzähler, Ergebnis und Verarbeitungszeiten helfen bei der Fehlersuche.
Die Liste beginnt nach jedem Neustart des Funkdienstes neu. Sie bestätigt
keine Funkreichweite und ist kein dauerhaftes Prüfprotokoll.

**Ausgeführt** bedeutet, dass die Steuerung den Druck angenommen hat. Bei
Spielen kann ein angenommener Druck ohne Spielaktion bleiben, zum Beispiel
vor dem Start. Eine abgelehnte Quizantwort zeigt den Grund, etwa eine
Wiederholung, eine schon aufgelöste Frage oder einen Druck aus der vorherigen
Frage. Ohne Eintrag Funkempfang und lokale Übergabe prüfen. Das Anlernen
während eines Funktionstests ausschalten, da es Tastendrücke zum Zuordnen
entgegennimmt.

Für einen Quiztest Rot, Gelb und Grün einzeln bei einer offenen Frage drücken:
auf der ersten Frage, nach einem Fragenwechsel, nach einigen Sekunden und
nach Zurückblättern. Ein neuer V2-Druck kann sofort antworten; Wiederholungen
des Drucks, der weitergeblättert hat, dürfen keine Antwort auslösen. Bei
älteren Sendern ohne Tastenzähler bleibt eine kurze Schutzzeit gegen ihre
Funkwiederholungen erforderlich. Bei einem Aussetzer Uhrzeit, Farbe,
Fragenstand und Diagnoseergebnis notieren. Anschließend die übrigen
Bedienbereiche gemäß [Abnahmeliste](ABNAHME.md) am Hallengerät prüfen.
