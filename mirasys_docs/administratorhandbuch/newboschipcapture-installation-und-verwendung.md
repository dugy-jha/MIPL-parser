# NewBoschIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/newboschipcapture-installation-und-verwendung

NewBoschIPCapture - Installation und Verwendung

Wenn sich zwischen VMS und den Kameras eine Firewall befindet, müssen die folgenden RTSP/UDP/HTTP- oder HTTPS-Ports geöffnet sein:HTTP: default port is 80,

HTTPS: Der Standard-Port ist 443,

RTSP: Der Standard-Port ist 554,

UDP: Pro Video-/Audio-Stream sind zwei aufeinanderfolgende Ports in einem Portbereich von 3556 bis 4556 erforderlich.

Wenn beispielsweise 4 IP-Kameras in einem DVMS vorhanden sind, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Für den MPEG-4-Videostream-Empfang verwendet der Treiber die Bosch RCP+ SDK-Bibliothek. Er öffnet beliebige UDP-Ports für den Empfang von Videodaten. Der Treiber kann mithilfe einer XML-Konfigurationsdatei konfiguriert werden, um die folgenden Parameter für die Bosch IP-Geräte festzulegen:

PTZ protocol (PelcoD, OSRD, BiCom)

Fish-eye video channel (only one can be used)

Jpeg stream (Recording, Live or Remote, default Remote)

Edge storage functionality support

Time sync (enabled / disabled)

Control mode (active/passive)

Transport

Key frame interval

Video loss check (enabled / disabled)

Einschränkungen

Für alle Bosch-Geräte sollten ein Benutzer und ein Passwort festgelegt sein. Andernfalls erkennen die Treiber die Kamera nicht (das Passwort sollte nicht leer sein).

Der Systemmanager kann den Treiber für ältere Versionen mit abonnierten Bosch Kameras ab VMS 7.0 auf 1.3.0.0 aktualisieren. Bei älteren VMS-Versionen sollten die Kameras aus DVMS entfernt und nach der Treiberaktualisierung wieder hinzugefügt werden.

Wenn die Kamera ohne Audiokanäle hinzugefügt wurde, sollte die Kamera auch entfernt und erneut zu DVMS hinzugefügt werden, um sie zu aktivieren.

Der Treiber entfernt oder ändert den alten BoschIPCapture-Treiber nicht, sondern verwendet die rcpp.dll wie der alte Treiber.

Um den Treiber zu installieren, sollten also keine Bosch-Kameras angeschlossen sein. Andernfalls wird die Installation des Treibers fehlschlagen.

Für NTSC-Kameras, die an die Video-Jet-Server-Serie für den MPEG-4-Codec angeschlossen sind, beträgt die maximale Auflösung 352x240 (CIF). Die D1-Auflösung funktioniert nicht, daher wird die CIF-Auflösung anstelle von D1 angezeigt.

Eine Kombination von NTSC- und PAL-Kameras, die an einen Video Jet-Server angeschlossen sind, ist nicht zulässig.

Die tatsächliche Framerate für den MJPEG-Videokanal kann niedriger sein als die in den Einstellungen angegebenen Werte.

Die Qualitätseinstellung im VMS verwendet den Bitratenwert der Kamera oder des Videoservers. Daher kann die tatsächliche Bildqualität bei unterschiedlichen Werten gleich sein (wenn das Bild die angegebenen Bitraten durchlaufen kann).

Bosch PTZ-Kameras verwenden das OSRD-Protokoll zur Steuerung der Kamera. Dieses Protokoll lässt keine Änderung der Blenden-/Fokussiergeschwindigkeit zu. Daher können Blende und Fokus mit einem vordefinierten Geschwindigkeitswert ausgeführt werden. Die Geschwindigkeitswerte können über das Web-Interface eingestellt werden. Diese Einstellungen für die VG4 AutoDome Kamera finden Sie hier: Einstellungen > Erweiterter Modus > Kamera > Objektiv > Einstellungsgruppe 1

Das OSRD-Protokoll erlaubt es nicht, Voreinstellungen zu löschen. Auch die VG4-Kamera erlaubt es nicht, eine bestehende Präposition ohne Bestätigung zu überschreiben. Die Kamera zeigt die Frage „Overwrite current scene?“ als OSD-Menü mit den Tasten [Yes] und [No] an.

Die Änderung von Fokus/Blende wird zur Bestätigung der Auswahl verwendet. Der Treiber sendet den Iris-Befehl nach dem Speichern der Voreinstellung, damit der Benutzer die Überschreibung der Voreinstellung nicht manuell bestätigen muss. Dieser Algorithmus hat ein Problem: Wenn der Präpositions-Slot leer ist (noch nicht gespeichert), wird der Text für die Irisänderung angezeigt.

