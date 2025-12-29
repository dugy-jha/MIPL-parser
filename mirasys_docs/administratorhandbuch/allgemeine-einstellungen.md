# Allgemeine Einstellungen | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/allgemeine-einstellungen

Allgemeine Einstellungen

In den allgemeinen Einstellungen zeigen die Spalten die Kameranummer, wenn die Kamera in Gebrauch ist, den Kameranamen, die Qualität, die Auflösung und die Rate, wenn die Kamera einen AI-Dienst verwendet, welchen Dienst und welchen Kameratreiber die Kamera verwendet. Alle Spalten können in aufsteigender oder absteigender Reihenfolge sortiert werden.

Name

Der Name der Kamera. Das System schlägt Namen des Typs Kamera 1, Kamera 2 usw. vor.

Im Einsatz

Deaktivieren Sie dieses Kontrollkästchen, wenn keine Kamera an den Kameraeingang angeschlossen ist oder wenn Sie die Kamera deaktivieren möchten.

360 Kamera

Dies teilt dem Spotter-Client mit, dass es sich bei der Kamera um eine 360-Grad-Kamera handelt, und Spotter zeigt die Bildentzerrungsoptionen in der Kamerasymbolleiste an (sofern installiert).

Steuermodus

Diese Einstellung hat zwei Optionen, Aktiv (Standard) und Passiv.
Wenn mehrere Server dieselbe Kamera konfiguriert haben, sollte einer auf Aktiv und die anderen auf Passiv gesetzt werden.
Auf diese Weise werden nur die aktiven Servereinstellungen an die Kamera übermittelt .

Transportart

Diese Einstellung steuert, wie der Medienstream von der Kamera zum Server transportiert wird.
Die verfügbaren Optionen sind RTP over UDP (Standard) und RTP over RTSP.
Wenn die Kamera mit einer Einstellung schlecht zu funktionieren scheint (z. B. wenn es Löcher im Kameramaterial gibt oder es schwierig ist, alle Bilder von einer Kamera zu erhalten), kann die andere Einstellung verwendet werden.

Dekomprimierungscodecs

Codecs werden zum Kodieren und Dekodieren von Videodaten verwendet

Beschreibung

Hier können Sie eine Beschreibung der Kamera eingeben, die allen Benutzern im Spotter-Programm angezeigt wird.

Administrative Beschreibung

Hier können Sie eine Beschreibung der Kamera eingeben. Die Beschreibung wird im Spotter-Programm nur Systemadministratoren angezeigt.

Kamera-Infos

Die Registerkarte „Kamerainfo“ enthält Kontrollkästchen für die Angaben, die automatisch in die Kamerainfo aufgenommen werden sollen:

VMS-Server

IP-Adresse

Kameramodell

Verwendete AI-Funktionen

Auflösung

Einstellungen der Bildrate

Die Informationen, die Sie durch Ankreuzen der Kästchen für die Kamera erhalten, werden automatisch in die Kamerabeschreibung in Spotter für diese Kamera übernommen. Standardmäßig sind alle Kästchen aktiviert.

Damit die Informationen in Spotter angezeigt werden, muss unter Benutzergruppe > Eigenschaften der Mirasys Spotter Enterprise-Rolle > Bildschirm > Bildschirmelemente die Erlaubnis erteilt werden, Kamera-Infos anzuzeigen.

Referenzbild

Ein Referenzbild ist ein von der Kamera aufgenommenes Bild, das die Identifizierung der Kameras erleichtert.

Darüber hinaus können die Benutzer im Spotter-Programm das, was sie in der Videoansicht sehen, mit dem Referenzbild vergleichen, um sicherzustellen, dass die Kamera darauf gerichtet ist in die richtige Richtung.

Um das aktuelle Referenzbild zu ändern, klicken Sie auf die Schaltfläche Bild aufnehmen  . Um ein Referenzbild zu löschen, klicken Sie auf die Schaltfläche Bild löschen.

Pagination
Previous page
Kameraeinstellungen
Next page
Streams (Kameras)