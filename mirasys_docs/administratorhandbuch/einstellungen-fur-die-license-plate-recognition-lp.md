# Einstellungen für die License Plate Recognition (LPR) | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/einstellungen-fur-die-license-plate-recognition-lp

Einstellungen für die License Plate Recognition (LPR)

Systemadministrator-Einstellungen, die es Betreibern ermöglichen, die Nummernschilderkennung in Spotter Smart Search und Spotter Smart Recognition zu nutzen.

Für die Smart LPR-Funktion ist eine RTSP-Server-Streaming-Lizenz erforderlich.

Einstellungen für die License Plate Recognition

Die Einstellungen für die Nummernschilderkennung finden Sie im Systemmanager auf der Registerkarte VMS-Server > Kameras.

Wechseln Sie im Fenster Kameraeinstellungen zur Registerkarte LPR-Einstellungen.

Wenn Ihre Lizenz die Smart LPR-Funktion nicht unterstützt, wird die Registerkarte LPR-Einstellungen ausgeblendet.

Kamera auswählen, streamen und LPR aktivieren

Wählen Sie die Kamera aus dem Dropdown-Menü in LPR

Wenn es mehr als einen Stream gibt, können Sie den Stream auswählen. Wenn nur ein Stream vorhanden ist, gibt es einen Standardstream wie in der Abbildung oben, und das Dropdown-Menü ist deaktiviert.

Sie können erst dann einen Dienst auswählen, wenn Sie den Dienst durch Anklicken des Kästchens LPR für ausgewählte Kamera aktivieren aktiviert haben.

Wenn das Kontrollkästchen LPR für die ausgewählte Kamera aktivieren nicht markiert ist, ist das Dropdown-Menü Dienst deaktiviert.

Das Textfeld Lizenz zeigt die Anzahl der verwendeten Lizenzen und die maximale Anzahl der Lizenzen an.

Erkennungsparameter

Nachdem die Kamera, ihr Stream und der LPR-Erkennungsdienst ausgewählt wurden, können die Kennzeichenerkennungseinstellungen angepasst werden. Die Kennzeichenerkennungseinstellungen befinden sich im Gruppenfeld Erkennungsparameter auf der Registerkarte LPR-Einstellungen im Fenster Kameraeinstellungen.

Die Kennzeichenerkennungseinstellungen werden für die Konfiguration des Kennzeichenerkennungsdetektors verwendet.

Bereich von Interesse - Definieren Sie den Bereich, in dem die Erkennungen durchgeführt werden.

Verzögerung bei gleichem Kennzeichen - die Anzahl der Sekunden, die vergehen sollen, bevor das gleiche Kennzeichen zweimal gelesen wird.

Max plates - maximale Anzahl der zu erkennenden Platten. Erkannte Kennzeichen werden in absteigender Reihenfolge nach der Kennzeichenkonfidenznummer sortiert.

Minimale Zeichenkonfidenz - Konfidenzniveau für die Erkennung von Plattenzeichen. Gültige Werte liegen zwischen 25% und 95%.

Minimale Kennzeichenkonfidenz - Konfidenzniveau des Erkenners. Gültige Werte liegen im Bereich von 25% - 95%.

Minimale Plattenhöhe - minimale Plattenhöhe in %. Gültige Werte liegen im Bereich von 1% - 50%. Der Standardwert ist 5%.

Erkennungsintervall - die Anzahl der Millisekunden, die beschreibt, wie oft die Kennzeichenerkennung durchgeführt wird: wenn es z.B. 250ms ist, dann wird die Kennzeichenerkennung 4 mal in einer Sekunde durchgeführt (auch wenn die Bildrate des Videostroms viel höher ist, wie 30 fps).

Gerät - wird für die Inferenz verwendet. Die verfügbaren Geräte hängen von der Hardware des aktuellen Dienstes ab.

Region - Das Erkennungsmodell (Eurasien oder Amerika), das für die Erkennung verwendet werden soll.

Minimum country confidence - Konfidenzniveau des Ländererkenners. Gültige Werte liegen zwischen 25% und 95%.

Ländererkennung aktivieren - Aktivieren oder Deaktivieren der Ländererkennung. Die Aktivierung der Ländererkennung kann in einigen Fällen die Kennzeichenerkennung verbessern.

