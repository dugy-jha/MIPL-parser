# NewPanasonicIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/newpanasonicipcapture-installation-und-verwendung

NewPanasonicIPCapture - Installation und Verwendung

In allen Komprimierungsmodi verwendet der Treiber die Protokolle RTSP/RTP/UDP für den Videoempfang und HTTP/HTTPS für die Einstellung der Parameter und für die PTZ-Funktionalität.

Im H.264/MPEG4-Komprimierungsmodus verwendet der Treiber RTSP/RTP/UDP/IP-Protokolle für den Videoempfang. Das HTTP-Protokoll wird für das Einstellen/Abrufen von Parametern und den kontinuierlichen Empfang von MJPEG-Streams verwendet.

Wenn sich zwischen DVMS und den Kameras eine Firewall befindet, müssen die folgenden RTSP/UDP/HTTP-Ports geöffnet werden:

HTTP: Der Standard-Port ist 80,

RTSP: Der Standard-Port ist 554,

UDP: Zwei aufeinanderfolgende Ports pro Videostream in einem Portbereich von 3556 bis 4556 benötigt werden.

Die Datei NewPanasonicIPCapture.xml wird zur Konfiguration verwendet:

Verhalten des Fahrers:

Unicast

Multicast:Primary

Multicast:Listener

Priorität der Übertragung:

Bitrate

Framerate

Beste Leistung

Erweitertes VBR

VBR

Minimale Bitrate (nur für den Best Effort Modus)




Pagination
Previous page
NewMobotixIPCapture - Installation und Verwendung
Next page
NewSamsungIPCapture - Installation und Verwendung