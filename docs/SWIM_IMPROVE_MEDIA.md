# Swim & Improve: Originalvideos vorbereiten

Die Offline-Medien werden getrennt vom Anwendungsupdate vorbereitet. Große
Videodateien gehören weder ins Git-Repository noch in den Service-Worker-Cache
des Handys. Die folgenden Werkzeuge sind Entwicklungswerkzeuge, keine Befehle
für das laufende Hallensystem.

## Quellen und Freigabe

Ausgangspunkt ist die [Lernbibliothek von Sichere Schule](https://www.sichere-schule.de/schwimmhalle/unterrichtshilfen/schwimmen).
Erfasst werden ausschließlich deren Schwimm-Unterrichtshilfen und Niveaustufen.
Das Werkzeug übernimmt die Vimeo-Kennungen aus den Originaleinbettungen; es rät
keine Video-Adressen und übernimmt keine beliebigen Links aus Seitentexten.

Der Auftraggeber hat im Projektgespräch die Freigabe für Bearbeitung und
öffentliche Weitergabe der verwendeten Materialien bestätigt. Diese Bestätigung
ist keine pauschale Lizenz der Quellwebsite. Quellen, Urheberhinweise und
Sicherheitshinweise müssen auch im späteren Medienkatalog erhalten bleiben.
Vor einer Veröffentlichung sind Umfang und Freigabe der tatsächlich enthaltenen
Materialien abzugleichen.

## Download

In einer Entwicklungs-Python-Umgebung `yt-dlp` installieren. Die beim Abruf
verwendete Version für die Dokumentation mit `python -m yt_dlp --version`
auslesen. Ein einzelner öffentlicher Abruf lässt sich so prüfen:

```powershell
python -m yt_dlp --ignore-config --no-playlist https://player.vimeo.com/video/127053481
```

Der vollständige, wiederaufnehmbare Quellabruf erfolgt außerhalb des Checkouts:

```powershell
python ops/download-learning-sources.py --output C:/WFD-Medien/swim-source
```

Unter Linux entsprechend einen absoluten Medienpfad außerhalb des Checkouts
verwenden. `--scan-only` erstellt nur das Quelleninventar. `--workers 1` begrenzt
den Download auf eine Datei gleichzeitig; voreingestellt sind höchstens drei.
Vorhandene Dateien werden anhand ihrer Prüfsumme wiederverwendet; unvollständige
Downloads können fortgesetzt werden. Fehler bleiben pro Datei sichtbar.

Es werden keine Browser-Cookies, Zugangsdaten, Proxywechsel oder Umgehungen von
Vimeo-Zugangssperren verwendet. Nicht abrufbare Videos bleiben als fehlend
gekennzeichnet. Die Rohseiten liegen zur späteren Inhaltszuordnung unter
`pages/`; die Videodateien und Originalmetadaten unter `videos/`.

## Prüfung

Nach dem abgeschlossenen Download mit einer lokalen FFmpeg-Installation prüfen:

```powershell
python ops/verify-learning-sources.py --source C:/WFD-Medien/swim-source --ffmpeg C:/Tools/ffmpeg/bin/ffmpeg.exe
```

Die Prüfung kontrolliert Dateiname, Dateigröße und SHA-256-Prüfsumme und dekodiert
jedes Video vollständig einschließlich vorhandener Tonspuren. Erst wenn alle
Videos bestehen und keine Quellseiten fehlen, wird `verification.json` als
gültig markiert. Die Originalauflösung wird dokumentiert, nicht künstlich
hochskaliert.

Der Quellabruf ist ein Vorbereitungsschritt und erzeugt für sich allein keinen
installierbaren Medienkatalog. Die Hallenanlage verwendet die bereits getrennt
veröffentlichte, signierte Bibliothek `swim-20261021-1` mit 318 Einträgen,
160 Mediendateien und redigierten Merkpunkten für 131 unterschiedliche Videos.
Sie wird unter Admin geladen; für die Installation sind diese Entwicklungsbefehle
nicht erforderlich.

Bei neuen Medienständen folgen auf den Quellabruf Zuordnung, didaktische Texte,
fachliche und visuelle Prüfung sowie signierter Katalog und Paketfreigabe.
Die Bedienung und der Offlinebetrieb stehen in [Swim & Improve](SWIM_IMPROVE.md).
