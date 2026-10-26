BESTANDSFIRMWARE V1 (unveraendert)
====================

Aktuelle Firmware V2 mit Zeitstempeln/CRC16 liegt im Unterordner v2. Zuerst den
Pi-Empfaenger diamex-5 installieren! README_V2.md im Paket-Hauptordner lesen.
Echte Funkabnahme der V2 steht noch aus. Dieser Text beschreibt V1.

Die fünf HEX-Dateien in diesem Ordner sind die bisherigen festen Builds.
Sie wurden aus den danebenliegenden AVR-Assembly-Dateien erzeugt.

Warum Assembly statt Compiler-Abhaengigkeit?
- Trainer brauchen auf ihrem PC keinen AVR-C-Compiler.
- Jede Datei ist klein und deterministisch.
- Die Firmware laesst sich anhand der Disassembly pruefen.

Hardware:
- ATtiny13A
- 9,6 MHz interner RC (LFUSE 0x76)
- BOD ca. 2,7 V (HFUSE 0xFB)
- PB3 / phys. Pin 2 -> STX882 DATA

Telegramme:
1: D3 6C 01 9C
2: D3 6C 02 95
3: D3 6C 03 92
4: D3 6C 04 87
5: D3 6C 05 80

Ablauf:
- 15 ms warten
- 5 Frames senden
- zwischen Frames ca. 3 ms Pause
- DATA LOW
- Power-down bis Reset/erneutes Einschalten
