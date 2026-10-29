# Neuinstallation ab null: Raspberry Pi, Hallendisplay und Online-App

Softwarestand **2.20.10**, Ausgangsstand **2.20.3**. Diese Anleitung beginnt mit
einem leeren Speichermedium und einem neuen Webhosting. Benötigt werden keine
privaten Quelltexte und kein Frontend-Build. Alle Daten entstehen neu.

Eine **zweite Anlage** folgt denselben Schritten, erhält aber einen anderen
Hostnamen, eine eigene Domain oder Subdomain und eine getrennte Datenbank.
Für einen **Ersatz nach Ausfall** zuerst [Wiederherstellung](WIEDERHERSTELLUNG.md)
lesen. Für den vorbereiteten Hallen-Pi gilt [Installation vor Ort](INSTALLATION.md).
Eine bestandene Hardwareprüfung ist damit noch nicht nachgewiesen.

## 1. Geräte und Zugänge bereitlegen

- Raspberry Pi **4B oder 5**, passendes Netzteil, Kühlung und mindestens 32 GB Speicher;
- Tastatur und Maus, Micro-HDMI-Kabel, Display und dessen Fernbedienung;
- LAN oder ein WLAN ohne Anmeldeseite und ohne gegenseitige Gerätesperre;
- für die Cloud eine eigene HTTPS-Adresse und leere MariaDB auf PHP-Webhosting;
- für lokale Werkzeuge Python **3.11 oder neuer**, OpenSSL und für Sicherungen [age](https://github.com/FiloSottile/age).

Zuerst am Tisch einrichten und prüfen. Der Pi wird direkt über HDMI mit dem
Display verbunden. Anschluss notieren, beispielsweise Pi HDMI0 → LG HDMI1.
Feuchteschutz, sichere Montage, Stromversorgung und Belüftung durch die
Hallenverantwortlichen freigeben lassen.

Pi und Trainergeräte müssen sich im Hallennetz erreichen können. Die Hallen-IT
kann dem Pi eine feste DHCP-Adresse zuweisen. Keine Internet-Portfreigaben für
22 oder 8080 einrichten. Die Cloudverbindung läuft ausgehend über HTTPS/443.
Zur Erstinstallation werden DNS, richtige Uhrzeit und Internetzugriff auf Debian-,
Raspberry-Pi-, Python- und GitHub-Paketquellen benötigt.

## 2. Das Betriebssystem installieren

Feste Grundlage ist **Raspberry Pi OS Trixie, 64 Bit, mit Desktop und Labwc/Wayland**,
Image vom **6. Oktober 2026**. Kein Lite-Image verwenden.

- [Offizielle Betriebssystemauswahl](https://www.raspberrypi.com/software/operating-systems/)
- [Festgelegtes Image herunterladen](https://downloads.raspberrypi.com/raspios_arm64/images/raspios_arm64-2026-10-06/2026-10-06-raspios-trixie-arm64.img.xz)
- Dateiname: `2026-10-06-raspios-trixie-arm64.img.xz`
- SHA-256: `976766570bee2aaf3047dd78649cfe82abb8fe9687b7f15030cd533ba4e9f7a9`

Image-Prüfsumme kontrollieren. Mit Raspberry Pi Imager auf das ausgewählte leere
Speichermedium schreiben. Das Schreiben löscht dessen Inhalt.

1. Als ersten Benutzer **pi** anlegen, mit einem eigenen Kennwort. Er muss UID **1000** haben.
2. Einen eindeutigen Hostnamen festlegen, für die erste Anlage beispielsweise `trainingsanzeige`.
3. Land, Tastaturlayout, WLAN-Land und Zeitzone `Europe/Berlin` einstellen.
4. Bei Bedarf SSH für die lokale Einrichtung aktivieren. Zugang privat aufbewahren.
5. Pi starten, Netzwerk verbinden und den Desktop mit Labwc/Wayland öffnen.
6. Im Terminal `id -u pi`, `uname -m` und `timedatectl` prüfen: erwartet werden `1000`, `aarch64` und die richtige Uhrzeit.

## 3. Alle Installationsdateien herunterladen

Aus [Release 2.20.10](https://github.com/C31N/trainingsanzeige-releases/releases/tag/trainingsanzeige-v2.20.10)
die folgenden Dateien gemeinsam in einen neuen Downloadordner legen:

| Datei | Zweck |
| --- | --- |
| `trainingsanzeige-installation-2.20.10.zip` | Fertige Pi-Anwendung, Websetup, Werkzeuge und Anleitungen |
| `installation.json` | Verzeichnis und Prüfsummen von Installations- und Medienpaket |
| `installation.sig` | Digitale Unterschrift dieses Verzeichnisses |
| `release-signing.pub` | Öffentlicher Prüfschlüssel |
| `trainingsanzeige-media-swim-20261021-1.zip` | 318 Lerneinträge mit 160 Mediendateien |

„Source code“ ist kein Installationspaket. Der öffentliche Prüfschlüssel muss
unabhängig bestätigt sein. Sein Datei-SHA-256 lautet:
`360b449f66d26e9c9d933892f2583b50b3b3c7a5fd0b97b43b36ee282f74d3e8`.
Der private Signierschlüssel gehört weder in das Paket noch auf Pi oder Webhosting.

Im Downloadordner auf dem Pi:

```bash
sha256sum release-signing.pub
openssl pkeyutl -verify -pubin -inkey release-signing.pub -rawin \
  -in installation.json -sigfile installation.sig
python3 -c 'import json,hashlib,pathlib; m=json.loads(pathlib.Path("installation.json").read_bytes()); assert m["format"]=="trainingsanzeige-installation-1"; assert all(pathlib.Path(n).stat().st_size==v["bytes"] and hashlib.file_digest(pathlib.Path(n).open("rb"),"sha256").hexdigest()==v["sha256"] for n,v in m["artifacts"].items()); print("Alle Pakete geprueft")'
```

Nur nach erfolgreicher Signatur- **und** Prüfsummenkontrolle fortfahren. Diese
Signatur schützt auch sämtliche Einrichtungsskripte im ZIP. Die separate
Update-Signatur behält ihren bisherigen Umfang. Unter Windows `python` statt
`python3` verwenden; die weiteren Pi-Befehle werden am Pi ausgeführt.

## 4. Die Pi-Anwendung installieren

```bash
python3 -m zipfile -e trainingsanzeige-installation-2.20.10.zip kit
python3 -B kit/tools/installation.py --key release-signing.pub --unpack vorbereitet
sudo bash vorbereitet/pi/ops/install-pi.sh --check
sudo bash vorbereitet/pi/ops/install-pi.sh
sudo reboot
```

Die Ordner `kit` und `vorbereitet` müssen neu sein. Die Vorprüfung kontrolliert
Modell, Architektur, Trixie, Desktop, Benutzer `pi`, mindestens 8 GiB freien Speicher
und erreichbare Paketquellen. Eine bestehende Anlage wird abgewiesen.
Der Installer richtet Dienste, Verzeichnisse, Rechte, Desktop-Autostart und
Hardwareabhängigkeiten ein. Betriebssystem- und Python-Pakete werden aus dem
Internet geladen; die Bedienoberfläche ist bereits fertig gebaut.

Bei einem Abbruch Ursache beheben und **dieselben geprüften Dateien** behalten.
Mit `sudo bash vorbereitet/pi/ops/install-pi.sh --resume` fortsetzen. Keine andere
Version dazwischen installieren. Der Status steht unter
`/var/lib/trainingsanzeige-installer/`. Ein abgeschlossenes System erhält Updates.

## 5. Lokal einrichten und WLAN verbinden

1. IP mit `hostname -I` ermitteln. Am Handy im selben Netz `http://PI-IP:8080/setup` öffnen.
2. Mit Admin-Start-PIN **136542** anmelden und den Einrichtungsassistenten abschließen.
3. Verein, Logo, Halle, Zeitzone, tatsächliche Beckenlänge und Bahnen eintragen.
4. Für Dalum gelten **16,6667 m** und **drei Bodenlinien**. Andere Hallen erhalten ihre eigenen Werte.
5. Cloud zunächst ausgeschaltet lassen, bis die neue Kopplung vorbereitet ist.
6. Unter **Admin → Zugang & PINs** eigene PINs setzen und privat aufbewahren.

| Zugang | Öffentliche Start-PIN |
| --- | --- |
| Administration | 136542 |
| Training | 123456 |
| Musik | 654321 |
| IPTV | 654322 |
| Infotafel | 654323 |
| Lernen / Swim & Improve | 654333 |
| Bildschirmspiegelung | 13698642 |

Die Werte gelten nur für neue Standardinstallationen. Updates setzen geänderte
PINs nicht zurück. Bei Wiederherstellung gelten die gesicherten PINs.
Die Berechtigungen stehen in der [Standardausstattung](STANDARD-AUSSTATTUNG.md).

Für das Hallen-WLAN **Admin → Netzwerk & Systemdienste → WLANs suchen** öffnen,
Netz auswählen und Kennwort eingeben. Nach dem Verbinden kann die IP wechseln.
Für die Einrichtung ohne funktionierendes Hallen-WLAN am Pi die Uhr mit der Maus
länger als zwei Sekunden gedrückt halten und die lokale Admin-PIN bestätigen.
Unter **Notfall-WLAN** stehen Hotspot-Name, individuelles Kennwort und Notfall-Adresse.
**Hotspot jetzt aktivieren** trennt die WLAN-Verbindung zum Hallennetz. Danach
mit dem Handy dem Hotspot beitreten, `http://10.42.0.1:8080/control` öffnen und
das Hallen-WLAN einrichten. Gespeicherte Zugänge bleiben erhalten.
Ausführliche Schritte: [Halleninstallation und WLAN](INSTALLATION.md).

## 6. Eine neue Cloud vorbereiten

Benötigt werden HTTPS, Apache mit erlaubten `.htaccess`-/Rewrite-Regeln, PHP ab 8.1
mit PDO-MySQL, Argon2id und Sodium sowie MariaDB/InnoDB. Im Hosting-Dashboard eine
**neue leere Datenbank** mit eigenem Benutzer anlegen. Keine Datenbank der
Vereinswebsite verwenden. Der Webpfad bleibt `/trainingsanzeige`.

Im Downloadordner mit den bereits geprüften Dateien:

```bash
python3 -B kit/tools/setup-webhosting.py --websetup vorbereitet/websetup \
  --output /GESCHUETZT/web-neu
```

Der neue Ausgabeordner muss außerhalb von Git und öffentlichem Webroot liegen.
Das Werkzeug fragt Domain/Cloudadresse, Datenbankhost, Port, Namen, Benutzer und
Kennwort ab. Das Kennwort wird verdeckt eingegeben. Es erzeugt:

- `www/`: fertige Upload-Dateien einschließlich privater `config.php`;
- `datenbank-neu.sql`: vollständiges Schema mit neuer Gerätekennung;
- `pi-kopplung.json`: neue Gerätekennung, neues Gerätesekret und eigene Cloudadresse;
- `LESEN.txt`: Hinweise für diesen Installationsweg.

In phpMyAdmin die neue leere Datenbank auswählen und `datenbank-neu.sql` importieren.
Das letzte Ergebnis muss **Installation importiert** melden. Eine belegte
Datenbank wird nicht verändert; das Ergebnis meldet **ABBRUCH**. Nach einem
fehlgeschlagenen Teilimport eine neue leere Datenbank verwenden.

Mit WinSCP/SFTP nur den **Inhalt von `www/`** in den neuen Webordner
`/trainingsanzeige/` hochladen, einschließlich `.htaccess` und `.release-signing.pub`.
SQL- und Kopplungsdateien neben `www/` niemals veröffentlichen. `config.php` nur
für den Hostingbenutzer lesbar lassen, üblicherweise mit Dateirechten 0600.
PHP muss unter diesem Benutzer lesen können.

`https://EIGENER-HOST/trainingsanzeige/control` und `/api/v1/health` öffnen.
Ein Abruf von `/config.php` oder `/schema.sql` darf keine privaten Inhalte liefern.
Keine alten Sicherungen im Webordner ablegen.

## 7. Pi und Cloud koppeln

Den lokalen Einrichtungsassistenten zuerst abschließen. `pi-kopplung.json`
privat auf den neuen Pi übertragen. Am Pi:

```bash
sudo systemctl stop trainingsanzeige-sync.service trainingsanzeige.service
sudo python3 /opt/trainingsanzeige/ops/configure-cloud.py /GESCHUETZT/pi-kopplung.json
sudo systemctl start trainingsanzeige.service trainingsanzeige-sync.service
```

Lokal und online anmelden, Verbindungsstatus prüfen und einen Testplan auf beiden
Seiten vergleichen. Die Kopplungsdatei privat aufbewahren. Neue Anlagen erhalten
keine Dalumer Identität und keine vorhandenen Bestandsdaten.
Für Ersatzgeräte gilt die [kontrollierte Umschaltung](WIEDERHERSTELLUNG.md).

## 8. Lernbibliothek und eigene Medien

Das signierte Medienpaket lässt sich vollständig ohne die bisherige Vereinswebsite
installieren. Auf dem Technikrechner für das neue Hosting:

```bash
python3 -B kit/tools/media-package.py --key release-signing.pub install \
  --archive trainingsanzeige-media-swim-20261021-1.zip --destination /GESCHUETZT/learning-library
```

Den erzeugten Ordner `learning-library` nach `/trainingsanzeige/learning-library`
hochladen. Dann am Pi unter Lernen die Bibliothek laden. Bei eingerichteter Cloud
wird deren Adresse als Quelle verwendet; Signatur und jede Dateiprüfsumme werden geprüft.

Alternativ das Paket direkt am Pi installieren. Anwendung vorher anhalten.
Der Zielordner muss neu sein. Eine vorhandene leere Bibliothek nach Kontrolle
umbenennen und als Rückfall behalten, nicht darüber kopieren:

```bash
sudo systemctl stop trainingsanzeige.service
sudo python3 -B kit/tools/media-package.py --key release-signing.pub install \
  --archive trainingsanzeige-media-swim-20261021-1.zip --destination /var/lib/trainingsanzeige/learning/library
sudo chown -R trainingsanzeige:trainingsanzeige /var/lib/trainingsanzeige/learning
sudo systemctl start trainingsanzeige.service
```

In Lernen müssen **318 Einträge** und vollständige Offline-Verfügbarkeit erscheinen.
Quellen- und Freigabehinweise bleiben im Katalog erhalten. Eigene Bilder, Audio,
Infotafelinhalte und Sender anschließend einrichten; sie gehören in die private Sicherung.

## 9. Display und Funktaster prüfen

Am LG 65UH5Q-E den tatsächlich verwendeten HDMI-Eingang wählen. Energiespar- und
Abschaltautomatik bewusst einstellen. Bei Bedarf CEC/SIMPLINK aktivieren und
mit dem eigenen Kabel prüfen. Bildformat ohne abgeschnittene Ränder wählen;
Helligkeit und Lautstärke für die Halle einstellen. Keine funktionierende
CEC-Steuerung allein aus einem Softwarestatus ableiten.

Am Pi HDMI-Ton prüfen, Bildschirmränder in der Administration einstellen und
Neustart, HDMI-Unterbrechung, Uhr und Standby testen. Die Fernsehtaste beendet
aktive Anzeigeinhalte und archiviert ein Training, führt zuerst zur Uhr und
ermöglicht von dort Standby. Ein geladenes Training läuft erst nach **Start**.

Funktaster einzeln anlernen und in Training, Lernen, Quiz und Spielen prüfen.
Auch den ersten Druck nach mehreren Sekunden Wartezeit, kurze und gehaltene
Betätigung sowie Reichweite testen. [Funktaster-Anleitung](../hardware/funktaster/README.md)
und [gemeinsame Abnahmeliste](ABNAHME.md) verwenden. Bluetooth-Geräte neu koppeln.
Miracast bleibt experimentell: [Grenzen und Einrichtung](MIRACAST.md).

## 10. Vor der Hallenmontage

- Lokal und online anmelden; Testplan erstellen, laden, starten, pausieren und archivieren.
- Ohne Internet Training, Uhr, Quiz und heruntergeladene Medien ausprobieren.
- HDMI-Ton, Fernsehtaste, Standby, Neustart und alle verwendeten Funktaster prüfen.
- Hallen-WLAN und Notfall-Hotspot einschließlich Rückkehr ins Hallennetz testen.
- Eine vollständige private Sicherung erstellen und auf getrennten Testzielen wiederherstellen.
- Danach ein signiertes Update unter **Admin → Sicherung & Updates → Trainingssystem** prüfen.

Ergebnisse mit Datum und Gerät in der [Abnahme](ABNAHME.md) dokumentieren.
Zugänge, age-Entschlüsselungsschlüssel, Wiederherstellungsdateien und einen privaten
Übergabezettel außerhalb von Git aufbewahren. Der Entschlüsselungsschlüssel gehört
auf einen getrennten Datenträger beziehungsweise in den Passwortmanager.
Ohne geprüfte Wiederherstellung ist der Ausgangsstand noch nicht vollständig abgenommen.
