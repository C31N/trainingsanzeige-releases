# Vorhandenen Raspberry Pi in der Schwimmhalle installieren

Diese Anleitung übernimmt den vorbereiteten **Raspberry Pi 5** am endgültigen
Hallenbildschirm. Bestehende Trainings, PINs, Medien, Netzwerkeinstellungen und
Cloud-Kopplung bleiben erhalten. Für einen leeren Datenträger gilt stattdessen die
[vollständige Neuinstallation ab null](NEUINSTALLATION-LG-UND-CLOUD.md).

## 1. Vor dem Transport sichern

1. Training, Spiel und Medienwiedergabe beenden; außerhalb des Badebetriebs arbeiten.
2. Als Admin unter **Sicherung & Updates** eine Sicherung exportieren und auf
   einem zweiten Gerät ablegen. Lesbarkeit und vorgesehenen Wiederherstellungsweg prüfen.
3. Durch die Technik zusätzlich ein Systemabbild und die geschützten
   Gerätekonfigurationen sichern lassen. Der Datenexport ersetzt kein Systemabbild.
4. Aktuell installierte Version und Cloudadresse notieren. Der veröffentlichte
   Softwarestand beweist nicht, dass er bereits auf dem Hallengerät installiert ist.
5. Falls erforderlich das [Trainingssystem aktualisieren](ANWENDUNGSUPDATES.md).
6. Über den Wartungsdesktop kontrolliert herunterfahren, dann die Versorgung trennen.

Zugänge und Gerätesekret bleiben im Passwortmanager beziehungsweise in geschützten
Sicherungen. Keine neue Cloud-Datenbank anlegen und keinen zweiten Pi gleichzeitig
mit derselben Geräteidentität betreiben. Das Reservegerät bleibt außer Betrieb.

## 2. Anschließen

Montageort, Halterung, Schutz, Belüftung, Stromversorgung und Kabelführung mit den
Hallenverantwortlichen abstimmen; Montage- und Elektroarbeiten durch Fachpersonal.
Pi und Display zunächst zugänglich lassen.

1. Pi stromlos per Micro-HDMI/HDMI direkt mit dem vorgesehenen LG-Display verbinden.
   Die tatsächlich verwendeten Buchsen notieren.
2. Netzwerk anschließen beziehungsweise das vorbereitete Hallen-WLAN bereitstellen.
   Handy und Pi müssen sich lokal erreichen können; Gastnetz-Isolation verhindert das.
3. CC1101 nur stromlos anschließen oder umstecken. Die bestehende Verdrahtung
   beibehalten; das Modul benötigt 3,3 V, keine 5 V.
4. Display einschalten und den Pi-Eingang wählen, danach den Pi starten.
5. Kontrollieren, dass die Hallenanzeige selbstständig erscheint.

Beim Pi 5 erfolgt der Ton über **HDMI** oder eine ausdrücklich eingerichtete
andere Audioausgabe. Ein AUX-/Cinch-Eingang an einer Anlage ist kein Funkempfänger.

## 3. Netzwerk und vorhandene Einrichtung prüfen

Am Pi mit `hostname -I` die aktuelle Adresse ermitteln. Alte Prüfstandsadressen
sind keine verbindlichen Hallenadressen. Eine feste DHCP-Zuordnung erleichtert
später die Bedienung.

1. Am Handy `http://PI-IP:8080/control` öffnen; `PI-IP` durch die aktuelle Adresse ersetzen.
2. Mit der bestehenden Admin-PIN anmelden.
3. Unter **System & Kiosk** Hostname und angebotene lokale Links kontrollieren.
4. Unter **Verein & Erscheinungsbild**, **Halle** und **Trainingszeiten** die
   vorhandenen Angaben prüfen. Keine leere Grundeinrichtung darüber speichern.
5. Für Dalum Beckenlänge 16,6667 m, Beckenbreite für Spiele 8 m und tatsächliche
   Bahnzahl prüfen. Die Anlage misst die Stellung des Hubbodens nicht.
6. Bei Bedarf unter **Netzwerk & Systemdienste** das Hallen-WLAN verbinden.
7. Bei fehlendem bekannten WLAN mit dem geschützten Pi-Hotspot verbinden und
   `http://10.42.0.1:8080/control` öffnen. Das individuelle Hotspot-Kennwort
   steht im PIN-geschützten Wartungsfenster unter **Notfall-WLAN**. Dafür am
   angeschlossenen Pi mit einer USB-Maus die Bahnhofsuhr länger als zwei Sekunden
   gedrückt halten und die Admin-PIN eingeben. Das Fenster zeigt auch Hotspot-Name
   und Notfall-Adresse. Es ist über die lokale Pi-Anzeige erreichbar.

