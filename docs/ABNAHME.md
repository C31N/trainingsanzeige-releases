# Abnahme der Trainingsanzeige in der Schwimmhalle

**Status: am endgültigen Hallengerät noch durchzuführen.** Softwaretests bestätigen
keine Montage, Funkreichweite, hörbare Ausgabe oder HDMI-CEC-Funktion am Standort.
Alle Felder erst nach der tatsächlichen Prüfung ausfüllen.

Gerät / Seriennummer: ____________________  Display: ____________________

Installierte Pi-/Onlineversion: ____________________  Datum: ____________________

Prüfende und verantwortliche Person: __________________________________________

## Montage und Grundbetrieb

- [ ] Montageort, Halterung, Schutz, Belüftung, Kabelführung und Stromversorgung freigegeben.
- [ ] Kiosk und Steuerung starten nach Neustart selbstständig; alle vier Bildränder sichtbar.
- [ ] Vereinsprofil, Zeitzone, Beckenmaße, Bahnzahl und Tasterposition stimmen.
- [ ] Hallennetz und lokale Bedienung am Beckenrand funktionieren; Adresse dokumentiert.
- [ ] Alle benötigten Zugänge funktionieren mit ihren vorgesehenen Rechten; öffentliche Start-PINs vor Internetfreigabe geändert.
- [ ] Bestehende Daten und Cloud-Kopplung erhalten; kein zweites Gerät mit gleicher Identität aktiv.

## Training und Archiv

- [ ] Vorbereiteten Termin laden: noch keine Bahn startet allein durch das Laden.
- [ ] Jede benötigte Bahn einzeln und gemeinsam starten, pausieren, fortsetzen, vor/zurückschalten und zurücksetzen.
- [ ] Distanzbestätigung, Abgangszeiten und Satzpausen mit einem Testplan prüfen.
- [ ] Training beenden und genau einen vollständigen Archiveintrag prüfen.
- [ ] Direktplan ohne Termin beenden: Eintrag unter „Ohne Termin“ sichtbar und erneut planbar.
- [ ] Kontrollierter Neustart stellt ein laufendes Training pausiert wieder her.

## Fernsehtaste, Quellen und Ton

- [ ] Training starten, Musik zuschalten, Lerninhalt darüber zeigen; Fernsehtaste drücken: genau einmal archiviert, Inhalte beendet, gewählte Uhr sichtbar, Display bleibt an.
- [ ] Dasselbe mit Direktplan ohne Termin prüfen.
- [ ] Während langsamen Medienendes mehrfach drücken: kein vorzeitiger Standby; Abschluss oder Fehler in Funkdiagnose erkennbar.
- [ ] Nächster Druck auf der Uhr: tatsächlicher Standby. Weiterer Druck: Display wacht auf.
- [ ] Ein noch geladenes Training beim Aufwecken nicht allein durch das Einschalten verlieren.
- [ ] Bahnhofsuhr und Sekundenkreuz jeweils prüfen; Infotafel bei Rückkehr per Fernsehtaste pausiert.
- [ ] Anderen HDMI-Eingang wählen: Pi übernimmt oder beendet diese Quelle nicht automatisch.
- [ ] Trainingsklänge, Musik, Spiel- und Quizton über den vorgesehenen Hallenausgang hörbar; Pegel getrennt und sofort stummschaltbar.
- [ ] Bluetooth koppeln, wiedergeben und trennen; Webradio und IPTV starten, wechseln und beenden.
- [ ] Spiegelung, sofern benötigt, mit vorgesehenen Quellgeräten prüfen; nach Beenden Hallen-WLAN und Kiosk wieder erreichbar.

## Funktaster, Lernen und Spiele

