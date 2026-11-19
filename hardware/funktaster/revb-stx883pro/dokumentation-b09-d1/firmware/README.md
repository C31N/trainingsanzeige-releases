# Firmware für Rev B0.9

Alle fünf Platinen erhalten ATtiny402_HOLD_RevA.hex. U4 erhält genau eine der Dateien ATtiny13A_V2_ID1.hex bis ID5.hex. Sender-ID und Gehäusebeschriftung müssen übereinstimmen.

SHA256SUMS.txt prüft die sechs unveränderten HEX-Dateien. ATtiny402_manifest.json ist das originale Rev-A-Buildmanifest; sein ursprünglicher Dateiname buzzer-hold.hex entspricht hier ATtiny402_HOLD_RevA.hex mit identischem SHA-256. Die ursprünglichen C-Quellen und Buildhinweise sind im Rev-A-ZIP unter ../source/ enthalten. ATtiny13A-Fuses: LFUSE0x76, HFUSE0xFB. ATtiny402-Referenzwerte: ATtiny402_fuses.json. Rücklesen und Verifikation sind Pflicht.

J4 und J5 haben getrennte Versorgungsbereiche; die neue PDF hat Vorrang vor der V5-Anweisung zum Gedrückthalten des Tasters. Die Mikrocontroller werden nicht durch dieses Paket automatisch programmiert. Programmierung und Funktionsprüfung auf realer Rev-B-Hardware sind offen.
