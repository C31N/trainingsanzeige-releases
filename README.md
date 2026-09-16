# Trainingsanzeige – Installation und Updates

Öffentlicher Downloadkanal für die eigenständige Trainingsanzeige für Schwimmvereine.
Das Entwicklungsrepository ist separat und privat. Dieses Repository enthält
freigegebene Anwendungspakete einschließlich des darin benötigten Anwendungscodes,
aber keine Vereinsdaten, PINs oder Zugangsdaten.

## Eine vollständig neue Anlage einrichten

Die [Schritt-für-Schritt-Anleitung für Raspberry Pi, LG-Display und Webserver](NEUINSTALLATION-LG-UND-CLOUD.md)
beginnt mit einem leeren Raspberry Pi, einer neuen Webinstallation und einer neuen Datenbank.

## Vorhandenen Raspberry Pi aktualisieren

In der Trainingssteuerung als Administrator anmelden und **Sicherung & Updates →
Trainingssoftware → Neue Version prüfen** öffnen. Installation mit Admin-PIN
bestätigen. Der Pi benötigt ausgehenden HTTPS-Zugriff auf GitHub und dessen
Release-Downloads; eine eingehende SSH-Freigabe oder ein GitHub-Konto ist nicht nötig.

Der Prüfschlüssel muss unabhängig vom Downloadkanal auf dem Gerät eingerichtet
sein. Pakete werden anhand einer Ed25519-Signatur und einer SHA-256-Prüfsumme geprüft.
Während eines geladenen Trainings ist die Installation gesperrt. Vor dem Wechsel
werden Anwendung und Daten gesichert; ein fehlgeschlagener Start löst eine Rückkehr
zur vorherigen Version aus.

## Dateien eines Releases

- `trainingsanzeige.tar.gz`: Anwendung, lokales Frontend und Betriebsdateien.
- `trainingsanzeige.json`: Version, Hinweise und SHA-256-Prüfsumme.
- `trainingsanzeige.sig`: abgetrennte Ed25519-Signatur des Manifests.
- `INSTALLATION.md`: Installationsanleitung für eine neue Anlage.
- `ANWENDUNGSUPDATES.md`: Update- und Wiederherstellungsverfahren.

Ein Releasepaket ist kein vollständiges Raspberry-Pi-Betriebssystemimage.
Neue Anlagen benötigen Raspberry Pi OS/Debian, eine gesonderte Erstinstallation
und eine Prüfung der Stromversorgung, Montage und Displaysteuerung vor Ort.
Installationen und Updates nur außerhalb des Trainings durchführen und die
Stromversorgung währenddessen nicht unterbrechen.

## Sicherheit

Keine PINs, Kennwörter, personenbezogenen Trainingsdaten oder privaten Schlüssel
in öffentliche Issues hochladen. Die automatische Updatefunktion ersetzt weder
eine externe Datensicherung noch die technische Abnahme in der jeweiligen Halle.
