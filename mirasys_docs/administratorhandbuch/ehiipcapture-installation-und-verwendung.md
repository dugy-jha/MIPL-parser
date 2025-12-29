# EHIIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/ehiipcapture-installation-und-verwendung

EHIIPCapture - Installation und Verwendung

Der Treiber verwendet RTSP/RTP/HTTP/HTTPS/UDP/IP-Protokolle für den Videoempfang in allen Komprimierungsmodi. Außerdem werden HTTP/HTTPS-Protokolle für das Einstellen/Abrufen von Parametern und für Remote Stream Video verwendet. Wenn sich zwischen DVMS und den Kameras eine Firewall befindet, müssen die folgenden RTSP/UDP/HTTP/HTTPS-Ports geöffnet werden:

HTTP: Der Standard-Port ist 80,

HTTPS: Der Standard-Port ist 443,

RTSP: Hafen 554,

UDP: zwei aufeinanderfolgende Ports pro Videostream werden in einem Portbereich von 3556 bis 4556 benötigt.

Wenn beispielsweise 4 Kameras in DVMS vorhanden sind, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Die Datei EHIIPCapture.xml kann verwendet werden, um eine 360-Grad-Ansicht (Kanal) auszuwählen - bitte geben Sie die Kanalnummern an, die im folgenden Abschnitt in XML verwendet werden sollen:

<Channel360>1</Channel360>
<Channel360>2</Channel360>


Nach dem Festlegen der Kanalnummern für eine 360-Grad-Kamera muss die Kamera entfernt und wieder hinzugefügt werden, um die korrekten Funktionen für die Kanäle zu erkennen.

Für das Multicast-Streaming sind ebenfalls zwei aufeinanderfolgende Ports pro Audio- oder Videostream erforderlich, aber die Portnummern hängen von den Geräteeinstellungen oder der XML-Konfiguration ab.

Beispielsweise kann das Gerät so konfiguriert sein, dass alle Datenströme nur an einen einzigen Anschluss gesendet werden. Wenn für diese Einstellung der Anschluss 40000 angegeben ist, sollten die Anschlüsse 40000-40001 geöffnet werden.

Beschränkungen

Es wird nur ein Audio-Multicast-Stream unterstützt. Eine Multicast-IP-Adresse wird für den Audiokanal und für den Videokanal verwendet, aber der Multicast-Audio-Port für denselben Stream sollte mindestens um 2 größer sein als der Video-Port, der Multicast-Video-Port für einen anderen Stream (z. B. Live) sollte mindestens um 6 größer sein als der Video-Port des vorherigen Streams (z. B. Aufnahme).

Der Audiokanal verwendet die gleiche Multicast-IP-Adresse wie der Videostream-Empfänger. Wenn unterschiedliche Multicast-Adressen definiert sind, kann dies zu einem Konflikt in der Multicast-Konfiguration führen, die vom Videokanal (aus der Dynamic UI-Konfiguration) und dem Audiokanal (aus der XML-Datei geladen) angewendet wird.

Sie müssen IGMP Snooping auf dem Netzwerk-Switch für die Multicast-Kommunikation aktivieren.

Für den HTTP/HTTPS-Transport wird die folgende Logik implementiert: Das dynamische Feld RTPoverHTTP wird hinzugefügt, wenn die Kommunikation über HTTP verwendet wird oder wenn die Kommunikation über HTTPS verwendet wird. Das Gerät unterstützt die Funktion RTPoverHTTPS.

Was das TLS-Zertifikat betrifft, so gibt die Kamera bei einer RTSP-Verbindung über HTTPS (TLS) ihr öffentliches Zertifikat während des Handshake-Verfahrens weiter. Daher müssen Clients das öffentliche Zertifikat der Kamera nicht speichern oder besitzen.

Der Mehrfach-Streaming-Modus wird erst ab DVMS 6.1 korrekt unterstützt.

Das Komprimierungsformat für die Aufzeichnung und das Live-Streaming sollte im Mehrfach-Streaming-Modus identisch sein.

Die Kameras werden nach dem Ändern des Komprimierungsformats neu gestartet, so dass es etwa 30 Sekunden dauert, bis das Video nach dem Ändern des Komprimierungsformats wiederhergestellt ist.

Bei Geräten mit zwei Streams pro Kanal („Main“ und „Sub“) hat der Remote-Stream die gleiche Auflösung wie der Aufnahmestream, so dass die Auflösungseinstellung für einen solchen Stream, bei dem es sich um eine HTTP-JPEG-Aufnahme handelt, nicht verwendet wird.

Bei Geräten mit 3 Streams pro Kanal gibt es diese Einschränkung nicht.

Einige Versionen der Hikvision-Firmware geben eine Liste von Auflösungen zurück, die von der Kamera nicht unterstützt werden. Diese Auflösungen können in DVMS angewendet werden, aber die Kamerabilder weisen Artefakte auf.

Hikvision-Kameras unterstützen nur 6 RTSP-Sitzungen zur gleichen Zeit. Dies ist eine Einschränkung der Hikvision-Firmware.

Die Bewegungserkennung sollte vor der Verwendung im DVMS manuell auf dem Gerät konfiguriert werden. Die MD-Funktionalität funktioniert möglicherweise nicht korrekt mit alten Firmware-Versionen. Bitte verwenden Sie die neueste Firmware-Version, um alle Treiberfunktionen zu nutzen.

Der Empfang von Eingangszuständen sollte in der XML-Konfigurationsdatei aktiviert und in der Webschnittstelle des Geräts konfiguriert werden (z. B. das Senden von Eingangszuständen mit „Notify Surveillance Center“ aktivieren).

Der dritte Stream der Hikvsion-Geräte wird als Live-Stream und der zweite als Remote-Stream verwendet.

Die Videoverlusterkennung sollte manuell auf dem Gerät konfiguriert werden, bevor sie im DVMS verwendet wird. Sie kann auch in der Konfigurationsdatei deaktiviert/aktiviert werden.

Pagination
Previous page
DahuaIPCapture - Installation und Verwendung
Next page
EIPCapture - Installation und Verwendung