Kennzeichenbilder einbeziehen - Kennzeichenbilder in die zurückgegebenen Daten einbeziehen oder nicht.

Bilder HW-Dekodierung aktivieren - aktiviert die Dekodierung von Eingabebildern mit der am besten geeigneten Computerplattform (CUDA, DXVA oder DirectX).

Einstellungen speichern

Klicken Sie auf die Schaltfläche OK mit dem grünen Häkchensymbol am unteren Rand des Fensters Kameraeinstellungen.

Klicken Sie auf die Schaltfläche Abbrechen mit dem roten Kreuzsymbol, um das Speichern der LPR-Einstellungen abzubrechen und zu den Einstellungswerten zurückzukehren, die nach dem Öffnen der Anwendung System-Manager geladen wurden.

Die LPR-Einstellungen für die ausgewählte Kamera werden nach dem Einschalten anderer Kameras, Streams oder Registerkarten vorübergehend gespeichert.

Wenn Sie die Stream-Einstellungen für die ausgewählte Kamera und den ausgewählten Erkennungs-Stream löschen möchten, wählen Sie im Feld Dienstname Combobx für die ausgewählte Kamera und den ausgewählten Erkennungs-Stream "Keine" aus.

Einfluss auf die Einstellungen

Die folgenden Aktionen wirken sich unabhängig von den Aktionen auf der Registerkarte LPR-Einstellungen auf die Diensteinstellungen aus:

Löschen eines Rekorders: Beim Löschen eines Rekorders werden alle Streams in den Einstellungen aller LPR-Dienste, die mit dem entfernten Rekorder gearbeitet haben, gelöscht und die LPR-Einstellungen gespeichert.

Löschen einer Kamera: Beim Löschen einer Kamera wird der Stream in den Einstellungen aller LPR-Dienste, die mit dieser Kamera gearbeitet haben, und beim Speichern der LPR-Einstellungen gelöscht. Es gibt eine Regel - eine Kamera mit einem Stream kann nur von einem LPR-Dienst verwendet werden, aber ein LPR-Dienst kann mit mehreren Kameras arbeiten.

Ändern der Bildgröße und des Kompressionstyps auf der Unterregisterkarte Streams der Registerkarte Allgemein: Wenn Sie die Auflösung oder den Kompressionstyp für die Kamera und den Stream ändern, die in den Einstellungen eines beliebigen LPR-Dienstes enthalten sind, werden die Einstellungen des LPR-Dienstes geändert und gespeichert, wenn das Fenster Kameraeinstellungen geschlossen wird.

Ändern der RTSP-Streaming-Einstellungen in der Gruppe "Streaming-Einstellungen" auf der Registerkarte "RTSP-Server-Streaming": Wenn Sie das "Kennwort", den "Benutzernamen", den "RTSP-Port" und den "Streaming-Modus" (Sicherheitstyp) für die ausgewählte Kamera und den Stream ändern, die in den Einstellungen eines beliebigen LPR-Dienstes enthalten sind, werden die Einstellungen des LPR-Dienstes geändert und gespeichert, wenn das Fenster "Kameraeinstellungen" geschlossen wird.

Ändern der Bildgröße in der Gruppe "Geräteeinstellungen" auf der Registerkarte "Video" im Fenster "Hardware-Einstellungen": Wenn Sie die Auflösung für die ausgewählte Kamera ändern (hier ist es möglich, die Auflösung nur für den Aufzeichnungs-Stream zu ändern), die in den Einstellungen eines beliebigen LPR-Dienstes vorhanden ist, werden die Einstellungen des LPR-Dienstes geändert und gespeichert, wenn das Fenster "Hardware-Einstellungen" geschlossen wird.

Ändern der Kamera durch Klicken auf die Schaltfläche IP-Kamera bearbeiten auf der Registerkarte Video im Fenster Hardware-Einstellungen: Wenn Sie die Kamera durch Klicken auf die Schaltfläche IP-Kamera bearbeiten ändern, werden die Auflösung und der Kompressionstyp für die neue Kamera (nur für Aufzeichnungs-Stream) in den Einstellungen des LPR-Dienstes neu geschrieben, wo die Kamera-ID angezeigt wird.

Pagination
Previous page
Unschärfe von Objekten
Next page
Einstellungen für die Face Recognition (FR)