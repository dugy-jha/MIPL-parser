# NewIQEyeIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/newiqeyeipcapture-installation-und-verwendung

NewIQEyeIPCapture - Installation und Verwendung

Der Treiber verwendet RTSP/RTP/UDP/IP-Protokolle für den Empfang von H.264-komprimierten Video- und Audioströmen. Das HTTP-Protokoll wird für das Einstellen/Abrufen von Parametern und den kontinuierlichen Empfang von MJPEG-Streams verwendet.

Wenn sich eine Firewall zwischen DVMS und den Kameras befindet, müssen die folgenden RTSP/UDP/HTTP-Ports geöffnet werden:

HTTP: Der Standard-Port ist 80,

RTSP: Der Standard-Port ist 554,

UDP: Zwei aufeinanderfolgende Ports pro Audio-/Videostream werden in einem Portbereich von 3554 bis 4556 benötigt.

Beschränkungen

IQEye-Kameras haben eine Auflösung und mehrere beschnittene Auflösungen. Gekürzte Auflösungen werden im Treiber nicht verwendet. Der Treiber verwendet nur den Downsampling-Prozess, um die Bildgröße zu ändern (Größe / 2, Größe / 4 und Größe / 8). Downsampling ist für Kameras aktiviert, die es unterstützen (Kameras IQ73xx, IQ04xx, IQD4xx, IQ54xx unterstützen es nicht).

Die IQ712-Kamera hat eine Beschränkung für maximale fps für MJPEG - 15 fps.

IQEye-Kameras (außer IQ73xx) haben nur eine Auflösung für H264 ñ 640x480. Die anderen können nur für MJPEG verwendet werden.

Der H.264-Codec unterstützt für alle Kameras nur die Werte 5, 10, 15 und 30 für die Bildrate. Andere Werte werden nur für MJPEG verwendet, sie werden auf die oben aufgeführten Werte skaliert, wenn der H.264-Codec aktiv ist.

Für IQA25S-Kamera für MJPEG-Codec 2560x1920 und 1280x960 Auflösungen unterstützen maximale fps Wert 7, für 640x480 und 320x240 Auflösungen - nur 10 fps max.

Für IQA25S Kamera für JPEG-Codec Auflösung max /2 sollte auf 10 fps zu arbeiten, aber es funktioniert, wie es ist - max fps ist 7, wenn höher angegeben - es 5 oder 4 fps gesetzt, ist dies ein Problem der Firmware.

Der Treiber unterstützt nur den Empfang von G.711-Audiostreams. AAC-Codec wird im Moment nicht unterstützt.

Pagination
Previous page
NewBoschIPCapture - Installation und Verwendung
Next page
NewMobotixIPCapture - Installation und Verwendung