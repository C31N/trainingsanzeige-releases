# Trainingsanzeige – Installation und Updates

Öffentlicher Downloadkanal für die eigenständige Trainingsanzeige für Schwimmvereine.
Das Entwicklungsrepository ist separat und privat. Dieses Repository enthält
freigegebene Anwendungspakete einschließlich des darin benötigten Anwendungscodes,
und die freigegebenen Vereinsgrafiken und Trainingssounds. Private Gerätedaten,
PIN-Hashes und Zugangsschlüssel sind nicht enthalten. Die öffentlich bekannten
Start-PINs für neue Anlagen stehen unter [Standardausstattung](STANDARD-AUSSTATTUNG.md).

## Medien und Trainingssignale

Ab Version 2.11.51 enthalten die Installationspakete die aktuelle SVG-/PNG-Grafik
und 14 Sounds der Testanlage. Sie sind zusätzlich unter `standard-media/`
einzeln verfügbar. Bestehende Bibliotheken werden nicht überschrieben.
Siehe [Trainingssignale einstellen](TRAININGSSIGNALE.md).

## WFD Games und IPTV

**Update 2.12.7:** Vollständige Wiedergabe kurzer Spielklänge und eigener
Dateien in der Vorschau. Das echte Audio-Ende mit kurzem Ausgabepuffer gibt
den Testbutton wieder frei – kein vorzeitiger Abschluss per Timer. Auch
Tonbibliothek und allgemeiner Testton sind abgesichert. Geladene Spiele und
Trainings halten den Audioausgang bereit; die Leerlaufuhr tut das nicht.

**Update 2.12.6:** Kurze DNS-/TLS-Verbindungsfehler werden vor einer Rücksetzung
begrenzt erneut versucht. Schreibbefehle mit unklarem Ausgang werden nicht blind
wiederholt. Die Online-Gesundheitsprüfung erhält drei Versuche; nach einem
Rollback zeigt die App den verursachenden Schritt an. Enthält die Spielklang-
Vorschau aus 2.12.5. Installation weiterhin manuell im Update-Menü.

**Update 2.12.5:** Unter Admin → Spiele lassen sich Start-, Treffer-, Fehler-
und Siegklang mit „Auf Anzeige anhören“ am Display testen. Aktuelle Auswahl
und Spielpegel gelten auch ohne Speichern. Wiedergabestart und Fehler werden
direkt am Button bestätigt. Nur live, bei eingeschaltetem Display und ohne
geladenes Training/Spiel beziehungsweise IPTV/Miracast.

**Update 2.12.4:** Sofortige IPTV-Senderanzeige ohne Rücksprünge, stabiler
Lautstärkeregler und HDMI-Hauptpegel auf 100 % (0 dB, keine Verstärkung).
Musik und IPTV haben getrennte Regler. WFD-Cup nutzt zwei Buzzer an jeder
Stirnseite: 1/3 Startblöcke, 2/4 gegenüber, ganze Beckenlängen.
Das Löschen der Highscore-Liste funktioniert auch über die Online-App,
einschließlich älterer Anfragen mit leerer Liste. Rennergebnisse bleiben erhalten.

**Update 2.12.3:** Klare Aktualisierungsmeldung für noch geöffnete alte
Spielauswahlen, statt technischer Validierungsfehler. Admins können unter
**Spiele → Highscores verwalten** einzelne Einträge oder alle Highscores löschen;
die Rennergebnisse bleiben erhalten. Neue Modusgrafiken zeigen Schwimmwege bei
Run, virtuelle Becher bei Cup und Rennfelder mit Platzierungen beim Sprint.

**Update 2.12.2:** Neue TV-Fernansicht mit großen Zielnummern, Seiten, Zeiten
und Spielständen. Bei Run/Cup liegen die Buzzer direkt an den Beckenrändern.
Neu statt Reaktionsduell: **WFD-Sprint** für zwei bis vier Personen mit 1/2
Beckenlängen oder 50/100 m, gemeinsamem Countdown, eigenem Zielbuzzer,
Platzierung, Zielzeiten und Revanche. Der Sprint zeigt große Spielerfelder.
Run-/Cup-Regeln und gespeicherte Zuordnungen bleiben erhalten. Lesbarkeit aus
ungefähr 20 m bitte in der Halle am tatsächlichen Display bestätigen.

