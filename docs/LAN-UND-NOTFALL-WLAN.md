# LAN-Internet und Notfall-WLAN

Ab Softwarestand 2.20.14 kann der Pi Internet ausschließlich über seinen Netzwerkanschluss beziehen. Diese Anleitung betrifft den Pi; das angeschlossene Netzwerkgerät muss bereits Internet am LAN-Port bereitstellen.

## Vorhandenen Pi umstellen

1. Pi und Netzwerkgerät mit einem Netzwerkkabel verbinden. Beide Geräte eingeschaltet lassen.
2. **Administration → Netzwerk & Internet** öffnen. LAN-Adresse und **Internet erreichbar** abwarten. Ein eingestecktes Kabel allein genügt nicht. Der Pi bezieht seine Adresse normalerweise automatisch per DHCP; vorhandene eigene LAN-Profile werden nicht überschrieben.
3. **LAN-Betrieb: Internet nur über Netzwerkkabel** einschalten. **WLAN bei funktionierendem LAN-Internet ausschalten** eingeschaltet lassen, wenn der Pi sein eigenes WLAN im Normalbetrieb nicht benötigt.
4. Die Notfall-Hotspot-Automatik eingeschaltet lassen und **Netzwerkdaten speichern** drücken. Ohne bestätigtes LAN-Internet wird die Umstellung abgewiesen.
5. Die angezeigte LAN-Adresse öffnen: `http://<LAN-Adresse>:8080/control`. Telefon oder PC müssen das lokale Netzwerk des LAN-Anschlusses erreichen können. Eine Cloud-Verbindung beweist diese lokale Erreichbarkeit nicht.

Ein Update schaltet den LAN-Betrieb nicht selbstständig ein. Die bisherige WLAN-Verbindung bleibt bis zur bewussten Umstellung erhalten. Hostname, gespeicherte WLAN-Kennwörter, PINs und Cloud-Kopplung werden nicht zurückgesetzt.

## Automatische Umschaltung

- Im LAN-Betrieb werden alte Hallen-WLANs nicht automatisch ausprobiert. Ihre Profile bleiben gespeichert; beim Verlassen dieses Betriebs werden ihre vorherigen Autoconnect-Einstellungen wiederhergestellt.
- Nach dem Start hat die Netzwerkverbindung mindestens 120 Sekunden Zeit. Danach startet bei mindestens 30 Sekunden fehlendem bestätigtem LAN-Internet der Notfall-Hotspot. Das gilt auch bei angeschlossenem Kabel ohne DHCP-Adresse oder ohne Internetzugang.
- Internet wird alle zehn Sekunden über Ethernet geprüft. Ein einzelner ausgefallener Cloudserver reicht nicht zum Auslösen: zusätzlich wird ein unabhängiges HTTPS-Prüfziel verwendet. Zertifikatsprüfung bleibt aktiv; Anmeldeseiten eines Gastnetzes gelten nicht als bestätigter Internetzugang. Werden sämtliche Prüfziele im Hallennetz blockiert, startet der Hotspot ebenfalls.
- Ethernet bleibt während des Hotspots eingeschaltet. Nach mindestens 30 Sekunden bestätigtem LAN-Internet endet der Hotspot. Bei gewählter WLAN-Abschaltung wird anschließend das Pi-WLAN ausgeschaltet.
- Kurze Störungen lösen keinen sofortigen Wechsel aus. Training und Buzzer werden durch die Netzwerküberwachung nicht neu gestartet.

Die Administration zeigt Kabelstatus, LAN-Adressen, Ergebnis und Zeitpunkt der Internetprüfung sowie WLAN-/Hotspot-Zustand. Fehlende oder veraltete Statuswerte bestätigen keinen funktionierenden Internetzugang.

## Adressen verstehen und kopieren

Unter **Administration → Netzwerk & Internet → Netzwerk einrichten** erhält jede
Adresse eine eigene Beschreibung. Tippe auf die Adresse, um nur diese zu kopieren,
oder auf den darunterstehenden Bedienlink, um die vollständige Browseradresse zu
kopieren. Eine Meldung bestätigt das Kopieren. Das funktioniert auch auf der lokalen
HTTP-Bedienseite; wenn der Browser das Kopieren vollständig verhindert, zeigt die
Oberfläche eine entsprechende Meldung an.

