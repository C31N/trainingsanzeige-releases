# Trainingssoftware aktualisieren

## Für Administratoren

1. Ein geladenes Training zuerst beenden. Nicht während des Badebetriebs aktualisieren.
2. Ganz unten **Admin → Sicherung & Updates → Trainingssystem** öffnen.
3. **Version prüfen** drücken. Die Versionsstände von Raspberry Pi und Online-App kontrollieren.
4. **Trainingssystem aktualisieren** wählen und mit der Admin-PIN bestätigen.
5. Stromversorgung und Netzwerk angeschlossen lassen. Die Verbindung wird beim
   Neustart der Anwendung kurz unterbrochen; danach erneut den Status prüfen.

Der Pi lädt ein signiertes Paket selbst über ausgehendes HTTPS (Port 443).
Ein eingehender SSH-Port ist nicht nötig. Die Onlineoberfläche kann den Auftrag
nur an einen gerade erreichbaren Pi senden. Offlineaufträge werden nicht vorgemerkt.
Debian-Systemupdates stehen darunter als eigener, bewusst getrennter Bereich.

Ist die Online-App gekoppelt, wird niemals nur eine Seite aktualisiert. Ist der
Webserver nicht erreichbar oder lehnt er die Prüfung ab, beginnt die Installation
auf dem Pi nicht.

## Was das Update schützt

- Der Releasebuild prüft die vorhandenen Größenlimits vor Freigabe:
  maximal 6 MiB dekodierte Webdateien, 250 Dateien, 8 MiB Web-Download und
  8 MiB Geräteanfrage einschließlich beider Base64-Schichten. Die bestehenden
  Pi- und Server-Schutzgrenzen bleiben unverändert. Die mitgelieferten
  Spielansagen werden ohne Klang- oder Zeitverlust als FLAC transportiert.

Für Änderungen an den mitgelieferten Spielansagen erzeugt
`ops/build-game-voices.ps1` die WAV-Originale und mit FFmpeg die FLAC-Dateien.
Bei Bedarf `-Ffmpeg <Pfad>` und `-Python <Pfad>` angeben. Das nachgeschaltete
`ops/compress-game-voices.py` dekodiert jede erzeugte Datei und vergleicht die
PCM-Prüfsumme mit dem Original. Die Browser-Abnahme prüft zusätzlich alle
17 Dateien aus dem signierten Paket auf identische Samples und Dauer.
- Ed25519-Signatur des gemeinsamen Manifests und eigene SHA-256-Prüfsummen für Pi- und Webpaket.
- Feste GitHub-Downloadquellen; keine freien URLs oder Shellbefehle im Browser.
- Ein gemeinsames Schloss verhindert parallele Anwendungs- und Systemupdates.
- Keine Installation bei geladenem Training; erneute Prüfung nach dem Stoppen.
- Transaktionale Sicherung von Pi-Anwendung, Daten und verwalteten Webdateien vor dem Wechsel. PINs, Kopplung, MariaDB und `config.php` bleiben erhalten.
- Drei erfolgreiche Prüfungen von Anwendung und Anzeigeseite nach dem Start.
- Bei einem Start- oder Webfehler: beide Anwendungen auf den vorherigen Stand zurückholen.
- Nach Stromausfall während des Wechsels: Wiederherstellungsdienst vor dem Anwendungsstart.

Die Sicherungen liegen unter `/var/lib/trainingsanzeige-updater/backup-*`.
Nach einem erfolgreichen Update bleiben die zwei neuesten Rückfallstände erhalten;
ein laufender oder fehlgeschlagener Updatevorgang wird nicht automatisch bereinigt.

## Einmalige Einrichtung durch die Technik

`sudo bash /opt/trainingsanzeige/ops/install-application-updater.sh`

Konfiguration: `/etc/trainingsanzeige-updater.json`, Eigentümer root, Modus 0600.
Standardkanal: `C31N/trainingsanzeige-releases` (öffentlich, kein Token nötig).
Felder: `repository` als `Besitzer/Repository`, optional `token` für private Repositories.
Für den Token ausschließlich das benötigte Repository und **Contents: Read-only**
freigeben; keinen persönlichen Vollzugriffstoken verwenden. Nicht im Browser oder
Git speichern. Der öffentliche Standardkanal benötigt keinen Token. Der HTTP-Proxy der Halle muss GitHub-API und
GitHub-Release-Downloads erlauben; HTTPS allein garantiert keine Firewallfreigabe.

