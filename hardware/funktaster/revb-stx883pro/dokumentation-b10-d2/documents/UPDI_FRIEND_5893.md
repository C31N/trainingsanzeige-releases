# Adafruit High Voltage UPDI Friend 5893 - Arbeitsanleitung

1. Dokumentations-ZIP entpacken. PowerShell im entpackten Ordner öffnen. `python tools/verify_archive.py` ausführen und PASS abwarten. Python bei Bedarf installieren; danach `py -m pip install pymcuprog` ausführen.
2. Akku, DIAMEX und alle externen Spannungsquellen abziehen. USB am Friend abziehen. Den Spannungsschalter auf **3V** stellen. Nicht5V wählen.
3. Den bedruckten J4-Header verwenden: **weiß UPDI an J4/1**, **rot PWR an J4/2 Controller3V3**, **schwarz GND an J4/3**. Nach Signalnamen und Pinnummern verdrahten; den JST-Stecker nicht auf einen anders belegten Header zwingen. Der RX/TX-Widerstand ist im Friend bereits enthalten.
4. USB-C-Datenkabel verbinden. Der Friend versorgt jetzt die Controller-Schiene. Keine zusätzliche3,3-V-Quelle und keine Verbindung von J4/2 zu J5/2 anschließen. Etwa3,3V an U1/1 gegen U1/8 messen.
5. Im Windows-Geräte-Manager unter Anschlüsse (COM und LPT) den CH340-Port ablesen. Bei fehlendem Port Datenkabel und den von Adafruit verlinkten CH340-Treiber prüfen. COM7 auf Seite4 durch den tatsächlichen Port ersetzen.
6. Die Befehle auf Seite4 nacheinander ausführen: ping, Fuses lesen, HOLD-HEX mit --erase --verify schreiben. Gerätekennung ATtiny402 und erfolgreiche Flash-Verifikation kontrollieren. Danach die Fuses mit der Tabelle vergleichen; UPDI aktiv lassen.
7. Der5893 enthält einen automatischen12-V-Aktivierungsimpuls an UPDI. Die3V-Stellung stellt Versorgung und Logikpegel ein, deaktiviert diese HV-Funktion aber nicht. Kein zusätzliches -H verwenden, keine externe12-V-Quelle anschließen und UPDI nicht als RESET/GPIO umkonfigurieren. Signal ausschließlich an J4/1 anschließen.
8. Bei Fehlern COM-Port, Kabel, Masse, Pinfolge und Versorgung prüfen. Keine Signatur erzwingen und nicht auf5V wechseln. Eine HV-freie Verbindung darf für dieses HV-Modell nicht allein aus einer Softwareoption abgeleitet werden.
9. USB trennen, alle J4-Leitungen abnehmen. Erst danach U4 über DIAMEX-ISP nach Seite5 programmieren: eigene geregelte3,3-V-Versorgung an J5/2, beide DIAMEX-Targetversorgungsschalter AUS. Friend und J4 bleiben getrennt.
10. Nach beiden Verifikationen eindeutige ID1-9 auf der Platine markieren. Programmer und externe Versorgung entfernen, Antenne montieren und erst dann Akku verbinden. IDs6-9 unter Admin - Funktaster als neue Sender anlernen.

Hersteller: https://learn.adafruit.com/adafruit-updi-friend/pinouts-high-voltage
Produkt: https://www.adafruit.com/product/5893
Befehle: https://github.com/microchip-pic-avr-tools/pymcuprog/blob/main/help.md
