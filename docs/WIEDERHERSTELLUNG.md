# Private Sicherung und Ersatz nach Ausfall

Die vollständige Sicherung besteht aus **Pi** und **Cloud**. Sie enthält private
Daten und Zugangswerte und gehört niemals in Git oder auf einen Downloadserver.
Eine neue unabhängige Anlage folgt der [Neuinstallation](NEUINSTALLATION-LG-UND-CLOUD.md).
Ein Ersatzgerät übernimmt die bestehende Identität erst bei der Umschaltung.

## Was gesichert wird

| Komponente | Inhalt |
| --- | --- |
| Pi | Konsistente SQLite-Datenbank mit Plänen, Archiven, PIN-Hashes, Funkzuordnungen und Einstellungen; eigene Medien und Lernbibliothek; Anwendungskonfiguration, Kopplungsgeheimnis, Updatekonfiguration; WLAN-Profile und Hotspot-Kennwort |
| Cloud | Vollständiges Schema und alle Anwendungstabellen; Cloudkonfiguration, Kopplungswerte, Vereinslogo und Lernbibliothek |
| Manifest je Sicherung | Version, Zeitpunkt, Installationskennung, Dateigrößen und SHA-256-Prüfsummen |

Alte automatische Sicherungen, temporäre Status-/Befehlsdateien und Betriebssystem-
Caches werden nicht als aktive Daten wiederhergestellt. Betriebssystem und Dienste
kommen aus dem geprüften Installationspaket. Bluetooth-Geräte werden neu gekoppelt.
Die tägliche lokale Sicherung ersetzt diese vollständige private Sicherung nicht.

## 1. Verschlüsselung vorbereiten