Am Router werden keine Internet-Portfreigaben für den Pi eingerichtet. Online
verbindet er sich ausgehend per HTTPS. Die vorhandene Cloudadresse und Kopplung
übernehmen; online **Verbunden** und einen bestätigten Datenabgleich prüfen.

### Hotspot bei Bedarf sofort aktivieren

Im PIN-geschützten Bereich **Notfall-WLAN** aktiviert **Hotspot jetzt aktivieren**
den Hotspot unmittelbar. Dabei wird die WLAN-Verbindung zum Hallennetz getrennt;
den Hinweis vorher bestätigen. Gespeicherte Zugänge und Kennwort bleiben erhalten.
Nach der Aktivierung mit dem Handy dem angezeigten Hotspot beitreten und die
Notfall-Adresse öffnen. Am Handy über **Admin → Netzwerk & Systemdienste → WLANs suchen** wieder
mit dem Hallen-WLAN verbinden.

## 4. Bild, Ton und Displaysteuerung

1. Unter **System & Kiosk → Bildausgabe** erkanntes Display, Anschluss und
   tatsächliche Auflösung prüfen. Es werden vom Display angebotene Modi verwendet.
2. **Bild kalibrieren** öffnen. Alle vier Eckmarkierungen müssen sichtbar sein;
   Sicherheitsränder speichern und das Testbild wieder schließen.
3. Im Displaymenü HDMI-CEC aktivieren; genaue Menübezeichnung am Gerät nachsehen.
4. Ein/Standby praktisch testen und während einer Umschaltung die Rückmeldung abwarten.
   Den Status nur bestätigen, wenn das Display tatsächlich entsprechend reagiert hat.
5. **Ton testen** und einen Trainingsklang am Hallendisplay hören. Ausgang,
   Stummschaltung und Displaylautstärke prüfen; ein Ton am Handy genügt nicht.
6. Weitere HDMI-Quellen einzeln prüfen. Die Standbyautomatik darf einen anderen
   Eingang nicht übernehmen. Bei unklarer Eingangserkennung Automatik vorerst deaktivieren.

Details: [Displayerkennung](DISPLAY_AUTO.md), [Standby-Eingangskontrolle](input-guard.md).

## 5. Neustart und Übergabe

Die Technik kann lokal prüfen:

```bash
systemctl is-active trainingsanzeige.service trainingsanzeige-kiosk.service
systemctl is-active trainingsanzeige-backup.timer
systemctl is-enabled trainingsanzeige-miracast-recovery.service
curl -fsS http://127.0.0.1:8080/api/v1/health
```

Anwendung, Kiosk und Sicherungstimer sollen laufen; die Healthprüfung meldet
`status: ok`. Der Recovery-Dienst muss eingerichtet sein. Ein erfolgreich
beendeter Einmaldienst muss nicht dauerhaft `active` sein. Der Miracast-Empfänger
läuft nur während der Spiegelung; ein aktiver Syncdienst beweist keine Cloudkopplung.

Nach einem kontrollierten Neustart Anzeige, Ton und Steuerung erneut prüfen.
Eine zuvor laufende Trainingseinheit muss pausiert wiederhergestellt werden.
Anschließend die gesamte [Abnahmeliste](ABNAHME.md) am Montageort durchführen,
Ergebnisse dokumentieren und Trainer- sowie Adminanleitung übergeben.

## Fehlerhilfe

| Problem | Prüfung |
| --- | --- |
| Lokale Seite fehlt | Strom, aktuelle IP, gleiches Netz, keine Client-Isolation |
| Nur Desktop sichtbar | Kioskdienst, automatische Desktopanmeldung und vorgesehenes Browserprofil |
| Kein Ton | HDMI-Ausgang, Displaylautstärke und Stummschaltung |
| Online getrennt | Internet, Uhrzeit, Cloudadresse und Syncprotokoll; lokal weiterarbeiten |
| CEC reagiert nicht | HDMI-Verbindung und CEC am Display; keine feste `/dev/cec0`-Zuordnung erzwingen |
| Funk reagiert falsch | Empfängerstatus und Senderzuordnung unter Admin → Funktaster |

Weitere Schritte stehen im [Adminhandbuch](ADMIN-HANDBUCH.md).
