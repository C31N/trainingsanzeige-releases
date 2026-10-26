# Automatische Displayerkennung

Der Raspberry erkennt das tatsächlich angeschlossene HDMI-Display anhand gültiger
EDID-Daten. 60/59,94 Hz haben Vorrang: zuerst 3840 × 2160, dann 1920 × 1080.
Ist beides nicht verfügbar, wird der gemeldete bevorzugte Modus verwendet.
4K mit 30 Hz wird nicht anstelle von verfügbarem Full HD mit 60 Hz gewählt.
Für Bahnzeiten und Zeiger hat flüssige Darstellung Vorrang.

Unter **Admin → System & Kiosk → Bildausgabe** stehen erkanntes Display,
tatsächliche Auflösung, Bildfrequenz und Automatikmeldung. Diese Informationen
stehen auch in der Online-App. `system/info` enthält ergänzend
`display_hardware` mit Modell, Anschluss, Gerätekennung, Modus, Zustand und Meldung.

## Neues Display anschließen

1. HDMI direkt anschließen, Display einschalten und den Pi-Eingang wählen.
2. Am Display HDMI-CEC/SIMPLINK einschalten und den Empfang von Standby erlauben.
3. Der Pi erkennt den Anschluss, wählt einen angebotenen Modus und ordnet
   HDMI-Ton sowie CEC neu zu. Dafür ist normalerweise kein Einrichtungsassistent nötig.

Ein bereits gesunder Modus wird nicht wiederholt gesetzt. Eine bei EDID-losem
Boot veraltete Grafik-Modusliste wird einmal pro Display/EDID und Pi-Start neu
eingelesen. Ein dafür nötiger grafischer Neustart wartet auf echten Leerlauf;
Training, Spiel, Lernen, Musik, IPTV, Miracast und Kalibrierung sperren ihn.
Der Trainingsprozess wird dafür nicht neu gestartet. Das Wiederherstellen der
grafischen Sitzung erfolgt höchstens einmal, nicht als Neustartschleife.

Fehlende Displaydaten im Standby löschen weder Profile noch lösen sie Weckbefehle
aus. Eine bestätigte andere HDMI-Quelle wird nicht übernommen. Bei mehreren
gleichzeitig angeschlossenen, noch nicht zugeordneten Displays wird zunächst
keine automatische Auswahl getroffen.

## Bildränder und Ton

Jedes erkannte Display erhält ein eigenes Randprofil. Neue Displays beginnen bei
0 % zusätzlicher Einrückung. Änderungen unter **Bild kalibrieren** bleiben für
dieses Display gespeichert und werden beim Wiederanschließen übernommen.
Alte globale Ränder bleiben als `legacy-global` gesichert; ohne frühere EDID lässt
sich ihre Zugehörigkeit nicht nachträglich zuverlässig rekonstruieren.
Displays ohne eindeutige Seriennummer und mit gleicher Geräteidentität teilen
ein Profil. Profile sind in SQLite- und JSON-Sicherungen enthalten.

HDMI-Ton folgt dem erkannten Pi-HDMI-Anschluss. Eine ausdrücklich gewählte
USB-/andere Tonausgabe wird nicht überschrieben. Musik- und Signalregler bleiben
getrennt; der HDMI-Hauptpegel wird weiterhin nicht über 100 % verstärkt.
Alte physische Standby-/Ein-Bestätigungen gelten nicht für ein anderes Display.

## Wenn 4K/60 Hz fehlt

Es wird kein unbestätigter Modus erzwungen. Zunächst bleibt Full HD/60 Hz aktiv.
Am LG gegebenenfalls **UHD Deep Color / HDMI-Format / 6G** für den genutzten Eingang
prüfen sowie ein geeignetes HDMI-Kabel verwenden. Nach geänderten Displaydaten
wird erneut erkannt; falls nötig erfolgt eine einmalige Neuerkennung im Leerlauf.

LG-eigene Einblendungen, Startlogo, SIMPLINK-Freigabe oder Energiesymbole sind keine
Pi-Bildinhalte. Diese Menüpunkte kann der vorhandene HDMI-/CEC-Zugang nicht
zuverlässig automatisch konfigurieren. Die Funktion behauptet daher keine
vollautomatische Einrichtung solcher Herstellermenüs.

Boot- und Desktopkonfiguration vor Änderungen sichern. Das alte automatisch
erzeugte Ein-Ausgang-Kanshi-Profil wird gesichert und entfernt; abweichende
eigene Desktopprofile bleiben unberührt. Ein vorhandenes eigenes Profil kann
die Automatik weiterhin übersteuern und muss gegebenenfalls manuell angepasst werden.
