# LGEIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/lgeipcapture-installation-und-verwendung

LGEIPCapture - Installation und Verwendung

Der Treiber verwendet RTSP/RTP/UDP/IP-Protokolle, um Videoströme und Eingangszustände in allen Komprimierungsmodi zu empfangen. Das HTTP-Protokoll wird für das Setzen/Abrufen von Parametern verwendet.

Wenn sich eine Firewall zwischen DVMS und den Kameras befindet, müssen die folgenden RTSP/UDP/HTTP-Ports geöffnet sein:

HTTP: Die Standard-Ports sind 80 und 81,

RTSP: Hafen 554,

UDP: Es werden zwei sequentielle Ports pro Videostrom und zwei sequentielle Ports pro Metadatenstrom (Eingangszustände) in einem Portbereich von 3556 bis 4556 benötigt.

Wenn zum Beispiel 2 LG Electronics IP-Kameras in einem DVMS vorhanden sind, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Beschränkungen

Bei einigen LG Electronics-Geräten kann das Gerätemodell nicht empfangen werden. Bei diesen Kameras wird der Modellname als „LG Electronics IP-Kamera“ angezeigt.

Die Kamera LDW2010F-N sendet einen QCIF-Stream mit einer Auflösung von 160x112 anstelle von 176x112. Dies ist ein Merkmal der Kamera.

Die digitalen Ausgänge der LG Electronics-Geräte haben eine Besonderheit: Sie verfügen über eine Dauer-Option und können nicht über einen längeren Zeitraum geschlossen werden. Das Gerät öffnet den Ausgang automatisch, wenn die Zeitspanne abgelaufen ist.

Die SOAP-API unterstützt keine Befehle zum Umschalten von Fokus- und Blendenmodi zwischen automatischen und manuellen Werten. Wenn der Benutzer also die Blenden-/Fokuseinstellung in DVMS verwenden möchte, sollte er diesen Wert über die Weboberfläche auf manuell ändern.




Pagination
Previous page
IPCameraCapture - Installation und Verwendung
Next page
NewActiIPCapture - Installation und Verwendung