Der öffentliche Prüfschlüssel liegt unter `/etc/trainingsanzeige-release.pub`.
Der private Signierschlüssel bleibt ausschließlich auf dem Veröffentlichungsrechner.
Verlust des privaten Schlüssels erfordert einen bewusst eingerichteten Schlüsselwechsel
auf Pi und Webserver, bevor ein neues Release bereitgestellt wird. Eine neue Signatur
allein lässt sich mit den alten Prüfschlüsseln nicht installieren.

## Neue Version veröffentlichen

1. Tests ausführen; Versionsnummern aktualisieren.
2. Node.js und die lokalen Frontend-Abhängigkeiten mit `npm ci` bereitstellen.
   Der Releasebuilder prüft TypeScript und baut Pi- und Online-Oberfläche frisch.
3. `ops/build-application-release.py --key <privater-schlüssel> --output <release-ordner>`
   ausführen. Unter Windows bei Bedarf `--openssl <pfad-zu-openssl.exe>` ergänzen.
4. GitHub-Release mit Tag `trainingsanzeige-vX.Y.Z` erstellen; kein Vorabrelease.
5. Aktuelle öffentliche Anleitungen und das getrennte Websetup-Paket für
   Neuinstallationen bereitstellen. Das Websetup ersetzt keine bestehende Cloud.
6. `trainingsanzeige.json`, `trainingsanzeige.sig`, `trainingsanzeige.tar.gz` und `trainingsanzeige-web.json` anhängen.

Das Paket enthält keine lokale Datenbank, Zugangsdaten, node_modules oder
Entwicklungsumgebung. Die Signatur muss zum separat installierten Prüfschlüssel passen.
Neue Python-Abhängigkeiten müssen bereits verfügbar sein; `pip check` bricht
andernfalls vor dem Wechsel ab. Neue Betriebssystempakete und zusätzliche systemd-Dienste müssen durch den
Installer beziehungsweise die Technik eingerichtet werden.
Der root-geschützte Updater übernimmt seine geprüfte neue Version nach erfolgreichem
Gesamtupdate. Anwendung und Sicherung müssen auf demselben Dateisystem
liegen; mindestens 2 GB freier Speicher werden vorab verlangt.

Die stabile, geräteauthentifizierte Web-Updatebrücke und der öffentliche
Signaturprüfschlüssel werden einmalig bei der Ersteinrichtung installiert. Danach
aktualisiert derselbe Knopf Pi und Online-App. Zugangsdaten des Hosters liegen
weder im Release noch auf dem Pi.

Für eine leere Anlage gilt die [Neuinstallation ab null](NEUINSTALLATION-LG-UND-CLOUD.md).
Für das vorhandene Hallengerät gilt die [Installationsanleitung](INSTALLATION.md).

## Anleitungen und Erstinstallationspaket veröffentlichen

Nach dem signierten Releasebuild aus demselben unveränderten Checkout:

```bash
python ops/build-websetup.py --release-dir /PFAD/ZUM/RELEASE
python ops/export-documentation.py --output /PFAD/ZUM/OEFFENTLICHEN-REPOSITORY
```

Unter Windows bei Bedarf bei `build-websetup.py` zusätzlich `--openssl` mit dem
vollständigen Programmpfad angeben. Das Werkzeug prüft Signatur, Webprüfsumme,
Versionsgleichheit und erlaubte Webdateien vor dem Erstellen des Websetups.
Es enthält die fertige Onlineoberfläche, Einrichtungshilfen und aktuelle
Anleitungen. Das zusätzliche ZIP und seine `.sha256`-Datei am selben Release
anhängen; die vier signierten Updateartefakte bleiben unverändert in Aufbau
und Sicherheitsprüfung.

Die exportierten Anleitungen separat im öffentlichen Downloadrepository
committen und veröffentlichen. Der Export kopiert nur ausdrücklich vorgesehene
Dokumentation, Bauplan und Funktaster-Download, keine lokalen Daten oder Schlüssel.
Die private Schlüsseldatei wird dabei niemals exportiert. Alte öffentliche
Anleitungsadressen verweisen auf die jeweils aktuelle Fassung.
