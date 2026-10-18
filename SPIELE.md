# WFD Games mit vier Funktastern

Unter **Aktiv** öffnet die zusätzliche Pille **Spiele** die Spielauswahl für Trainer und Administratoren. Ein geladenes Training muss vor dem Laden eines Spiels beendet werden. Die Spiele benötigen keinen weiteren PIN.

### Hallenbad Dalum

Laut Hallenangaben beträgt das Becken 16,66 × 8 Meter. Der Hubboden ermöglicht eine variable Wassertiefe von 0,90 bis 2,00 Metern. Die Spiele verwenden Länge und Breite für die Streckenberechnung; sie erkennen oder steuern den Hubboden nicht. Die tatsächliche Tiefe muss vor Ort geprüft werden. Die Beckenbreite wird unter **Admin → Spiele** auf **8 m** eingestellt; die Länge bleibt in der Halleneinrichtung bearbeitbar.

## Einmal einrichten

1. Unter **Admin → Spiele** die Beckenbreite eingeben. Die Länge stammt aus der Halleneinrichtung.
2. Vier unterschiedliche aktive Funktaster den vier Beckenseiten zuweisen. Die Skizze zeigt den Blick von den Startblöcken ins Becken: unten **Startblockseite**, oben **Gegenüberliegende Seite**, rechts **Rechts**, links **Links**. Stationsnummern und bisher gespeicherte Buzzerzuordnungen bleiben unverändert. Individuelle Beschriftungen sind weiterhin möglich.
3. Für WFD-Run/Cup die Buzzer jeweils mittig an der entsprechenden Beckenseite aufstellen. Für den Sprint die verwendeten Buzzer nebeneinander an die Startblockseite setzen, je einer pro Schwimmbahn/Person. Spieler 1 verwendet Buzzer 1 usw. Beschriftung und Farbe müssen zum tatsächlichen Buzzer passen. Die ursprünglichen Zuordnungen zu Trainingsbahnen bleiben erhalten.
4. Maße und Positionen bestätigen und speichern. Ohne geladenes Training oder Spiel **Buzzer 30 Sekunden testen** starten und jede Taste einmal drücken. Die erkannte Station wird angezeigt.
5. Lautstärke, Sprachansagen und die vier Spielklänge einstellen. Eigene Klänge aus der vorhandenen Klangbibliothek können ausgewählt werden.

Ab Version **2.12.1** übernimmt Speichern die bestätigten Einstellungen unmittelbar in Beckenskizze und Spielbereitschaft, lokal wie online. Rückmeldungen stehen direkt bei der jeweiligen Aktion. Veraltete Statusantworten setzen gespeicherte Werte nicht zurück. Spielkarten und ihre Eingabefelder wechseln sofort; Bestenlisten laden unabhängig im Hintergrund, ohne Eingaben oder Fokus zu ersetzen.

Der Aktivierungsschalter blendet die Spiele bei Trainern und Administratoren aus. Während eines geladenen Spiels erfordert das Deaktivieren die Bestätigung, dass der laufende Durchgang beendet wird.

## WFD-Run

Zwei Spieler starten an den gegenüberliegenden Stationen 1 und 3. Nach der Zielansage und dem Countdown schwimmen sie jeweils zu einer benachbarten Station und drücken ihren Zielbuzzer. Die Ziele sind stets um 180 Grad gespiegelt. Beide schwimmen pro Etappe dieselbe direkte Strecke: `sqrt((Beckenlänge / 2)² + (Beckenbreite / 2)²)`. Gegenkurse zur gegenüberliegenden Beckenseite sind ausgeschlossen.

Der schnellere Anschlag erhält einen Punkt. Innerhalb von 0,01 Sekunden erhalten beide einen Punkt. Nach beiden Anschlägen folgen die nächste Zielansage und der Countdown. Standard sind sechs Etappen; möglich sind drei bis zwölf. Bei Punktgleichheit entscheidet die summierte Schwimmzeit.

Nach 90 Sekunden ohne beide Ziele pausiert das Spiel. Für eine Wiederholung müssen beide Spieler an die Startpositionen der aktuellen Etappe zurückkehren. Falsche Buzzer verändern die Wertung nicht.

## WFD-Cup

Team 1 pendelt zwischen Station 1 und 2, Team 2 zwischen Station 3 und 4. Jeder korrekte Anschlag räumt einen virtuellen Becher ab und schaltet auf die andere eigene Station um. Beide Teams schwimmen damit dieselbe Gesamtstrecke. Das zuerst fertige Team gewinnt; nahe Zieleinläufe werden anhand der Empfangszeitstempel verglichen.

Sechs Becher sind voreingestellt; alternativ sind zehn möglich. Einzelduell und Staffel funktionieren mit denselben Regeln. Bei einer Staffel erfolgt die Übergabe am jeweils erreichten Ziel. Echte Becher oder Bälle werden nicht benötigt.

## WFD-Sprint (ab 2.12.2 statt Reaktionsduell)

