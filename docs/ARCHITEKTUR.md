# Architektur und Datenfluss

## Komponenten

```text
Handy / Tablet im Hallennetz ─── Raspberry Pi ─── HDMI ─── Hallendisplay
                                  │
                           FastAPI / Timer / Funk
                                  │
                         SQLite und private Medien
                                  │
                     ausgehende HTTPS-Synchronisierung
                                  │
                      eigene PHP-/MariaDB-Online-App
```

Der Pi ist die Zeit- und Zustandsquelle. Die lokale Steuerung liegt unter
`/control`, der Kiosk unter `/display`, der Einrichtungsassistent unter `/setup`.
Browser zeigen bestätigte Zustände und interpolieren die Zeitdarstellung zwischen
Meldungen. Sie ersetzen die Timerlogik des Pi nicht. Funktaster wirken über den
lokalen Empfänger und dessen gespeicherte Zuordnungen.

## Training und Anzeige

Eine geladene Einheit enthält die Bahnpläne. Laden und Starten sind getrennte
Aktionen. Bahnen haben eigene Abschnitte, Wiederholungen, Pausen und Laufzustände;
gemeinsame Befehle werden zusammen angewandt. Nach einem Prozess- oder Stromausfall
wird eine zuvor laufende Einheit absichtlich pausiert wiederhergestellt.

Abgeschlossene Einheiten werden archiviert. Direkt geladene Pläne ohne Termin
bleiben unter „Ohne Termin“ erreichbar. Vorlagen und künftige Einheiten sind
von diesem Abschluss getrennt.

Training, Spiele und Medien besitzen definierte Wechselbedingungen. Lernkarten
und Videos dürfen Training überblenden; die Engine läuft weiter. Ein Quiz darf
geladene Trainingsbuzzer nicht gleichzeitig belegen. Das Schließen eines
Bedienbrowsers beendet die laufende Hallenanzeige nicht.

Die Funkfunktion „Fernseher ein / Standby“ schließt zunächst Inhalte, archiviert
ein geladenes Training und führt zur Uhr. Erst ein weiterer Druck auf der Uhr
führt zu Standby. Die physische Bestätigung erfolgt über den HDMI-/CEC-Weg.

## Zugänge und Cloud

Argon2-Hashes, getrennte Sitzungen und CSRF schützen schreibende Browserbefehle.
Die sieben Zugänge haben eigene Berechtigungen; die öffentlichen Erstwerte stehen
in der [Standardausstattung](STANDARD-AUSSTATTUNG.md). Der lokale Gerätedienst
besitzt eine eigene geschützte Identität. PINs und Gerätesekret sind verschiedene Dinge.

Die Online-App gehört zu genau einer Geräteinstallation und verwendet eine eigene
MariaDB. HMAC-Geräteanfragen tragen Zeitstempel und Einmal-Nonce. Der Pi baut die
Verbindung ausgehend auf; eine Internet-Portweiterleitung zum Pi ist nicht nötig.
Vorbereitende Änderungen werden abgeglichen. Direkte Gerätebefehle benötigen den
live erreichbaren Pi und werden nicht für eine spätere Ausführung vorgemerkt.

## Daten, Sicherungen und Updates

Lokale Daten liegen unter `/var/lib/trainingsanzeige`. Die Datenbank verwendet
SQLite im WAL-Modus. Sicherungswerkzeuge erstellen konsistente Datenbankstände
und zugehörige private Medien. Die große herunterladbare Lernbibliothek ist
getrennt; sie kann anhand ihres signierten Katalogs erneut geladen werden.

Anwendungsupdates verwenden ein gemeinsames Ed25519-signiertes Manifest mit
eigenen Prüfsummen für Pi- und Webpaket. Die gekoppelte Anlage aktualisiert beide
Seiten gemeinsam und hält Rückfallstände vor. Konfiguration, Identität und
bestehende PINs werden nicht aus dem öffentlichen Paket ersetzt. Betriebssystem-
updates bleiben ein gesonderter Vorgang.

Betrieb und Wiederherstellung: [Administration](ADMIN-HANDBUCH.md),
[Cloud](../cloud/README.md) und [Anwendungsupdates](ANWENDUNGSUPDATES.md).