**Update 2.12.1:** Buzzerzuordnungen und Beckenskizze aktualisieren sich direkt
nach dem Speichern. Die Skizze richtet sich nach den Startblöcken (unten), der
gegenüberliegenden Seite (oben), links und rechts. Spiel-Eingabefelder erscheinen
ohne auf Bestenlisten zu warten. Rückmeldungen im Adminmenü stehen an der
jeweiligen Aktion, nicht mehr gesammelt weit oben.

Ab **2.12.2** stehen **WFD-Run**, **WFD-Cup** und **WFD-Sprint** unter
**Aktiv → Spiele** für Trainer und Administratoren bereit. Vor dem ersten Spiel
unter **Admin → Spiele** Beckenbreite und vier Buzzer einrichten und prüfen.
Dort lassen sich Spiele auch deaktivieren, Farben und Klänge ändern sowie
Bestenlisten verwalten. Ein geladenes Training muss vorher beendet werden.
Die reale Prüfung von Buzzerpositionen und HDMI-Spielton bleibt erforderlich.

**IPTV** öffnet sich am normalen Anmeldeschirm über den separaten **Start-PIN
654322**. Dieser änderbare Startwert ist kein fest eingebauter Zugang und gibt
keine Trainer-/Adminrechte. Unter **Admin → Zugang & PINs** kann er geändert
werden. Senderauswahl, Lautstärke und Beenden erfolgen am Handy; Bild und Ton
laufen im Vollbild über den Raspberry und HDMI auf dem Display.

Unter **Admin → IPTV** Sender samt Logos pflegen, eigene Sender ergänzen und
die tägliche Aktualisierung der Standard-M3U-Liste aktivieren. Regionalsender
wie **ems TV** sind ebenfalls enthalten. Lokale Änderungen bleiben bei einem
Listenabgleich erhalten. Geladene Trainings und Spiele blockieren IPTV;
Online-Steuerung setzt einen aktuell verbundenen Pi voraus.

- [Spiele: Einrichtung und Regeln](SPIELE.md)
- [IPTV: Zugang, Sender und Bedienung](IPTV.md)

## Eine vollständig neue Anlage einrichten

Die [Schritt-für-Schritt-Anleitung für Raspberry Pi, LG-Display und Webserver](NEUINSTALLATION-LG-UND-CLOUD.md)
beginnt mit einem leeren Raspberry Pi, einer neuen Webinstallation und einer neuen Datenbank.

## Vorhandenen Raspberry Pi aktualisieren

In der Trainingssteuerung als Administrator anmelden und **Sicherung & Updates →
Trainingssystem → Version prüfen** öffnen. Installation mit Admin-PIN
bestätigen. Der Pi benötigt ausgehenden HTTPS-Zugriff auf GitHub und dessen
Release-Downloads; eine eingehende SSH-Freigabe oder ein GitHub-Konto ist nicht nötig.

Der Prüfschlüssel muss unabhängig vom Downloadkanal auf dem Gerät eingerichtet
sein. Pakete werden anhand einer Ed25519-Signatur und einer SHA-256-Prüfsumme geprüft.
Während eines geladenen Trainings oder Spiels ist die Installation gesperrt. Vor dem Wechsel
werden Anwendung und Daten gesichert; ein fehlgeschlagener Start löst eine Rückkehr
zur vorherigen Version aus.
Gekoppelte Pi- und Online-App werden gemeinsam aktualisiert; Sicherungen des
Anwendungsupdaters bleiben auf zwei vorherige Stände begrenzt.

## Dateien eines Releases

- `trainingsanzeige.tar.gz`: Anwendung, lokales Frontend und Betriebsdateien.
- `trainingsanzeige.json`: Version, Hinweise und SHA-256-Prüfsumme.
- `trainingsanzeige.sig`: abgetrennte Ed25519-Signatur des Manifests.
- `trainingsanzeige-web.json`: geprüfte Dateien der gekoppelten Online-App.
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
