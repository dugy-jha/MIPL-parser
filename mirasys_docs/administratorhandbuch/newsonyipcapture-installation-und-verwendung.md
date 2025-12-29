# NewSonyIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/newsonyipcapture-installation-und-verwendung

NewSonyIPCapture - Installation und Verwendung

Der Treiber verwendet die folgenden Protokolle für den Videoempfang:

Das HTTP/HTTPS-Protokoll wird für den Empfang von MJPEG-Video- und Bewegungserkennungsdaten verwendet;

RTP/UDP/IP-Protokolle werden für den Empfang von MPEG-4-, H.264-Videostreams und Audiostreams verwendet;

Das RTSP-Protokoll wird für die Steuerung des RTP-Streams für G5 (5. Generation) und neuere Geräte verwendet;

Das HTTP-Protokoll wird zum Senden des Audiostroms an die Kamera verwendet.

Das HTTP/HTTPS-Protokoll wird auch zum Setzen/Abrufen von Parametern verwendet.

Wenn sich zwischen DVMS und den Kameras eine Firewall befindet, müssen die folgenden RTSP/UDP/HTTP/HTTPS-Ports
geöffnet sein:

HTTP: Standard-Port ist 80,

HTTPS: Der Standardanschluss ist 443,

RTSP: Der Standardanschluss ist 554,

UDP: zwei aufeinanderfolgende Ports pro Videostream werden im Portbereich 3556 bis 4556 benötigt.

Beispiel: Wenn 4 SONY IP-Kameras für den Empfang von MPEG-4- oder H.264-Video in einem DVMS konfiguriert sind einem DVMS, dann werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei, wird er übersprungen.

Der Treiber kann mithilfe einer XML-Konfigurationsdatei konfiguriert werden, um die Audioparameter für die SONY G5-G7 IP-Geräte einzustellen.

Beschränkungen

Die Kameramodelle SNC-DM160, SNC-DM110 und SNC-CM120 unterstützen eine Lichttrichterfunktion:

Der Treiber setzt den Lichttrichter immer auf den Modus „Auto“. Wenn er bei geringer Beleuchtung aktiv wird, erhöht er die Bildempfindlichkeit, schaltet aber bei einer Auflösung von 1280x960 automatisch auf eine niedrigere Auflösung von 640x480 um.

Die Aktivierungs-/Deaktivierungsverzögerung des Lichttrichters beträgt etwa 40 Sekunden.

Der Lichttrichter funktioniert nicht, wenn einer der folgenden Werte eingestellt ist:

Die Bildgröße ist eine der folgenden:

JPEG - 960x720: MPEG4 - AUS

JPEG - 768x576: MPEG4 - AUS

JPEG-Beschneidung ist eingeschaltet

SolidPTZ ist eingeschaltet

Blende offen ist eingeschaltet.

Bitte beachten Sie, dass bei ausgeschaltetem Lichttrichter die maximale Bildrate 15 fps beträgt. Weitere Einzelheiten finden Sie im Benutzerhandbuch der Kamera.

Bei hohen Bildauflösungen kann die Bildrate niedriger als gewünscht sein.

Hinweise zur Funktion Analoger Videoausgang

Der Treiber deaktiviert die Funktion Analog Video-Out für SONY G4 IP-Kameras (4. Generation). Die Aktivierung dieser Funktion führt zu einer Einschränkung der unterstützten Codecs und Auflösungen (z. B. unterstützt die Kamera SCN-CS20 nur die Auflösung 640x480).

Der Treiber ändert die Einstellung für den analogen Videoausgang bei G5/G6 SONY IP-Kameras nicht. Bitte beachten Sie, dass die Leistung der Kamera beeinträchtigt werden kann, wenn diese Funktion auf „Ein“ eingestellt ist.

Hinweise zur Bewegungserkennungsfunktion

Bitte konfigurieren Sie die Bewegungserkennungszonen manuell über die Weboberfläche, bevor Sie die Bewegungserkennungstreiberfunktion verwenden.

