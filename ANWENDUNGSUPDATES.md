# Trainingssoftware aktualisieren

## Für Administratoren

1. Ein geladenes Training zuerst beenden. Nicht während des Badebetriebs aktualisieren.
2. **Admin → Sicherung & Updates → Trainingssoftware** öffnen.
3. **Neue Version prüfen** drücken. Versionsnummer und Hinweise lesen.
4. **Neue Version installieren** wählen und mit der Admin-PIN bestätigen.
5. Stromversorgung und Netzwerk angeschlossen lassen. Die Verbindung wird beim
   Neustart der Anwendung kurz unterbrochen; danach erneut den Status prüfen.

Der Pi lädt ein signiertes Paket selbst über ausgehendes HTTPS (Port 443).
Ein eingehender SSH-Port ist nicht nötig. Die Onlineoberfläche kann den Auftrag
nur an einen gerade erreichbaren Pi senden. Offlineaufträge werden nicht vorgemerkt.
Debian-Systemupdates sind weiterhin ein eigener Bereich.

## Was das Update schützt

- Ed25519-Signatur des Manifests und SHA-256-Prüfsumme des Pakets.
- Feste GitHub-Downloadquellen; keine freien URLs oder Shellbefehle im Browser.
- Ein gemeinsames Schloss verhindert parallele Anwendungs- und Systemupdates.
- Keine Installation bei geladenem Training; erneute Prüfung nach dem Stoppen.
- Sicherung der Anwendung und Daten vor dem Wechsel. PINs, Kopplung und Konfiguration bleiben erhalten.
- Drei erfolgreiche Prüfungen von Anwendung und Anzeigeseite nach dem Start.
- Bei einem Startfehler: alte Anwendung und gesicherte Daten zurückholen.
- Nach Stromausfall während des Wechsels: Wiederherstellungsdienst vor dem Anwendungsstart.

Die Sicherungen liegen unter `/var/lib/trainingsanzeige-updater/backup-*`.
Fehlgeschlagene Stände werden dort zur Diagnose aufbewahrt. Keine automatische
Löschung von Sicherungen. Speicher bei regelmäßigen Updates kontrollieren.

## Einmalige Einrichtung durch die Technik

`sudo bash /opt/trainingsanzeige/ops/install-application-updater.sh`

Konfiguration: `/etc/trainingsanzeige-updater.json`, Eigentümer root, Modus 0600.
Standardkanal: `C31N/trainingsanzeige-releases` (öffentlich, kein Token nötig).
Felder: `repository` als `Besitzer/Repository`, optional `token` für private Repositories.
Für den Token ausschließlich das benötigte Repository und **Contents: Read-only**
freigeben; keinen persönlichen Vollzugriffstoken verwenden. Nicht im Browser oder
Git speichern. Ohne Zugriff auf das private Repository ist die Downloadfunktion
noch nicht betriebsbereit. Der HTTP-Proxy der Halle muss GitHub-API und
GitHub-Release-Downloads erlauben; HTTPS allein garantiert keine Firewallfreigabe.

Der öffentliche Prüfschlüssel liegt unter `/etc/trainingsanzeige-release.pub`.
Der private Signierschlüssel bleibt ausschließlich auf dem Veröffentlichungsrechner.
Verlust des privaten Schlüssels erfordert einen bewusst eingerichteten Schlüsselwechsel.

## Neue Version veröffentlichen

1. Tests ausführen; Versionsnummern aktualisieren.
2. Im Frontend `npm run build` ausführen (nicht den Cloudbuild).
3. `ops/build-application-release.py --key <privater-schlüssel> --output <release-ordner>`
   ausführen. Unter Windows bei Bedarf `--openssl <pfad-zu-openssl.exe>` ergänzen.
4. GitHub-Release mit Tag `trainingsanzeige-vX.Y.Z` erstellen; kein Vorabrelease.
5. `trainingsanzeige.json`, `trainingsanzeige.sig` und `trainingsanzeige.tar.gz` anhängen.

Das Paket enthält keine lokale Datenbank, Zugangsdaten, node_modules oder
Entwicklungsumgebung. Die Signatur muss zum separat installierten Prüfschlüssel passen.
Neue Python-Abhängigkeiten müssen bereits verfügbar sein; `pip check` bricht
andernfalls vor dem Wechsel ab. Neue Betriebssystempakete, systemd-Dienste oder
Änderungen am Updater selbst werden nicht stillschweigend installiert und benötigen
eine gesonderte Wartung. Anwendung und Sicherung müssen auf demselben Dateisystem
liegen; mindestens 2 GB freier Speicher werden vorab verlangt.

Die Online-Webinstallation selbst wird weiterhin gesondert veröffentlicht. Dieser
Updateknopf aktualisiert die Trainingssoftware auf dem ausgewählten Raspberry Pi.
