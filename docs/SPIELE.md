# WFD Games mit vier Funktastern

Unter **Aktiv** öffnet die zusätzliche Pille **Spiele** die Spielauswahl für Trainer und Administratoren. Während eines geladenen Trainings ist sie ausgeblendet und erscheint nach dem Beenden wieder. Ein Training blockiert auch direkte Spielaufrufe. Die Spiele benötigen keinen weiteren PIN.

## Aktualisierung und Highscores

Eine nach einem Update noch geöffnete ältere App kann die alte Kennung des Reaktionsduells senden. Das startet kein Schwimmrennen: Die App fordert verständlich zum Neuladen und zur Wahl von WFD-Sprint samt Strecke auf. Neue Oberflächen vergleichen zusätzlich die Spielregel-Revision und bieten bei einer abweichenden Auswahl **App aktualisieren** an. Laufende Trainings, Spiele und Timer werden nicht automatisch durch ein Neuladen unterbrochen.

Unter **Admin → Spiele → Highscores verwalten** können Administratoren einen einzelnen Spieler-Eintrag oder **Alle Highscores löschen** wählen, jeweils nach Bestätigung. Andere Spieler-Einträge bleiben beim einzelnen Löschen erhalten. Die ursprünglichen Rennergebnisse und deren Platzierungen bleiben als Historie gespeichert; die gelöschten Einträge werden nicht mehr in Bestenlisten gewertet. Neue Rennen können neue Highscores erzeugen. Trainer dürfen nicht löschen. Die Verwaltung zeigt zunächst 50 Einträge; weitere lassen sich nachladen. Änderungen erscheinen sofort, lokal und online.

Die Grafik ist je Spielmodus unterschiedlich: WFD-Run zeigt farbige Wege zu den Zielbuzzern, WFD-Cup die noch übrigen virtuellen Becher und Sprint separate Rennfelder mit festen Buzzerfarben und Platzierungen. Die Sprint-Grafik behauptet keinen Streckenfortschritt: Ohne zusätzliche Sensoren wird nur der Zielanschlag erkannt. Die Gestaltung verwendet keine dauerhaft laufenden Dekorationsanimationen.

### Hallenbad Dalum

Laut Hallenangaben beträgt das Becken 16,66 × 8 Meter. Der Hubboden ermöglicht eine variable Wassertiefe von 0,90 bis 2,00 Metern. Die Spiele verwenden Länge und Breite für die Streckenberechnung; sie erkennen oder steuern den Hubboden nicht. Die tatsächliche Tiefe muss vor Ort geprüft werden. Die Beckenbreite wird unter **Admin → Spiele** auf **8 m** eingestellt; die Länge bleibt in der Halleneinrichtung bearbeitbar.

## Einmal einrichten

1. Unter **Admin → Spiele** die Beckenbreite eingeben. Die Länge stammt aus der Halleneinrichtung.
2. Vier unterschiedliche aktive Funktaster den vier Beckenseiten zuweisen. Die Skizze zeigt den Blick von den Startblöcken ins Becken: unten **Startblockseite**, oben **Gegenüberliegende Seite**, rechts **Rechts**, links **Links**. Stationsnummern und bisher gespeicherte Buzzerzuordnungen bleiben unverändert. Individuelle Beschriftungen sind weiterhin möglich.
3. Für WFD-Run die Buzzer mittig an jeder Beckenseite aufstellen. Für WFD-Cup Buzzer 1/3 an die Startblöcke und 2/4 gegenüber stellen (Team 1 links: 1/2, Team 2 rechts: 3/4). Für den Sprint die verwendeten Buzzer nebeneinander an die Startblockseite setzen, je einer pro Schwimmbahn/Person. Spieler 1 verwendet Buzzer 1 usw. Beschriftung und Farbe müssen zum tatsächlichen Buzzer passen. Die ursprünglichen Zuordnungen zu Trainingsbahnen bleiben erhalten.
4. Maße und Positionen bestätigen und speichern. Ohne geladenes Training oder Spiel **Buzzer 30 Sekunden testen** starten und jede Taste einmal drücken. Die erkannte Station wird angezeigt.
5. Lautstärke, Sprachansagen und die vier Spielklänge einstellen. Eigene Klänge aus der vorhandenen Klangbibliothek können ausgewählt werden.

