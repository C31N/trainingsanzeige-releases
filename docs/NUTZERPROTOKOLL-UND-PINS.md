# Nutzerprotokoll und direkte PIN-Verwaltung

Ab Version 2.20.34 befindet sich beides unter **Administration → Zugang & PINs**.
Dieser Bereich ist ausschließlich für die Administration zugänglich.

## Eine PIN anzeigen oder ändern

Die sieben Pillen stehen für **Administration**, **Training**, **Musik**,
**IPTV**, **Infotafel**, **Lernen** und **Bildschirmspiegelung**. Es sind gemeinsame
Zugänge, keine persönlichen Nutzerkonten. Ein Protokolleintrag „Training“ benennt
daher keine bestimmte Person.

1. Die gewünschte Pille anklicken. Es ist jeweils nur ein Zugang geöffnet.
2. Ist die PIN bereits für die Anzeige hinterlegt, wird sie unmittelbar geladen.
3. Andernfalls die **bestehende PIN einmal bestätigen**. Nur eine erfolgreiche
   Prüfung übernimmt sie in den Tresor. Die PIN selbst und ihre Version bleiben
   dabei unverändert. Ein noch nicht eingerichteter Zugang erhält eine neue PIN.
4. Für eine Änderung **Neue PIN** und **Neue PIN wiederholen** ausfüllen und
   **Speichern** wählen. Es gelten die bisherigen Zugangs- und Kollisionsregeln.
5. Mit **Schließen** den Bereich schließen. Die gesonderte allgemeine Schaltfläche
   „PIN ändern“ gibt es nicht mehr.

Die aktuelle PIN wird nach 30 Sekunden ausgeblendet. Schließen, Verlassen des
Bereichs, Wechseln in den Hintergrund und Abmelden entfernen die Anzeige ebenfalls.
PINs werden weder in Browser-Speichern noch im Service-Worker-Cache abgelegt.
Eine automatische Wiederholung fehlgeschlagener PIN-Änderungen findet nicht statt.
Bei einer zwischenzeitlichen Änderung auf einem anderen Gerät den Zugang neu öffnen.

## Weshalb bisherige PINs bestätigt werden müssen

Bisher wurden ausschließlich Argon2-Prüfwerte gespeichert. Aus ihnen lässt sich
die ursprüngliche PIN nicht anzeigen. Das Update errät keine PIN und stellt
keine öffentlichen Startwerte wieder her. Bestehende geänderte PINs bleiben gültig.

Neue und bestätigte PINs werden zusätzlich mit OpenSSL-CMS und AES-256-GCM
verschlüsselt im lokalen Tresor hinterlegt. Schlüssel und Zertifikat liegen im
privaten Datenverzeichnis `pin-vault`; Verzeichnis und private Dateien sind nur
für den Anwendungsbenutzer zugänglich. Die Anmeldung verwendet weiter die
vorhandenen Argon2-Prüfwerte.

Online benötigt jede PIN-Anzeige einen verbundenen Pi und einen ausdrücklichen
Admin-Klick. Der Pi verschlüsselt seine Anzeigeantwort zusätzlich für einen
kurzlebigen RSA-OAEP-Schlüssel dieses Browsers. In der Cloud-Warteschlange steht
daher keine lesbare Anzeigeantwort. Der private Browserschlüssel wird nicht
persistiert. Ein Verbindungsabbruch erzeugt keine spätere automatische PIN-Anzeige.

Fehlt der Tresorschlüssel, bleiben die bisherigen Anmeldungen funktionsfähig.
Nach erneuter erfolgreicher PIN-Bestätigung kann ein neuer Tresorschlüssel
angelegt werden. Andere mit dem verlorenen Schlüssel gespeicherte PINs müssen
anschließend ebenfalls bestätigt werden. Ohne bekannte PIN oder passende private
Sicherung lässt sich der alte Zahlenwert nicht aus dem Prüfwert zurückholen;
eine berechtigte Administration kann stattdessen eine neue PIN vergeben.

## Nutzerprotokoll lesen

Unter den Zugangspillen stehen Filter und die Ereignisliste. Die neuesten
50 Einträge erscheinen zuerst; **Weitere Einträge laden** lädt die nächsten nach.
Einträge lassen sich für Details aufklappen. Filter sind **Zugang**, **Herkunft**,
**Ereignis**, **Von** und **Bis**. Die Zeitraumfelder beziehen sich auf die
angezeigte Anlagenzeitzone, in Dalum `Europe/Berlin`.

Erfasst werden An- und Abmeldungen, fehlgeschlagene Anmeldeversuche, ausdrücklich
geöffnete Menüpunkte und Unterbereiche, Inhaltsauswahl, Bedienbefehle und
bestätigte Änderungen. Für geeignete Einstellungen werden Vorher-/Nachher-Werte
angezeigt. PIN-Bestätigung, PIN-Anzeige und PIN-Änderung erscheinen ohne PIN-Ziffern.
Es werden keine einzelnen Tastatureingaben oder regelmäßigen Statusabfragen erfasst.

