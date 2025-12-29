# NewSiquraIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/newsiquraipcapture-installation-und-verwendung

NewSiquraIPCapture - Installation und Verwendung

In allen Komprimierungsmodi verwendet der Treiber RTSP/RTP/UDP/IP-Protokolle für den Videoempfang. Das HTTP-Protokoll wird für das Setzen/Abrufen von Parametern und für die PTZ-Funktionalität verwendet.

Wenn sich zwischen VMS und den Kameras eine Firewall befindet, müssen die folgenden RTSP/UDP/HTTP-Ports geöffnet werden:

HTTP: Standard-Port ist 80,

RTSP: Der Standard-Port ist Port 554,

UDP: zwei aufeinanderfolgende Ports pro Videostream werden im Portbereich 3556 bis 4556 benötigt.

Beispiel: Wenn es in einem DVMS 4 Siqura-Codecs gibt, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Beschränkungen

Der H.264-Decoder kann manchmal nicht in der Lage sein, das empfangene Bild zu dekodieren, was zu einem Fehler in der DVR-Logdatei führt.

Manchmal verarbeitet eine analoge Dome-Kamera keine PTZ-Befehle. Beispielsweise hält die Dome-Kamera manchmal nicht an, nachdem die Steuerung beendet wurde, oder sie bewegt sich nicht nach einer abrupten Richtungsänderung. Außerdem wird ein weiterer HTTP-Befehl mit denselben Parametern ignoriert, bis ein HTTP-Befehl mit anderen Parametern empfangen wird. Wahrscheinlich handelt es sich hierbei um eine Funktion des Siqura Video-Servers.

MJPEG-Videos von Siqura MD2x/HD2x-Kameras bleiben während der Live-Übertragung für einen Moment stehen. Es scheint, als ob ein Bild übersprungen wird. Das gleiche Verhalten tritt im Web-Interface auf. Dies ist ein Kameraproblem.

Siqura MD2x-Kameras mit alter Hardwarebasis unterstützen die Output-Funktionalität nicht. Der Treiber kann die Hardwareinformationen nicht erkennen, so dass die Ausgabe in jedem Fall in DVMS angezeigt wird.

Siqura-Geräte unterstützen keinen kontinuierlichen Blendenwechsel - dies ist eine Funktion der Firmware.

Alle Preset-Befehle, die im MD2x/MD6x/HD2x/HD6x-Protokoll (Dateiname „NKF - Protocol Hotkey 20090805“) als Befehle für den Zugriff auf spezielle Kamerafunktionen beschrieben sind, werden im PTZ-Modul deaktiviert. Daher wird die Anzahl der unterstützten Voreinstellungen für Siqura PTZ-Kameras weniger als 256 betragen.

Live MJPEG Encoder auf Siqura PTZ Kameras arbeiten mit niedrigerer Priorität als andere Encoder (MPEG-4 und H.264). Daher können die tatsächlichen Framerate-Werte geringer sein als für den MJPEG-HTTP-Kanal erforderlich, insbesondere bei schlechten Lichtverhältnissen.

Der Treiber speichert Voreinstellungsnamen in einer XML-Datei. Unicode-Voreinstellungsnamen werden seit Treiberversion 1.9.2.0 unterstützt.

Pagination
Previous page
NewSamsungIPCapture - Installation und Verwendung
Next page
NewSonyIPCapture - Installation und Verwendung