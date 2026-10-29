# Musik über Bluetooth und Webradio

## Zugang

Am Anmeldeschirm den eingerichteten Musik-PIN eingeben. Öffentlicher Startwert:
**654321**. Der Zugang öffnet die Musik- und Displaysteuerung, keine Trainingspläne
oder Administration. Unter [Start-PINs](STANDARD-AUSSTATTUNG.md) stehen alle Zugänge.

## Bluetooth verwenden

1. Musiksteuerung öffnen und **Neues Gerät koppeln** wählen.
2. Am Smartphone Bluetooth öffnen, nach dem angezeigten Namen suchen und koppeln.
3. Die gewünschte Audioquelle am Smartphone starten und Lautstärke prüfen.
4. Bereits bekannte Geräte bei Bedarf bewusst aus der Liste verbinden.
5. Zum Abschluss die Quelle trennen beziehungsweise **Audiomodus beenden** wählen.

Ein gespeichertes Gerät wird nicht allein durch seine Nähe automatisch verbunden.
Das Schließen des Handy-Browsers beendet die Wiedergabe nicht. Nach einem
Pi-Wechsel kann wegen der neuen Bluetooth-Adresse erneutes Koppeln nötig sein.

## Webradio und Lautstärke

Einen der eingerichteten Sender wählen und dessen Wiedergabe starten. Webradio
benötigt Internet am Pi. Bluetooth benötigt für die lokale Übertragung keine
Internetverbindung; die verwendete Musik-App kann selbst Internet benötigen.

Die Musiklautstärke ist von Trainingssignalen, Spielen, Lernvideo und IPTV getrennt.
Musik wird bei Trainingssignalen oder Lernvideos nicht automatisch abgesenkt.
Die Lautstärke des Displays und dessen Stummschaltung wirken zusätzlich.
Am Pi 5 erfolgt die Ausgabe normalerweise über HDMI.

## Einstellungen und Zusammenspiel

Unter **Admin → Bluetooth & Webradio** Namen, Ausgabegerät und freigegebene
Webradioadressen pflegen. Der Musikzugang kann diese Einstellungen nicht ändern.
Der Lernzugang bietet ebenfalls begrenzte Musiksteuerung; sein Videoton hat einen
eigenen Regler. IPTV und Spiegelung haben eigene Wechselbedingungen.

Die Funktaste **Fernseher ein / Standby** beendet zunächst die Musik und weitere
Anzeigeinhalte und führt zur Uhr. Erst der nächste Druck schaltet in Standby.
Onlinebefehle benötigen einen verbundenen Pi und werden nicht für später vorgemerkt.

Wenn kein Ton kommt: tatsächliche Quelle, Verbindung, richtigen Audioausgang,
App-Lautstärke und Displaylautstärke prüfen. Anschließend Trainingssignal und Musik
getrennt testen. Die physische Hörprüfung gehört zur [Abnahme](ABNAHME.md).

## Bluetooth-Musik mit kurzen Aussetzern

Ab 2.20.8 beendet die Anlage die Sichtbarkeit für neue Kopplungen, sobald ein
Telefon verbunden ist. Die bestehende Musikverbindung bleibt erhalten.
„Koppeln“ öffnet bei bestehender Verbindung ein zweiminütiges Kopplungsfenster.
Ohne verbundenes Telefon ist die Musikfunktion weiterhin sichtbar.

Bei Aussetzern Telefon nahe am Pi testen und die Audioausgabe prüfen. Einträge
„Unexpected continuation frame“ im Kernelprotokoll weisen auf fehlerhafte
Bluetooth-Paketverarbeitung hin. Sie beweisen allein keine bestimmte Ursache.
Die Hallenabnahme enthält deshalb einen Hörtest über mehrere Minuten; eine
verbundene App ist kein Nachweis störungsfreien Tons.

## Lange Songtitel und Interpreten

Ab 2.20.9 laufen Titel und Interpretennamen in der Musikansicht langsam hin und
zurück, wenn die Zeile zu schmal ist. Kurze Angaben bleiben stehen. Die Anzeige
passt sich an Handy, Hallenbildschirm und Größenänderungen an. Bei aktivierter
Betriebssystem-Einstellung „Bewegung reduzieren“ bleibt der Text ruhig und wird
umgebrochen. Die Funktion zeigt Titelinformationen, keine Liedtexte.