Zwei bis vier Personen schwimmen auf getrennten Bahnen ein einzelnes Rennen. Wählbar sind **1 Beckenlänge**, **2 Beckenlängen**, **50 m** und **100 m**. 50/100 m werden nur angenommen, wenn sie ganzen Beckenlängen entsprechen (bis 5 cm Toleranz für gerundete Hallenmaße). In Dalum sind 50 m drei und 100 m sechs Beckenlängen. Strecke, Längenzahl und Startseite erscheinen nach dem Laden vor dem Start.

Die Zielbuzzer stehen nebeneinander an der **Startblockseite**, einer pro Person. Bei ungerader Längenzahl wird **gegenüber**, sonst an der Startblockseite gestartet. Der Trainer startet alle gemeinsam nach Ansage und 3–2–1/GO. Erst nach der gesamten Strecke den eigenen Buzzer drücken; Zwischenwenden werden nicht gebuzzert. Die Uhren starten gemeinsam, jeder Zielbuzzer stoppt nur die eigene Uhr. Gleiche angezeigte Hundertstel erhalten denselben Platz. Erst nach allen Zieleinläufen wird das Ergebnis gespeichert; **Revanche** lädt dieselben Personen und dieselbe Strecke für einen neuen gemeinsamen Start. Frühere Reaktionsduell-Ergebnisse bleiben im Archiv erhalten.

Das ist Trainingszeitmessung anhand vollständiger Funktelegramme, keine wettkampfzertifizierte Anschlagmatte. Streckenerfüllung und Frühstarts müssen die Aufsicht prüfen: Ein alleiniger Zielbuzzer erkennt keine Wenden und keine Frühstarts am anderen Beckenende. Vor GO gedrückte Zielbuzzer zählen nicht. Pause hält die offenen Uhren an; nach 15 Minuten ohne vollständigen Zieleinlauf pausiert das Rennen und muss neu gestartet oder beendet werden. Unvollständige Rennen erhalten kein Ergebnis. Nur unter Aufsicht und mit geeigneter Wassertiefe und freien Bahnen verwenden; der Countdown ist keine Freigabe für einen Kopfsprung.

## Anzeige, Musik und Ergebnisse

### TV-Fernansicht ab 2.12.2

Die großen Zahlen entsprechen weiterhin denselben vier gespeicherten Stationen.
Auf dem TV sitzen die Buzzer direkt auf den vier Beckenrändern. Die kurzen
Seitenbezeichnungen **Startblöcke**, **Gegenüber**, **Links** und **Rechts**
orientieren sich am Blick von den Startblöcken ins Becken. Zielnummer, Seite,
Zeit und Spielstand haben Vorrang vor Zusatzinformationen. Bei WFD-Cup steht
die Anzahl der übrigen Becher groß im Teamfeld; beim Sprint erscheinen
zwei oder vier gleich große Felder ohne Beckenskizze. Angezeigte Buzzerfarben
und Kennungen werden nicht geändert; die Ziffern passen ihren Kontrast an.

Eigene Beschriftungen, Erklärungen und Gesamtstrecken bleiben am Handy verfügbar.
Vor der Nutzung die Lesbarkeit aus ungefähr 20 m am tatsächlichen Display
prüfen, auch nach Änderungen an der Bildkalibrierung. Eine 4K-Auflösung allein
ersetzt diesen Test nicht. Zeitmessung, Wertung und Tonabläufe von Run und Cup bleiben unverändert.

Die Hallenanzeige bestätigt Bild- und Klangbereitschaft, bevor sich das Spiel starten lässt. Alle Sprachclips werden lokal vorgehalten. Die Lautstärke der Spielsignale und die Musiklautstärke sind getrennt einstellbar. Bestehende Bluetooth- oder Webradio-Wiedergabe kann weiterlaufen.

Eine geschlossene Handyansicht beendet das Spiel nicht. **Spiel beenden** oder **Zur Spielauswahl** gibt die Anzeige wieder frei: Bei weiterlaufender Musik erscheint die Musikansicht, sonst die Uhr mit Standby-Countdown. Ergebnisse schließen nach zwei Minuten automatisch; eine unbediente Vorbereitung oder Pause endet nach zehn Minuten.

Ergebnisse liegen auf dem Raspberry und werden für die angemeldete Online-App gespiegelt. Bestenlisten gruppieren nach Spiel, Rundenzahl, Teilnehmerzahl und Beckenmaßen, beim Sprint zusätzlich nach Schwimmstrecke/Längenzahl. Die Sprint-Bestenliste enthält alle vollständigen Zielzeiten, nicht nur die Siegerzeit. Gespeichert werden höchstens 500 Durchgänge. Admins können einzelne Ergebnisse oder alle Bestenlisten löschen. Anwendungssicherungen enthalten Spieleinstellungen und Ergebnisse, jedoch kein automatisch fortzusetzendes Spiel.

Nach einem Neustart wird ein unterbrochenes Spiel nicht fortgesetzt. Anwendungs- und Systemupdates sind während eines geladenen Spiels gesperrt.
