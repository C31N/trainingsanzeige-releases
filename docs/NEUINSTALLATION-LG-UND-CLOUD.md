# Neuinstallation ab null: Raspberry Pi, Hallendisplay und Online-App

Vollständige Schritt-für-Schritt-Anleitung für ein leeres System. Softwarestand: **2.20.3**.

**Ziel:** Der Raspberry Pi zeigt das Training am LG 65UH5Q-E. Trainer bedienen ihn im Hallennetz oder über `https://wasserfreunde-dalum.de/trainingsanzeige/`. Der lokale Trainingsbetrieb funktioniert auch ohne Internet.

Diese Anleitung ist für eine neue, getrennte Anlage oder den Wiederaufbau nach einem Ausfall bestimmt. Für den bereits vorbereiteten Hallen-Pi gilt [Vorhandenen Pi installieren](INSTALLATION.md). Eine vollständige Erstinstallation und die Displaysteuerung am endgültigen LG müssen vor Ort abgenommen werden. Diese Anleitung ist kein Nachweis einer bestandenen Hardwareprüfung.

## 1. Was diese Anleitung voraussetzt

Wir beginnen mit einem **vollständig neuen System**: leerem Pi-Speichermedium, neuem Webserverordner, neuer eigener MariaDB und noch keiner Gerätekopplung. Es werden keine alten Pläne, PINs oder Einstellungen übernommen.

Alle Abschnitte der Reihe nach durchführen. Für die Webserver-Schritte werden Hosting-Administratorrechte und PHP-/Dateiverwaltungskenntnisse benötigt. Die fertige Trainerbedienung erfordert danach keine technischen Kenntnisse.

Die Beispieladresse lautet `https://wasserfreunde-dalum.de/trainingsanzeige/`. **Falls dort bereits etwas betrieben wird, darf es nicht überschrieben werden.** Eine neue separate Installation benötigt dann zunächst einen freien Host beziehungsweise eine Subdomain mit dem Pfad `/trainingsanzeige/`. Die Beispieladresse überall durch die tatsächlich gewählte Adresse ersetzen.

## 2. Anschließen und Netzwerk vorbereiten

Bereitlegen:

- neuer Raspberry Pi 4B oder 5 mit passendem Netzteil, Kühlung und Speichermedium;
- Raspberry Pi OS **64 Bit mit Desktop und Labwc/Wayland**, kein Lite-System;
- Micro-HDMI-auf-HDMI-Kabel, Tastatur und Maus für die Ersteinrichtung;
- LG 65UH5Q-E, dessen Fernbedienung und Zugang zum Displaymenü;
- nach Möglichkeit LAN am Pi, alternativ Hallen-WLAN;
- für Wake-on-LAN zusätzlich Netzwerkanschluss am LG;
- Zugang zur bestehenden Webverwaltung nur für die verantwortliche Technik.

Verbindung:

```text
Smartphone/Notebook ── Hallennetz ── Raspberry Pi ── HDMI ── LG-Display
                                          │
                                          └── ausgehend HTTPS ── Webserver + MariaDB
FireTV / weiterer PC ────────────────── andere HDMI-Eingänge am LG
```

1. Pi und Display zunächst auf einem Prüfstand einrichten, noch nicht unzugänglich montieren.
2. Pi direkt mit dem LG verbinden. Für den ersten Test weitere HDMI-Geräte abziehen.
3. Anschluss notieren, beispielsweise **Pi HDMI0 → LG HDMI1**. Die Nummer am LG ist nicht die Nummer von `/dev/cec0` am Pi!
4. Pi und später Trainergeräte im selben erreichbaren Hallennetz betreiben. Gast-WLAN mit Client-Isolation verhindert die lokale Bedienung.
5. Netzwerkverwaltung um feste DHCP-Zuordnung für den Pi bitten.
6. Keine Internet-Portfreigabe für 22 oder 8080 einrichten. Die Cloudkommunikation läuft vom Pi nach außen über HTTPS/443.

