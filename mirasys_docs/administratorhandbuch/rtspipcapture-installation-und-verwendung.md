# RTSPIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/rtspipcapture-installation-und-verwendung

RTSPIPCapture - Installation und Verwendung

Der Treiber verwendet RTSP/RTP/UDP/IP-Protokolle für den Empfang von Videostreams von IP-Geräten.

Der Treiber erwartet eine RTP- oder RTSP-URI für das Hinzufügen des Geräts. Diese URI sollte in das Feld „IP-Adresse“ eingetragen werden.

Der erforderliche Port kann separat im Feld „Port“ angegeben werden oder im RTSP/RTP-URI enthalten sein. Der RTSP-URI-Port hat höhere Priorität, wenn er gesetzt ist, wird das VMS-Port-Feld ignoriert.

Die Stream-URI-Anforderungen:

Der RTSP-URI sollte im vollständigen Format angegeben werden, z. B.: rtsp://192.168.1.70:554/?h264x=0

Bei Kameras, die mehrere Videoströme senden (wie ACTi), sollte auch die korrekte Spur-ID angegeben werden: rtsp://192.168.1.75:7070/track1

Die RTP-Streaming-Geräte sollten auch das richtige Präfix haben: rtp://62.97.61.37:15000/

Der RTP-Dampf-URI akzeptiert auch Multicast-Adressen: rtp://239.232.192.255:20000/

Bitte beachten Sie, dass die Stream-URI über einen Player eines Drittanbieters, wie VLC oder QuickTime, überprüft werden kann.

Wenn sich zwischen VMS und den Kameras eine Firewall befindet, müssen die folgenden Ports geöffnet werden:

RTSP: Der Standard-Port ist 554,

UDP: Für den RTSP-Modus werden zwei aufeinanderfolgende Ports pro Videostream in einem Portbereich von 3556 bis 4556 benötigt. Der in den Parametern angegebene Port sollte für den RTP-Streaming-Modus geöffnet werden.

Beispiel: Wenn in einem VMS 2 IP-Kameras vorhanden sind, werden die Ports 3556, 3557, 3558 und 3559 für RTSP-Sitzungen verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Das RTSP-Streaming kann auch über die Konfigurationsdatei RTSPIPCapture.xml konfiguriert werden. Sie erlaubt es, die folgenden Optionen zu ändern:

RTP-Videotransport. Die folgenden Typen werden unterstützt: RTPoverUDP und RTPoverRTSP
<RTPMode>RTPoverRTSP</RTPMode>

Deaktivierung von Keep-alive-Meldungen. Einige Geräte unterstützen die Keep-alive-Verarbeitung möglicherweise nicht, so dass sie durch die Option 0 mit der Angabe <KeepAlive>1</KeepAlive> deaktiviert werden kann. Diese Werte können für jedes Gerät einzeln eingestellt werden.

Die Lippensynchronisation kann mit der folgenden Option aktiviert werden: <LogLevel>4</LogLevel>

Beschränkungen

Wenn die Kamera eine RTSP-Autorisierung erfordert, sollten der richtige Benutzername und das richtige Kennwort festgelegt werden, andernfalls wird kein Video angezeigt.

Hinweise zum RTP-Modus:

Die RTP-Video-Streaming-IP-Geräte sollten in der Lage sein, SPS- und PPS-Header im Stream zu senden. Ohne diese Header ist der Treiber nicht in der Lage, den H.264-Stream korrekt zu dekodieren.

Der Treiber ist nicht in der Lage, RTP-Streaming selbst zu starten - er verwendet nur RTP-Streams, die kontinuierlich vom Gerät erzeugt werden.

Die Audiosynchronisierung mit RTCP funktioniert in den folgenden Fällen möglicherweise NICHT:

wenn das Gerät nach dem Datenpaket einen RTCP-Bericht sendet;

für den Modus RTP über RTSP;

Wenn die RTCP-Synchronisierung verfügbar ist, können Sie die folgenden Meldungen in der Datei DVRLog.txt finden: „Video frame time was synchronized by RTCP successfully“

Hinweise zum MPEG2 TS-Format

Version 1.2.0.0 des Treibers unterstützt nur H.264 und AAC Codecs für das MPEG2 TS Format.

Es ist nicht möglich, nur Video- oder Audiostreams zu empfangen, da diese über einen einzigen RTP-Stream übertragen werden.

Der Audiokanal wird für alle Geräte erkannt, die das MPEG2 TS-Format (MPEG II Transport Stream) verwenden.

 Bitte setzen Sie den folgenden Wert auf „false“, um Audio auf dem ausgewählten Gerät zu deaktivieren:

XML
        <AudioChannel>

          <Enabled>false</Enabled> 

        </AudioChannel>


Das Betriebssystem Windows XP wird seit der Treiberversion 1.0.1.5 nicht mehr unterstützt.

Pagination
Previous page
PSIAIPCapture - Installation und Verwendung
Next page
SIPIPCapture - Installation und Verwendung