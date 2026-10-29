# Trainingsanzeige – Downloads und Anleitungen

**Aktueller Stand: 2.20.13.** Die Software ist für die Installation und Abnahme
in der Schwimmhalle vorbereitet. Die tatsächliche Hardwareprüfung am Standort
ist noch durchzuführen.

Im lokalen Wartungsfenster zeigt der Bereich **Notfall-WLAN** nach bestätigter
Admin-PIN den gespeicherten Hotspot-Namen, die Notfall-Adresse und das individuelle
Kennwort. Über die Online-Adresse ist dieser lokale Zugang nicht verfügbar.

Im PIN-geschützten Bereich **Notfall-WLAN** aktiviert **Hotspot jetzt aktivieren**
den Hotspot unmittelbar. Dabei wird die WLAN-Verbindung zum Hallennetz getrennt;
den Hinweis vorher bestätigen. Gespeicherte Zugänge und Kennwort bleiben erhalten.
Nach der Aktivierung mit dem Handy dem angezeigten Hotspot beitreten und die
Notfall-Adresse öffnen. Am Handy über **Admin → Netzwerk & Systemdienste → WLANs suchen** wieder
mit dem Hallen-WLAN verbinden.

Die Uhr-Umschaltung bei lokaler Trainer-Anmeldung funktioniert auch in einem
neu geöffneten Anzeigetab und nach erneuter Anmeldung in einem anderen Tab.
Der CSRF-Schutz bleibt dabei erhalten.

## Welche Anleitung brauche ich?

- [Funkdiagnose, Sendetests und Fernbedienungen](docs/FUNKDIAGNOSE.md)

- [Vorhandenen Raspberry Pi in der Halle installieren](docs/INSTALLATION.md)
- [Vollständige Neuinstallation ab null](docs/NEUINSTALLATION-LG-UND-CLOUD.md)
- [Zweite Anlage mit eigener Identität](docs/NEUINSTALLATION-LG-UND-CLOUD.md)
- [Ersatz nach Ausfall und private Sicherung](docs/WIEDERHERSTELLUNG.md)
- [Training planen und bedienen](docs/TRAINER-HANDBUCH.md)
- [Administration und Sicherungen](docs/ADMIN-HANDBUCH.md)
- [Abnahme am Hallengerät](docs/ABNAHME.md)
- [Alle Anleitungen](DOKUMENTATION.md)

## Öffentliche Start-PINs

| Zugang | Öffentliche Start-PIN | Funktion |
| --- | --- | --- |
| Administration | 136542 | Einstellungen, Zugangsdaten, Sicherungen und Training |
| Training | 123456 | Trainingspläne vorbereiten, laden und steuern |
| Musik | 654321 | Bluetooth, Webradio und Displaysteuerung |
| IPTV | 654322 | Sender auf dem Hallenbildschirm wiedergeben |
| Infotafel | 654323 | Bilder, Informationen und Einschaltzeiten verwalten |
| Lernen / Swim & Improve | 654333 | Lerninhalte, Abzeichenfragen und begrenzte Musiksteuerung |
| Bildschirmspiegelung | 13698642 | Experimentellen Miracast-Modus öffnen |

Diese PINs sind öffentlich bekannte **Startwerte für eine neue Standardinstallation**.
Bereits eingerichtete oder geänderte PINs gelten weiter. Ein Update setzt sie
nicht zurück. Auch bei älteren Installationen können andere Startwerte gelten.
Jeder Zugang braucht eine andere PIN. Vor der Internetfreigabe unter
**Admin → Zugang & PINs** eigene PINs festlegen und vertraulich aufbewahren.
Die getrennten Zugänge für Medien und Lernen vergeben keine Trainer- oder Adminrechte.

## Downloads

Unter [Releases](https://github.com/C31N/trainingsanzeige-releases/releases) liegen
je Version die vier zusammengehörenden Dateien `trainingsanzeige.tar.gz`,
`trainingsanzeige-web.json`, `trainingsanzeige.json` und `trainingsanzeige.sig`.
Für eine Neuinstallation das vollständige `trainingsanzeige-installation-2.20.13.zip`
mit `installation.json`, `installation.sig`, `release-signing.pub` und dem separaten
`trainingsanzeige-media-swim-20261021-1.zip` verwenden. Die zusätzliche Signatur schützt
auch die Einrichtungsskripte. Das Websetup ist bereits darin enthalten.
Die [Neuinstallation](docs/NEUINSTALLATION-LG-UND-CLOUD.md) erklärt die Prüfung und alle Schritte.
„Source code“ ersetzt kein Installationspaket.

Bestehende Anlagen werden unter **Admin → Sicherung & Updates → Trainingssystem**
aktualisiert. Das signierte Update führt Pi und gekoppelte Online-App gemeinsam
weiter und erhält Daten, PINs und Kopplung. Eine Neuinstallation ist dafür nicht nötig.
Die Lernvideobibliothek ist ein eigener Download im Adminbereich.

- [Standardausstattung](STANDARD-AUSSTATTUNG.md)
- [Updates im Detail](docs/ANWENDUNGSUPDATES.md)
- [Funktaster, aktueller V5-Bauplan und Windows-Programmierpaket](hardware/funktaster/README.md)

Geräteschlüssel, WLAN-Kennwörter, Datenbanken, private Medien, PIN-Hashes und
private Signierschlüssel sind keine öffentlichen Downloadinhalte.
