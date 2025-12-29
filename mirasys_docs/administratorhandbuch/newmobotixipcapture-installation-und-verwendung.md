# NewMobotixIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/newmobotixipcapture-installation-und-verwendung

NewMobotixIPCapture - Installation und Verwendung

In allen Komprimierungsmodi verwendet der Treiber das HTTP-Protokoll für den Videoempfang und für die Einstellung/Rücksetzung von Parametern.

Wenn sich eine Firewall zwischen DVMS und den Kameras befindet, müssen die folgenden Ports geöffnet werden: HTTP: Standard-Port ist 80.

Beschränkungen

Die realen FPS sind durch die Auflösungseinstellungen (Kamerafunktion) begrenzt: höhere Auflösungen haben niedrigere reale FPS-Werte. Bei einer Auflösung von 800x600 beträgt die maximale FPS beispielsweise 9 für den MJPEG-Codec.

Die Audiodaten können gemäß der HTTP-API-Dokumentation als Teil des MxPEG-Rahmens empfangen werden. Daher ist der Audiostrom für MJPEG-Streams nicht verfügbar.

Der Stream-Modus wurde von „schnell“ auf manuell geändert - diese Einstellung kann im Web-Interface geändert werden.

Pagination
Previous page
NewIQEyeIPCapture - Installation und Verwendung
Next page
NewPanasonicIPCapture - Installation und Verwendung