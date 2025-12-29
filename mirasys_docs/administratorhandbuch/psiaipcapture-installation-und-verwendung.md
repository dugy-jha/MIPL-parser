# PSIAIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/psiaipcapture-installation-und-verwendung

PSIAIPCapture - Installation und Verwendung

In allen Komprimierungsmodi verwendet der Treiber RTSP/RTP/UDP/IP-Protokolle für den Videoempfang. Das HTTP-Protokoll wird für das Setzen/Abrufen von Parametern verwendet.

Wenn sich eine Firewall zwischen VMS und den Kameras befindet, müssen die folgenden RTSP/UDP/HTTP-Ports geöffnet sein:

HTTP: Der Standard-Port ist 80,

RTSP: Hafen 554,

UDP: Zwei aufeinanderfolgende Ports pro Videostream in einem Portbereich von 3556 bis 4556 benötigt werden.

Beispiel: Wenn ein VMS über 4 Kameras verfügt, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Beschränkungen

Nur der primäre Videokanal wird unterstützt (wenn die Kamera mehrere Kanäle hat)

Pagination
Previous page
PelcoIPCapture - Installation und Verwendung
Next page
RTSPIPCapture - Installation und Verwendung