Für Installation/Updates benötigt der Pi zusätzlich DNS, korrekte Uhrzeit und Zugriff auf Paketquellen, Python-Paketquellen sowie `api.github.com`, `github.com` und GitHub-Release-Downloads. Freigaben mit der Hallen-IT abstimmen. Andere Hallennutzer dürfen nicht unkontrolliert auf die lokale Steuerung zugreifen.

Montage, Stromversorgung, Feuchte-/Korrosionsschutz und Belüftung durch Hallenverantwortliche beziehungsweise Fachpersonal freigeben lassen.

## 3. Betriebssystem auf dem neuen Pi einrichten

1. Mit Raspberry Pi Imager ein 64-Bit-System **mit Desktop** auf das neue Speichermedium schreiben. Achtung: Das Schreiben löscht dessen bisherigen Inhalt.
2. Als ersten Benutzer **`pi`** anlegen. Ein eigenes starkes Kennwort wählen, nicht `pi`. Die aktuellen Kioskdienste erwarten Benutzer `pi` mit UID 1000; ein anderer Benutzer erfordert Anpassungen durch die Technik.
3. Hostnamen `trainingsanzeige` verwenden. Falls dieser im Netz bereits vergeben ist, einen eindeutigen Namen wählen; nicht zwei gleichnamige Geräte betreiben.
4. Sprache/Zeitzone einstellen: Deutschland, `Europe/Berlin`; WLAN-Land korrekt setzen.
5. SSH nur bei Bedarf für die Einrichtung aktivieren; nicht ins Internet weiterleiten.
6. Pi starten, Netzwerk verbinden und Desktop-Autologin für `pi` einschalten. Desktop muss Labwc/Wayland verwenden.
7. Im Terminal prüfen:

```bash
id -u pi
uname -m
hostname -I
timedatectl
```

Erwartet: UID `1000`, Architektur `aarch64`, eine lokale IP und richtige Zeit. IP notieren.

## 4. Signiertes Installationspaket herunterladen

