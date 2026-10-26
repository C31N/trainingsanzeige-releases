# Eingangskontrolle für automatischen Standby

Automatischer Standby ist nur zulässig, wenn kein Training geladen ist,
das Display bestätigt eingeschaltet ist und die letzte TV-Routingmeldung
den HDMI-Eingang des Pi bestätigt. Andere oder unbekannte Eingänge stoppen
den Countdown. Bei erneuter Bestätigung beginnt die volle Wartezeit neu.
Die manuelle Displaysteuerung bleibt unverändert.

## Manuelle Sichtbestätigung

Unter Administration → Displaysteuerung gibt es „Trainingseingang aktiv bestätigen“.
Nur drücken, wenn die Trainingsanzeige oder Bahnhofsuhr wirklich auf dem
angeschlossenen Display sichtbar ist. Die Bestätigung wird als Adminbestätigung
protokolliert, nicht als CEC-Messung. Bei leerer Anzeige beginnt die eingestellte
Standbyzeit neu. Bei geladenem Training läuft kein Leerlauftimer.
Gemeldete Eingangswechsel überschreiben diese Bestätigung wieder.
Online ist die Aktion nur bei erreichbarem Pi möglich. Nach einem Neustart
ist eine neue Bestätigung notwendig, wenn das Display keine passende Quelle meldet.

Der CEC-Monitor speichert Eingangsmeldungen in
`/run/trainingsanzeige/display-input.json`. Eigene Active-Source-Meldungen
gelten nicht als Nachweis des tatsächlich gewählten TV-Eingangs.
Die letzte Eingangsbestätigung bleibt bis zum nächsten gemeldeten Wechsel bestehen.
Standby allein ändert die Eingangsauswahl nicht. Neustart und Monitorende löschen sie.
Nur das Lebenszeichen des Monitors verfällt nach 15 Sekunden, nicht die Auswahl.
Vor dem automatischen Schaltauftrag wird innerhalb der Schaltsperre erneut geprüft.

Wichtig: CEC bietet keine universelle verlässliche Abfrage des ausgewählten
Eingangs. Insbesondere PCs können Eingangswechsel ohne CEC-Meldung verursachen.
Die Anlage verwendet den letzten bestätigten Eingang.
Ein einmaliges Routingereignis reicht damit für einen 30-Minuten-Countdown.
Nicht gemeldete Wechsel können unbemerkt bleiben und zu einer Abschaltung führen.
Ohne initiale Bestätigung oder bei ausgefallenem Monitor bleibt die Automatik gesperrt.
Für den geplanten LG ist eine direkte Eingangsabfrage über RS-232/IP als
zusätzlicher Statuslieferant erforderlich, falls CEC keine ausreichenden
Bestätigungen liefert. Dieser Treiber ist hier noch nicht implementiert.

Eine Hardwareabnahme umfasst Wechsel zwischen Pi, Fire TV und PC sowie
Einschalten per Fernbedienung auf fremdem Eingang. Gemeldete fremde Eingänge
müssen den Timer stoppen; die Grenze bei ungemeldeten Wechseln bleibt bestehen.