Bosch Videoserver geben PTZ-Befehle an Kameras weiter, die über den seriellen Anschluss angeschlossen sind. Es gibt keine Möglichkeit, die Kennung der Kamera über die Standard-Serveroptionen zu konfigurieren. Angeschlossene Kameras müssen daher korrekt konfiguriert sein (Hardware-Einstellungen der Kamera), um die PTZ-Steuerung zu ermöglichen:

Das PTZ-Protokoll sollte Pelco-D sein.

Die Kennung der PTZ-Kamera sollte mit der Nummer des Videokanals übereinstimmen. Bei einer Kamera, die an den zweiten Videoeingang angeschlossen ist, sollte die Kamera-ID beispielsweise auf 2 gesetzt werden.

Die anderen Einstellungen des seriellen Ports sollten mit denen des Servers übereinstimmen (Baudrate, Paritätsbit, Stoppbit usw.).

Bosch Videoserver haben keine interne PTZ-Funktionalität. Es werden nur Befehle an die seriellen Anschlüsse mit angeschlossenen Kameras weitergeleitet. Der Treiber kann also nicht erkennen, welche Funktion an der Kamera am seriellen Anschluss angeschlossen ist und ob es sich um eine PTZ-Kamera handelt.

Aufgrund dieser Funktion werden alle Server-Videokanäle als PTZ angezeigt.

NBC255 und NVC255 haben VGA- und QVGA-Auflösungen. DVMS zeigt stattdessen D1 und CIF an. (Diese Modelle können nicht über die Geräteeigenschaften erkannt werden)

Das Mehrfach-Streaming erfolgt entsprechend den Fähigkeiten der Encoder.

Jeder Videokanal verfügt über zwei Encoder mit der Anzahl der unterstützten Auflösungen, so dass nicht alle Auflösungen für Aufnahme- und Live-Streams verfügbar sind.

Einige Auflösungen werden nur durch spezielle Kombinationen auf dem ersten und zweiten Encoder unterstützt, so dass die Auflösung des Live-Streams von den Einstellungen abweichen kann, wenn sie nicht mit der aktuellen Aufnahmeauflösung eingestellt werden kann.

Der Remote-Stream ist MJPEG; er verfügt über alle verfügbaren Auflösungen.

Einschränkungen beim Streaming

Um die H.264-Auflösung und -Framerate für den sekundären Stream zu ändern, muss der Modus „Stream 1 kopieren“ in der Weboberfläche deaktiviert werden (Einstellungen -> Erweiterter Modus -> Kamera -> Encoder-Streams -> Stream 2 -> Die Eigenschaft „Stream 1 kopieren“ gilt NICHT für „Stream 2“);

Es ist nicht möglich, mehrere Auflösungen anzuwenden (jeder Videokanal verfügt über zwei Encoder mit unterschiedlichen unterstützten Auflösungen);

Der Remote-Stream ist MJPEG mit allen verfügbaren Auflösungen.

MJPEG im Mehrfach-Streaming-Modus funktioniert nicht bei alten Serien mit Firmware 4.x

Die Bewegungserkennung für PTZ-Kameras muss auf der Webseite der Kamera nach jeder Kamerabewegung konfiguriert werden (Einschränkung von Bosch).

Privatzonen für PTZ-Kameras werden nicht unterstützt.

Kameras, die über einen COM-Anschluss verfügen, werden in DVMS als PTZ-Kameras angezeigt. Sie können an die PTZ-Plattform angeschlossen werden und PTZ wird funktionieren.

Der Treiber synchronisiert die Zeit des PCs mit der Kamera unter Verwendung der UTC-Zeit (GMT+00:00) für die Edge-Storage-Funktion. Edge-Storage wird nicht korrekt funktionieren, wenn die Zeit auf eine andere geändert wird.

Die Edge-Storage-Funktionalität funktioniert nur bei Netzwerkausfällen zwischen Kamera und VMS.

Wenn VMS neu gestartet oder der Treiber geschlossen wurde, empfängt DVMS keine aufgezeichneten Videos von der Kamera.

Außerdem sollte die Aufzeichnung auf der Kamera konfiguriert sein, um die Edge-Storage-Funktionalität in VMS zu nutzen.

Einschränkungen bei der Multicast-Erfassung

Die Treiberinstanz kann so konfiguriert werden, dass sie als aktive oder passive Instanz verwendet wird. Die aktive Instanz kann die IP-Geräteeinstellungen ändern und zusätzliche Funktionen nutzen. Passive Instanzen können Video- und Audioströme per Multicast empfangen und ermöglichen die Nutzung digitaler E/A-Funktionen.

Die Passivfunktion ändert die folgenden Kameraeinstellungen nicht:

Codec

Quality

Resolution

Framerate

Die Kamera sollte dem aktiven Rekorder hinzugefügt werden, bevor sie in der passiven Konfiguration verwendet wird.

Der Benutzer sollte sicherstellen, dass nur ein Rekorder die Einstellungen der Kamera ändert. Andere Rekorder, die diese Kamera verwenden, sollten sich im passiven Modus befinden.

