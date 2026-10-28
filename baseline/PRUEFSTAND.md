# Prüfstand für Ausgangsstand und Installation 2.20.4

Stand: 28. Oktober 2026. Der Quellstand 2.20.3 bleibt durch den Tag
`trainingsanzeige-baseline-2.20.3` erhalten.

Nachgewiesen:

- 844 Backendtests bestanden; ein plattformabhängiger Test übersprungen.
- 103 Oberflächentests bestanden.
- Installation ausschließlich aus dem signierten Installationspaket in einer
  getrennten Software-Testumgebung: leere Datenbank, erste lokale Anmeldung,
  neue Gerätekennung, signierter Cloud-Heartbeat und erste Online-Anmeldung.
- Erneuter SQL-Import in die belegte Testdatenbank verändert deren Kopplung nicht.
- Medienpaket: Katalogsignatur und Dateiprüfsummen geprüft; 318 Einträge, 160 Dateien.
- Echte private Bestandssicherungen von Pi und Cloud erstellt und verschlüsselt
  außerhalb aller Repositories gespeichert. Komponentenkennung stimmt überein.
- Pi-Wiederherstellung auf getrenntem Testziel: 19 Tabellen und 376 Mediendateien
  verglichen. Cloud-Wiederherstellung in eine getrennte MariaDB: 12 Tabellen,
  fünf dauerhafte Datentabellen inhaltlich verglichen; alte Sitzungen und Befehle entfernt.
- 49 veraltete Installations-/Diagnosepfade auf dem Pi nach geprüfter verschlüsselter
  Archivierung entfernt. Rund 347 MB freigegeben; Anwendungsdienste danach aktiv.

Auf Wunsch entfällt die Erstinstallation auf einem leeren echten Pi. Die Prüfung
der Installationswerkzeuge und der getrennten Softwareumgebung ersetzt keine
Hardwareabnahme. Funkreichweite, HDMI-Ton, CEC und Spiegelung am endgültigen
Hallengerät bleiben in der gemeinsamen Abnahmeliste offen.

Diese Datei enthält weder private Sicherungen noch Zugangsdaten oder Schlüssel.
