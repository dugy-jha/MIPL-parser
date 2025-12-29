# Einstellungen für die Face Recognition (FR) | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/einstellungen-fur-die-face-recognition-fr

Einstellungen für die Face Recognition (FR)

Systemadministrator-Einstellungen, die es Bedienern ermöglichen, die Gesichtserkennung in Spotter Smart Search und Spotter Smart Recognition zu nutzen.

Für diese Funktion ist eine RTSP-Server-Streaming-Lizenz erforderlich.

Einstellungen für die Face Recognition

Die Einstellungen für die Gesichtserkennung finden Sie im System Manager auf der Registerkarte VMS Server > Kameras.

Gehen Sie im Fenster Kameraeinstellungen auf die Registerkarte FR-Einstellungen.

Wenn Ihre Lizenz die Smart FR-Funktion nicht unterstützt, wird die Registerkarte FR-Einstellungen ausgeblendet.

Kamera auswählen, streamen und FR aktivieren

Wählen Sie die Kamera aus dem Dropdown-Menü in FR

Wenn es mehr als einen Stream gibt, können Sie den Stream auswählen. Wenn nur ein Stream vorhanden ist, gibt es einen Standard-Stream, wie in der Abbildung oben, und das Dropdown-Menü ist deaktiviert.

Sie können einen Dienst erst auswählen, nachdem Sie den Dienst durch Anklicken des Kästchens FR für ausgewählte Kamera aktivieren aktiviert haben.

Wenn das Kästchen FR für ausgewählte Kamera aktivieren nicht angekreuzt ist, ist das Dropdown-Menü Dienst deaktiviert.

Das Textfeld Lizenz zeigt die Anzahl der verwendeten Lizenzen und die maximale Anzahl der Lizenzen an.

Face detection Einstellungen

Nachdem die Kamera, ihr Stream und der FR-Erkennungsdienst ausgewählt wurden, können die Einstellungen für die Gesichtserkennung angepasst werden. Die Einstellungen für die Gesichtserkennung finden Sie im Gruppenfeld Erkennungsparameter auf der Registerkarte FR-Einstellungen im Fenster Kameraeinstellungen.

Erkennungsparameter

Die Gesichtserkennungseinstellungen werden für die Konfiguration des Gesichtserkennungsdetektors verwendet. 

Bereich von Interesse - Definieren Sie den Bereich, in dem die Erkennungen durchgeführt werden.

Max faces - maximale Anzahl der Gesichter, die im Bild erkannt werden sollen. Der Wert sollte zwischen 1 und 5 liegen.

Mindestvertrauen - Vertrauensniveau des Erkenners. Wenn das Vertrauen für das erkannte Gesicht unter diesem Schwellenwert liegt, wird das Gesicht ignoriert. Gültige Werte liegen zwischen 25% und 95%.

Minimale Gesichtshöhe - minimale Gesichtshöhe in %. Gültige Werte liegen zwischen 5 und 50%%. Standardwert 10%.

Minimale Gesichtsähnlichkeit - Wenn die Ähnlichkeit größer oder gleich diesem Wert ist, handelt es sich um dasselbe Gesicht. Der Wert sollte zwischen 50% und 95% liegen.

Verzögerung bei Ereignissen mit demselben Gesicht - die Anzahl der Sekunden, die vergehen sollten, bevor ein Ereignis mit demselben Gesicht auftritt.

Gerät - wird für die Inferenz verwendet. Die verfügbaren Geräte hängen von der Hardware des aktuellen Dienstes ab.

Thumbnail height - die Höhe des Thumbnail-Bildes in Pixeln. Der Wert sollte zwischen 32 und 128 Pixeln liegen.

Miniaturbild einschließen - schließt das Miniaturbild der Erkennungsquelle in die zurückgegebenen Daten ein oder nicht.

Gesichtsbilder einschließen - schließt Gesichtsbilder in die zurückgegebenen Daten ein oder nicht. 

