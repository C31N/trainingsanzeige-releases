# Online-App und Cloudbetrieb

Das PHP-/MariaDB-Gateway gehört zu genau einer lokalen Trainingsanzeige. Der Pi
bleibt Zeitquelle und führt Gerätebefehle aus. Die Online-App ermöglicht
Vorbereitung und Fernbedienung unter der vorhandenen HTTPS-Adresse.

## Vorhandene Anlage übernehmen

Die bestehende Datenbank, `config.php`, Installations-ID und Gerätekopplung
weiterverwenden. Kein leeres Schema darüber importieren, keine neue Identität
erzeugen und keinen zweiten Pi mit demselben Sekret starten. Vor Eingriffen die
eigene MariaDB, private Medien und die geschützte Konfiguration sichern.

Pi und Online-App werden über das [gemeinsame signierte Update](../docs/ANWENDUNGSUPDATES.md)
aktualisiert. Keine einzelne Oberfläche aus einem anderen Release hochladen.
Die stabile `update-gateway.php` und `.release-signing.pub` werden einmalig bei
der Einrichtung installiert und nicht durch normale Webupdates ersetzt.

## Zugänge und Livebedienung

Die [sieben Start-PINs mit ihren Funktionen](../docs/STANDARD-AUSSTATTUNG.md) gelten
nur für neue Standardinstallationen. Vorhandene geänderte Werte bleiben erhalten.
Die gültigen PIN-Hashes kommen vom Pi; vor der ersten Synchronisierung ist die
Onlineanmeldung noch nicht vollständig eingerichtet.

**Verbunden** zeigt einen aktuell erreichbaren Pi. Pläne, Infotafelbilder und
Einschaltzeiten können online vorbereitet und danach abgeglichen werden.
Start, Bahnsteuerung, TV-, Musik-, IPTV-, Lern- und Spielbefehle benötigen eine
Liveverbindung und werden nicht für später vorgemerkt. Bei Konflikten wird der
gewünschte Stand ausdrücklich gewählt.

Lernkarten und Videos können laufendes Training überblenden. Das Abzeichenquiz
benötigt freie Trainingsbuzzer; Antworten erfolgen über Handy oder die physischen
Buzzer. Es gibt 72 Übungsfragen in Runden mit 5/7/12/14/16/18 Fragen. Quiz und
Spiele werden lokal ausgewertet. Der Lernzugang erhält keine Trainerrechte.

## Neuinstallation ab null

Eine neue eigene Cloud benötigt HTTPS, PHP mit PDO-MySQL, Argon2id und
Signaturprüfung, eine eigene MariaDB und einen nur dafür berechtigten Benutzer.
Das aktuelle Websetup liefert Schema, Provisionierungsskripte und den fertigen
Cloudbuild. Alle Schritte einschließlich Schlüssel, Kopplung und Schutz der
Konfiguration stehen in der [vollständigen Neuinstallation](../docs/NEUINSTALLATION-LG-UND-CLOUD.md).

Nur den erzeugten Webinhalt veröffentlichen. Python, SQLite, Pi-Anwendung,
Zugangsdatenlisten und Provisionierungsskripte gehören nicht in den öffentlichen
Webspace. Der Pi verbindet sich ausgehend per HTTPS; keine Routerfreigabe zu ihm.

## Daten und Medien

Das Gateway prüft HMAC-Geräteanfragen mit Zeitfenster und Einmal-Nonce. Die
Browsersteuerung verwendet Sitzungen, CSRF und die synchronisierten PIN-Hashes.
Infotafel- und Lernsitzungen sind getrennt und zeitlich begrenzt. Die MariaDB-
Sicherung muss alle `ta_*`-Tabellen einschließlich Medien und Sitzungen umfassen.

Infotafelbilder werden privat und nicht ausführbar gespeichert. Nur der Pi gibt
geprüfte Anzeigebilder frei. Die Videobibliothek liegt getrennt unter
`learning-library/` neben dem Gateway und wird signiert verteilt. Sie gehört
weder in MariaDB noch in das kleine Anwendungsupdate oder den Handycache.
Die zugehörigen Quellen und Urheberhinweise bleiben erhalten.

Anleitungen: [Lernen](../docs/SWIM_IMPROVE.md), [Infotafel](../docs/GEMEINDEANZEIGE.md),
[IPTV](../docs/IPTV.md), [Spiele](../docs/SPIELE.md) und [Administration](../docs/ADMIN-HANDBUCH.md).