Jeder Zugang besitzt eine **PIN-Version**. Eine Änderung erzeugt eine neue Version,
eine Bestätigung nicht. Einträge einer bereits angemeldeten Sitzung behalten die
Version, mit der diese Sitzung eröffnet wurde. Bei älteren Einträgen oder
übernommenen Sitzungen kann die Version unbekannt sein; sie wird nicht erfunden.
Fehlgeschlagene Anmeldungen ohne erkannten Zugang heißen **Unbekannter Zugang**.
Funktaster und automatische Vorgänge erscheinen getrennt von PIN-Zugängen.

PINs, Passwörter, API-Schlüssel und Sitzungsschlüssel werden nicht protokolliert.
Die Beschreibung verwendet nur freigegebene Angaben; vollständige Anfrageinhalte
werden nicht gespeichert. Online-Auftrag und tatsächliche Ausführung werden über
eine gemeinsame Auftragskennung zugeordnet. Wiederholte Übergaben erzeugen keine
doppelten Ausführungsereignisse.

## Abgleich und Grenzen

Lokale Ereignisse und Online-Ereignisse werden im Hintergrund in begrenzten
Paketen abgeglichen. Die Funk- und Trainingsverarbeitung wartet nicht auf den
Cloud-Abgleich oder eine geöffnete Protokollansicht. Funktaster-Protokolle werden
über einen auf 512 wartende Einträge begrenzten Hintergrundpuffer geschrieben.
Ein Ausfall oder Überlauf wird als Erfassungsproblem angezeigt; verlorene
Einträge werden nicht nachträglich erfunden.

Die Übersicht zeigt den letzten bestätigten Abgleich, wartende Einträge und
Verbindungsfehler. Bei einem getrennten Pi kann die Online-Liste neuere lokale
Ereignisse noch nicht enthalten. Mit **Aktualisieren** den neuen Stand laden.
Bei einem Navigationsfehler erscheint ein Hinweis; die Bedienung bleibt möglich.

## Drei Kalendermonate und Sicherungen

Einträge älter als drei Kalendermonate werden automatisch gelöscht. Intern werden
Zeitpunkte in UTC gespeichert. Fällt der entsprechende Tag im Zielmonat weg,
gilt dessen letzter Tag. Bereinigt wird beim Start, regelmäßig während des
Betriebs und bei Serverzugriffen. Abfragen und Abgleich schließen ältere Einträge
zusätzlich aus, damit sie nicht durch erneute Übertragung zurückkehren.

Die verschlüsselte private Pi-Sicherung umfasst SQLite-Daten, PIN-Tresor und
zugehörigen Schlüssel. Bei der Wiederherstellung werden alte Sitzungen und
PIN-Auftragsbelege entfernt und abgelaufene Protokolleinträge bereinigt. Die
allgemeine JSON-Sicherung exportiert keinen entschlüsselbaren PIN-Tresor und
keinen Tresorschlüssel. Bereits bestehende verschlüsselte Sicherungsdateien
werden durch die laufende Protokollbereinigung nicht umgeschrieben.

**Diese Version wird zunächst nur veröffentlicht. Die Installation auf dem
Hallen-Pi erfolgt später manuell; die Standortprüfung steht in der
[Abnahmeliste](ABNAHME.md).**

## Steigende Wartezeiten bei falschen PINs

Ab Version 2.20.35 gelten lokal und online dieselben Stufen: Nach drei falschen
Eingaben beträgt die Wartezeit 5 Sekunden. Weitere falsche Eingaben nach Ablauf
der jeweiligen Sperre erhöhen sie auf 10, 20, 40, 80, 160 und höchstens 300 Sekunden.
Die Fehlermeldung nennt die verbleibenden Sekunden. Während dieser Zeit werden
auch richtige PINs derselben Verbindungsherkunft noch nicht geprüft. Wiederholte
Klicks verlängern die Sperre nicht; Anmeldeversuche werden nicht automatisch wiederholt.

Eine erfolgreiche PIN-Prüfung setzt die Stufe zurück. Nach 30 Minuten ohne neuen
zugelassenen Versuch beginnt sie ebenfalls von vorn. Die Stufe übersteht einen
Pi-Neustart. Nach einer privaten Wiederherstellung werden diese alten Sperren verworfen.
Die Sperre betrifft die Verbindungsherkunft, nicht sämtliche Vereinszugänge.
Online können Geräte hinter derselben öffentlichen Netzwerkadresse dieselbe
Herkunft teilen. Andere bestehende Sitzungen und die Buzzer bleiben nutzbar.
