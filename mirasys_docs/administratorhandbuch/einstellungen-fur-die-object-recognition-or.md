# Einstellungen für die Object Recognition (OR) | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/einstellungen-fur-die-object-recognition-or

Einstellungen für die Object Recognition (OR)

Systemadministrator-Einstellungen, die es Operatoren ermöglichen, die Objekterkennung in der Spotter Smart Search zu nutzen.

Object Recognition Settings

Die Einstellungen für die Objekterkennung finden Sie im Systemmanager auf der Registerkarte VMS Server > Kameras.

Gehen Sie im Fenster Kameraeinstellungen auf die Registerkarte OP-Einstellungen.

Wenn die Benutzerlizenz die Objekterkennungsfunktion nicht unterstützt, wird die Registerkarte OR-Einstellungen ausgeblendet.

Kamera auswählen, streamen und aktivieren ODER

Wählen Sie die Kamera aus dem Dropdown-Menü in ODER

Wenn es mehr als einen Stream gibt, können Sie den Stream auswählen. Wenn nur ein Stream vorhanden ist, gibt es einen Standardstream wie in der Abbildung oben, und das Dropdown-Menü ist deaktiviert.

Sie können einen Dienst erst auswählen, nachdem Sie den Dienst durch Anklicken des Kästchens OR für ausgewählte Kamera aktivieren aktiviert haben.

Wenn das Kontrollkästchen OR für ausgewählte Kamera aktivieren nicht markiert ist, ist das Dropdown-Menü Dienst deaktiviert.

Das Textfeld Lizenz zeigt die Anzahl der verwendeten Lizenzen und die maximale Anzahl von Lizenzen an.

Wenn die Kamera den ODER-Dienst nicht unterstützt oder kein Dienst für sie aktiv ist, kann der Dienst nicht aktiviert werden.

Das gelbe Symbol zeigt dies an, und wenn der Benutzer den Mauszeiger darüber bewegt, erscheint ein Tooltip mit dem Text Für diese Kamera ist kein OR-Dienst aktiv.

Erfassungsbereich / Minimale Objektgröße

Ein Bild im Erkennungsbereich wird sofort hochgeladen, nachdem die aktuelle Kamera in der Kamera-Kombibox ausgewählt wurde. Die minimale Objektgröße kann auf zwei Arten angepasst werden:

Anpassen des Prozentsatzes in Min. Objekthöhe (%)

Stellen Sie ihn im Rahmen mit dem angezeigten Quadrat für Mindestobjektgröße ein. Das Quadrat hat die gleiche Farbe wie im Selektor rechts neben dem Rahmen.

Die Mindestgröße kann nicht weniger als 10% betragen.

Erkennungsparameter

Max objects - maximale Anzahl der zu erkennenden Objekte im Bild. Der Wert sollte zwischen 1 und 100 liegen.

Minimale Erkennungssicherheit (%) - Vertrauensniveau des Erkenners. Liegt das Vertrauen in das erkannte Objekt unter diesem Schwellenwert, wird das Objekt ignoriert. Gültige Werte liegen zwischen 25% und 95%.

Detektionsintervall (ms) - die Anzahl der Millisekunden, die beschreibt, wie oft die Objekterkennung durchgeführt wird: wenn sie z. B. 250 ms beträgt, wird die Objekterkennung 4 Mal in einer Sekunde durchgeführt (auch wenn die Bildrate des Videostroms viel höher ist, z. B. 30 fps).

Gerät - wird für die Inferenz verwendet. Die verfügbaren Geräte hängen von der Hardware des aktuellen Dienstes ab.

Schließe Thumbnail ein - schließt das Thumbnail der Erkennungsquelle in die zurückgegebenen Daten ein oder nicht.

Thumbnail höhe (px) - die Höhe des Thumbnail-Bildes in Pixeln. NUR aktiviert, wenn das Kästchen Miniaturbild einschließen markiert ist. Der Wert sollte zwischen 32 und 128 Pixeln liegen.

Objektbilder einschließen - schließt Objektbilder in die zurückgegebenen Daten ein oder nicht.

Aktiviere Bilder HW-Dekodierung - aktivieren Sie die Dekodierung der eingegebenen Bilder mit der am besten geeigneten Computerplattform (CUDA, DXVA oder DirectX).

Einstellungen für den Objektdatenspeicher

Um die maximale Anzahl von Ereignissen, die in der Datenbank gespeichert werden sollen, und den Zeitraum, in dem diese Ereignisse aufbewahrt werden sollen, auszuwählen, gehen Sie im System-Manager zu Systemeinstellungen > Objektdatenspeichereinstellungen.




Pagination
Previous page
Einstellungen für die Face Recognition (FR)
Next page
VCA-Einstellungen