Speichern übernimmt die bestätigten Einstellungen unmittelbar in Beckenskizze und Spielbereitschaft, lokal wie online. Rückmeldungen stehen direkt bei der jeweiligen Aktion. Veraltete Statusantworten setzen gespeicherte Werte nicht zurück. Spielkarten und ihre Eingabefelder wechseln sofort; Bestenlisten laden unabhängig im Hintergrund, ohne Eingaben oder Fokus zu ersetzen.

Der Aktivierungsschalter blendet die Spiele bei Trainern und Administratoren aus. Während eines geladenen Spiels erfordert das Deaktivieren die Bestätigung, dass der laufende Durchgang beendet wird.

## WFD-Run

Zwei Spieler oder Gruppen starten an den gegenüberliegenden Stationen 1 und 3. Für jeden Durchlauf wird eine neue Route geplant; das erste Zielpaar unterscheidet sich vom vorherigen Spiel. Diagonalwege zu benachbarten Stationen wechseln mit Begegnungsstrecken zur gegenüberliegenden Seite. Die Ziele bleiben um 180 Grad gespiegelt: Beide Teams schwimmen in jeder Etappe dieselbe Strecke und damit auch insgesamt gleich weit. Diagonalen haben die Länge `sqrt((Beckenlänge / 2)² + (Beckenbreite / 2)²)`, Begegnungsstrecken je nach Ausgangsseite Beckenlänge oder -breite. Etappen- und Gesamtstrecke werden aus dem tatsächlichen Kurs berechnet.

**Begegnungsstrecken nur bei freiem, von der Aufsicht freigegebenem Becken nutzen. Rechts aneinander vorbeischwimmen, keine Gegenkurse auf derselben Linie.** Die TV-Pfeile zeigen getrennte Passierseiten und der Hinweis „Rechts aneinander vorbei“ steht bei diesen Etappen auf der Anzeige. Das System erkennt weder andere Schwimmer noch Kollisionen. Der Countdown ist keine Sicherheitsfreigabe. Eine Etappenwiederholung behält dieselben Ziele und Entfernungen. Variable Kurse werden nicht mit alten Diagonal-Kursen oder anderen Streckenprofilen in derselben Bestenliste verglichen.

Der schnellere Anschlag erhält einen Punkt. Innerhalb von 0,01 Sekunden erhalten beide einen Punkt. Nach beiden Anschlägen folgen die nächste Zielansage und der Countdown. Standard sind sechs Etappen; möglich sind drei bis zwölf. Bei Punktgleichheit entscheidet die summierte Schwimmzeit.

Nach 90 Sekunden ohne beide Ziele pausiert das Spiel. Für eine Wiederholung müssen beide Spieler an die Startpositionen der aktuellen Etappe zurückkehren. Falsche Buzzer verändern die Wertung nicht.

## WFD-Cup

Für WFD-Cup stehen **zwei Buzzer an der Startblockseite und zwei gegenüber**:

- Links: Buzzer **1 an den Startblöcken**, **2 gegenüber** (Team 1).
- Rechts: Buzzer **3 an den Startblöcken**, **4 gegenüber** (Team 2).

Beide Teams starten an der Startblockseite und pendeln über ganze Beckenlängen zwischen ihren beiden Buzzern. Jeder korrekte Anschlag räumt einen virtuellen Becher ab und schaltet auf die andere eigene Station um. Beide Teams schwimmen dieselbe Gesamtstrecke. Das zuerst fertige Team gewinnt; nahe Zieleinläufe werden anhand der Empfangszeitstempel verglichen. Die Buzzerkennungen und Farben bleiben erhalten; die geänderte Aufstellung gilt nur für Cup. Frühere diagonale Cup-Ergebnisse werden nicht mit diesem Parcours in derselben Bestenliste verglichen.

Sechs Becher sind voreingestellt; alternativ sind zehn möglich. Einzelduell und Staffel funktionieren mit denselben Regeln. Bei einer Staffel erfolgt die Übergabe am jeweils erreichten Ziel. Echte Becher oder Bälle werden nicht benötigt.

## WFD-Sprint

Zwei bis vier Personen schwimmen auf getrennten Bahnen ein einzelnes Rennen. Wählbar sind **1 Beckenlänge**, **2 Beckenlängen**, **50 m** und **100 m**. 50/100 m werden nur angenommen, wenn sie ganzen Beckenlängen entsprechen (bis 5 cm Toleranz für gerundete Hallenmaße). In Dalum sind 50 m drei und 100 m sechs Beckenlängen. Strecke, Längenzahl und Startseite erscheinen nach dem Laden vor dem Start.