- [ ] Jede Bahn- und Trainerzuordnung aus den üblichen Hallenpositionen bei geschlossenem Gehäuse prüfen.
- [ ] Kurze Drücke, Halten und erneutes Drücken: je Betätigung genau eine passende Aktion.
- [ ] Zwei und alle verwendeten Buzzer gemeinsam prüfen; verlorene Drücke oder auffällige Verzögerung protokollieren.
- [ ] Lernvideo und Lernkarte über Training zeigen: Bahnzeiten und berechtigte Trainingsbefehle laufen weiter.
- [ ] Quiz bei geladenem Training gesperrt; letzte Erklärung bleibt sichtbar.
- [ ] Quiz für alle sechs Abzeichen per Handy und Buzzer beantworten; Runden 5/7/12/14/16/18, Rückmeldung und Auswertung prüfen.
- [ ] Jede Quizfarbe einzeln prüfen: erste Frage, direkt nach Fragenwechsel, nach einigen Sekunden Wartezeit und nach Zurückblättern. Jeweils nur ein kurzer Druck; sofort genau eine Antwort.
- [ ] Mit V2-Buzzern nach dem Fragenwechsel einen neuen Druck prüfen: keine zusätzliche Antwortsperre. Halten und Funkwiederholungen dürfen die nächste Frage nicht beantworten.
- [ ] In Administration → Funktaster → „Letzte Tastendrücke prüfen“ Ergebnis und Tastenzähler kontrollieren. Für einen Aussetzer Farbe, Fragenstand, Wartezeit und sichtbaren Diagnoseeintrag notieren. Ohne Eintrag Funkempfang und lokale Übergabe prüfen; nicht durch mehrfaches Drücken überdecken.
- [ ] Zwei Trainerfernbedienungen mit gleicher Funktion nacheinander verwenden: jeder neue Druck wirkt unabhängig vom Tastenzähler des anderen Senders.
- [ ] Spiele bei freiem Becken einrichten, Buzzerpositionen und reale Wassertiefe durch Aufsicht prüfen.

## Ausfall, Sicherung und Übergabe

- [ ] Internet unterbrechen: lokales Training läuft weiter; Wiederverbindung gleicht vorbereitete Änderungen ab.
- [ ] Ohne bekanntes WLAN geschützten Notfall-Hotspot erreichen; bei erneut verfügbarem gespeichertem WLAN automatische Rückkehr prüfen (Hotspot-Automatik eingeschaltet).
- [ ] Notfall-WLAN mit Name, Adresse und individuellem Kennwort erst nach Admin-PIN sichtbar; nach Schließen nicht mehr angezeigt.
- [ ] Hotspot direkt aktivieren: Bestätigung abbrechen verändert nichts; nach Bestätigung ist der Hotspot am Handy erreichbar. Bestehendes Kennwort bleibt gültig; Rückwechsel ins Hallen-WLAN funktioniert.
- [ ] Manuelles Standby und Infotafel-Einschaltzeiten auch nach Neustart prüfen.
- [ ] Täglichen Sicherungstimer und lesbare Sicherung kontrollieren.
- [ ] Export außerhalb des Pi ablegen und auf getrenntem Testsystem wiederherstellen.
- [ ] Mindestens vier Stunden Dauerbetrieb protokollieren; Anzeige, Uhrzeit, Funk und Ton beobachten.
- [ ] Trainer einweisen; aktuelle Anleitungen, Geräteadresse, Verantwortliche und Sicherungsort übergeben.

Nicht benötigte Zusatzfunktionen als „nicht verwendet“ mit Begründung markieren.
Für Fehler Zeitpunkt, Handlung, erwartetes Ergebnis und tatsächliches Ergebnis
notieren. Zugangsdaten separat im Passwortmanager verwahren.

Offene Punkte / Maßnahmen: ___________________________________________________

Freigabe durch / Datum: ______________________________________________________

## Neue Funkverwaltung ab 2.20.5 – am Standort zu prüfen

