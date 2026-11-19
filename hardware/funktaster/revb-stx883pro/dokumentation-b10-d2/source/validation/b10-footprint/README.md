# Rev B0.10 - metrischer C3001517-Abgleich

Quelle: **JLCEDA/EasyEDA Official Library**, https://lceda.cn/ und https://easyeda.com/ . Die unveränderte Quelldatei einschließlich ihrer Herkunfts-/Lizenzangabe ist beigefügt. Sie wurde am 18.11.2026 über den sichtbaren Dialog Datei > Quelldatei des offiziellen LCSC-Footprints gelesen, nachdem die JLCPCB-Teiledetailseite den Editor verlinkt hatte. Kein Zugriff auf versteckten Browserzustand.

- Teil: https://jlcpcb.com/partdetail/gnicerf-STX883PRO433MHz/C3001517
- Bibliothek: `COMM-SMD_STX883PRO-433MHZ`, UUID `a9205db4edc6417e8063158c3dd307e5`, Mitwirkender `LCSC`.
- SHA-256 der Quelldatei: `e8cd56807da3faa64c29bf804f4b9cf5a7ddbab7180704956427b433fce09242`.
- Hersteller-Gegenprüfung: https://www.nicerf.com/pdf/stx883pro-ce-fcc-certified-ask-transmitter-module-v1.3.pdf , Rev 1.3, mechanische Zeichnung Seite 5, Pinbelegung Seite 4. Das Datenblatt nennt eine Aktualisierung der Mechanik im Januar 2026. Es ersetzt nicht die landpatternbezogenen Maße der Fertigerbibliothek.

## Ergebnis und Korrektur

Das bestehende 2,54-mm-Raster und die Netze 1 GND, 2 TX3V3, 3 RF_DATA, 4 ANT stimmen. Rev B0.9 verwendet jedoch kleinere, abgerundete Pads als die ausgewählte offizielle Bibliothek. B0.10 gleicht die Kupfer-, Lötpasten- und Maskenpads an die rechteckigen Bibliothekspads an.

| Merkmal | B0.9 | B0.10 / offizielle Bibliothek |
|---|---|---|
| Pads 1-3 Breite x Höhe | 1,70 x 2,50 mm | 1,90 x 2,70 mm |
| Pad 4 Breite x Höhe | 1,80 x 2,20 mm | 2,00 x 2,50 mm |
| Form | abgerundetes Rechteck | Rechteck |
| Abstand untere Padreihe zu ANT-Mitte | 13,20000 mm | 13,15517 mm |
| ANT-Mitte auf PCB, X / Y nach unten | 19,73000 / 6,40000 mm | 19,72999 / 6,44483 mm |
| Untere Padreihe Y auf PCB | 19,60000 mm | 19,60000 mm |

Pad 2 bleibt als Anker an (15,000 / 19,600) mm. Modulgehäuse-Umriss und Courtyard wurden entsprechend der Bibliotheksgeometrie korrigiert. Die ANT-Leiterbahn endet nun am neuen Padmittelpunkt; die Verlängerung beträgt rund 0,045 mm. Die native Zwischenprüfung fand mit dem größeren GND-Pad einen auf 0,1508 mm verkleinerten Abstand zur TX3V3-Diagonale. Deshalb wird diese Diagonale um 0,25 mm nach außen versetzt und mit einem kurzen Anschlusssegment geschlossen; die 0,20-mm-Regel wird nicht reduziert. Keine Änderung an der programmierten Funktion oder Sender-ID.

Der unabhängige Vergleich in B10_GEOMETRY_COMPARISON.json liest das KiCad-S-Expression-Modell und prüft alle vier Padpositionen und -größen relativ zu Pad 2 gegen die gesicherte Bibliothek. Maximal zugelassener Rundungsfehler: 0,00005 mm. Pin-zu-Netz-Zuordnung und rechteckige Form werden zusätzlich geprüft. Das ist ein geometrischer Abgleich; keine Zusage über Lötqualität, Maschinenplatzierung oder die tatsächlich gelieferten Module.

## Bestückungsdatei und aktueller Status

B0.10-S2 ist bestellt (Bestellverlauf am 19.11.2026 geprüft): zehn PCBs, davon neun Standard-PCBA. Die exakte finale numerische CPL und S2-Gerber sind unter dokumentation-b10-d2/manufacturing gesichert. U1/U4: 270 Grad; U2/U3 und Q1-Q4: 180 Grad; D1/D2 und übrige Referenzen: 0 Grad. U5: Mid X 16,095019 / Mid Y -13,022416 mm gemäß Bibliotheksursprung. Alle Gerber-Y-Werte sind negativ. Die Datei wurde frisch importiert; danach keine manuellen Drehungen oder Positionsänderungen. Der Bildexport sichert die sichtbare Orientierung aller 35 Referenzen. Keine Behauptung über einen nicht verfügbaren Live-CPL-Export.

Native KiCad8.0.9-Prüfung (CI 44374130631): DRC0/ERC0/Unconnected0/Parität0. B10_GEOMETRY_COMPARISON.json wurde am aktuellen S2-ROUTED-V3-EXPERIMENT-Quellboard erneuert. Das CI füllt daraus Zonen und erzeugt das für DRC und Gerber verwendete Board. Der Geometrievergleich prüft nur Landpattern; seine Statusfelder sind keine Maschinen- oder Hardwarefreigabe. B10_GERBER_PAD_CHECK.json stammt vom kupfergleichen B0.10-Stand vor S2 und dient als historischer Zusatzbeleg. Die neue Dokumentation prüft die tatsächlich hochgeladenen S2-Gerber separat.

Reale Programmier-, Akku-, Gehäuse- und Funkprüfungen bleiben offen. dokumentation-b09-d1 bleibt historische Dokumentation und ist keine Bestellgrundlage.