SONY-Kameras senden möglicherweise nicht den korrekten Stream von Bewegungsereignissen, wenn die Seite Bewegungserkennung auf der Weboberfläche der Kamera geöffnet wird. Dies bedeutet, dass die MD-Funktionalität in diesem Fall nicht korrekt funktioniert.

Andere Einschränkungen

Die Kameras SNC-DM160, SNC-DM110 und SNC-CM120 unterstützen die Auflösungen 1280x960, 960x720 und 768x576 und werden nur mit JPEG-Komprimierung verwendet, aber diese Auflösungen werden auch mit MPEG-4 in den Kameraeinstellungen im System Manager angezeigt. Wenn eine dieser Auflösungen mit MPEG-4 ausgewählt wird, ist die tatsächliche Auflösung immer 640x480.

Die Kameras SNC-CS20, SNC-DS60 und SNC-DS10 unterstützen nur die Auflösung 768x576 bei JPEG-Kompression, aber diese Auflösung wird im System Manager auch bei MPEG-4 angezeigt.

Alle P-Modelle der G3-Kameras (3. Generation) haben eine maximale Framerate von 8 fps (N-Modelle 10 fps) mit H.264-Kompression, aber die Kameraeinstellungen im System Manager zeigen 25 fps als Maximum an. Da einige Kameramodelle bis zu 12 fps liefern können, verwendet der Treiber diesen Wert als maximale Framerate.

Bei JPEG-Kompression zeigt der System Manager die Frameraten der G2-Kameras (2. Generation) mit 1 bis 25 an, die Kameras unterstützen jedoch nur 5, 6, 8, 10, 15, 20 (und 30 im NTSC-Modus) fps.

Die Voreinstellungsfunktion und die Funktion für Privatzonen funktionieren in DVMS 5.9.8 nicht korrekt. Dieses Problem wird durch die Inkompatibilität einiger Programmschnittstellen verursacht.

In einigen Fällen senden SONY-Kameras Videos für den MJPEG-Codec mit einer höheren Bildrate als erforderlich. Zum Beispiel sendet die SONY SNC-Z20P Kamera nach dem Zoomen einen MJPEG-Videostream mit 24-25 fps, auch wenn die Bildrate im Systemmanager auf 20 eingestellt ist. Dies ist eine Funktion der Firmware der Kamera.

Die SONY SNC-Z20-Kamera sendet einen MJPEG-Videostrom mit einer niedrigeren Bildrate als erforderlich, wenn die maximale Auflösung und die Qualitätseinstellungen festgelegt sind. Zum Beispiel kann die maximale Bildrate bei einer Auflösung von 736x544 und einer Qualitätseinstellung von 100 % nicht höher als 3 sein. Dies ist eine Funktion der Kamera.

Die SONY SNC-Z20-Kamera unterstützt die Funktionen Zoom und Fokus, aber nicht die Funktion Schwenken/Neigen. DVMS zeigt jedoch in jedem Fall die Schwenk-/Neigefunktion im Gerätefenster an (auch wenn die Kamera die Schwenk-/Neigefunktion nicht unterstützt und diese Funktion im Treiber deaktiviert ist). Dies ist ein VMS-Problem.

Die SONY SNC-Z20 Kamera unterstützt keine Voreinstellungsfunktion. Aber die Schaltfläche „Voreinstellung hinzufügen“ ist in DVMS 5.4.4 für sie immer aktiviert. Dies ist ein VMS-Problem.

Die SONY SNC-CH210 unterstützt die Auflösung 2048x1536 nur für den MJPEG-Videocodec (das Seitenverhältnis sollte auf 16:9 eingestellt werden). Für andere Codecs beträgt die maximale Auflösung 1600x1200.

Einige G5-Kameras (5. Generation) haben eine Beschränkung für die Größe des Datenschutzrechtecks. Das Rechteck darf nicht größer als 1/16 des Kamerabildes sein:

640x480 Pixel für SNC-CH220/DH220-Kameras (bezogen auf die maximale Auflösung von 1920x1080)

200x140 Pixel für SNC-EM520/EM521-Kameras (bezogen auf die maximale Auflösung von 800x600)So, real privacy zones may be lower than applied by users because of this camera's feature.