- [ ] Trainerfernbedienung mit vier Tasten gruppieren; Bahnbuzzer einzeln belassen; jede Funktion unverändert prüfen.
- [ ] Mit geöffneter Empfangsdiagnose den ersten roten Tastendruck bei bereits sichtbarer Quizfrage prüfen.
- [ ] Alle Buzzer schnell nacheinander in Training, Lernen, Quiz und Spielen prüfen; keine fehlenden oder doppelten Aktionen.
- [ ] Signalstärke, erfasste Dauer und Impulsdetails ansehen; Empfangsfrequenz nicht mit gemessener Sendefrequenz verwechseln.
- [ ] Bei geladenem und pausiertem Training sowie aktivem Quiz/Spiel bleiben Sendetest und Lernsender gesperrt.
- [ ] Im Ruhezustand ein geeignetes Testsignal senden, tatsächlichen Gegenempfang und Rückkehr zum Buzzerempfang prüfen.
- [ ] Lokale und Cloud-Diagnose einschließlich Verbindungsabbruch prüfen.
- [ ] Gesicherte Fernbedienungsgruppen und Signalaufzeichnungen nach Wiederherstellung vergleichen.

## Technische Vorprüfung am Bestandsgerät – 28. Oktober 2026

Mit Version 2.20.5 wurden Empfangsdiagnose und Gruppenverwaltung lokal sowie
über die produktive Cloud geprüft. Eine vorübergehende Testgruppe ließ sich
anlegen und wieder auflösen. Ungültige Sendefrequenzen wurden abgewiesen.
Ein einzelnes kurzes EV1527-Testtelegramm wurde vom vorhandenen Pi angenommen;
der Funkdienst kehrte ohne Fehler zum Empfang zurück. Ein externer Gegenempfang
wurde dabei **nicht** nachgewiesen. Die vorhandenen 56 Trainingspläne und acht
Tastenzuordnungen blieben erhalten.

Die Hallenprüfungen oben, insbesondere reale Tastendrücke aus den Bahnpositionen
und der Gegenempfang eines Sendetests, bleiben offen. Die Vorprüfung ersetzt
keine Abnahme in der Schwimmhalle.


## Vorabprüfung am vorhandenen Gerät

Am 29.10.2026 mit Pi- und Cloudversion 2.20.13 wurde der Hotspot tatsächlich
aktiviert. Die Netzwerküberwachung startete nach rund zwei Minuten einen
Verbindungsversuch und meldete um 18:55:01 Uhr die automatische Rückkehr ins
gespeicherte WLAN (`saved_network_restored`). Der unabhängige Rückschalttimer
war noch nicht ausgeführt und wurde danach abgeschaltet. Die Hauptdienste
blieben aktiv. Dies ersetzt die Prüfung im endgültigen Hallennetz nicht;
die Standortprüfungen oben bleiben offen.


## LAN-Betrieb ab 2.20.14 – Hardwareprüfung offen

- [ ] LAN-Adresse und Internet prüfen, erst dann LAN-Betrieb aktivieren.
- [ ] Nach Neustart LAN automatisch verbunden, normales Pi-WLAN ausgeschaltet.
- [ ] Kabelverlust und Internetausfall trotz Kabel: Notfall-Hotspot erreichbar.
- [ ] Nach Rückkehr des LAN-Internets Hotspot beendet, WLAN wieder ausgeschaltet.
- [ ] Spiegelung schaltet WLAN ein; LAN und Cloud bleiben verbunden.
- [ ] Ende und Abbruch der Spiegelung stellen die Netzwerkautomatik wieder her.
- [ ] Bluetooth, Training und erste/schnelle Buzzerdrücke bleiben funktionsfähig.

Diese Hardwareprüfungen sind nicht durch Softwaretests oder frühere WLAN-Prüfungen abgenommen.


## Trainingsabläufe und Anmeldung – Update 2.20.33

Die frühere Online-Anmeldestörung ist historisch nicht nachgewiesen. Die
verfügbaren letzten 300 Anwendungslogzeilen deckten den gemeldeten Zeitraum
nicht ab; das Synchronisationsprotokoll enthielt keine Einträge. Ein aktueller
Anmeldeversuch war erfolgreich. Daraus wird keine rückwirkende Fehlerursache
abgeleitet. Die neue Fehlerbehandlung wird mit gezielten Ausfällen geprüft.
Browserdiagnosen speichern höchstens 30 Einträge mit Zeitpunkt, festem
Verarbeitungsschritt und Status im Sitzungsspeicher (`connection-diagnostics`).
PINs, Anfrageinhalte, Cookies und Sitzungsschlüssel werden nicht protokolliert.

