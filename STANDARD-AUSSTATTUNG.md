# Standardausstattung für neue Geräte

Das signierte Installationspaket enthält die aktuelle Vereinsgrafik der
Testanlage (PNG sowie editierbare SVG-Quelle) und ihre 14 Trainingssounds,
jeweils als Originaldatei und vorbereitete WAV-Datei. Die Zuordnungen je Bahn
werden bei einer Neuinstallation ebenfalls übernommen.

`ops/install-pi.sh` übernimmt diese Medien beim Einrichten eines leeren Geräts.
Vorhandene Grafik- und Klangbibliotheken werden **nicht überschrieben**.
Die Vereinsgrafik wird für Bootbild, Desktop, App und Hallenanzeige verwendet.
Nach Kopplung des neuen Geräts überträgt die Synchronisierung die Bibliothek
und Grafik auch an die zugehörige Onlineinstallation.

## Öffentliche Start-PINs

| Zugang | Start-PIN |
| --- | --- |
| Admin | 136542 |
| Trainer | 123456 |
| Musik | 654321 |
| Spiegelung | 13698642 |

**Diese PINs sind öffentlich bekannt. Vor Freigabe im Internet unter
„Zugang & PINs“ ändern.** Updates ändern keine bereits eingerichteten PINs.
Geräteschlüssel werden weiterhin individuell erzeugt. WLAN-Zugänge,
Datenbanken, PIN-Hashes, private Schlüssel und Sicherungen der Testanlage
sind nicht Bestandteil dieser Standardausstattung.

Weitere eigene Sounds oder Grafikänderungen werden nicht automatisch auf
GitHub veröffentlicht; dafür muss bewusst eine neue Standardausstattung
freigegeben und in ein geprüftes Release aufgenommen werden.