[age](https://github.com/FiloSottile/age) auf einem vertrauenswürdigen Technikrechner
installieren. Die mitgelieferten Werkzeuge brauchen Python ab 3.11.
Den **Entschlüsselungsschlüssel getrennt von den Sicherungen** aufbewahren:

```bash
umask 077
age-keygen -o /SCHLUESSELDATENTRAEGER/trainingsanzeige-age.txt
age-keygen -y /SCHLUESSELDATENTRAEGER/trainingsanzeige-age.txt > recipient.txt
```

Nur `recipient.txt` an Pi und Hosting übertragen. Damit kann verschlüsselt, aber
nicht entschlüsselt werden. Den privaten Schlüssel nicht auf Pi oder Hosting legen.
Unter Windows zusätzlich die Ordnerberechtigungen auf die verantwortliche Person
beschränken. Die verschlüsselten Sicherungen auf mindestens einen zweiten Datenträger kopieren.

## 2. Bestand im Wartungsfenster sichern

Vorher Training und Medien beenden, andere Bediener informieren und keine neuen
Eingaben mehr machen. Auf dem Pi die Synchronisierung anhalten:

```bash
sudo systemctl stop trainingsanzeige-sync.service
sudo python3 /opt/trainingsanzeige/ops/recovery.py backup-pi \
  --recipient /PRIVAT/recipient.txt --output /PRIVAT/pi-DATUM.age
```

Das Werkzeug hält die aktiven Anwendungsdienste für den Datenabzug an und startet
sie anschließend wieder. SQLite wird über die Sicherungsschnittstelle kopiert.
Die bereits angehaltene Synchronisierung bleibt bis zum Ende des gemeinsamen
Wartungsfensters aus. Bestehende Sicherungsdateien werden nicht überschrieben.

Die geprüften Dateien `backup-cloud-host.py`, `backup-cloud-db.php`, `recovery.py`
und `installation_common.py` aus `kit/tools/` in einen **privaten Ordner außerhalb
des Webroots** auf dem Hosting übertragen. Dort werden Python ab 3.11, PHP-CLI
und age benötigt. Dann über den Hosting-SSH-Zugang:

```bash
python3 /PRIVAT/tools/backup-cloud-host.py \
  --webroot /WEBROOT/trainingsanzeige \
  --recipient /PRIVAT/recipient.txt --output /PRIVAT/cloud-DATUM.age
```

Das Werkzeug schaltet die Online-App während Datenbank- und Medienabzug auf
HTTP 503 und stellt anschließend die ursprüngliche `.htaccess` wieder her.
Die Verschlüsselung läuft nach dieser kurzen Sperre. Bei einem vollständigen
Prozessabbruch bleibt eine private `.htaccess-rescue` zum Zurückkopieren erhalten.
Den Webzugang danach prüfen. Alle Tabellen müssen InnoDB verwenden.

Hat das Hosting keinen SSH-Zugang, kann die verantwortliche Technik mit
`backup-cloud-db.php` über einen erlaubten privaten Datenbankzugang den gleichen
konsistenten JSONL-Abzug erzeugen und Webdateien per SFTP privat kopieren.
Danach `recovery.py backup-cloud --webroot PRIVATER-WEBABZUG --database-dump ABZUG.jsonl.gz
--recipient recipient.txt --output cloud-DATUM.age` verwenden. Datenbank und Dateien
müssen aus demselben Wartungsfenster stammen. Keine Sicherungsskripte öffentlich abrufbar machen.

Beide `.age`-Dateien auf den Technikrechner übertragen. Danach am Pi:

```bash
sudo systemctl start trainingsanzeige-sync.service
```

Pi und Cloud wieder auf Erreichbarkeit prüfen. Die Werkzeuge geben keine PINs,
Datenbankkennwörter oder Kopplungsgeheimnisse aus.

## 3. Vor einer Wiederherstellung prüfen

```bash
python3 -B kit/tools/recovery.py verify --archive /SICHERUNG/pi-DATUM.age \
  --identity /SCHLUESSELDATENTRAEGER/trainingsanzeige-age.txt
python3 -B kit/tools/recovery.py verify --archive /SICHERUNG/cloud-DATUM.age \
  --identity /SCHLUESSELDATENTRAEGER/trainingsanzeige-age.txt
```

Falsche Schlüssel, beschädigte Archive und abweichende Dateiprüfsummen führen
zum Abbruch, bevor Daten übernommen werden. Für beide Komponenten die gleiche
Installationskennung und dasselbe Wartungsfenster sicherstellen. Zur Prüfung
immer getrennte Testziele verwenden, niemals eine produktive Datenbank leeren.

## 4. Nur den Pi ersetzen

1. Ersatz-Pi mit dem geprüften Installationspaket einrichten; den lokalen Einrichtungsassistenten **noch nicht abschließen**.
2. Bisherigen Pi ausschalten beziehungsweise dauerhaft vom Netz trennen. Er darf später nicht parallel synchronisieren.
3. Sicherung und Entschlüsselungsschlüssel vorübergehend über einen geschützten Datenträger am Ersatzgerät bereitstellen.
4. Im Terminal wiederherstellen:

```bash
sudo python3 /opt/trainingsanzeige/ops/recovery.py restore-pi \
  --archive /SICHERUNG/pi-DATUM.age \
  --identity /SCHLUESSELDATENTRAEGER/trainingsanzeige-age.txt --old-device-offline
```

Bei einer neuen Cloudadresse zusätzlich `--url https://NEUER-HOST/trainingsanzeige`
angeben. Das Werkzeug verweigert ein bereits vollständig eingerichtetes Ziel.
Es übernimmt die Daten und startet den Pi lokal. **Die Cloud bleibt ausgeschaltet.**
Alte Anmeldesitzungen und Gerätebefehle werden verworfen. Ein geladenes laufendes
Training kehrt pausiert mit dem Stand des Sicherungszeitpunkts zurück.

5. Mit der bisherigen PIN anmelden. Pläne, Archive, PINs, Taster, eigene Medien und Offline-Lernbibliothek vergleichen.
6. WLAN, Hotspot, HDMI-Ausgang, Ton, CEC, Funkempfänger und Spiegelung am neuen Gerät prüfen. Bluetooth neu koppeln.
7. Erst nach bestandenem Vergleich die Cloud im Installationsprofil wieder aktivieren und den ersten Abgleich kontrollieren.
8. Entschlüsselungsschlüssel vom Ersatzgerät entfernen beziehungsweise Datenträger abziehen.

## 5. Nur das Webhosting ersetzen

Den bestehenden Pi während der Wiederherstellung nicht synchronisieren lassen.
Neue Domain und leere Datenbank vorbereiten. Mit dem geprüften Websetup einen
Uploadordner für die **neuen Hostingzugänge** erzeugen:

```bash
python3 -B kit/tools/setup-webhosting.py --websetup vorbereitet/websetup \
  --output /PRIVAT/hosting-ersatz --replacement
python3 -B kit/tools/recovery.py restore-cloud --archive /SICHERUNG/cloud-DATUM.age \
  --identity /SCHLUESSELDATENTRAEGER/trainingsanzeige-age.txt --output /PRIVAT/cloud-restauriert
```

`datenbank-wiederherstellen.sql` aus dem zweiten Ordner in die neue leere Datenbank
importieren. Das letzte Ergebnis kontrollieren. Der Import einer belegten Datenbank
ändert nichts. Bei einem Abbruch eine neue leere Testdatenbank verwenden.

Den Inhalt von `hosting-ersatz/www/` in die neue Webinstanz hochladen. Danach aus
`cloud-restauriert/private-web/` nur Lernbibliothek, Vereinslogo und öffentlichen
Prüfschlüssel übernehmen. **Die alte `config.php` nicht darüber kopieren**: Ihre
Zugänge gelten nur für das bisherige Hosting. Die neue `config.php` aus dem
Einrichtungswerkzeug verwendet die neuen Zugänge. SQL-Abzug und private Konfiguration
bleiben außerhalb des Webroots.

Die vorhandene Installationskennung und das Gerätesekret kommen aus der Sicherung.
Keine neue Kopplungsdatei erzeugen. Bei einer anderen Domain am Pi die Cloudadresse
ändern. Alte Cloudinstanz stilllegen, dann Synchronisierung wieder aktivieren.
Alte Online-Sitzungen, Loginversuche, Nonces, Livezustände und Gerätebefehle werden
nicht wiederhergestellt; nach dem ersten Abgleich erneut anmelden.

## 6. Beide Komponenten ersetzen und Abnahme

Zuerst Cloud gemäß Abschnitt 5 herstellen, danach Pi gemäß Abschnitt 4. Beide
Sicherungen müssen zur selben Anlagenkennung gehören. Altes Gerät und alte
Cloud vor dem ersten Abgleich stilllegen. Die Umschaltung ausdrücklich protokollieren.

Für den Nachweis vergleichen: Anzahl und Inhalt der Pläne und Archive, PIN-Hashes,
Funkzuordnungen, Einstellungen, Medienprüfsummen und Lernbibliothek. Danach lokal
und online anmelden, einen Testplan laden/starten/archivieren und ein signiertes
Update prüfen. Hardwaretests aus [Abnahme](ABNAHME.md) gesondert durchführen.

Die erfolgreiche Entschlüsselung allein beweist noch keine betriebsfähige
Wiederherstellung. Erst der Datenvergleich und der Funktionstest auf getrennten
Zielen schließen diesen Schritt ab. Ergebnisse ohne Zugangsdaten dokumentieren.