Nach der späteren, selbst durchgeführten Installation vor Ort offen:

- [ ] Erste und mittlere Bahn ausblenden; alle verbleibenden realen Buzzer prüfen.
- [ ] Hinzugefügte Bahn und archivierten eingefrorenen Fortschritt kontrollieren.
- [ ] Pause zwischen Übungen und nach letzter Übung auf dem Fernseher abwarten.
- [ ] Einzelstart und Alle starten mit unterschiedlichen eigenen Klängen hören:
      Der ganze Startklang endet am sichtbaren Zeitstart.
- [ ] Automatische Abgänge, Countdown, Stumm, Pause und Fortsetzen prüfen.
- [ ] Online-Anmeldung mit Hallennetz und neuem Sitzungsaufbau kontrollieren.

Das Update wird veröffentlicht, aber nicht automatisch auf dem Hallen-Pi
installiert. Die Hardwareprüfung wird erst nach tatsächlicher Durchführung
abgehakt.


## Zugang & PINs und Nutzerprotokoll – 2.20.34

Die Veröffentlichung installiert dieses Update nicht auf dem Hallen-Pi.
Nach der späteren manuellen Installation bleiben diese Standortprüfungen offen:

- [ ] Alle sieben Zugangspillen lokal und online öffnen. Bereits geänderte PINs
      bleiben gültig; bei Bedarf einmalig bestätigen.
- [ ] Eine Anzeige verschwindet nach 30 Sekunden, beim Schließen, beim Verlassen
      und beim Abmelden. Bei getrenntem Pi ist keine Online-PIN-Anzeige möglich.
- [ ] PIN-Änderung, Wiederholungsprüfung und Zugangsrechte kontrollieren.
- [ ] Anmeldung, Menüwechsel, Medienauswahl und Änderung erscheinen unter dem
      tatsächlichen Zugang; PIN-Ziffern stehen nicht im Protokoll.
- [ ] Protokollabgleich und letzte Übertragung lokal und online vergleichen.
- [ ] Erste und schnelle reale Buzzerdrücke während geöffneter Protokollansicht
      prüfen; Empfang und Trainingsablauf bleiben unmittelbar bedienbar.

Softwaretests verwenden isolierte Datenbanken und öffentliche Test-PINs.
Sie ersetzen weder eine Bestandsdatensicherung noch die Standortprüfung.


## Die Eule & das Schwimmen – 2.20.36

Die Veröffentlichung installiert weder Anwendung noch Medien auf dem Hallen-Pi.
Softwareprüfung und Medienprüfung erfolgen mit isolierten Testdaten.
Nach der späteren manuellen Installation vor Ort offen:

- [ ] Anwendung und Online-App mindestens 2.20.36; Medienstand
      `swim-eule-20261112-1` mit 409 Inhalten vollständig offline verfügbar.
- [ ] Eulen-Bereich lokal und online öffnen; fünf Phasen, Basis-Check, Blaue Bahn,
      Detailblick und alle Druckvorlagen erreichbar.
- [ ] Kinderauftrag, Originalbild und Video am Hallenfernseher lesbar; Ton und
      deutsche Untertitel prüfen. Eine tatsächliche Hörprüfung bleibt offen.
- [ ] Phasenfolge starten; Filmende hält, Weiter/Zurück und Beenden funktionieren.
- [ ] Echte erste und schnelle Trainer-Tastendrücke prüfen; Bahn-Buzzer lösen
      keine Bewertung aus und behalten bei überlagertem Training ihre Funktion.
- [ ] Fernsehtaste sowie Wechsel von IPTV/Spiegelung und Sendesperren prüfen.
- [ ] Lokale Wiedergabe ohne Internet und nach Neustart prüfen; eigene Lernfolgen
      sowie ältere Lerninhalte, Abzeichen und Quiz sind weiter vorhanden.
