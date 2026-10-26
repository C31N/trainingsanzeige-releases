# IPTV: Fernsehen auf der Hallenanzeige

## Zugang und Bedienung

1. Die normale Trainingsanzeige-App am Handy öffnen.
2. Am PIN-Anmeldeschirm den **Start-PIN 654322** eingeben. Wurde der PIN
   geändert, stattdessen den aktuell eingerichteten IPTV-PIN verwenden.
3. Einen Sender auswählen. Der Raspberry Pi weckt bei Bedarf das Display,
   wählt seinen HDMI-Eingang und startet den Stream im Vollbild mit HDMI-Ton.
4. Über die Handyansicht Sender wechseln, Lautstärke ändern oder die Wiedergabe
   beenden. Die Wiedergabe läuft beim Schließen des Handy-Browsers weiter.
5. Nach dem Beenden erscheinen wieder Uhr und automatischer Standby-Countdown.

Der IPTV-PIN gewährt ausschließlich IPTV-Zugriff, keine Trainingsdaten und
keine Trainer- oder Adminrechte. Die Prüfung erfolgt gegen den geschützten
gespeicherten PIN; der Startwert ist keine fest einprogrammierte Hintertür.
Administratoren ändern ihn unter **Admin → Zugang & PINs → IPTV-PIN**.

## Sender einrichten

Unter **Admin → IPTV** können Administratoren die Funktion ein- oder ausschalten,
Sender sichtbar oder unsichtbar stellen, Namen, Reihenfolge und Logos bearbeiten
sowie eigene HTTP-/HTTPS-Streams ergänzen. Nach Änderungen speichern.

Grundbestand ist die [German-TV-M3U-Senderliste](https://raw.githubusercontent.com/josxha/german-tv-m3u/main/german-tv.m3u).
Regionalsender wie **ems TV**, NDR Niedersachsen HD, h1 und TV38 ergänzen sie.
**Senderliste täglich aktualisieren** aktiviert den automatischen Abgleich;
**Jetzt aktualisieren** startet ihn sofort. Lokale Anpassungen bleiben erhalten.
Die erste Inbetriebnahme lädt die Liste automatisch. Schlägt der Abruf fehl oder ist die Liste ungültig, bleibt die letzte gültige
Senderliste bestehen.

Der Handyzugang sendet Senderkennungen, keine frei eingegebenen Playerbefehle.
Die Streamadressen werden ausschließlich in der administrierten Liste gepflegt.

## Zusammenspiel mit anderen Modi

- Ein geladenes Training oder Spiel blockiert den IPTV-Start.
- Läuft Musik oder Miracast, muss der Wechsel bestätigt werden; der vorherige
  Modus wird kontrolliert beendet.
- Online sind Start und Steuerung nur bei einer aktuellen Live-Verbindung zum
  Pi möglich. Befehle werden niemals für eine spätere Ausführung vorgemerkt.
- Bei einem Playerfehler wird die normale Anzeige wiederhergestellt.

## Wenn Bild oder Ton fehlen

Der gewählte Sender wird sofort angezeigt. Bestätigte Live-Zustände
ersetzen die Ladeanzeige ohne Neuladen; verspätete alte Antworten setzen die
Auswahl nicht zurück. Schnelle Lautstärkeänderungen übernehmen den letzten Wert.
Während des Senderstarts wird eine Änderung bis zur Wiedergabebereitschaft gehalten.

Die Lautstärkeregler übertragen auch bei durchgehendem Ziehen regelmäßig den
neuesten Wert. Noch nicht verarbeitete, aufeinanderfolgende Pegelwerte werden
zusammengefasst; Wiedergabe- und Quellenbefehle bleiben erhalten.

Ein Senderwechsel verwendet den laufenden Player weiter, statt Decoder,
HDMI-Ausgabe und Audiostream vollständig neu zu starten. Die Anzeige meldet
„Live“ erst bei bestätigter Wiedergabe des neuen Senders. Ein weiterer Sender
oder „Beenden“ unterbricht das Warten auf einen nicht erreichbaren Stream.
Die Anlaufzeit der jeweiligen Senderquelle und notwendige Wechsel der
Bildfrequenz können weiterhin einen kurzen Moment beanspruchen.

Der ausgewählte HDMI-Hauptausgang arbeitet mit 100 % (0 dB, keine Verstärkung).
Die Lautstärke wird pro Quelle geregelt; Musik beeinflusst IPTV nicht.
Die eigene Lautstärke beziehungsweise Stummschaltung des Fernsehers bleibt
zusätzlich wirksam. HDMI-Reparatur hebt keine Stummschaltung auf und verändert
keine USB-/anderen Audioausgänge.

Zuerst einen anderen Sender testen und den Fehlertext in der App prüfen.
Einzelne öffentlich erreichbare Streams können ausfallen oder regional gesperrt
sein. Für HDMI-Ton müssen der richtige Pi-Audioausgang und die Lautstärke am
Display stimmen. Die Playerdiagnose findet sich im IPTV-/Systembereich.

Netflix, Disney+ und andere geschützte Dienste gehören nicht zu dieser
M3U-Funktion; DRM-Schutz wird nicht umgangen. Senderlogos und Streams verbleiben
bei den jeweiligen Rechteinhabern.
