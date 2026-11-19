# Zeitauflösung und theoretische Genauigkeit: V2-N9.1

## Ein Buzzer
Der interne Sender-Timer hat nominal 26,667 Mikrosekunden je Tick (9,6 MHz /256), also0,026667ms. Eine zeitliche Quantisierung ist damit kleiner als ein Tick. Diese Auflösung ist keine Genauigkeitszusage am Taster.

Der Empfänger rekonstruiert den Firmwarestart aus dem mitgesendeten Alter und der am Paket gemessenen Taktrate. Im Instruktionsmodell wird je Paket ein absoluter Rekonstruktionsfehler kleiner als2ms bei Taktskalierung0,8,1 und1,25 verlangt. Der tatsächliche maximale Modellfehler steht in firmware-nine-slot/verification.json. Das umfasst mehrere IDs und Ereigniszähler, aber keine Messung der Hardware.

Vom elektrischen Tastenkontakt bis zum Firmwarestart kommen Eingangsfilter, Einschaltvorgang, Spannungsanstieg und Reset hinzu. Diese Beiträge sind am montierten Gerät nicht gemessen; deshalb ist keine belastbare Gesamtgenauigkeit ab Kontakt angegeben. Die erste sichtbare Empfangsreaktion ist nominal frühestens ungefähr40ms nach Firmwarestart plus Empfänger-/App-Laufzeit möglich. Das erste Paket beginnt nach15ms und dauert etwa25,3ms.

## Mehrere gleichzeitig gedrückte Buzzer
Jeder Sender führt einen eigenen Timer. Die Quantisierung bleibt je Gerät0,026667ms; für eine Zeitdifferenz zweier Geräte beträgt eine konservative Quantisierungsgrenze unter zwei Ticks, also0,053334ms, bei ideal bekannten Takten. Das ist nicht die praktische Genauigkeit der Zeitdifferenz.

Wenn für beide Geräte der getestete Rekonstruktionsfehler kleiner als2ms gilt, ist die daraus folgende konservative Fehlergrenze ihrer Differenz kleiner als4ms relativ zu ihren jeweiligen Firmwarestarts. Unterschiede zwischen Tastenkontakt und Firmwarestart kommen zusätzlich hinzu. Eine Reihenfolge bei Abständen innerhalb dieses Fehlerbereichs ist dadurch nicht zuverlässig belegt. Bei exakt gleichen Tastenkontakten ist die Ankunftsreihenfolge der Pakete kein Nachweis einer tatsächlichen Reihenfolge.

Ein kollidiertes erstes Paket kann durch eine Wiederholung ersetzt werden. Das zusätzliche Warten wird anhand des Paket-Alters zurückgerechnet; die Anzeige reagiert später, ihr Ereigniszeitpunkt soll sich aber auf den Firmwarestart beziehen. Erfolgreicher Empfang der letzten Wiederholung ist nominal bis ungefähr775ms möglich; bei1,25-facher Zeitskalierung vor975ms. Diese Modellgrenze ist keine garantierte Empfangsfrist im Funkbetrieb.

Sind alle vier Pakete eines Buzzers verloren, gibt es für diesen Druck keinen Messwert. Dafür lässt sich keine endliche Zeitfehlergrenze angeben. Auch unterschiedliche Oszillatortakte, zeitversetzte Drücke und externe Funkstörungen können Pakete weiterhin überlagern. Keine gemessene Verlustquote und keine Zusage von0,1Prozent oder Wettkampfgenauigkeit.

## Ergebnis des kompilierten Modells
Über die geprüften IDs, Ereignisse und Taktskalierungen: maximal0,123307ms Rekonstruktionsfehler, daraus konservativ0,246614ms für die Differenz zweier Geräte innerhalb dieser Modelle. Späteste Sendeflanke772,314792ms nominal, entsprechend965,39349ms bei1,25-facher Zeitskalierung. Diese Stichprobe ist kein allgemeiner Fehlergrenzennachweis für reale Hardware.

## Spätere Hallenabnahme
Für eine Genauigkeitsmessung gemeinsame elektrische Referenzkontakte verwenden, Kontakt und Senderversorgung mit Logikanalysator erfassen und mit den zurückgerechneten Empfangszeiten vergleichen. Einzeln und für mehrere Sender gleichzeitig wiederholen, auch mit wechselnden zuerst empfangenen Wiederholungsnummern. Verlustquote getrennt von Zeitfehler und Anzeigelatenz auswerten.
