# Systemupdates mit Paketentfernungen

Standardmäßig verhindert die Trainingsanzeige, dass ein Systemupdate Pakete entfernt.
Manche Aktualisierungen ersetzen jedoch ein Paket durch einen Nachfolger. Beispielsweise
kann `rpd-common` den Austausch von `pcmanfm` gegen `pcmanfm-pi` benötigen.

## Bewusst nur für einen Auftrag freigeben

1. Außerhalb des Trainings arbeiten; lokalen Zugang zum Pi sicherstellen.
2. Zusätzlich zur Trainingsdaten-Sicherung ein vollständiges Systemabbild bereithalten.
3. **Admin → Sicherung & Updates → Systemupdates installieren** öffnen.
4. **Paketentfernungen nur für dieses Update erlauben** aktivieren.
5. Vorschau abwarten. Entfernte Pakete und Installationen prüfen. Bei unklaren
   Auswirkungen abbrechen und die Technik fragen.
6. Warnhinweis separat bestätigen, Admin-PIN eingeben und Installation starten.

Die Freigabe gilt nur für diesen Auftrag. Beim nächsten Öffnen ist sie wieder aus.
Ändert sich der Paketplan nach der Vorschau, wird die Installation abgebrochen;
Vorschau neu laden und nochmals entscheiden. Weder Paketnamen noch Shellbefehle
können frei eingegeben werden. APT-Sperren gegen die Entfernung essenzieller Pakete
werden nicht aufgehoben.

**Risiko:** Desktop, Netzwerk oder Trainingsanzeige können durch einen Paketwechsel
ausfallen. Die automatische Trainingsdaten-Sicherung ist kein vollständiges
Betriebssystembackup. Der automatische Rückweg für Anwendungsupdates gilt nicht
für Debian-/Raspberry-Pi-Systempakete.

Nach einem Paketwechsel Desktop/Wartungsmodus, Kiosk, Netzwerk, Ton und Displaysteuerung
prüfen. Einen Neustart nur außerhalb des Trainings bewusst durchführen.