Enable images HW decoding - Aktiviert die Dekodierung von Eingabebildern mit der am besten geeigneten Computerplattform (CUDA, DXVA oder DirectX).

Einstellungen speichern

Klicken Sie auf die Schaltfläche OK mit dem grünen Häkchen am unteren Rand des Fensters Kameraeinstellungen, um zu speichern.

Klicken Sie auf die Schaltfläche Abbrechen mit dem roten Kreuzsymbol, um das Speichern der FR-Einstellungen abzubrechen und zu den Einstellungswerten zurückzukehren, die nach dem Öffnen der Anwendung System Manager geladen wurden.

Wenn Sie Stream-Einstellungen für die ausgewählte Kamera und den ausgewählten Erkennungs-Stream löschen, sollte in der Combobox für den Dienstnamen der Wert "Kein" ausgewählt sein.

Beeinflussung der Einstellungen

Die folgenden Aktionen wirken sich unabhängig von den Aktionen auf der Registerkarte FR-Einstellungen auf die Diensteinstellungen aus:

Löschen eines Rekorders: Beim Löschen eines Rekorders werden alle Streams in den Einstellungen aller FR-Dienste, die mit dem entfernten Rekorder gearbeitet haben, gelöscht und die FR-Einstellungen gespeichert.

Löschen einer Kamera: Beim Löschen einer Kamera wird der Stream in den Einstellungen aller FR-Dienste, die mit dieser Kamera gearbeitet haben, gelöscht und die FR-Einstellungen gespeichert. Es gibt eine Regel - eine Kamera mit einem Stream kann nur von einem FR-Dienst verwendet werden, aber ein FR-Dienst kann mit mehreren Kameras arbeiten.

Ändern der Bildgröße und des Kompressionstyps auf der Unterregisterkarte Streams der Registerkarte Allgemein: Wenn Sie die Auflösung oder den Kompressionstyp für die Kamera und den Stream ändern, die in den Einstellungen eines beliebigen FR-Dienstes vorhanden sind, werden die Einstellungen des FR-Dienstes geändert und gespeichert, wenn das Fenster Kameraeinstellungen geschlossen wird.

Ändern der RTSP-Streaming-Einstellungen in der Gruppe Streaming-Einstellungen auf der Registerkarte RTSP-Server-Streaming: Wenn Sie das "Kennwort", den "Benutzernamen", den "RTSP-Port" und den "Streaming-Modus" (Sicherheitstyp) für die ausgewählte Kamera und den Stream ändern, die in den Einstellungen eines beliebigen FR-Dienstes enthalten sind, werden die Einstellungen des FR-Dienstes geändert und gespeichert, wenn das Fenster Kameraeinstellungen geschlossen wird.

Ändern der Bildgröße in der Gruppe Geräteeinstellungen auf der Registerkarte Video im Fenster Hardware-Einstellungen: Wenn Sie die Auflösung für die ausgewählte Kamera ändern (hier ist es möglich, die Auflösung nur für den Aufzeichnungs-Stream zu ändern), die in den Einstellungen eines beliebigen FR-Dienstes vorhanden ist, werden die Einstellungen des FR-Dienstes geändert und gespeichert, wenn das Fenster Hardware-Einstellungen geschlossen wird.

Ändern der Kamera durch Klicken auf die Schaltfläche IP-Kamera bearbeiten auf der Registerkarte Video im Fenster Hardware-Einstellungen: Wenn Sie die Kamera durch Klicken auf die Schaltfläche IP-Kamera bearbeiten ändern, werden die Auflösung und der Kompressionstyp für die neue Kamera (nur für den Aufzeichnungs-Stream) in den Einstellungen des FR-Dienstes neu geschrieben, wo die Kamera-ID angezeigt wird; die Einstellungen des FR-Dienstes werden geändert und gespeichert, wenn das Fenster Hardware-Einstellungen geschlossen wird.

Pagination
Previous page
Einstellungen für die License Plate Recognition (LPR)
Next page
Einstellungen für die Object Recognition (OR)