SONY G5 Kameras senden HD-Videostreams mit einer Geschwindigkeit von bis zu 15 Mbps. Das Abonnieren von Videos mit HD-Auflösung

Hochqualitätsvideos für H.264/MPEG-4-Codec oder HD-Auflösungsvideos für MJPEG-Codec von mehr als einer Kamera können zu Verzögerungen im Videostrom führen. Zum Beispiel springt die tatsächliche Bildrate bei einer Einstellung von 15 fps in einem Intervall von 2..13.

SONY G5/G6-Kameras starten ihren eigenen Video-Encoder neu, nachdem die Videooptionen geändert wurden. Dieser Vorgang dauert 3-8 Sekunden, so dass die Funktionen CCRiA und CCFiA (Ändern der Optionen durch Alarm) bei diesen Kameras nicht verwendet werden können.

Die SONY SNC-VB630-Kamera startet den H.264-Stream bei Bewegung mit 10-20 Bildern pro Sekunde statt mit 50 Bildern pro Sekunde, wenn eine Qualität von 1 % ausgewählt ist. Bitte verwenden Sie einen Qualitätswert von 2%, um dieses Verhalten zu vermeiden.

Die SONY G6-Kameras verwenden Qualitätseinstellungen (variable Bitrate), um die Qualität des H.264-Streams festzulegen. Frühere Kameragenerationen verwenden die Option Konstante Bitrate (CBR) für MPEG-4- und H.264-Kodierungen.

Die Funktion für mehrfaches Streaming ist für SONY G5- und G6-Geräte und für DVMS Version 6.1.1 und neuer verfügbar. Ältere SONY-Geräte unterstützen diese Funktion nicht.

Die SONY G5/G6-Kameras wenden die Videoeinstellungen während mehrerer Sekunden an und können während dieses Vorgangs das Streaming anhalten. Daher kann das Starten eines Streams dazu führen, dass andere aktive Streams erneut abonniert werden.

Für SONY G5-Kameras gelten die folgenden Einschränkungen für die Funktion Mehrfach-Streaming

Die Kameras SNC-RS44/RS46/RS84/RS86 unterstützen bis zu 3 Streams. Andere G5-Geräte unterstützen nur 2 Streams (Aufzeichnung und Live)

Die Auflösung des zweiten Streams kann nicht größer als 640x480 sein, es sei denn, sie ist gleich der Auflösung des ersten Streams.Resolution of third stream should be equal to current resolution of first or second stream.

Die G5-Kameras starten möglicherweise keinen Videostream, wenn MJPEG für den Live-Stream mit maximaler Auflösung ausgewählt ist. Dieses Problem wird durch ein unerwartetes Verhalten der Kamera verursacht (RTSP PLAY-Anfrage liefert Fehlercode 451). Bitte ändern Sie die Kodierung oder verringern Sie die Auflösungseinstellungen, wenn Sie dieses Problem feststellen.

Der Treiber wählt während der Anwendung der Einstellungen automatisch die passende Auflösung, wenn die aktuelle Auflösung von der Kamera nicht unterstützt wird. Daher kann die Auflösung des Streams von den im VMS vorgenommenen Einstellungen abweichen. Bitte informieren Sie sich in der Web-Schnittstelle der Kamera über die Einschränkungen der Videoeinstellungen.

Bei den SONY G5/G6-Kameras kann es zu Problemen bei der Kodierung/Dekodierung des G.726-Audiostreams kommen (Rauschen, kein Ton usw.). Bitte verwenden Sie den G.711-Codec, wenn Sie Probleme mit dem G.726-Codec haben.

Die Audioausgabe (Senden an die Kamera) wird bei SONY G6-Kameras nach einem Signalverlust möglicherweise nicht wiederhergestellt.

Die Kamera gibt möglicherweise den HTTP-Fehlercode 503 zurück. Um die Funktion der Audioausgabe wiederherzustellen, starten Sie die Kamera über die Webschnittstelle neu, „System“ - „Initialisieren“ - „Neustart“.

Die Einschränkungen der SONY G7 Kamera

„Ausgabemodi":

