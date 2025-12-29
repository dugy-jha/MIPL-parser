# StanleyIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/stanleyipcapture-installation-und-verwendung

StanleyIPCapture - Installation und Verwendung

In allen Komprimierungsmodi verwendet der Treiber RTSP/RTP/UDP/IP-Protokolle für den Videoempfang. Das HTTP-Protokoll wird für das Setzen/Abrufen von Parametern verwendet.

Wenn sich eine Firewall zwischen VMS und den Kameras befindet, müssen die folgenden RTSP/UDP/HTTP-Ports geöffnet sein:

HTTP: Der Standard-Port ist 80,

RTSP: Hafen 554,

UDP: Zwei aufeinanderfolgende Ports pro Videostream in einem Portbereich von 3556 bis 4556 benötigt werden.

Beispiel: Wenn 4 Kameras in VMS vorhanden sind, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Beschränkungen

Der Treiber erkennt nur die Fähigkeiten des aktuell aktivierten Profils. Wenn der Benutzer das Profil in der Weboberfläche der Kamera geändert hat, müssen die Kamerafunktionen in VMS aktualisiert werden (Neustart der automatischen Suche im Systemmanager oder erneutes Hinzufügen der Kamera).

In VMS ist es nicht möglich, eine unterschiedliche Anzahl von Auflösungen für verschiedene Komprimierungsformate einzustellen, daher werden im Systemmanager alle unterstützten Auflösungen angezeigt. Wenn eine bestimmte Auflösung vom Komprimierungsformat nicht unterstützt wird, wird die nächstgelegene gültige Auflösung verwendet.

Unterschiedliche Auflösungen unterstützen unterschiedliche maximale Frameraten, so dass der Treiber den nächstgelegenen gültigen Wert für die Framerate verwendet. Wenn beispielsweise die maximale Framerate für die 1080p-Auflösung 15 fps beträgt und der Benutzer in den Systemmanager-Einstellungen 30 fps angibt, legt der Treiber 15 fps für die Kamera fest.

H.264-Videostreams haben keine Qualitätseinstellung, daher wird zur Steuerung der Streamqualität der Modus mit konstanter Bitrate (CBR) verwendet. 1 % Qualität im System Manager bedeutet minimalen Bitratenwert und 100 % Qualität bedeutet maximalen Bitratenwert.

Bei Mehrfach-Streaming hat jeder Stream nur einen Codec und eine Auflösung. Zum Beispiel hat das erste Profil in der Kamera die folgenden Kombinationen:

      -> H.264 :1920 x 1080

      -> H.264 :720 x 480

      -> JPEG :720 x 480

      -> JPEG :352 x 240

Der erste Stream hat also den H.264-Codec und die Auflösung 1920x1080, der zweite Stream den H.264-Codec und die Auflösung 720x480, der dritte Stream den JPEG-Codec und die Auflösung 720x480. Und die vierte Kombination (JPEG-Codec und 352 x 240 Auflösung) wird wieder für den ersten Stream verwendet. Mehrfaches Streaming kann in der XML-Datei des Treibers deaktiviert werden.

Die Privatzonen können größer sein als im System Manager angezeigt, da die Stanley-Kameras feste Blöcke zur Einstellung der Maske verwenden (20 Blöcke in der Horizontalen und 12 Blöcke in der Vertikalen).




Pagination
Previous page
SIPIPCapture - Installation und Verwendung
Next page
VivotekIPCapture - Installation und Verwendung