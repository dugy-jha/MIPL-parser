# NewActiIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/newactiipcapture-installation-und-verwendung

NewActiIPCapture - Installation und Verwendung

In allen Komprimierungsmodi verwendet der Treiber RTSP/RTP/UDP/IP-Protokolle für den Videoempfang. Das HTTP-Protokoll wird für die Einstellung/Abruf der Parameter verwendet.

Wenn sich zwischen DVMS und den Kameras eine Firewall befindet, müssen die folgenden RTSP/UDP/HTTP-Ports geöffnet werden:

HTTP: Standard-Port ist 80,

RTSP: Anschluss 7070,

UDP: zwei aufeinanderfolgende Ports pro Videostream werden in einem Portbereich von 3556 bis 5556 benötigt.

Die Datei NewActiIPCapture.xml wird zur Konfiguration verwendet:

Verhalten des Fahrers:

Unicast

Multicast:Primary

Multicast:Listener

Der Stream-Modus der Kamera und der Montagetyp (bei Fisheye-Kameras) erlauben eine Entschärfung der Kamera.

Mögliche Werte für Stream-Modi: SINGLE, DUAL, EPTZ, MD_PRESET, FISHEYE_VIEW

Mögliche Werte für Montagearten: WALL, CEILING

Die erste PTZ-Kanal-ID für ACTi-Videoserver:
Allgemeine und IP-Geräte-spezifische Konfiguration ist möglich
E.g:
<Device address="192.168.1.75" port="80">
<FirstPTZChannelID>2</FirstPTZChannelID>
</Device>
Für das Gerät 192.168.1.75:80 ist die erste PTZ-Kanal-ID die 2, die nächste (bei einem Mehrkanalgerät) die 3, usw.

Beschränkungen

ACTi TCM-5311 kann den korrekten Stream nicht mehr senden, wenn die Hintergrundbeleuchtung abrupt geändert wird.

ACTi MPEG4-Kameras benötigen eine Verzögerung zwischen der Einstellung der Parameter und dem Start des Streams (etwa 3 Sekunden).

ACTi CAM-6510 arbeitet nicht korrekt mit 1 fps, daher ist dieser Wert für diese Kamera nicht verfügbar. Die ACTi CAM-6510 Kamera unterstützt keine Qualitätsänderung, daher ist die Qualität für alle Werte gleich.

ACTi-Kameras haben unterschiedliche Bildraten für unterschiedliche Komprimierungsformate. Die Einstellungen werden automatisch auf den nächstgelegenen korrekten Wert umgerechnet.

ACTi E96, B54, B55 und B56 Kameras unterstützen kein De-Warping auf der Kamera, daher hat die XML-Konfiguration keine Auswirkungen auf diese Modelle.

ACD-Videoserver funktionieren nur mit einer PTZ-Kamera, die an jeden Kanal angeschlossen ist, mit einer Kamera-ID = 1. Der ACD2100 funktioniert beispielsweise nur mit einer Kamera, der ACD2200 mit vier Kameras. ACD-Mehrkanalgeräte haben unterschiedliche RS485-Anschlüsse für PTZ-Kameraverbindungen, und alle Kamera-IDs müssen gleich 1 sein.

Die tatsächliche Bildrate für ACTi-Kameras kann von den Einstellungen abweichen. Sie hängt von den Kameraeinstellungen (Objektivausgleich und Verschlusszeit) und der Beleuchtungsstärke ab.

Videokameras unterstützen keine E/A-Funktionalität. Sie funktionieren in PAL, aber die Werkseinstellung ist NTSC. Nach Anwendung der Werkseinstellung funktioniert die Kamera nicht mehr.

SED2100 arbeitet mit ACTi-Bibliotheken. SED2100 muss nach jeder Änderung der Parameter einen Neustart durchführen (dauert 30-60 Sekunden).

Voreinstellungsnamen werden in einer XML-Datei gespeichert (keine Voreinstellungsverwaltung der Kamera)

Für KCM kann die K2 Fischaugenkamera in zwei Video-Stream-Modi verwendet werden: EINZELN und EPTZ. Der Stream-Modus wird bei der Anmeldung der Kamera an DVMS erkannt, der Treiber behält diesen Modus bei. Um den Stream-Modus zu ändern, muss die Kamera aus dem DVMS entfernt werden, der Stream-Modus muss über die Weboberfläche der Kamera geändert werden, und dann kann die Kamera abonniert werden. Der Treiber stellt ihn automatisch für alle anderen KCM- und TCM-Serien im SINGLE-Video-Stream-Modus ein.

Der ACTi-Treiber verwendet konstante Bitrateneinstellungen, die aus dem entsprechenden VMS-Qualitätswert skaliert werden:

CAM values: 256K, 384K, 500K, 750K, 1M, 1.5M, 2M, 2.5M, 3M

ACM values: 28K, 56K, 128K, 256K, 384K, 500K, 750K, 1M, 1.2M, 1.5M, 2M, 2.5M, 3M, UNLIMITED

TCM/KCM values: 28K, 56K, 128K, 256K, 384K, 500K, 750K, 1M, 1.2M, 1.5M, 2M, 2.5M, 3M, 3.5M, 4M, 4.5M, 5M, 5.5M, 6M, UNLIMITED

So wird die VMS-Qualität 50% auf einen Bitratenwert von 1Mbit/sec skaliert. Die richtige DVMS-Qualität sollte so eingestellt werden, dass sie der erforderlichen Netzwerkbandbreite entspricht.