Im Browser des Pi die [Releaseübersicht](https://github.com/C31N/trainingsanzeige-releases/releases) öffnen. Unter **Assets** herunterladen:

- `trainingsanzeige.tar.gz`
- `trainingsanzeige.json`
- `trainingsanzeige.sig`
- `trainingsanzeige-web.json`

Nicht „Source code“ verwenden: Das öffentliche Repository ist der Downloadkanal, nicht das vollständige Entwicklungsrepository.

Den öffentlichen Prüfschlüssel `release-signing.pub` über die verantwortliche Technik beziehen und unabhängig vom Download bestätigen lassen. Der im aktuellen Quellstand hinterlegte öffentliche Schlüssel lautet:

```text
-----BEGIN PUBLIC KEY-----
MCowBQYDK2VwAyEAUESVrdRd6cUgzaKvDwq2pDt9sFYZ6SEHpf5aPPlVCwE=
-----END PUBLIC KEY-----
```

Der Schlüssel ist öffentlich. **Der private Signierschlüssel gehört niemals auf den Pi, Webserver oder GitHub.** Alle vier Dateien in einen neuen Ordner legen und dort ein Terminal öffnen. Prüfen:

```bash
openssl pkeyutl -verify -pubin -inkey release-signing.pub -rawin \
  -in trainingsanzeige.json -sigfile trainingsanzeige.sig
python3 -c 'import json,hashlib,pathlib; m=json.loads(pathlib.Path("trainingsanzeige.json").read_text()); a=m["artifacts"]; assert all(hashlib.sha256(pathlib.Path(v["name"]).read_bytes()).hexdigest()==v["sha256"] for v in a.values()), "Pruefsumme falsch"; print("Pakete geprueft, Version",m["version"])'
```

Nur nach `Signature Verified Successfully` und erfolgreicher Prüfsumme fortfahren. Bei einem Fehler nicht installieren.

```bash
mkdir trainingsanzeige-install
tar -xzf trainingsanzeige.tar.gz -C trainingsanzeige-install
cd trainingsanzeige-install
mkdir -p /home/pi/.config/autostart
sudo bash ops/install-pi.sh
```

Der Ordner `trainingsanzeige-install` soll vorher noch nicht existieren. Der im Befehlsblock angelegte
Desktopordner wird vom Installer benötigt. Der Installer verändert Boot-/Desktopkonfiguration und richtet einen dedizierten Kiosk ein. Er lädt Betriebssystem- und Python-Pakete aus dem Internet. Das Frontend ist im Release bereits gebaut.

Die öffentlichen Start-PINs stehen im nächsten Abschnitt. Nach der Einrichtung eigene PINs festlegen und vertraulich aufbewahren. Bei Installationsfehlern nicht einfach neu starten: Fehlermeldung notieren und Ursache beheben.

Nach erfolgreichem Abschluss:

```bash
sudo reboot
```

## 5. Lokale Einrichtung und Zugänge abschließen

1. Mit einem Gerät im selben Netz `http://PI-IP:8080/control` öffnen. `PI-IP` durch die notierte Adresse ersetzen.
2. `http://PI-IP:8080/setup` öffnen und mit dem Admin-Startwert **136542** den Assistenten abschließen. Anschließend stehen unter **Admin** die Bereiche **Verein & Erscheinungsbild**, **Halle** und **Trainingszeiten** bereit.
3. Vereinsname, transparentes Logo, Hallenname und Zeitzone kontrollieren.
4. Beckenlänge **16,6667 m**, vorhandene Schwimmbahnen und Tasterposition am Startblock eintragen.
5. Trainingsgruppen und Zeiten prüfen. Eine neue neutrale Installation enthält nicht automatisch euren gesamten bisherigen Datenbestand.
6. WLAN bei Bedarf suchen und verbinden. Nach Netzwerkwechsel kann sich die IP ändern.
7. Die optionale Cloud-/Internetanbindung im Installationsprofil zunächst **ausgeschaltet lassen**, bis die Kopplung abgeschlossen ist. Der Netzwerkzugang des Pi für Downloads bleibt bestehen.
8. Neue PINs unter den Admin-Sicherheitseinstellungen setzen.

| Zugang | Öffentliche Start-PIN | Funktion |
| --- | --- | --- |
| Administration | 136542 | Einstellungen, Zugangsdaten, Sicherungen und Training |
| Training | 123456 | Trainingspläne vorbereiten, laden und steuern |
| Musik | 654321 | Bluetooth, Webradio und Displaysteuerung |
| IPTV | 654322 | Sender auf dem Hallenbildschirm wiedergeben |
| Infotafel | 654323 | Bilder, Informationen und Einschaltzeiten verwalten |
| Lernen / Swim & Improve | 654333 | Lerninhalte, Abzeichenfragen und begrenzte Musiksteuerung |
| Bildschirmspiegelung | 13698642 | Experimentellen Miracast-Modus öffnen |

Dies sind öffentliche Erstwerte. Jeder Zugang benötigt eine andere PIN. Unter **Admin → Zugang & PINs** alle verwendeten Werte vor Internetfreigabe ändern. Medien- und Lernzugänge erhalten keine Trainerrechte. Bei einer Wiederherstellung gelten die übernommenen PINs; Updates setzen sie nicht zurück. Details: [Standardausstattung](STANDARD-AUSSTATTUNG.md).

Falls das normale WLAN fehlt, kann der Pi den Notfall-Hotspot bereitstellen. Dessen Kennwort wird individuell erzeugt, nicht mit der Admin-PIN gleichsetzen. Lokal auslesen:

```bash
sudo cat /var/lib/trainingsanzeige/hotspot-password
```

Nach Verbindung mit diesem Hotspot: `http://10.42.0.1:8080/control`. Das Kennwort vertraulich behandeln. Nach der lokalen Admin-PIN-Prüfung zeigt
auch das Wartungsfenster auf der Hallenanzeige unter **Notfall-WLAN** den Namen,
die Notfall-Adresse und das individuelle Kennwort. Dafür am Pi die Uhr mit der
Maus länger als zwei Sekunden gedrückt halten.

### Hotspot bei Bedarf sofort aktivieren

Im PIN-geschützten Bereich **Notfall-WLAN** aktiviert **Hotspot jetzt aktivieren**
den Hotspot unmittelbar. Dabei wird die WLAN-Verbindung zum Hallennetz getrennt;
den Hinweis vorher bestätigen. Gespeicherte Zugänge und Kennwort bleiben erhalten.
Nach der Aktivierung mit dem Handy dem angezeigten Hotspot beitreten und die
Notfall-Adresse öffnen. Am Handy über **Admin → Netzwerk & Systemdienste → WLANs suchen** wieder
mit dem Hallen-WLAN verbinden.

## 6. Webserver vollständig neu einrichten

Dieser Teil ist nur für eine **neue eigene Cloudinstallation**. Für lokalen Betrieb
ohne Cloud direkt mit Displayprüfung und Abnahme fortfahren. Bei einem Ersatzgerät
für eine bestehende Anlage stattdessen die geschützte Sicherung und Kopplung
wiederherstellen; keine neue Datenbank über den vorhandenen Bestand schreiben.

Aus **demselben Release wie das Pi-Paket** zusätzlich
`trainingsanzeige-websetup-2.20.3.zip` und seine `.sha256`-Datei laden. Die Prüfsumme
mit `sha256sum trainingsanzeige-websetup-2.20.3.zip` vergleichen. Der ZIP-Prüfwert
ist eine Transportkontrolle; die Herkunft muss ebenfalls vertrauenswürdig sein.
Auf dem Technikrechner werden Python 3, OpenSSL und PHP-CLI für die folgenden
Prüf- und Einrichtungsschritte benötigt. Das Websetup enthält das fertige
Online-Frontend und aktuelle Einrichtungsskripte,
aber keine Zugangsdaten. Keine Einrichtungsdateien aus alten Releases mischen.

Das ZIP auf dem Technikrechner entpacken. Die enthaltenen Dateien
`trainingsanzeige.json`, `trainingsanzeige.sig` und `trainingsanzeige-web.json`
mit dem unabhängig bestätigten öffentlichen Schlüssel prüfen:

```bash
openssl pkeyutl -verify -pubin -inkey release-signing.pub -rawin \
  -in trainingsanzeige.json -sigfile trainingsanzeige.sig
python3 -c 'import json,hashlib,pathlib; m=json.loads(pathlib.Path("trainingsanzeige.json").read_text()); a=m["artifacts"]["web"]; p=pathlib.Path("trainingsanzeige-web.json"); assert a["name"]==p.name and hashlib.sha256(p.read_bytes()).hexdigest()==a["sha256"], "Pruefsumme falsch"; print("Webpaket geprueft, Version",m["version"])'
```

Das Pi-Archiv liegt nicht im Websetup. `frontend/dist` wird beim Paketbau aus
genau diesem geprüften Webbundle erzeugt. Die Einrichtungsskripte selbst gehören
zum ergänzenden Websetup und sind nicht Bestandteil des signierten Webbundles.

### 6.1 Hosting vorbereiten

- HTTPS mit gültigem Zertifikat für die Zieladresse.
- PHP 8.1 oder neuer mit PDO-MySQL, Argon2id und Sodium für Ed25519-Prüfungen.
- MariaDB mit InnoDB/JSON-Unterstützung.
- Apache mit Rewrite-Regeln und zugelassener `.htaccess`; bei Nginx muss die Technik entsprechende Regeln einrichten.
- Eine eigene Datenbank und ein Benutzer ausschließlich für diese Datenbank.

Bei hosting.de im Dashboard Datenbank und zugehörigen Benutzer anlegen. Host, Datenbankname, Benutzer und Passwort im Passwortmanager speichern. Keine Joomla-, Zeltlager- oder Teilnehmerdatenbank überschreiben. Die Trainingsanzeige bleibt eine eigenständige Anwendung.

### 6.2 Kopplungswerte erzeugen

Auf einem vertrauenswürdigen Technikrechner mit Python:

```bash
python3 -c 'import uuid,secrets; print("Installations-ID: "+str(uuid.uuid4())); print("Gerätesekret: "+secrets.token_hex(32))'
```

Diese beiden Werte gehören zusammen. Installations-ID ist die Gerätekennung; Gerätesekret ist ein Passwort für die Synchronisierung. Beides sicher aufbewahren, nicht in Git einchecken.

In einer **geschützten UTF-8-Textdatei ohne BOM außerhalb des Webroots und Git-Repositories** folgende sechs Zeilen mit den tatsächlichen Werten anlegen:

```text
Datenbank-Host: DATENBANKHOST
Datenbank-Name: DATENBANKNAME
Datenbank-Benutzer: DATENBANKBENUTZER
Datenbank-Kennwort: INDIVIDUELLES_KENNWORT
Installations-ID: ERZEUGTE_UUID
Gerätesekret: ERZEUGTES_SEKRET
```

### 6.3 Datenbank und Webpaket vorbereiten

Im entpackten Websetup-Ordner liegt `frontend/dist` bereits fertig vor. Node.js und ein eigener Frontend-Build sind für diese Installation nicht erforderlich. Ein Terminal in diesem Ordner öffnen. Mit PHP-CLI und erlaubtem Zugriff auf die neue Datenbank ausführen:

```bash
php cloud/provision-db.php /GESCHUETZT/zugangsdaten.txt cloud/schema.sql
php cloud/prepare-release.php /GESCHUETZT/zugangsdaten.txt frontend/dist /GESCHUETZT/webpaket-neu
cp cloud/update-gateway.php /GESCHUETZT/webpaket-neu/update-gateway.php
cp cloud/version.php /GESCHUETZT/webpaket-neu/version.php
cp release-signing.pub /GESCHUETZT/webpaket-neu/.release-signing.pub
```

Unter Windows die drei Kopiervorgänge entsprechend mit `Copy-Item` ausführen.
Die Updatebrücke und ihr öffentlicher Schlüssel werden einmalig mit eingerichtet.
Platzhalterpfade ersetzen. Der Zielordner `webpaket-neu` darf noch nicht existieren. Falls die Datenbank nur vom Hoster erreichbar ist, Provisionierung dort per SSH außerhalb des öffentlichen Webroots ausführen. Das Provisionierungsskript **nicht als öffentlich aufrufbare Webseite** hochladen.

Das Paket ist für den Basispfad `/trainingsanzeige` ausgelegt. Eine andere Domain oder Subdomain ist möglich; denselben Pfad beibehalten und die Adresse beim Koppeln in Abschnitt 7 eintragen. Ein anderer Basispfad erfordert einen neuen Frontend-Build und angepasste PHP-Konfiguration durch die Technik. Das Cloudgateway ist für **eine Installation pro Datenbank/Webinstanz** ausgelegt.

### 6.4 Mit WinSCP veröffentlichen

1. Per SFTP mit dem Webhosting verbinden.
2. Im Webroot den Unterordner `trainingsanzeige` anlegen.
3. Nur den **Inhalt** des erzeugten Webpakets dorthin übertragen, einschließlich versteckter `.htaccess`.
4. Zielstruktur kontrollieren:

```text
trainingsanzeige/
  index.php
  index.html
  config.php
  update-gateway.php
  version.php
  .release-signing.pub
  .htaccess
  assets/
  sw.js
  ... öffentliche Logos und App-Dateien
```

`config.php` enthält das Datenbankpasswort: nur für den PHP-/Hostingbenutzer lesbar machen. `.htaccess` muss den HTTP-Zugriff darauf sperren. Niemals `zugangsdaten.txt`, SQL-Dumps, `.env`, SQLite-Dateien, private Schlüssel oder das ganze Pi-Release hochladen.

5. `https://wasserfreunde-dalum.de/trainingsanzeige/control` öffnen.
6. Zugriff auf `/trainingsanzeige/config.php` und `/trainingsanzeige/schema.sql` prüfen: Er muss verweigert werden, typischerweise HTTP 403. Bei erreichbaren Geheimnissen sofort stoppen und Hostingkonfiguration korrigieren.
7. Kein Cache/CDN darf `/api/`, `/device/` oder angemeldete Antworten zwischenspeichern. Joomla darf diese Unterordner-Routen nicht übernehmen.

**Vor der ersten erfolgreichen Pi-Synchronisierung funktioniert die Online-PIN-Anmeldung noch nicht zuverlässig:** Die gültigen PIN-Hashes kommen vom Pi.

## 7. Neue Cloud und neuen Pi miteinander koppeln

Jetzt werden die neue lokale Installation und die neue Webdatenbank erstmalig gekoppelt.

1. Auf dem Pi zuerst lokale Einrichtung und Admin-Anmeldung abschließen.
2. In `/root/trainingsanzeige-kopplung.txt` als root nur die zwei Zeilen `Installations-ID: ...` und `Gerätesekret: ...` aus Abschnitt 6 ablegen; Datei Modus `0600`. Das Datenbankpasswort wird auf dem Pi nicht benötigt.
3. Auf dem Pi ausführen:

```bash
sudo systemctl stop trainingsanzeige-sync.service trainingsanzeige.service
sudo /opt/trainingsanzeige/.venv/bin/python /opt/trainingsanzeige/ops/configure-cloud.py /root/trainingsanzeige-kopplung.txt
sudo systemctl start trainingsanzeige.service
```

Das Skript braucht ein bereits angelegtes lokales Installationsprofil und trägt zunächst `https://wasserfreunde-dalum.de/trainingsanzeige` ein. **Bevor der Syncdienst gestartet wird**, lokal als Admin unter Verein/Halle/Netzwerk die öffentliche Basisadresse auf die tatsächlich eingerichtete Adresse setzen, Internetanbindung aktivieren und speichern. Bei der Dalumer Beispieladresse reicht deren Kontrolle. Dann:

```bash
sudo systemctl restart trainingsanzeige-sync.service
```

4. Nach etwa einer Minute online mit der lokalen Trainer-/Admin-PIN anmelden.
5. Kopplungsdatei nach gesicherter Ablage im Passwortmanager vom Pi entfernen lassen; das notwendige Laufzeitsekret bleibt root-geschützt in `/etc/trainingsanzeige.env`.
6. Ein kleines Testtraining online vorbereiten. Warten, bis **Wird zum Gerät übertragen** verschwindet; lokal denselben Eintrag prüfen.
7. Status **Verbunden** kontrollieren. Das ist nicht automatisch eine Bestätigung, dass der LG eingeschaltet ist; Displaystatus separat prüfen.

## 8. LG 65UH5Q-E einrichten und abnehmen

Displaymenüs anhand des zum tatsächlich eingesetzten LG gehörenden Handbuchs prüfen. Die folgende Funktionsprüfung muss am Gerät erfolgen; Energiesparzustände und weitere HDMI-Geräte können die Steuerung beeinflussen.

1. Am LG den tatsächlich belegten HDMI-Eingang auswählen und HDMI-CEC aktivieren. Menübezeichnungen anhand des mitgelieferten LG-Handbuchs prüfen.
2. Im lokalen Adminbereich **Display / System & Kiosk** die automatische Ausgangserkennung kontrollieren. Physische HDMI-Buchse am Pi und Eingang am LG korrekt zuordnen.
3. Einrichtungsassistent für die Displaysteuerung starten. Zuerst CEC prüfen, dann gegebenenfalls CEC mit Neuaufbau oder WOL + CEC.
4. Nach jeder Umschaltung mindestens die 30-Sekunden-Sperrzeit abwarten. **Display ist an/aus nur bestätigen, wenn es tatsächlich stimmt.**
5. Für WOL: LG an dasselbe geeignete LAN anschließen, WOL/Netzwerkbereitschaft am LG aktivieren und dessen LAN-MAC im Assistenten eintragen. Nicht die MAC des Pi verwenden. WOL funktioniert nicht bei stromlosem Display.
6. Nur eine wirklich funktionierende Kombination speichern. RS-232/IP ist im aktuellen Stand kein fertig abgenommener Ersatztreiber.
7. Auflösung und sämtliche Bildränder prüfen. Die Desktop-Konfiguration versucht UHD/60 Hz und fällt bei Bedarf zurück. Die Bootausgabe kann davon abweichen; 4K/60 am konkreten Kabel/Pi überprüfen, nicht nur voraussetzen.
8. Testton am **Hallenbildschirm** ausgeben und Lautstärke einstellen.
9. FireTV und PC wieder anschließen. Jeweils auf deren Eingang wechseln und testen, dass der Pi dort **keinen automatischen Standby** auslöst. Anschließend zum Pi zurückwechseln und den Leerlaufcountdown prüfen.

Wenn der LG seinen aktiven Eingang nicht eindeutig meldet, Automatik zunächst deaktivieren. „Letzten bestätigten Eingang verwenden“ ist keine sichere Erkennung eines späteren, nicht gemeldeten Eingangswechsels. Erst nach bestandenem Mehrgeräte-Test die gewünschte automatische Standbyzeit aktivieren.

## 9. Funk, Medien und Lernbibliothek einrichten

1. CC1101 stromlos anschließen: 3,3 V und GND, SPI0 CE0/GPIO 8, SCLK/GPIO 11,
   MOSI/GPIO 10, MISO/GPIO 9, GDO0/GPIO 24 und GDO2/GPIO 25. Keine 5 V anlegen.
   SPI-Verfügbarkeit und Empfängerstatus durch die Technik prüfen lassen.
2. Unter **Admin → Funktaster** jeden vorhandenen Sender anlernen und eine Bahn
   oder Trainerfunktion zuordnen. Sender-ID und Bahnnummer sind nicht dasselbe.
   Für DIAMEX gelten [Bau- und Programmieranleitung](../hardware/funktaster/README.md).
3. **Trainingssignale** öffnen, vorhandene Standardklänge und Bahnzuordnungen
   prüfen. Ein neuer Datenträger übernimmt keine privaten Medien aus einer Altanlage.
4. Unter **Bluetooth & Webradio** Namen und Audioausgang kontrollieren; mit dem
   Musikzugang koppeln und hören. Bluetooth-Geräte bei Ersatz des Pi neu koppeln.
5. **IPTV**, **Infotafel**, **Spiele** und **Bildschirmspiegelung** nur soweit
   benötigt einrichten und anschließend jeweils getrennt prüfen.
6. Unter **Schwimmen lernen – Swim & Improve** Bibliothek laden und vollständigen
   Prüfstatus abwarten. Mindestens 6 GiB frei lassen. Die signierten Lernvideos
   werden separat geladen und gehören nicht zum kleinen Anwendungsupdate.
7. Mit Lern-PIN Text, Bild und Video zeigen. Nach dem Download lokalen Betrieb
   ohne Internet prüfen. Quizfragen sind eine Übung, keine offizielle Prüfung.
8. Trainingszeit anlegen und unter **Vorlagen → Neue Vorlage** den ersten Plan
   speichern. Über **Als kommende Trainingseinheit planen** einen Termin anlegen. Einheit laden,
   unter **Aktiv** erst starten, anschließend mit Archivierung beenden.

## 10. Abschlusstest vor der Montage

- [ ] Lokale Steuerung und `/display` erreichbar; Logo und alle vier Ränder sichtbar.
- [ ] Richtige Auflösung, ausreichende Schriftgröße und Ton am LG.
- [ ] Trainer-PIN und Admin-PIN funktionieren; Adminbereiche für Trainer gesperrt.
- [ ] Eigene Gruppen und mindestens eine Vorlage angelegt; Testtermin gespeichert.
- [ ] Online erstellte Änderung erscheint lokal; Übertragungsmarkierung verschwindet.
- [ ] Bei Internetausfall funktioniert lokales Training weiter.
- [ ] Display schaltet real ein und aus; Status stimmt danach.
- [ ] Fremder HDMI-Eingang wird nicht automatisch abgeschaltet.
- [ ] Funkempfänger und Bahnzuordnung gegebenenfalls geprüft. Verdrahtung nur bei stromlosem Pi ändern.
- [ ] Kontrollierter Neustart: Kiosk startet, laufendes Training wird sicher pausiert wiederhergestellt.
- [ ] Backup und externer Sicherungsort vorhanden; Wiederherstellung auf einem Teststand geprüft.
- [ ] Mehrstündiger Probebetrieb und echtes Training am LG erfolgreich.

Dienstprüfung am Pi:

```bash
systemctl is-active trainingsanzeige.service trainingsanzeige-kiosk.service
systemctl is-active trainingsanzeige-sync.service trainingsanzeige-backup.timer
curl -fsS http://127.0.0.1:8080/api/v1/health
```

Erwartet: die genannten Dauerdienste und der Sicherungstimer `active`, Health `status: ok`. Ein aktiver Syncdienst allein beweist noch keine erfolgreiche Cloudkopplung. Miracast läuft nur während einer Spiegelung; erfolgreich beendete Einmaldienste müssen nicht dauerhaft aktiv sein.

Danach die vollständige [Abnahmeliste für den Hallenstandort](ABNAHME.md) abarbeiten, Ergebnisse und offene Punkte festhalten. Erst eine tatsächlich bestandene Prüfung freigeben.

## 11. Spätere Updates in der Schwimmhalle

**Trainingssystem:** Ganz unten Admin → Sicherung & Updates → Trainingssystem → Version prüfen → aktualisieren und Admin-PIN bestätigen. Derselbe Auftrag aktualisiert Raspberry Pi und gekoppelte Online-App. Kein Training geladen lassen; Stromversorgung nicht trennen. Signaturprüfung, gemeinsame Sicherung und automatische Rückkehr beider Seiten bei Fehlern sind integriert.

**Betriebssystem:** eigener Systemupdatebereich; nicht mit Anwendungsupdates verwechseln.

**Webserver:** wird nach der einmaligen Installation der Updatebrücke automatisch mitgeführt. Ist er nicht erreichbar, bleibt auch der Pi unverändert. `config.php`, Geräteschlüssel und MariaDB werden nie aus dem öffentlichen Release ersetzt.

Details: [Anwendungsupdates](ANWENDUNGSUPDATES.md).

## 12. Wenn etwas nicht funktioniert

| Problem | Zuerst prüfen |
| --- | --- |
| `.local` geht nicht | IP mit `hostname -I` ermitteln; gleicher Netzbereich, keine Client-Isolation. |
| Kiosk fehlt / Desktop sichtbar | Benutzer `pi`, UID 1000, Autologin, Labwc/Wayland; Kioskdienst prüfen. |
| Online PIN ungültig | Erste Synchronisierung abwarten; ID/Sekret/HTTPS und Uhrzeit prüfen, PIN nicht wahllos ändern. |
| Online „Getrennt“ | Pi-Netz, Cloudadresse, Ausgangsfirewall, Syncprotokoll und identische Kopplungswerte prüfen. |
| HTTP 500 | PHP-Fehlerprotokoll des Hosters, PHP-Version/Erweiterungen, Datenbankzugang und Tabellen prüfen. |
| Onlinepfad springt zu `/control` | Cloudbuild mit `/trainingsanzeige/` verwenden, `.htaccess` und Cache prüfen; kein Pi-Frontend hochladen. |
| LG blinkt, schaltet aber nicht | Richtige CEC-Verbindung und Methode testen; weitere Geräte einzeln anschließen; WOL alternativ abnehmen. |
| Uhr/Standby falsch | Aktiven Eingang, letzte Bestätigung und Automatik prüfen; bei unbekannter Eingangslage Automatik ausschalten. |

Protokolle lokal lesen:

```bash
sudo journalctl -u trainingsanzeige.service -n 60 --no-pager
sudo journalctl -u trainingsanzeige-sync.service -n 60 --no-pager
sudo journalctl -u trainingsanzeige-kiosk.service -n 60 --no-pager
```

Vor Weitergabe PINs, Schlüssel, persönliche Daten und vertrauliche Adressen entfernen.

## Übergabezettel — getrennt von dieser öffentlichen Anleitung aufbewahren

Notieren: Pi-Hostname/IP, belegte HDMI-Anschlüsse, LG-LAN-MAC, gewähltes Schaltverfahren, Cloudadresse, Installations-ID, Verantwortlicher und Sicherungsort. Zugangsdaten ausschließlich im Passwortmanager speichern. **Keine ausgefüllte Zugangsdatenliste auf GitHub hochladen.**