Die Zielbuzzer stehen nebeneinander an der **Startblockseite**, einer pro Person. Bei ungerader Längenzahl wird **gegenüber**, sonst an der Startblockseite gestartet. Der Trainer startet alle gemeinsam nach Ansage und 3–2–1/GO. Erst nach der gesamten Strecke den eigenen Buzzer drücken; Zwischenwenden werden nicht gebuzzert. Die Uhren starten gemeinsam, jeder Zielbuzzer stoppt nur die eigene Uhr. Gleiche angezeigte Hundertstel erhalten denselben Platz. Erst nach allen Zieleinläufen wird das Ergebnis gespeichert; **Revanche** lädt dieselben Personen und dieselbe Strecke für einen neuen gemeinsamen Start. Frühere Reaktionsduell-Ergebnisse bleiben im Archiv erhalten.

Das ist Trainingszeitmessung anhand vollständiger Funktelegramme, keine wettkampfzertifizierte Anschlagmatte. Streckenerfüllung und Frühstarts müssen die Aufsicht prüfen: Ein alleiniger Zielbuzzer erkennt keine Wenden und keine Frühstarts am anderen Beckenende. Vor GO gedrückte Zielbuzzer zählen nicht. Pause hält die offenen Uhren an; nach 15 Minuten ohne vollständigen Zieleinlauf pausiert das Rennen und muss neu gestartet oder beendet werden. Unvollständige Rennen erhalten kein Ergebnis. Nur unter Aufsicht und mit geeigneter Wassertiefe und freien Bahnen verwenden; der Countdown ist keine Freigabe für einen Kopfsprung.

## Anzeige, Musik und Ergebnisse

### Bereitschaft und Autostart

Bei WFD-Run und WFD-Cup drückt jeder Spieler/Team seinen eigenen Startbuzzer.
Erst wenn beide „Bereit“ melden und der Kiosk Bild und Spielklänge bestätigt hat,
beginnen drei Sekunden bis zur **vollständigen Startsequenz**. Die verbleibenden
Sekunden laufen lokal flüssig auf TV und Handy. Zusätzliche Tastendrücke setzen
die Frist nicht zurück. Danach folgen die gewohnten Zielansagen und der ganze
Startklang bis null/GO; die drei Sekunden sind noch nicht der Schwimmstart.
„Autostart abbrechen“ setzt beide Bereitschaftsmeldungen zurück. Anschließend
beide Startbuzzer erneut drücken oder manuell starten. Spiel beenden verwirft
auch einen anstehenden Autostart. Dies ist keine Sicherheitsfreigabe der Aufsicht.

Beim Sprint bleibt der gemeinsame Trainerstart bestehen: Die Zielbuzzer stehen
je nach Streckenlänge am anderen Ende als die startenden Schwimmer und belegen
deshalb keine Bereitschaft am Start. Etappenwiederholung und Folgerunden behalten
ihren bisherigen Ablauf.

### Sieger klar erkennen

TV und Handy zeigen nach abgeschlossener Wertung groß **„Gewonnen!“**, einen
Pokal sowie Siegername und das entscheidende Ergebnis. Die betreffende Karte
ist zusätzlich goldfarben markiert; die Buzzerfarben bleiben unverändert.
Bei Gleichstand werden alle gemeinsamen Sieger unter **„Unentschieden!“** genannt.
Run zeigt Punkte und die Gesamtzeit aller Etappen, Cup abgeräumte Becher und Zeit,
Sprint die bestätigte Zielzeit/Platzierung. Die UI übernimmt immer das Urteil
des Pi und berechnet keinen eigenen Sieger aus Reihenfolge oder Punkten allein.
Während eines laufenden oder noch ausgewerteten Rennens erscheint kein Sieger.

### TV-Fernansicht

Die großen Zahlen entsprechen weiterhin denselben vier gespeicherten Stationen.
Auf dem TV sitzen die Buzzer bei Run an den vier Beckenrändern, bei Cup zu zweit an jeder Stirnseite. Die kurzen
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

Der vollständige Startklang endet bei null/GO, statt dort erst zu beginnen. Eigene Dateien werden um ihre tatsächliche Dauer vor dem gemeinsamen Start eingeplant. Zuerst kommen die Zielansagen, dann mit Abstand der Startklang; bei langen Dateien verlängert sich die Vorbereitungszeit entsprechend. Zu spät eingetroffene Startdateien werden nicht verkürzt nachgespielt. Die Browser-Ausgabepuffer werden über den gemeldeten Audio-Ausgabezeitstempel berücksichtigt, soweit verfügbar. Ein eigener Startklang erhält keine zusätzlich darübergelegten Countdown-Pieptöne.