ACTi-Videoserver haben kein internes PTZ-Protokoll; sie senden PTZ-Befehle im transparenten Modus an den COM-Port der Kamera zurück. Derzeit ist nur das PelcoD-Protokoll implementiert. Wenn eine analoge Kamera, die an einen ACTi-Videoserver angeschlossen ist, nicht mit PelcoD funktioniert, kann der Treiber nicht zur Steuerung der Kamera verwendet werden.

Nicht alle Stream-Modi werden von den ACTi Fischaugenmodellen unterstützt. Der ACTi I51 unterstützt z. B. nur die Stream-Modi DUAL (Panorama), FISH_EYE und EPTZ. Andere Einstellungen haben keine Auswirkungen und werden im Stream-Modus verwendet, der an der Kamera eingestellt ist.

Stream-Modus und Montageart sollten festgelegt werden, bevor die Kamera zu DVMS hinzugefügt wird. Um diese Werte zu ändern, sollte der Benutzer die Kamera aus DVMS entfernen, Änderungen in der Konfigurationsdatei vornehmen und die Kamera erneut zu DVMS hinzufügen.

Mehrfaches Streaming für die Fischaugenkamera wird nur für diese Stream-Modi unterstützt:

DUAL - 2 Ströme

MD_PRESET - 2 Ströme in WALL Befestigungsart, 3 in CEILING

Digitales PTZ funktioniert für die Fisheye-Kamera nur im EPTZ-Stream-Modus.

Wenn die Auflösung oder der Stream-Modus geändert wurde, werden die Voreinstellungen für die Fisheye-Kamera ungültig; sie müssen aus DVMS entfernt und erneut zugewiesen werden.

MPEG4 ist im DUAL-Stream-Modus deaktiviert, da es nur für den 1.

Die Stream-Modi 6VGA und 4VGA werden nicht unterstützt.

Die Stream-Modus-Einstellungen in der Datei NewActiIPCapture.xml gelten nur für die Fischaugen-Kameras. Die Einstellungen für den Stream-Modus anderer Kameras werden von der Kamera übernommen, wenn sie zu DVMS hinzugefügt wird. Wenn die Kamera den DUAL-Stream-Modus eingestellt hat, wird mehrfaches Streaming aktiviert, wenn SINGLE - nicht.

Im DUAL-Stream-Modus muss die Bildrate in Stream 1 höher oder gleich hoch sein wie die in Stream 2. Andernfalls ist die Bildrate in Stream 1 auf die Bildrate in Stream 2 begrenzt. Beispiel: Die Einstellungen für die Bildrate in Stream 1 und Stream 2 sind 30 und 25. Die tatsächliche Bildrate in Stream 1 beträgt 25

KCM/TCM-Kameras können keine Privatsphärenmasken für den zweiten Stream aktivieren. Daher werden Privatsphärenmasken nur für Single-Stream-Modi aktiviert (die Kamera sollte einen Single-Stream-Modus haben, bevor sie zu DVMS hinzugefügt wird). Bei KCM/TCM-Kameras gibt es ein allgemeines Problem im Zusammenhang mit Privatsphärenmasken und Auflösungen größer oder gleich 1920x1080: Die Privatsphärenmaske kann nur für den linken Teil des Bildschirms festgelegt werden (ACTi-Einschränkung).

ACTi ACM-Kameras haben ein Problem mit den Privatsphärenmaskeneinstellungen. Die Position der Privatsphärenmaske ist nur bei maximaler Auflösung korrekt; bei kleineren Auflösungen kann die Position der Privatsphärenmaske von den Einstellungen abweichen.

Die ACTi ACM-Serie kann Bewegungserkennung liefern, aber es gibt keine konfigurierbare MD auf der Webseite der Kamera. Für diese Modelle kann die „Rekorder- und Kamerahardware“ MD nicht verwendet werden.

Multicast ist für ACTi CAM-Modelle nicht aktiviert. Alle diese Modelle arbeiten nur mit Unicast. Diese Kameras können nicht in mehreren DVMS-Instanzen verwendet werden!

Unicast mode: Der Treiber ändert die Kameraeinstellungen entsprechend den DVMS-Einstellungen und empfängt Audio- und Videodaten von der Kamera über eine Unicast-Verbindung.

Multicast:Primary: Der Treiber ändert die Kameraeinstellungen entsprechend den DVMS-Einstellungen und empfängt Audio- und Videodaten von der Kamera über eine Multicast-Verbindung.

Multicast:Listener: Der Treiber ändert keine Kameraeinstellungen, sondern empfängt lediglich Audio- und Videodaten von der Kamera über eine Multicast-Verbindung.

Wenn die Kamera in mehreren DVMS-Instanzen verwendet werden soll, sollte ein DVMS auf Multicast:Primary und die anderen auf Multicast:Listener eingestellt werden.

Mehrere Multicast:Primary-Konfigurationen oder Multicast:Primary- und Unicast-Konfigurationen sind nicht zulässig; in anderen Fällen sollte die Kamera mit ständigen gleichzeitigen Einstellungsänderungen überlastet werden.

Edge Storage wird nur für die DEBI-Serie ab Firmware 6.07.23 und höher unterstützt.

Die Kamera ist mit UTC (GMT +00) synchronisiert, um Probleme mit der Ortszeit zu vermeiden.

Der Modus RTP über RTSP funktioniert nicht mit den folgenden Kameraserien. Diese Kameras unterstützen diesen Modus nicht oder sind nicht vollständig getestet worden:

VIDO AMU-xxx

ACTI KCM-xxx

ACTI ACM-xxx







Pagination
Previous page
LGEIPCapture - Installation und Verwendung
Next page
NewArecontIPCapture - Installation und Verwendung