Die SONY G7 kann in mehreren verschiedenen „Ausgabemodi“ arbeiten. Die Option „Ausgabemodus“ kann im Abschnitt „System“ - „Installation“ der Webschnittstelle geändert werden.

Bevor Sie diesen Modus ändern, sollten Sie die Kamera aus dem VMS entfernen. Nach dem Ändern des Ausgabemodus muss die Kamera erneut zum System hinzugefügt werden.

Die Funktion „Mehrfaches Streaming“ ist nur in den folgenden „Ausgabemodi“ verfügbar:

„4K-Multi-Streaming“

„Intelligentes Zuschneiden (FullHD)“

„Intelligentes Zuschneiden (VGA)“Die Kamera im Ausgabemodus „HDMI“ kann nicht erkannt und hinzugefügt werden.

Die Liste der verfügbaren Videoauflösungen, Videocodecs und Bildraten ist begrenzt und hängt vom gewählten „Ausgabemodus“ und „Seitenverhältnis“ ab. Bitte fügen Sie die Kamera erneut zum VMS hinzu, nachdem Sie diesen Modus geändert haben.

Die SONY G7-Kameras haben Bildratenwerte mit Fließkomma. Der Treiber rundet den Wert auf die nächstliegende Ganzzahl.

Die Option „H264Quality“ ist für die SONY G7-Geräteserie nicht zulässig. Der Treiber wandelt den Wert „Qualität“ in den Bitratenwert für den H.264-Codec um.

Bei den SONY G7-Kameras in den „4K“-Ausgabemodi kann der hochauflösende H.264-Stream vom DVMS-Videocodec nicht korrekt dekodiert werden, wenn die Option „B-Bild“ auf der Kamera aktiviert ist. Der Treiber deaktiviert diese Option standardmäßig.

Wenn die Edge-Storage-Aufzeichnung aktiviert ist, wird die Bitrate auf 8 Mbps oder weniger für den H.264-Codec begrenzt.

Geräte der SONY H-Serie (wie die Kamera SNC-HM662) verwenden ein anderes SDK als andere SONY G6-Kameras und können nicht mit dem nativen SONY-Treiber hinzugefügt werden. Bitte verwenden Sie stattdessen den Vivotek IP Capture-Treiber für diese Geräteserie.

SONY SNC-EMX32R/52R-Geräte verwenden ein anderes SDK als andere SONY G6/G7-Kameras und können nicht mit dem nativen SONY-Treiber hinzugefügt werden. Bitte verwenden Sie stattdessen den BOSCH-Treiber (NewBoschIPCapture) für diese Geräteserie.

Für die Zeitsynchronisierung gelten die folgenden Regeln:

Der Zeitsynchronisationsvorgang wird durch eine der folgenden Bedingungen ausgelöst:

Änderung der Windows-Systemzeit;

Wechsel der Windows-Zeitzone;

Bei der vorherigen Zeitsynchronisierung ist ein Fehler aufgetreten;

Die letzte erfolgreiche Synchronisierung wurde vor mehr als 30 Minuten durchgeführt.
Diese Bedingungen werden alle 5 Minuten überprüft

Die neue Zeit wird auf dem IP-Gerät eingestellt, wenn der Unterschied zwischen der Zeit des Geräts und der des Rekorders 10 oder mehr Sekunden beträgt.

Die SONY HTTP API ermöglicht die Anwendung der Zeit im GMT-Format, so dass der Treiber die Zeitzoneneinstellungen auf dem IP-Gerät nicht aktualisiert

Die Funktion zum Ändern von Optionen im Alarm (CRiA/CFA) kann nur im „aktiven“ Kontrollmodus verwendet werden. Im „Passiv“-Modus ändert der Treiber keine Optionen auf der IP-Kamera, so dass der Stream weiterläuft, ohne dass sich Auflösung oder Bildrate ändern.

Windows XP wird seit Treiberversion 2.6.0.0 nicht mehr unterstützt.




Pagination
Previous page
NewSiquraIPCapture - Installation und Verwendung
Next page
OnvifIPCapture - Installation und Verwendung