# Hinzufügen von Kameras über eine CSV-Datei | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/hinzufugen-von-kameras-uber-eine-csv-datei

Hinzufügen von Kameras über eine CSV-Datei

VSM-Kameraeinstellungen können in eine CSV-Datei exportiert und aus einer CSF-Datei in VMS importiert werden. Auf diese Weise können Administratoren umfangreiche Änderungen an den Kameraeinstellungen vornehmen und die geänderten Einstellungen anschließend in das VMS-System importieren. Es ist auch möglich, mit dieser Funktion neue Kameras zu VMS hinzuzufügen.

CSV file import and export

Der System-Manager Hardware-Einstellungen verfügt über die folgenden Schaltflächen zum Exportieren von Kameraeinstellungen in eine Datei und zum Importieren von Kameraeinstellungen aus einer Datei im CSV-Format.




CSV-Dateiformat

Das CSV-Dateiformat verwendet für jede Kamera die folgenden Kopfzeilen.

Name - Name des Kamerakanals.

Nummer - Nummer des Kamerakanals auf dem VMS-Server.

Beschreibung - Beschreibung des Kamerakanals.

AdmDescription - Administrative Beschreibung des Kamerakanals.

Adresse - Adresse des Kamerageräts.

Port - Anschluss des Kamerageräts.

UserName - Benutzername für das Kameragerät.

Passwort - Passwort für das Kameragerät.

Driver - Treibername / native (Suche unter allen verfügbaren nativen Treibern) / onvif (Verwendung des ONVIF-Treibers). Logic verwendet den ersten Treiber, der die angegebene Zeichenkette für den Treibernamen enthält. Zum Beispiel, Achse → NewAxisIPCapture.

Kanal - Verwendeter Kanal des Treibers, wenn das Gerät mehr als einen Kanal unterstützt. Bei Ein-Kanal-Geräten kann dies leer bleiben.

IsInUse - Ist die Kamera in Gebrauch.

IsAudioInUse - Ist Audio in Gebrauch, wenn der Treiber dies unterstützt.

IsIOInUse - Ist I/O in Gebrauch. Dies hat nur beim Export von CSV-Dateien eine Bedeutung. Beim Import wird E/A automatisch verwendet, wenn das Gerät dies unterstützt.

Ist360 - Ist 360 Kamera.

Framerate - Bilder / Sekunde des Aufnahmestroms, gerundet auf den nächsten verfügbaren Wert. Kopfzeile für andere Streams: Framerate1, Framerate2, Framerate3.

Auflösung - Auflösung des Aufnahmestreams im Format Breite x Höhe (z. B. 1920x1080), gerundet auf den nächstmöglichen Wert. Für andere Streams: Auflösung1, Auflösung2, Auflösung3.

Codec - Verwendeter Komprimierungscodec des Aufnahmestreams. Gerundet auf den nächsten verfügbaren Wert: JPEG, MPEG, H264, WMC9, PARSE, H265, MXPEG. Für andere Streams: Codec1, Codec2, Codec3.

Qualität - Komprimierungsqualität des Aufnahmestreams, gerundet auf den nächsten verfügbaren Wert im Bereich 1-100. Für andere Streams: Qualität1, Qualität2, Qualität3.

Bitrate - Bitrate des Aufnahmestreams, gerundet auf den nächstmöglichen Wert. Für andere Streams: Bitrate1, Bitrate2, Bitrate3.

Exportieren

Der Benutzer kann den Ordner auswählen, in den die CSV-Datei mit den Kameraeinstellungen exportiert werden soll, und einen Namen für die Datei vergeben. Sie können auch das Trennzeichen festlegen, das in der CSV-Datei verwendet wird.

Wenn der Export erfolgreich war, wird ein blinkendes grünes Symbol angezeigt. Bei einem Fehler wird ein blinkendes rotes Symbol angezeigt.

Importieren