Wenn mehr als ein Netzwerkadapter vorhanden ist, muss die IP-Adresse des Netzwerkadapters angegeben werden, über den die Kamera angeschlossen ist, um Multicast-Streaming korrekt zu empfangen. Der in Windows als Standard markierte Netzwerkadapter wird verwendet, wenn keine Option konfiguriert ist. Für den Audiokanal sollte der Netzwerkadapter (falls mehrere Netzwerkadapter im PC verwendet werden) in der XML-Datei festgelegt werden, die dynamische Benutzeroberfläche wird nur für den Videokanal verwendet.

Die Zeitsynchronisierung ist für den passiven Speicher deaktiviert und der Edge-Speicher funktioniert möglicherweise nicht richtig.

Die Verwendung sollte die Zeitsynchronisation für den PC mit dem Aktiv-Modus-Recorder und den PC mit dem Passiv-Modus-Recorder gewährleisten.

Alte Bosch-Serien mit Firmware 4.x haben die folgende Einschränkung:

Der HTTPS-Modus funktioniert nicht

MJPEG im Multicast-Modus funktioniert nicht (nur JPEG-Anfragen über HTTP)

Privacy Zones für Firmware 6.22 werden nicht unterstützt.

Alte Bosch-Serien (wie Gen4) führen manchmal „Auto Bounding“ durch. Während dieses Prozesses ist der Stream von der Kamera nicht flüssig.

Im passiven Modus sollten alte Kameras mit MPEG4-Unterstützung auf das richtige Kompressionsformat eingestellt werden, sonst wird „Kein Signal“ angezeigt.

Die Aufzeichnung im Edge-Storage sollte im Web-Interface der Kamera auf den 1.

Die Bosch IP-Geräte geben möglicherweise keine Informationen über Audiointervalle zurück, die über RCP+-Anfragen auf dem Speicher des Geräts aufgezeichnet wurden (durch num = 90 + Kanal-ID). Dies führt dazu, dass die Audio-Edge-Funktionalität nicht korrekt funktioniert. Das Problem wurde den Bosch-Technikern gemeldet (am 20/Nov/2019), aber es gibt noch keine Lösung.

Nicht alle Bosch-Kameras können Bewegung erkennen, daher sollte auf der Webseite der Kamera geprüft werden, ob sie Bewegungserkennung unterstützt oder nicht.

So verwenden Sie die Kamera im gesicherten Modus

Installieren Sie ein Zertifikat auf der Kamera und dem PC mit Rekorder

Stellen Sie den RTP-über-HTTP-Streaming-Modus in den Kameraeinstellungen im Systemmanager ein;

Stellen Sie die korrekten Anmeldedaten für die Kamera ein (für das Senden von Audio an die Kamera, wenn dies nicht erforderlich ist - es können beliebige Anmeldedaten verwendet werden, die Authentifizierung erfolgt über ein Zertifikat); Audio an die Kamera ist nicht gesichert, daher sind korrekte Anmeldedaten erforderlich, um zu funktionieren.Bosch-Kameras mit H.264- und H.265-Unterstützung sollten vor dem Hinzufügen zu DVMS auf den erforderlichen Codec eingestellt werden, da einige Kameras für jeden Codec eine andere Liste der unterstützten Auflösungen / Frameraten haben.

Die von der Kamera unterstützten Auflösungen hängen vom aktuell eingestellten Codec (H.264 / H.265) ab. Die Kamera wird also mit dem aktuell eingestellten Codec hinzugefügt, DVMS wird diesen während des Hinzufügens der Kamera nicht ändern.

Die Videoverlustprüfung wird nur für Encoder mit analogen Kameras verwendet, um zu erkennen, ob die Kamera funktioniert oder nicht. Sie sollte nicht für andere Bosch Geräte verwendet werden.

Wenn der Audiocodec geändert wurde, muss die SD-Karte formatiert werden, da der Treiber versucht, den Ton mit den aktuellen Einstellungen zu empfangen. Wenn für die Kamera AAC eingestellt ist, die Aufzeichnung aber für G711 durchgeführt wurde, werden Edge-Audiodaten nicht korrekt empfangen.

Beim Streaming mit mehreren Kanälen sollten alle Kanäle denselben Codec (H.264 oder H.265) haben, da Bosch-Kameras nicht beide gleichzeitig streamen können.

Bosch Geräte verarbeiten den RTSP PAUSE-Befehl nicht korrekt (der Stream wird danach weiter gesendet).

Daher verwenden wir RTSP TEARDOWN, um den Stream anzuhalten, wenn keine Bewegung stattfindet (wenn kamerabasiertes MD verwendet wird).

Pagination
Previous page
NewAxisIPCapture - Installation und Verwendung
Next page
NewIQEyeIPCapture - Installation und Verwendung