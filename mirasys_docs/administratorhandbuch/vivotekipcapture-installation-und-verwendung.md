# VivotekIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/vivotekipcapture-installation-und-verwendung

VivotekIPCapture - Installation und Verwendung

In allen Komprimierungsmodi verwendet der Treiber RTSP/RTP/UDP/IP-Protokolle für den Videoempfang. Das HTTP-Protokoll wird für das Setzen/Abrufen von Parametern verwendet.

Wenn sich eine Firewall zwischen VMS und den Kameras befindet, müssen die folgenden RTSP/UDP/HTTP-Ports geöffnet werden:

HTTP: Der Standard-Port ist 80,

RTSP: Hafen 554,

UDP: Zwei aufeinanderfolgende Ports pro Videostream in einem Portbereich von 3556 bis 4556 benötigt werden.

Beispiel: Wenn 4 Vivotek IP-Kameras in einem DVMS vorhanden sind, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Beschränkungen

Manchmal wechselt die Kamera in den „Nur HTTP“-Modus entsprechend dem Mechanismus zur Erkennung von Netzwerkfähigkeiten (kamerainterner Mechanismus). Um die Kamera wieder in den „RTP“-Modus zu versetzen, muss sie neu gebootet werden.

Die Kamera überspringt die Kanaleinstellungen beim Wechsel vom Modus „Qualitätspriorität“ zum Modus „Bildratenpriorität“. Der Videomodus kann in der Treiber-XML-Datei eingestellt werden.

Die Standard-Ansichtsmaske für hohe Auflösung zeigt nicht das gesamte Bild an. Sie kann über das Web-Interface konfiguriert werden.

Die maximale Bildrate für hohe Auflösungen ist niedriger als angegeben.

Befehle zum Ändern der Blende funktionieren nicht bei der getesteten SD7323-Kamera.

AAC-Audio-Dekompression wird ab DVMS 7.4.4 oder höher unterstützt.

Geräte der Sony H-Serie (wie die Kamera SNC-HM662) verwenden das Vivotek OEM SDK im Gegensatz zu anderen Sony G6 Kameras. Für diese Geräte sollte der Vivotek-Treiber anstelle des Sony-Treibers verwendet werden.

Windows XP wird seit der Treiberversion 1.6.1.0 nicht mehr unterstützt.

CCRiA- und CCFiA-Funktionen sind nur für Geräte der Serie 8xxx oder höher verfügbar

Wenn die Auflösung durch einen Alarm geändert wird, kann der Benutzer ein ungültiges Bild sehen. Dies ist ein Geräteproblem - die Kamera sendet ein ungültiges Bild - und der Treiber kann es nicht überspringen, da alle Header in Ordnung sind.




Pagination
Previous page
StanleyIPCapture - Installation und Verwendung
Next page
WisenetIPCapture - Installation und Verwendung