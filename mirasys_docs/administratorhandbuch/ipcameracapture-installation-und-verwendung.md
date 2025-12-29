# IPCameraCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/ipcameracapture-installation-und-verwendung

IPCameraCapture - Installation und Verwendung

Der Treiber verwendet RTSP/RTP/UDP/IP-Protokolle für den Video- und Audioempfang in allen Komprimierungsmodi.

Das HTTP/HTTPS-Protokoll wird zum Einstellen/Abrufen von Parametern und für die PTZ-Funktionalität verwendet.

Wenn sich eine Firewall zwischen DVMS und den UDP-IP-Geräten befindet, müssen die folgenden RTSP/UDP/HTTP/HTTPS-Ports geöffnet werden:

HTTP: Der Standard-Port ist 80,

HTTPS: Standardport ist 443 (wenn auf der Kamera aktiviert)

RTSP: Hafen 554,

UDP: Zwei aufeinanderfolgende Ports pro Audio-/Videostream werden in einem Portbereich von 3556 bis 4556 benötigt.

Beschränkungen

UDP-Kameras verarbeiten manchmal den PTZ-Stoppbefehl nicht. Um dieses Problem zu vermeiden, sendet der Treiber vier Stopps.

Es gibt keine Blendeneinstellungen für UDP/Amano/GANZ-Kameras. Die Firmware für UDP/Amano/GANZ-Kameras ermöglicht Änderungen der Videostandards, aber die Kameras unterstützen (im Allgemeinen) nur einen dieser Standards.

2Mpx-Kameras haben ein Problem mit MJPEG 100% Qualität - es stoppt Streaming. 2Mpx-Kameras haben unterschiedliche Auflösungen für MPEG4-Codec (keine 2Mpx).

Die IPE1100 M-Kameras haben eine Einstellung für die maximale Auflösung (SETUP > Video & Audio > Video-In > Parameter Videoauflösung). Diese Einstellung bestimmt die Liste der verfügbaren Auflösungen, z. B. ist die Mindestauflösung für 2Mpx VGA, und kleinere Auflösungen sind nicht verfügbar.

Das Aktivieren von Mehrfach- oder Multicast-Streaming-Funktionen kann die Geräteleistung verringern. Daher werden beide Videoströme mit niedrigeren Frameraten als derzeit verwendet gesendet.

Geräte der IPE-Serie senden alle Streams mit instabilen Bildraten, wenn mindestens einer dieser Streams für MJPEG-Codierung konfiguriert ist. Die Bildrate wird stabil, wenn der MJPEG-Stream gestoppt wird. Dies ist eine Funktion der Geräte der IPE-Serie.

Bei Geräten der IPN/IPX-Serie kann es vorkommen, dass die Videoeinstellungen für einen langen Zeitraum (70-90 Sekunden) gelten, wenn die Funktion für mehrfaches Streaming aktiviert ist. Bitte warten Sie, bis der Videostream beginnt, bevor Sie die Videoeinstellungen erneut ändern.

Geräte der IPN/IPX-Serie enthalten den folgenden Hinweis in der Webschnittstelle: „Wenn eine vertikale Auflösung von 1080P ausgewählt wird, können andere Videoströme keine höhere horizontale Auflösung als 1088 unterstützen.“ Das Verhalten der Kamera kann unerwartet sein, wenn der Benutzer versucht, für beide Videoströme eine Auflösung von 1080p zu verwenden.

Einschränkungen bei Multicast-Aufnahmen:Multicast capture can be enabled via an XML configuration file using the StreamingMode option. Refreshing device settings will be enough to activate the changed StreamingMode option.

Die Treiberinstanz kann so konfiguriert werden, dass sie als primäre oder als Listener-Instanz verwendet wird. Die primäre Instanz kann IP-Geräteeinstellungen ändern und zusätzliche Funktionen nutzen. Listener-Instanzen können Video- und Audioströme per Multicast empfangen und digitale E/A-Funktionen nutzen.

Der Benutzer sollte sicherstellen, dass nur ein Rekorder die Einstellungen von UDP IP-Geräten ändert. Andere Rekorder, die dieses Gerät verwenden, sollten sich im Zuhörermodus befinden.

Der Multicast-Stream verwendet dieselben Einstellungen, bis er neu gestartet wird, auch wenn die Stream-Einstellungen geändert werden. Die Änderung des Stream-Status (Starten oder Stoppen) erfordert 6-10 Sekunden. Die Anwendung von Stream-Einstellungen dauert also 30-60 Sekunden.

Bitte beachten Sie, dass der Treiber nur den Standardadapter für Multicast-Streaming verwendet. Daher funktioniert Multicast möglicherweise nicht korrekt, wenn Ihr PC mehr als eine Netzwerkkarte hat. Bitte wenden Sie sich an den Kundendienst, wenn Sie ein Problem mit der Multicast-Konfiguration haben.

Einschränkungen der Zeitsynchronisationsfunktionen:

Die Änderung der Zeitzone hat bis zum Neustart keine Auswirkungen auf die Systemzeit. Um die korrekte Zeit anzuwenden, kann der Treiber die Kamera nach der Änderung der Zeitzoneneinstellung neu starten.

Die Änderung der Zeitzone hat bis zum Neustart keine Auswirkungen auf die Systemzeit. Um die korrekte Zeit anzuwenden, kann der Treiber die Kamera nach der Änderung der Zeitzoneneinstellung neu starten.

Einschränkungen der Edge-Storage-Funktionalität:

Die Edge-Storage-Funktionalität wird nur für Kameras der IPX/IPN-Serie unterstützt, und zwar ab Firmware-Version 1.8.0.4

Die Aufzeichnung auf der SD-Karte sollte manuell über die Weboberfläche der Kamera konfiguriert werden, bevor Sie diese Funktion in VMS nutzen.

Die IPN/IPX-Kameras erlauben nur die Aufzeichnung eines H.264-Streams auf SD-Karte. Wenn Sie die Kodierung des für die Aufzeichnung verwendeten Profils ändern, wird die Speicherung von Videomaterial auf der SD-Karte deaktiviert.

Die IPN/IPX-Kameras ermöglichen die Suche nach aufgezeichnetem Material nur nach Ereignissen. Dies ist eine Einschränkung des SDK der Kamera. Aufgrund dieser Einschränkung können Videos, die mit den Einstellungen für kontinuierliche Aufzeichnung aufgezeichnet wurden, nicht verarbeitet werden.

Die maximale Ereignisdauer beträgt 65 Sekunden (5 Sekunden vor der Aufzeichnung und 60 Sekunden nach der Aufzeichnung). Es gibt keine Möglichkeit, die Aufzeichnung von längeren Zeitintervallen zu konfigurieren.







Pagination
Previous page
HTTPIPCapture - Installation und Verwendung
Next page
LGEIPCapture - Installation und Verwendung