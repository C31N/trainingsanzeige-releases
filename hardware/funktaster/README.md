# Funktaster: bauen, programmieren und zuordnen

Das vollständige [DIAMEX-Downloadpaket](DIAMEX_Funktaster.zip) enthält den
**Lochrasterplan V5**, Firmware **V2 für IDs 1–255**, den **V1-Rückfall für IDs 1–5**
und die Windows-Programmieroberfläche. Paketformat V7; die Anleitung entspricht
dem aktuellen Hallenbetrieb. Firmware und Schaltplan sind unverändert.

## Welche Anleitung brauche ich?

- [Lochrasterplan V5 mit Rückseitenverdrahtung](Lochrasterplan_Funktaster_V5_Rueckseitenverdrahtung.pdf)
- [Programmieren mit DIAMEX](diamex/README_DIAMEX_Trainer.md)
- [Kurzanleitung](diamex/KURZANLEITUNG.txt)
- [V2, Zeitübernahme und Rückfall](diamex/README_V2.md)
- [Empfänger und noch ausstehende Hallenprüfung](EMPFÄNGERFREIGABE.md)

V5 ist der maßgebliche Bauplan. Ältere Pläne werden nicht zum Aufbau verwendet.
Die archivierten Originaldateien dienen nur der technischen Nachvollziehbarkeit.

## Aufbau und Versorgung

ATtiny13A und STX882 arbeiten mit 3,3 V; DATA liegt an PB3 / physischem Pin 2.
Akku-Plus führt über die Sicherung zum Taster COM, NO an 09-A, Akku-Minus an 07-A.
Die Rückseitenverdrahtung und Bauteilorientierung aus dem V5-Plan übernehmen.
Den externen Sicherungshalter mechanisch befestigen. Akkuausgang vor Anschluss
messen; zum Laden Akku abstecken und dessen vorgesehenen USB-C-Anschluss verwenden.

Der fertige Taster versorgt sich beim Programmieren über den gedrückten Taster
selbst. **Beide Target-Versorgungsschalter am DIAMEX bleiben OFF.** Keine 5 V
auf die 3,3-V-Schaltung geben, keine lose Brücke zwischen COM und NO einsetzen.
ISP-Pin 1 vor Anschluss kontrollieren.

## Vor der Nutzung

1. Am Pi unter **Admin → Funktaster** Empfänger **diamex-5** prüfen.
2. Nur bei benötigter Programmierung das ZIP vollständig entpacken und der
   DIAMEX-Anleitung folgen. Ein Anwendungsupdate flasht keine Handsender.
3. Für jeden physischen Sender eine eigene ID verwenden. Die ID ist keine Bahnnummer.
4. Unter **Sender anlernen** den Code erkennen und Bahn oder Trainerfunktion zuweisen.
   Für DIAMEX nicht „Leere Universalfernbedienung vorbereiten“ verwenden.
5. Jede Taste einzeln, kurz, gehalten und zusammen mit anderen Tasten am Standort prüfen.

Die IDs 1–5 behalten beim Wechsel zwischen V1 und V2 ihre Zuordnung. Bereits
programmierte V2-Sender müssen wegen dieser Dokumentationsüberarbeitung nicht
neu programmiert werden. Die reale Hallen- und Zeitmessprüfung ist noch offen.

## Training, Spiele und Quiz

Im normalen Training arbeitet der Bahntaster passend zum Zustand. Für Spiele
werden vier Sender unter **Admin → Spiele** Stationen zugewiesen. Im Quiz sind
die physischen DIAMEX-IDs 1/2/3 die Antworten Rot/Gelb/Grün; die Bahnzuordnung
ändert diese Antwortpositionen nicht. Details stehen in den
[Spielregeln](../../docs/SPIELE.md) und der [Quizanleitung](../../docs/SCHWIMMABZEICHEN.md).

Die Trainerfunktion **Fernseher ein / Standby** beendet zuerst Anzeigeinhalte,
archiviert ein geladenes Training und führt zur Uhr. Erst der nächste Druck
auf der Uhr schaltet in Standby.

## Paket ohne Hardware prüfen

Im Verzeichnis `trainingsanzeige`:

```powershell
python hardware/funktaster/build_package_v5.py
python hardware/funktaster/verify_package.py
python hardware/funktaster/check_receiver_compatibility.py
```

Der historische Skriptname erzeugt das aktuelle Paket. Der Prüfer kontrolliert
Inhalt, Firmwareprüfsummen, HEX/BIN und CRC; er greift nicht auf einen Programmer
oder COM-Port zu. Das ersetzt die [Abnahme am Hallengerät](../../docs/ABNAHME.md) nicht.
