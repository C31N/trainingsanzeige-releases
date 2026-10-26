# Vereinslogo als PNG oder SVG

## Saubere Konturen auf großen Anzeigen

SVG-Logos werden zentral mit 2048 × 2048 Pixeln und transparentem Hintergrund
gerendert. App, TV, Startabdeckung, Desktop und Bootlogo verwenden dieselbe
Ausgabe. Eine größere Rasterdatei allein kann kantige Vektorpfade nicht glätten:
Die bekannten polygonisierten Dalumer Logo-Konturen erhalten deshalb echte
Kurven; der Ring erhält exakte elliptische Bögen. Schildspitzen bleiben erhalten.

Bestehende Anlagen übernehmen ausschließlich die anhand ihrer Prüfsummen
erkannten alten Konturen beim nächsten Anwendungsstart. Eigene Grafiken,
Schriftänderungen, Farben und unveränderte Originaldateien bleiben erhalten.
Die frühere Generation bleibt wiederherstellbar; Fehler lassen das bisherige
Logo aktiv. Neue, fremde Logos werden nicht automatisch nachgezeichnet oder
weichgezeichnet. Für kleine PNG-Originale ist weiterhin eine hochwertige
SVG-Quelle vorzuziehen; fehlende Bilddetails werden nicht künstlich erfunden.

Im Adminbereich sind **Verein & Erscheinungsbild**, **Halle** und **Trainingszeiten** getrennte Punkte. Grafiken finden Sie unter **Verein & Erscheinungsbild → Vereinsdaten & Grafiken bearbeiten**.

1. Unter **SVG-Quelle & Texte bearbeiten** eine PNG- oder SVG-Datei auswählen (maximal 5 MB).
2. Die Vorschau prüfen. Das bisherige Logo bleibt bis zur Übernahme aktiv.
3. Bei SVG lassen sich einfache Texte, Farbe, Schriftgröße, Schriftart und Position bearbeiten. Nach Änderungen zuerst **Vorschau aktualisieren** drücken.
4. **Überall übernehmen** aktiviert dieselbe PNG-Ausgabe in App, Hallenanzeige, Desktop und für den nächsten Bootvorgang. Ein automatischer Neustart erfolgt nicht.

Die SVG-Quelle behält echte Texte. **Ursprüngliche SVG herunterladen** liefert die unveränderte hochgeladene Datei; **Aktuelle SVG herunterladen** enthält die übernommenen Textänderungen. Die vorhandenen PNG-Downloads bleiben verfügbar. Formen, Pfade und strukturierte Textspannen bearbeiten Sie in einem externen SVG-Editor und laden die Datei anschließend erneut hoch.

Die Schriftfamilien des Imports bleiben erhalten. Auf dem Raspberry ersetzt Liberation Sans eine nicht installierte Arial-Schrift. Alternativ stehen 23 lokal installierte Schriftfamilien zur Auswahl. Die Vorschau stammt vom Raspberry und zeigt damit die tatsächlich verwendete Schrift.

Online muss der Pi zum Bearbeiten verbunden sein. Bestätigte Quelldateien können auch bei getrenntem Pi heruntergeladen werden. Bei gleichzeitigem Bearbeiten wird eine veraltete Vorschau nicht still übernommen: Einstellungen neu öffnen und die Änderung erneut prüfen.

SVG-Dateien benötigen eine `viewBox`. Skripte, Animationen, eingebettetes HTML, externe Bilder/Schriften und andere nicht unterstützte SVG-Funktionen werden mit einer Meldung abgewiesen. Es werden keine Elemente still entfernt. Bei einem Renderfehler bleibt das vorherige Logo aktiv.

## Installation und Sicherung

Der Pi benötigt `librsvg2-bin`, `fonts-liberation`, `fonts-urw-base35`, `fonts-dejavu-core`, `fonts-lato`, `fonts-noto-core` und `fonts-croscore`. Das Installationsskript richtet diese Pakete ein; `sudo bash /opt/trainingsanzeige/ops/install-svg-renderer.sh` prüft bestehende Installationen. Ohne SVG-Renderer funktioniert PNG weiter.

JSON-Sicherungen ab Format 9 enthalten Original, bearbeitete SVG und PNG. Ältere Sicherungen bleiben lesbar und verändern die vorhandene Grafik nicht. Zusätzlich sichert der lokale Sicherungsdienst den Branding-Ordner. Frühere übernommene Grafikversionen bleiben dort erhalten; nicht übernommene Vorschauen verfallen nach einem Tag.
## Schriftarten und Textformatierung

Im Logo-Texteditor stehen 23 lokal installierte Schriftfamilien zur Verfügung,
darunter Lato, Noto Sans/Serif, Liberation Sans/Serif/Mono, Nimbus und DejaVu.
Über **Fett**, **Kursiv** und **Unterstrichen** lässt sich jedes einfache
Textelement einzeln formatieren. Ein blauer Schalter bedeutet „aktiv“.
Unveränderte importierte Formatierungen bleiben erhalten.

Nach Änderungen zuerst **Vorschau aktualisieren**, danach **Überall übernehmen**
wählen. Handy, Online-App, Hallenanzeige und Bootbild verwenden dasselbe auf dem
Pi erzeugte Bild. Nicht jede dekorative Schrift besitzt eigene Fett-/Kursivdateien;
die verbindliche Darstellung ist daher immer die gerenderte Vorschau.
Die ursprüngliche SVG bleibt unverändert herunterladbar.