- **Lokale IPv4 · LAN/WLAN:** Adresse des jeweiligen Pi-Anschlusses. Telefon oder PC
  müssen dieses lokale Netzwerk erreichen können. Der Bedienlink lautet
  `http://<IPv4-Adresse>:8080/control`.
- **Öffentliche IPv6 · LAN/WLAN:** global adressierbare IPv6 des jeweiligen Anschlusses.
  Mehrere öffentliche IPv6-Adressen gleichzeitig sind möglich. Dein Bediengerät
  benötigt eine passende IPv6-Verbindung. Der vollständige Link enthält die Adresse
  in eckigen Klammern: `http://[<IPv6-Adresse>]:8080/control`. Zugriff von außerhalb
  hängt zusätzlich von Routing und Router-Firewall ab und wird hier nicht bestätigt.
  Das Update öffnet keine Router-Freigaben.
- **Vorübergehende IPv6:** kann regelmäßig wechseln. Für dauerhaft gespeicherte
  lokale Bedienlinks möglichst die lokale IPv4 oder den Gerätenamen verwenden.
- **Lokale IPv6:** für entsprechend verbundene lokale Netze; keine öffentliche
  Internetadresse. Auch dafür benötigt das Bediengerät IPv6.
- **Gerätename:** beispielsweise `trainingsanzeige.local`. Funktioniert bei
  unterstützter lokaler Namensauflösung. Der vollständige Bedienlink ist ebenfalls
  kopierbar.
- **Notfall-Hotspot:** `10.42.0.1` und der zugehörige Bedienlink sind nur erreichbar,
  wenn der Pi-Hotspot aktiv und das Bediengerät damit verbunden ist.
- **Öffentliche Basisadresse:** Adresse der Online-App auf dem Webserver, unabhängig
  von den lokalen Pi-Adressen. Fernbedienung benötigt die Internet-/Cloud-Verbindung.

Wurde die Schnittstelle oder der Geltungsbereich nicht gemeldet, steht dies
ausdrücklich dabei. Aktualisierungen der Adressliste verändern keine ungespeicherten
Eingaben im Netzwerkformular.

## Notfallzugang

Bei aktivem Hotspot das Telefon mit dem angezeigten Notfall-WLAN verbinden und `http://10.42.0.1:8080/control` öffnen. Das individuelle Kennwort steht im PIN-geschützten Wartungsfenster. Es bleibt beim Wechsel zwischen LAN und Hotspot erhalten.

Im LAN-Betrieb ist die manuelle Hotspot-Aktivierung bei bestätigtem Internet gesperrt. Ohne aktuellen Prüfstatus wird sie ebenfalls abgewiesen. Die automatische Überwachung arbeitet unabhängig von geöffneten Bedienseiten.

## Bildschirmspiegelung und Bluetooth

Bildschirmspiegelung bleibt möglich: Beim Start wird WLAN vorübergehend eingeschaltet und der Adapter an den Spiegelungsempfänger übergeben. NetworkManager läuft im LAN-Betrieb weiter und hält Ethernet, Internet und Cloud aktiv. Nach Ende, Abbruch oder behandeltem Fehler geht der Adapter zurück an die Netzwerküberwachung. Diese stellt WLAN-Abschaltung oder Notfall-Hotspot wieder her.

Spiegelung und Notfall-Hotspot benötigen denselben WLAN-Adapter und stehen während einer Spiegelrunde nicht gleichzeitig zur Verfügung. Bei fehlendem LAN-Internet die Spiegelung zuerst beenden, um den Notfallzugang wiederherzustellen. Bluetooth wird von der WLAN-Abschaltung nicht ausgeschaltet.

## Prüfung nach Anschluss

LAN-Start, Kabelziehen, Internetausfall bei gestecktem Kabel, Wiederkehr des Internets und Spiegelung einschließlich Abbruch vor Ort prüfen. Beobachten, dass der Hotspot erreichbar ist und nach Rückkehr des Internets wieder endet. Softwaretests ersetzen diese Hardwareabnahme nicht. Siehe [Abnahmeliste](ABNAHME.md).