Wenn ein Benutzer auf die Schaltfläche Importieren klickt, wird der Dialog Datei auswählen angezeigt, um die zu importierende CSV-Datei auszuwählen. Wenn die Datei ausgewählt ist, wird die Ansicht zum Hinzufügen der Kamera angezeigt, wenn das Parsen und die Validierung der CSV-Datei erfolgreich durchgeführt wurden.

Die folgenden Überprüfungsregeln werden beim Parsen importierter CSV-Dateien verwendet.

Das Spaltenbegrenzungszeichen der CSV-Datei ist ein Komma (,) oder Semikolon (;).

Die Reihenfolge der Kopfzeilennamen (d. h. die Spaltenreihenfolge) ist frei.

Nicht verwendete Kopfzeilennamen (d. h. Spalten) können weggelassen werden.

Nur der Name der Kopfzeile Adresse ist obligatorisch. Fehlt er, werden die Daten der CSV-Datei nicht akzeptiert.

Wenn einige Eigenschaftsnamen und Daten nicht vorhanden sind, wird ein interner Standardwert verwendet.

Bei Validierungsfehlern und -warnungen wird ein Popup-Fenster erzeugt, und weitere Informationen werden im Systemmanager-Protokoll ausgedruckt.

Kameras, die über CSV importiert werden, können als Teil des Importvorgangs in den passiven Modus versetzt werden. Systemadministratoren können diese Einstellung in der CSV-Datei festlegen.

Mehrere Streaming-Status (aktiviert oder deaktiviert) können verwendet werden, wenn dies von der Kamera unterstützt wird, ebenso wie der Bitratenmodus für die Bitrate.

Audiokanäle sollten nicht automatisch hinzugefügt werden, wenn sie beim Importieren von CSV-Dateien nicht hinzugefügt wurden.

Bitte beachten Sie, dass beim Import von Mehrkanalgeräten mit einer festgelegten Kanalnummer in der Spalte "Anzahl" für jedes Gerät eine Kanalnummer manuell definiert werden muss. Außerdem ist es notwendig, die Kanalnummer des Rekorders (aus der Spalte "Anzahl") der Kanalnummer des Geräts (Spalte "Kanal") zuzuordnen. Dieses Problem kann gelöst werden, indem die Spalten "Anzahl" und "Kanal" nicht einbezogen werden.

Nach der Validierung und dem Parsen der CSV-Datei informiert die Statusspalte darüber, ob die Kamera bereits zum System hinzugefügt wurde (bereits vorhanden) oder ob es sich um eine neue Kamera handelt (nicht hinzugefügt).

Die Kontrollkästchen Hinzufügen und Ändern werden angezeigt, wenn in der importierten CSV-Datei Änderungen an vorhandenen Kameras und neuen Kamerakonfigurationen vorgenommen wurden. Mit diesen Optionen können Sie auswählen, ob Kameras aus der CSV-Datei hinzugefügt und/oder geändert werden sollen.

Die Schaltfläche Ausführen ist aktiviert, wenn es Kameras gibt, die hinzugefügt oder geändert werden sollen. Wenn Sie auf die Schaltfläche Ausführen klicken, werden die Einstellungen aus der CSV-Datei auf die aktuellen Einstellungen angewendet (geändert und/oder hinzugefügt). Nachdem die Einstellungen übernommen wurden, wird der Status für jede Kamera aktualisiert.

Der Dialog kann nach dem Übernehmen der Einstellungen durch Klicken auf die Schaltfläche ok oder vor dem Übernehmen der Einstellungen durch Klicken auf die Schaltfläche cancel geschlossen werden.

Geänderte Kameraeinstellungen und/oder hinzugefügte Kameras werden auf den VMS-Server angewendet, sobald die Hardwareeinstellungen gespeichert sind.




Pagination
Previous page
Geräteeinstellungen
Next page
Hinzufügen und Entfernen von VMS-Servern