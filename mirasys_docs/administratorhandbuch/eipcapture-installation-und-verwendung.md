# EIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/eipcapture-installation-und-verwendung

EIPCapture - Installation und Verwendung

Der Treiber verwendet RTSP/RTP/UDP/IP-Protokolle für den Videoempfang in allen Komprimierungsmodi.

Das HTTP-Protokoll wird für das Setzen/Abrufen von Parametern verwendet.

Wenn sich zwischen DVMS und den Kameras eine Firewall befindet, müssen die folgenden RTSP/UDP/HTTP-Ports geöffnet sein:

HTTP: Der Standard-Port ist 80,

RTSP: Hafen 554,

UDP: zwei aufeinanderfolgende Ports pro Videostream werden in einem Portbereich von 3556 bis 4556 benötigt.

Beispiel: Wenn 4 El.MO oder Dynacolor IP-Kameras in einem DVMS vorhanden sind, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Beschränkungen

Die WinInet-Bibliothek wird zum Senden/Empfangen von HTTP-Daten zwischen DVMS und der e-Vision/Dynacolor-Kamera verwendet. Die Version 8.0 dieser Bibliothek hat eine Einschränkung: Es können nur 2 HTTP-Verbindungen gleichzeitig geöffnet werden (siehe den folgenden Artikel: http://support.microsoft.com/kb/183110).> Dieses Problem tritt auf, nachdem der Internet Explorer auf 8.0 oder höher aktualisiert wurde.

Wenn die Webschnittstelle der Kamera auf demselben PC geöffnet wird, auf dem dieser Treiber verwendet wird, können aufgrund dieser Einschränkung einige HTTP-Anfragen nicht gesendet werden. In diesem Fall wird die Kamera möglicherweise nicht von der automatischen Suche gefunden, oder einige Funktionen funktionieren überhaupt nicht.

Die Option „Video-OCX-Protokoll“ sollte auf „RTP über UDP“ (oder „RTP über RTSP(TCP)“ in einigen Fällen) eingestellt werden, damit der RTP/RTSP-Videostream korrekt empfangen wird. Diese Option kann nicht per CGI-Abfrage eingestellt werden. Stellen Sie sie daher vor der Verwendung der Kamera manuell über die Webschnittstelle (Registerkarte Streaming) ein.

Die El.MO- und Dynacolor-Kameras (außer Dynacolor HD WDR IP-Kameras) haben spezifische Auflösungseinstellungen. Die Kamera kann verschiedene Auflösungen für verschiedene Codecs unterstützen. Die Kameras der NH-Serie unterstützen beispielsweise die folgenden Auflösungen (die maximale Framerate ist in Klammern angegeben):

MJPEG video codec - 1280x960(12.5 fps), 640x480(25 fps);

MPEG4 video codec - 640x480(25 fps), 320x240(12.5 fps), 352x288(12.5 fps), 176x144(12.5 fps).

Wenn Sie versuchen, eine nicht unterstützte Auflösung einzustellen, wird die am besten geeignete Auflösung verwendet. Detaillierte Informationen zu den von der Kamera unterstützten Auflösungen finden Sie in den Kameraeinstellungen (Seite Streaming -> Videoformat, Abschnitt „Videoauflösung“).

Die El.MO- und Dynacolor-Kameras unterstützen nur eine oder zwei Bildraten (z. B. 25 oder 12,5 für PAL-Kameras der NH-Serie). Andere Bildwechselfrequenzen können über die Einstellung „Frame Skip“ angewendet werden. Normalerweise unterstützt die Kamera intern das Überspringen von 5, 10 und 15 Bildern. Wenn die Kamera 25 Bilder pro Sekunde für eine bestimmte Auflösung unterstützt, sendet die Kamera einen Stream mit 5, 2,5 und 1,67 Bildern pro Sekunde bei entsprechenden Einstellungen für die Bildüberspringung. Wenn Sie also versuchen, eine nicht unterstützte Framerate einzustellen, kann die tatsächliche Framerate größer sein als die in VMS verwendete. Es wird der am besten geeignete Wert verwendet.

Der Videostream für Kameras der NH-Serie weist bei VGA-Auflösung mit den höchsten Bildraten- und Qualitätseinstellungen (sowohl für MPEG-4- als auch für MJPEG-Codecs) eine unstetige Bildrate auf. Die tatsächliche Bildrate schwankt zwischen 18 und 30 Werten, aber der Durchschnittswert der Bildrate ist um 1-2 fps niedriger als erforderlich. Dies ist ein Problem der Kamera.

Dynacolor- und El.MO-Kameras wenden jede Anforderung von Stream-Einstellungen an, die sich in etwa 20 Sekunden ändern. Dies ist eine Funktion der Kamera.

Die IP-PTZ-Kameras haben die folgenden Probleme:

Die Kamera gibt bei jedem IO-Befehl immer einen HTTP-Fehlercode 503 zurück - dies ist ein Firmware-Problem. Das IO-Modul ist bei Kameras der IP PTZ-Serie vorübergehend deaktiviert.

Die Kamera kehrt den „Fokus“-Befehl um: Sie führt die Aktion „Fokus nah“ für den Befehl „Fokus fern“ aus und umgekehrt. Dies ist ein Firmware-Problem.

Die Kamera stellt die Verbindung nach dem Abziehen des Netzwerkkabels nicht wieder her. Nachdem die Verbindung wiederhergestellt ist, sollte die Kamera manuell neu gestartet werden.

Die HD-WDR-IP-Kameras haben die folgenden Probleme:

Die Kamera sendet MPEG-4-Bilder mit einer höheren Bildrate als erforderlich. Zum Beispiel kann die Kamera bei maximaler Auflösung (1280x960) bis zu 16 Bilder pro Sekunde senden, anstatt 12,5

Die Kamera unterstützt kein Frame Skipping für die maximale Auflösung (1280x960) für den H.264-Codec. Dies ist eine Funktion der Kamera. Daher ist nur eine Bildrate (maximal 25 oder 30 Bilder/s) für die maximale Auflösung des H.264-Codecs verfügbar.

Die Kameras der V-Serie haben ein Problem mit dem H.264-Codec. Nach der Anwendung von 100 % Qualität für den H.264-Codec sendet die Kamera einen falschen Videostream (der VLC-Player spielt ihn nicht ab, und VMS zeigt eine Menge Frame-Skipping-Meldungen an). Dieses Problem tritt gelegentlich auf.

Die 5-Megapixel-360∞-Fisheye-Kameras unterstützen nur Fischaugenansichten. Derzeit unterstützen sie nicht die Auswahl eines anderen Sichtbereichs.

Mehrere Streaming-Beschränkungen:

Ab DVMS 6.1.1 werden mehrere Streaming-Funktionen für Full-HD Quad Stream-Kameras unterstützt. Andere Kameras werden als Single-Stream-Geräte verwendet.

Aufzeichnung und Live-Streams unterstützen nur H.264-Kodierung. Der Remote-Stream unterstützt sowohl MJPEG- als auch H.264-Kodierungen.

Die Auflösungen der verschiedenen Streams hängen voneinander ab. Für die Auflösung gilt folgende Regel: Die Auflösung eines Live-Streams kann nicht größer sein als die Auflösung eines Aufzeichnungs-Streams. Die gleiche Regel gilt für Remote- und Live-Streams. Weitere Informationen zu diesen Auflösungsbeschränkungen finden Sie im Handbuch des Geräts oder im Webinterface.







Pagination
Previous page
EHIIPCapture - Installation und Verwendung
Next page
GatewayIPCapture - Installation und Verwendung