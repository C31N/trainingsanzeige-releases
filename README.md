# Trainingsanzeige – Downloads und Anleitungen

**Aktueller Stand: 2.21.0.** Die Software ist für die Installation und Abnahme
in der Schwimmhalle vorbereitet. Die tatsächliche Hardwareprüfung am Standort
ist noch durchzuführen.

Neu in **2.21.0**: Manueller Drei-Bahnen-Wettkampf mit lokaler Laufsteuerung, Stoppuhrwerten, Hallenanzeige, Ergebnisfreigabe und CSV. [Bedienung](docs/WETTKAMPF.md)

Neu in **2.20.43**: Nummerierte Trainingsblöcke, direktes Einfügen per Pluszeichen und eine manuell blätterbare Übersicht des gesamten Trainings auf Handy und Hallenanzeige.

Korrektur in **2.20.42**: Ungeeignete Impulsaufnahmen zählen als verworfen; nur tatsächliche Decoderfehler erscheinen als Analysefehler.

Neu in **2.20.41**: Unter Administration → Funktaster lassen sich weitere Sender und Sensoren passiv suchen. Die optionale Suche bleibt zunächst ausgeschaltet und ist ausschließlich im Ruhezustand möglich. Details und Empfangsgrenzen: [Funkdiagnose](FUNKDIAGNOSE.md).

Korrektur in **2.20.40**: Inaktive Bilder bleiben in der normalen Liste. Nur bewusstes Archivieren oder der Ablauf des Enddatums verschiebt sie ins Archiv.

Seit **2.20.39**: Informationen und Werbung erhalten ein Bildarchiv mit
Originaldownload, erneuter Aktivierung und bestätigten Aktivierungszeiträumen.
Optionale Start- und Enddaten mit Uhrzeiten begrenzen die Anzeige automatisch.
Nur die Administration darf Archivbilder endgültig löschen.
[Bedienung und Zeitplanung](https://github.com/C31N/trainingsanzeige-releases/blob/main/docs/GEMEINDEANZEIGE.md).

Seit 2.20.38: Vor und zurück funktioniert auch nach **Video zeigen** direkt
innerhalb der gewählten Eulen-Phase oder des geöffneten Checks. Die Fernbedienung
verwendet dieselbe Reihenfolge wie die Handybedienung.
Auch die Eulen-Videos laufen standardmäßig in Schleife.
Das ausgewählte Video wiederholt sich bis zum manuellen Wechsel oder Beenden;
unter **Weitere Optionen → Wiederholen** lässt sich dies ausschalten.

**Die Eule & das Schwimmen** ergänzt den Lernbereich um
18 Originalvideos, Kinderaufträge, Originalbilder, Druckvorlagen und sieben
vorbereitete Lernfolgen. Die fünf Phasen, der Basis-Check, die Blaue Bahn und
der Detailblick sind getrennt aufklappbar. [Anleitung](docs/DIE-EULE.md).

Die neue signierte Lernbibliothek **swim-eule-20261112-1** enthält alle bisherigen
Materialien sowie die Eulen-Inhalte: **409 Einträge und 251 Dateien**. Nach dem
Anwendungsupdate muss auch die Lernbibliothek aktualisiert werden.
Die Installation erfolgt über die Administration. Bereits geladene Medien
bleiben beim Anwendungsupdate erhalten.

Betrieb: [LAN-Internet und automatisches Notfall-WLAN](docs/LAN-UND-NOTFALL-WLAN.md),
einschließlich weiterhin verfügbarer Bildschirmspiegelung.

Im lokalen Wartungsfenster zeigt der Bereich **Notfall-WLAN** nach bestätigter
Admin-PIN den gespeicherten Hotspot-Namen, die Notfall-Adresse und das individuelle
Kennwort. Über die Online-Adresse ist dieser lokale Zugang nicht verfügbar.

Im PIN-geschützten Bereich **Notfall-WLAN** aktiviert **Hotspot jetzt aktivieren**
den Hotspot unmittelbar. Im LAN-Betrieb ist das bei bestätigtem Internet gesperrt.
Dabei wird die WLAN-Verbindung zum Hallennetz getrennt;
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
Für eine Neuinstallation das vollständige `trainingsanzeige-installation-2.21.0.zip`
mit `installation.json`, `installation.sig`, `release-signing.pub` und dem separaten
`trainingsanzeige-media-swim-eule-20261112-1.zip` verwenden. Die zusätzliche Signatur schützt
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

## Zusatzplatine für kurze Buzzerdrücke

Die [ATtiny402-Impulsverlängerung Rev A](hardware/funktaster/impulsverlaengerung/README.md) ist als separates Hardware-Prototyppaket verfügbar. Es enthält KiCad-Projekt, Gerber/Bohrdaten, Stückliste, Firmware und drei PDF-Anleitungen. Elektrische Messung, Akkutest und Funkabnahme am echten Buzzer stehen noch aus. Für die Zusatzplatine ist kein Pi-Anwendungsupdate nötig.
