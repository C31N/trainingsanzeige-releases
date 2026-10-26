# Bildschirm spiegeln

Am normalen Anmeldeschirm den eingerichteten Präsentations-PIN eingeben.
Öffentlicher Startwert: **13698642**. Die Spiegelung bleibt experimentell und
muss mit den tatsächlich verwendeten Quellgeräten abgenommen werden. Windows: **Win + K**;
Samsung: **Smart View**. Den im Display angezeigten Gerätenamen auswählen.
Der Präsentations-PIN ist nicht der gegebenenfalls angezeigte Kopplungscode.

## Bild und Ton einstellen

Unter **Admin → Bildschirmspiegelung** lassen sich die Werte an den Raspberry anpassen:

- **720p · 30 Hz** ist die verzögerungsarme Grundeinstellung.
- **Full-HD oder 60 Hz** erst nach einem Test auf der tatsächlich eingesetzten Hardware verwenden.
- **Videodecoder automatisch** prüft die H.264-Hardwaredecodierung mit einem kurzen Teststream.
  Schlägt dieser fehl, wird Softwaredecodierung verwendet. „Software“ erzwingt diese dauerhaft.
- **Empfangspuffer** und **Wiedergabepuffer**: jeweils 100 ms empfohlen, einstellbar von 20 bis 500 ms.
  Kleinere Werte können bei schwachem WLAN Bild- und Tonaussetzer verursachen.
  Größere Werte erhöhen die Verzögerung.

Speichern gilt erst für die **nächste Verbindung**, nicht mitten in einer Wiedergabe.
Unter **Tonausgabe** ist „Systemstandard · wie Webradio“ voreingestellt. Damit verwendet
Miracast denselben Ausgang wie das Webradio. Der Pi 5 hat keinen analogen Klinkenausgang.
Alternativ lassen sich **HDMI** für die
Display-Lautsprecher oder **Analog** für Kopfhörer/Klinke wählen. Bei mehreren passenden
Ausgängen muss der gewünschte als Systemstandard festgelegt sein. Ein fehlender oder
mehrdeutiger Ausgang wird als Fehler gemeldet, statt den Ton unbemerkt umzuleiten.

Der Pi gibt Bild und Ton mit gemeinsamer Zeitbasis aus. „Bildschirm wird gespiegelt“ erscheint
erst nach dem ersten tatsächlich wiedergegebenen Bild. Ohne erstes Bild wird abgebrochen
und WLAN sowie Trainingsanzeige werden wiederhergestellt.

## Prüfung nach einem Hardwarewechsel

„Hardware prüfen“ ausführen. Danach mit Windows und Samsung jeweils ein Video mit deutlich
sichtbarer Lippenbewegung abspielen und mindestens 15 Minuten testen. Es darf kein wachsender
Rückstand entstehen. Ziel ist ein Ton-/Bildversatz unter etwa 100 ms; dies ist keine Garantie
für die gesamte Verzögerung zwischen Quellgerät und Display. WLAN und Sender beeinflussen sie ebenfalls.

Während Miracast verwendet wird, steht der einzige WLAN-Adapter nicht für die normale
Trainingssteuerung zur Verfügung. Nach dem Beenden wird das gespeicherte WLAN wiederhergestellt.

## Beenden und Betriebsgrenzen

Vor dem Start ein geladenes Training oder Spiel beenden. Die Spiegelung nutzt
den WLAN-Adapter für eine direkte Verbindung; Hallen-WLAN und Onlinebedienung
können währenddessen ausfallen. Beim Beenden werden WLAN und Kiosk wiederhergestellt.
Eine Anmeldung zum Spiegeln vergibt keine Trainer- oder Adminrechte.

Am Quellgerät die Verbindung trennen oder den vorgesehenen Beenden-Weg verwenden.
Die Funktaste **Fernseher ein / Standby** beendet die Spiegelung ebenfalls und
führt zuerst zur Uhr. Erst der nächste Druck schaltet in Standby. Bei fehlender
Rückkehr Netzwerk und Kiosk durch die lokale Administration prüfen lassen.

Eine erfolgreiche Hardwareprüfung allein bestätigt noch keine stabile Kopplung
mit jedem Windows- oder Samsung-Gerät. Belegte WLAN-Adapter, Hotspotbetrieb und
das tatsächliche Funknetz beeinflussen den Empfang. Die Prüfung am Standort bleibt
offen, bis sie in der [Abnahme](ABNAHME.md) dokumentiert ist.
