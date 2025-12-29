# Kamera-Installation LPR-Leitfaden | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/kamera-installation-lpr-leitfaden

Kamera-Installation LPR-Leitfaden
Es wird empfohlen, die Kamera in der Mitte des Fahrzeugs zu installieren.




Wenn die Kamera am Straßenrand oder auf der Fahrbahn installiert ist, sollte der Winkel 30 Grad nicht überschreiten.




Die Kamera sollte höher als die Scheinwerfer des Fahrzeugs angebracht werden, damit die Scheinwerfer des Fahrzeugs nicht direkt auf die Kamera gerichtet sind.
Stellen Sie sicher, dass das Nummernschild mindestens 120 Pixel breit und mindestens 50 Pixel hoch ist.




Höhe mindestens 50 Pixel

Breite mindestens 120 Pixel

Der Neigungswinkel des Kennzeichens muss innerhalb von +/- 10 Grad liegen.







LPR-Einstellungen in der Anwendung System Manager




Stellen Sie sicher, dass die richtige Region (Amerika/Eurasien) ausgewählt ist.

Festlegung der Region von Interesse




Die Region von Interesse wird verwendet, um zu definieren, wo die Erkennung Nummernschilder findet.

Lassen Sie einen gewissen Spielraum zu der Region von Interesse, um nicht teilweise sichtbare Platten zu erkennen.




Das gesamte Nummernschild befindet sich innerhalb des interessierenden Bereichs, und das Nummernschild wird erkannt.




Das Nummernschild befindet sich nicht vollständig innerhalb des interessierenden Bereichs, und das Nummernschild wird nicht erkannt.

Ermöglichung der Anerkennung von Ländern

In vielen Ländern ähnelt der Buchstabe O der Zahl 0, und der Buchstabe I sieht genauso aus wie die Zahl 1. Die Aktivierung der Ländererkennung verbessert die Erkennungsgenauigkeit in diesen Fällen.

Das Format für das brasilianische Kfz-Kennzeichen ist beispielsweise "abc1d23".




Allgemeine Probleme und Lösungen
Unvollständiges Nummernschild

Lösung: Legen Sie den Interessenbereich nicht zu nahe an den Bildgrenzen fest.

Blickwinkel macht Nummernschilder unleserlich

Lösung 1: Bewegen Sie die Kamera an einen besseren Ort.

Lösung 2: Stellen Sie den Bereich von Interesse so ein, dass das Schild erkannt wird, wenn es aus einem besseren Winkel sichtbar ist.

Scheinwerfer anderer Fahrzeuge reflektieren vom Nummernschild

Lösung 1: Bringen Sie die Kamera an einen besseren Ort.

Lösung 2: Stellen Sie den Interessenbereich so ein, dass das Kennzeichen auch dann erkannt wird, wenn die Scheinwerfer anderer Fahrzeuge nicht in die Richtung des Kennzeichens zeigen.

Das Nummernschild ist zu klein

Lösung 1: Bewegen Sie die Kamera an einen besseren Ort oder zoomen Sie hinein.

Lösung 2: Stellen Sie den Bereich von Interesse so ein, dass das Kennzeichen erkannt wird, wenn sich das Fahrzeug näher an der Kamera befindet.

Lösung 3: Erhöhen Sie den Wert für die Mindesthöhe des Kennzeichens in den LPR-Einstellungen, damit die Erkennung kleiner Kennzeichen ignoriert wird.

Das Nummernschild ist unscharf

Lösung 1: Passen Sie die Schärfe an und verlängern Sie die Verschlusszeit in den Einstellungen der Kamera.

Lösung 2: Erhöhen Sie die Beleuchtung des Bereichs.

Das Nummernschild ist überbelichtet

Lösung 1: Passen Sie die Bildeinstellungen der Kamera an.

Lösung 2: Überprüfen Sie den Installationsort der Kamera und verschieben Sie sie höher, damit die Scheinwerfer nicht von der Platte reflektiert werden.

Pagination
Previous page
FR Alarmauslöser und Konfiguration
Next page
Mirasys License Plate Recognition (LPR)