Die deutschen Ansagen sind vollständige Sätze (48 kHz/16-Bit-Mono). Alle Sprachsegmente laufen mit Abstand nacheinander. Die Siegansage folgt erst nach dem vollständigen Siegklang. Verständlichkeit und akustischen Nachhall vor Ort prüfen; das Trainingssystem verändert die Musiklautstärke dafür nicht.

### Spielklänge auf dem Display testen

Unter **Admin → Spiele → Spiele & Buzzer** gibt es bei Start, Treffer,
falschem Buzzer und Sieg jeweils **Auf Anzeige anhören**. Die Vorschau nutzt
die gerade gewählte Datei beziehungsweise den Spielklang und den eingestellten
Spielpegel – auch vor dem Speichern. Sie verändert keine Einstellungen oder
Spielstände. „Kein Ton“ deaktiviert die Vorschau des betreffenden Signals.

Das Display muss eingeschaltet und der Kiosk verbunden sein. Während eines
geladenen Trainings/Spiels, IPTV oder Miracast ist die Vorschau gesperrt.
Der Testbutton bleibt bis zum tatsächlichen Audio-Ende einschließlich
kurzem Ausgabepuffer gesperrt. Die Rückmeldung bestätigt die vollständige
Software-Wiedergabe der lokalen Hallenanzeige; sie bestätigt nicht die Lautstärke
oder Stummschaltung am TV. Eigene Dateien werden nicht gekürzt. Vorschauen haben
1 s Bereitschaftsvorlauf und 250 ms Nachlauf. Während geladener
Spiele und Trainings hält derselbe Bereitschaftspuffer den Audiokanal offen;
beim Wechsel zur Uhr wird er freigegeben. Reale Start- und Countdown-Zeitpunkte
werden nicht verschoben.
Online funktioniert der Test nur live und wird nicht für später vorgemerkt.

#### HDMI-Ton und Abnahme

Der Kiosk hält den Audiokanal während geladener Spiele und Trainings sowie
Klangtests mit einem leisen Bereitschaftssignal offen. Das hilft Displays, die
kurze Signale sonst am Anfang verschlucken. Der Releasebuilder baut Pi- und
Onlineoberfläche frisch; die Prüfung erfolgt am tatsächlich erzeugten Paket.

Der feste, symmetrische Bereitschaftspegel liegt bei -60,2 dBFS (32/32768,
23,4 Hz). Er wird nicht vom Spiel-/Trainingslautstärkeregler verstärkt und
überlagert sich bei mehreren Vorschauen desselben Audiokontexts nicht mehrfach.
Ein kleiner Schleifenpuffer ersetzt zusätzliche Prozesse und Abfragetimer.
Er läuft nur während einer geladenen Einheit oder eines Klangtests, nicht
dauerhaft bei der Uhr, und sendet keine CEC-Befehle. Auf anderen Displays
und Tonanlagen die vollständige Wiedergabe und Störgeräuschfreiheit erneut
prüfen; die Bestätigung im Adminmenü allein belegt keine physische Tonausgabe.

Eine geschlossene Handyansicht beendet das Spiel nicht. **Spiel beenden** oder **Zur Spielauswahl** gibt die Anzeige wieder frei: Bei weiterlaufender Musik erscheint die Musikansicht, sonst die Uhr mit Standby-Countdown. Ergebnisse schließen nach zwei Minuten automatisch; eine unbediente Vorbereitung oder Pause endet nach zehn Minuten.

Ergebnisse liegen auf dem Raspberry und werden für die angemeldete Online-App gespiegelt. Bestenlisten gruppieren nach Spiel, Rundenzahl, Teilnehmerzahl und Beckenmaßen, beim Sprint zusätzlich nach Schwimmstrecke/Längenzahl. Die Sprint-Bestenliste enthält alle vollständigen Zielzeiten, nicht nur die Siegerzeit. Gespeichert werden höchstens 500 Durchgänge. Admins können einzelne Highscores oder die gesamte Highscore-Liste leeren; die ursprünglichen Rennergebnisse bleiben erhalten. Anwendungssicherungen enthalten Spieleinstellungen, Ergebnisse und gelöschte Highscore-Markierungen, jedoch kein automatisch fortzusetzendes Spiel.

Nach einem Neustart wird ein unterbrochenes Spiel nicht fortgesetzt. Anwendungs- und Systemupdates sind während eines geladenen Spiels gesperrt.
