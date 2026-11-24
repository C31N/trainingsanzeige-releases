# Manueller Wettkampf für drei Bahnen

Die lokale Trainingsanzeige begleitet einen Wettkampf mit unabhängigen Richter-Stoppuhren. Der Pi speichert die Startliste, die eingetragenen Zeiten und die Freigaben auch ohne Internet. Die Veranstaltung nutzt die Bezeichnungen aus der EasyWK-Startliste.

1. Auf dem Gerät im Hallennetz **Wettkampf** öffnen und mit der Wettkampf-PIN anmelden. Die Administration kann diese unter **Zugang & PINs** ändern. Für die Ergebnisfreigabe meldet sich ein Offizieller mit dem Admin-Zugang an.
2. Unter **Lauf anlegen** Veranstaltung, Wettkampfnummer, Disziplin und Laufnummer eintragen. Für jede belegte Bahn Name und Verein ergänzen. Leere Bahnen bleiben frei.
3. Den Lauf in der Liste wählen und **Lauf anzeigen** drücken. Startliste auf dem Hallenbildschirm kontrollieren. Als Startsignal steht ein externer Starter oder der vorbereitete Startton am konfigurierten Pi-Audioausgang zur Verfügung. Der ALSA-Ausgang verwendet standardmäßig `default`. Der Betreiber kann ihn über `TRAININGSANZEIGE_START_PCM` festlegen.
4. **Startbereit melden**. Play auf der zugeordneten Trainerfernbedienung oder **Start auslösen** startet den Versuch einmal. Im externen Betrieb den tatsächlichen Start organisatorisch mit dem Starter abstimmen. Die Zeitnehmer starten ihre unabhängigen Uhren auf das tatsächliche Startsignal. Die Hallenuhr dient der Orientierung. Bei Fehlstart den Grund eintragen, abbrechen und einen neuen Versuch vorbereiten.
5. Nach dem letzten Anschlag **Lauf beenden und Zeiten erfassen** wählen. Für jede Stoppuhr Zeitnehmer und Zeit eintragen. Schnellschrift wie `10437` zeigt vor der Bestätigung `01:04,37`. Den maßgeblichen Stoppuhrwert je Bahn ausdrücklich übernehmen. DNS, DNF und DSQ sowie spätere Änderungen begründen.
6. Der Offizielle prüft die drei Bahnen, trägt seinen Namen ein und gibt das Ergebnis frei. Für eine Korrektur die Freigabe mit Begründung öffnen. Beim Ändern einer Wertung Bearbeiter und Grund angeben. Freigegebene Platzierungen beruhen auf Hundertsteln. Gleiche Zeiten ergeben denselben Platz.
7. Vor und Zurück der Trainerfernbedienung wechseln zwischen Läufen derselben Veranstaltung. Der lokale Bildschirm bietet dieselben Aktionen. Unter **Ergebnisprotokoll** lassen sich die freigegebenen Läufe drucken oder als CSV für die manuelle Übernahme in EasyWK herunterladen. Die CSV enthält die Exportrevision. Die Antwort liefert zusätzlich die SHA-256-Prüfsumme.
8. Zum Abschluss die Hallenanzeige schließen und die Sicherung der Trainingsanzeige herunterladen. Nach einem Neustart ist ein unterbrochener Versuch als abgebrochen gekennzeichnet. Eingegebene Werte und Änderungsprotokoll sind weiter verfügbar.

## Abnahmestand

Die Wettkampfbedienung erfolgt am Pi im Hallennetz. Die gekoppelte Online-Anzeige verwendet den öffentlichen Laufzustand. Der Startton ist am tatsächlich verwendeten Hallenausgang zu prüfen. Der Godox-Anschluss ist für eine spätere abgenommene Ansteuerung vorbereitet und standardmäßig deaktiviert. Für elektronische Zeitmessung, EasyWK-SST und den offiziellen Wettkampfeinsatz sind die jeweiligen Abnahmen offen.
