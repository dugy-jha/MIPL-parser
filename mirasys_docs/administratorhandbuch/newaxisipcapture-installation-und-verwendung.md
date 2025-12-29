# NewAxisIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/newaxisipcapture-installation-und-verwendung

NewAxisIPCapture - Installation und Verwendung

Der Treiber verwendet die Protokolle RTSP/HTTP/HTTPS/RTP/UDP/IP, um Audio- und Video-Multicast-Streams und H.264/MPEG-4-komprimierte Unicast-Streams zu empfangen. Das HTTP-Protokoll wird auch zum Einstellen/Abrufen von Parametern und zum Empfang von Audio- und JPEG-Videoströmen im Unicast-Modus verwendet.

Wenn sich zwischen DVMS und den Kameras eine Firewall befindet, müssen die folgenden RTSP/UDP/HTTP/HTTPS-Ports geöffnet sein geöffnet sein:

HTTP: Der Standardport ist 80,

HTTPS: Der Standardport ist 443,

RTSP: Der Standardanschluss ist 554,

UDP: Pro Videostream werden zwei sequentielle Ports im Portbereich 3556 bis 4556 benötigt. Wenn der Multicast-Modus aktiviert ist, sollten zwei zusätzliche sequentielle Ports pro Audio-/Videostream entsprechend der Gerätekonfiguration geöffnet werden.

Wenn beispielsweise 4 IP-Kameras in einem DVMS vorhanden sind, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen. Die Ports 1024-1025 und 1028-1029 sollten zusätzlich zum Bereich 3556-4556 geöffnet werden, wenn das Gerät im Multicast-Modus verwendet wird und so konfiguriert ist, dass der Port 1024 für den Audiostrom und der Port 1028 für einen Videostrom verwendet wird.

Der Treiber kann mithilfe einer XML-Konfigurationsdatei konfiguriert werden, um die folgenden Funktionen zu aktivieren, wenn das Axis IP-Gerät diese Funktionen unterstützt:

Multicast audio/video capture

Axis Views

Wenn Sie Axis LPR verwenden und mehrere Netzwerkadapter haben, müssen Sie die richtige IP-Adresse (Adressen) in der Konfigurationsdatei festlegen.

Beschränkungen

Für die HTTPS (TLS)-Unterstützung müssen Sie das CA-Zertifikat auf dem PC-Zertifikatspeicher generieren und installieren und ein Zertifikat für jede Kamera mit Hilfe einer Anleitung von Axis generieren („HowTo. AXIS Device Manager. HTTPS certificate management“).

Der AXIS-Treiber unterstützt die Option „PTZ-Steuerungswarteschlange“ nicht. Wenn diese Option aktiviert ist, wird das AXIS Gerät als Nicht-PTZ-Gerät erkannt.

Die Privatzonen können um einige Pixel gegenüber dem in DVMS angewendeten Rechteck verschoben sein. Die Verschiebung hängt von der Bilddrehung und den Spiegeleinstellungen ab (bei einem normalen Bild nach rechts verschoben). Dies ist eine Funktion der Kamera-Firmware.

Wenn die Option „Seitenverhältniskorrektur“ auf dem Axis-Gerät aktiviert ist, kann die tatsächliche Bildauflösung von der in VMS abweichen. So beträgt die tatsächliche Auflösung beispielsweise 768x576 bei der Einstellung 704x576 oder 192x144 bei der Einstellung 176x144. Bitte deaktivieren Sie diese Option, wenn Ihr System keine Seitenverhältniskorrektur benötigt.

Wenn die Netzwerkverbindung unterbrochen wird, senden die Axis-Kameras der Serie P33 einige Sekunden Video und dann 5-10 Sekunden lang nichts mehr, nachdem die Verbindung wiederhergestellt wurde. Dieses Verhalten wird durch die DHCP-Implementierung der Kamera verursacht. Bitte verwenden Sie eine statische IP-Adresse, um dieses Verhalten zu vermeiden.

Das IP-Gerät sollte wie folgt manuell konfiguriert werden, wenn Sie die Edge-Speicherfunktion verwenden möchten:

Es ist nicht möglich, die koordinierte Weltzeit (UTC) von der Kamera zu empfangen, daher sollte die Zeitzone auf „GMT+0:00“ eingestellt werden. Die Option Sommerzeit sollte ebenfalls ausgeschaltet werden.

Die Kameraereignisse sollten für die Videoaufzeichnung entsprechend den Benutzereinstellungen konfiguriert werden. Die Ereignisdauer sollte mindestens 3 Sekunden betragen.

Es wird empfohlen, die automatische SD-Reinigung zu verwenden, um den erforderlichen Speicherplatz für Videoaufnahmen zu erhalten.

Die Videoaufzeichnungen auf dem Speicher der Kamera können Lücken von bis zu 10-15 Sekunden enthalten. Dies ist eine Funktion der Kamera, verwenden Sie also bitte nicht die maximalen Einstellungen für die Videoaufzeichnung, um solche Lücken zu vermeiden.

Axis-Kameras mit mehreren Ansichten (z. B. M3007) können mithilfe der XML-Konfigurationsdatei für den Empfang von Videos aus einem bestimmten Stream konfiguriert werden. Unterschiedliche Ansichten haben unterschiedliche Fähigkeiten, so dass die Kamera erneut bei VMS angemeldet werden sollte, um die geänderten StreamConfiguration-Optionen zu nutzen.

Die Datenschutzzonen-Funktionalität kann verwendet werden, wenn der Aufzeichnungskanal die Fischaugenansicht „Übersicht“ verwendet.

Andere Ansichten unterstützen die Privacy-Masking-Funktionalität nicht, da diese Ansichten Teil der Ansicht „Übersicht“ sind.

Einschränkungen bei der Multicast-Erfassung

Axis IP-Geräte unterstützen Multicast-Capture mit der Funktion Stream Profiles (Geräte mit Firmware-Version 5.0 oder höher) und können über eine XML-Datei konfiguriert werden. Ältere Geräte verwenden immer Unicast-Streaming.

Die Unterstützung von Stream Profiles kann über die Weboberfläche überprüft werden: der Abschnitt „Video & Audio >> Stream Profiles“ sollte verfügbar sein. Der Benutzer kann ein beliebiges vorhandenes Profil für die Multicast-Streaming-Konfiguration verwenden oder das System ein neues Profil erstellen lassen. Weitere Einzelheiten finden Sie im Abschnitt „MulticastProfiles“ in der XML-Konfigurationsdatei.

Bitte verwenden Sie nicht dasselbe Stream-Profil für verschiedene Streams - dies kann zu Konflikten bei der Anwendung der Videoeinstellungen führen.

Die Multicast-Erfassung kann über die XML-Konfigurationsdatei mit der Option StreamingMode aktiviert werden. Diese Option wird beim Start des Streams gelesen, so dass eine Aktualisierung der Geräteeinstellungen ausreicht, um die geänderte StreamingMode-Option zu verwenden. Bitte beachten Sie, dass DVMS seit Version 7.4.1 über eine Optimierung für den Kanalneustart verfügt, so dass in diesem Fall eine der Videooptionen für jede Kamera geändert werden muss, um den Stream neu zu starten.

Die Treiberinstanz kann so konfiguriert werden, dass sie als primäre Instanz oder als Listener verwendet wird. Die primäre Instanz ist in der Lage, IP-Geräteeinstellungen zu ändern und zusätzliche Funktionen zu nutzen. Listener-Instanzen können Video- und Audioströme per Multicast empfangen und ermöglichen die Nutzung der digitalen E/A-Funktionalität.

Der Listener-Recorder ändert keine Konfiguration auf der Kameraseite. Wenn z. B. kein konfiguriertes Profil auf der Kamera vorhanden ist, wird es nicht erstellt, und der Treiber kann das Video nicht empfangen. Die Kamera sollte zum primären Rekorder hinzugefügt werden, bevor sie in der Listener-Konfiguration verwendet wird.

Die zusätzlichen Streams (Live und Remote) sind nur dann aktiv, wenn sie in Clients geöffnet sind. Um also die aktualisierten Einstellungen für das Multiple Streaming zu verwenden, müssen Sie diese Streams für den primären Rekorder starten (oder offen halten), nachdem die Stream-Einstellungen in DVMS geändert wurden. Andernfalls kann die Kamera die aktuellen Stream-Einstellungen nicht verwenden.

Die Option Bewegungserkennung und -änderung in den Alarmfunktionen (CFiA/CRiA) kann im Multicast-Modus aufgrund der oben genannten Zeitüberschreitungsprobleme nicht verwendet werden.

Benutzer sollten sicherstellen, dass nur ein Rekorder die Einstellungen von Axis IP-Geräten ändert. Andere Rekorder, die diese Kamera verwenden, sollten sich im Zuhörermodus befinden.

Die Axis-Kameras unterstützen möglicherweise nicht mehr als einen Multicast-Stream, wenn die Kamera so konfiguriert ist, dass sie einen bestimmten Port für Multicasting verwendet (Einstellung „Video-Port“ ungleich Null in der Gruppe „Systemoptionen >> Netzwerk >> RTP“). Die Kamera gibt den Fehler RTSP 461 „Unsupported transport“ für den Start eines Streams zurück, wenn bereits ein Multicast-Stream gestartet ist. Bitte konfigurieren Sie die automatische Port-Auswahl (setzen Sie „Video port“ auf 0), um dieses Verhalten zu vermeiden.

Es wird empfohlen, die IP-Adresse des Netzwerkadapters anzugeben, über den die Kamera angeschlossen ist, um Multicast-Streaming korrekt zu empfangen, falls mehr als ein Netzwerkadapter verfügbar ist.

Jedes Unicode-Zeichen wird als Symbolcode (z. B. %u0227) gespeichert und benötigt 6 Bytes. Daher kann die Länge des Unicode-Präpositionsnamens auf 11 statt auf 64 Symbole begrenzt sein.

Die Axis P1428-E Kamera unterstützt nur 2 4K (3840x2160) Streams zur gleichen Zeit. Bitte vermeiden Sie die Verwendung der 4K-Auflösung für alle Streams in der Mehrfach-Streaming-Funktion und minimieren Sie die Anzahl der Regeln, die die 4K-Auflösung für die Aufzeichnung auf der SD-Karte verwenden.

Der Treiber ermöglicht seit Version 2.5.5.0 den Wechsel zwischen den Modi „Aktiv“ und „Passiv“. Im Modus „Passiv“ ändert der Treiber keine videorelevanten Parameter, so dass in diesem Modus die folgenden Funktionen nicht funktionieren:

Privatzonen konfigurieren

Optionen im Alarm ändern (z. B. CFiA/CRiA-Funktionen)

Wenn die Kamera Videoparameter über RTSP- oder HTTP-Stream-URI akzeptiert, startet der Treiber den Stream ohne diese Parameter. Mit anderen Worten, es werden die über die Webschnittstelle vorgenommenen Stream-Einstellungen verwendet.

Die Anwendung von Privatsphärenmasken kann sehr lange dauern (die Erstellung jeder Zone kann bis zu einer Sekunde dauern), was den Streamstart verlangsamen kann. Um das Abonnieren von Videos zu beschleunigen, wendet der Treiber Datenschutzmasken nach dem Start des Videostreams an.

Die Treiberversionen vor 2.5.7.0 haben ein Problem mit der Erstellung von Privatsphärenmasken für Geräte mit mehreren Sensoren. Der Treiber verwendete immer die Vorlage für den ersten Kanal, so dass die Privatzonen möglicherweise falsch angezeigt wurden (z. B. auf dem falschen Kanal).

Bitte entfernen Sie die Privatzonen manuell über das Web-Interface oder setzen Sie das Gerät einfach auf die Werkseinstellungen zurück, falls Sie auf ein solches Verhalten stoßen sollten. Danach erstellt der Treiber beim nächsten Start des Videokanals Privacy Masks mit den richtigen Vorlagen.

Die Axis Zipstream-Technologie (<http://www.axis.com/global/en/technologies/zipstream)> kann mit dem Treiber verwendet werden. Der Treiber hat keine Option zur Konfiguration dieser Funktion, so dass sie manuell über das Web-Interface aktiviert werden sollte.

Bitte beachten Sie dies:

Die über die Webschnittstelle vorgenommenen Änderungen der Videoeinstellungen (einschließlich der Axis Zipstream-Optionen) wirken sich auf die nach den Änderungen gestarteten Videostreams aus. Daher ist ein Neustart des Videostreams erforderlich, um die aktualisierten Einstellungen zu übernehmen.

Die VMS-Software muss ein Intraframe pro Sekunde empfangen, um die Nachbearbeitung des Videostroms (VCA, Bewegungserkennung usw.) durchzuführen. Die Verwendung der Option „Dynamic GOP“ kann zu Problemen bei der Nachbearbeitung führen, daher wird die Verwendung dieser Option nicht empfohlen.The Windows XP is not supported since driver version 2.5.0.0

Die neuen Axis-Kameras (Firmware 5.50 und neuer) verwenden eine neue API für die Bewegungserkennung, die derzeit nicht vom Treiber unterstützt wird. Die VMD-Funktion wird für diese Kameras deaktiviert, bis die neue API-Unterstützung zum Treiber hinzugefügt wird.

Die native Axis-Kennzeichenerkennungsanwendung verwendet HTTP-POST-Anfragen zum Senden von ANPR-Daten. Daher startet der Treiber den HTTP-Server, um diese HTTP-POST-Nachrichten zu empfangen. Wenn der PC mehr als einen Netzwerkadapter hat, müssen Sie die korrekte IP-Adresse des Netzwerkadapters, der für die Kommunikation mit der Kamera verwendet wird, in der XML-Datei des Treibers im Parameter AxisANPR/NetworkInterface angeben. In anderen Fällen sendet die Kamera keine ANPR-Daten an den PC. Wenn Failover verwendet wird, müssen beide Adressen eingestellt werden - Master-Server und Failover.

Axis hat die date.cgi API in die time.cgi API geändert, um die Zeit von der Kamera abzurufen oder zu setzen. Aber diese neue time.cgi API arbeitet langsam, so dass der Treiber die Zeit von der Kamera mit einer gewissen Verzögerung erhält. Außerdem hat time.cgi immer noch keine Milisekunden, so dass diese Zeitsynchronisation nicht präzise ist. Der Treiber versucht, die Zeitdifferenz zwischen Kamera und PC mit Recorder zu berechnen, aber diese Berechnung ist nicht präzise genug. Diese Berechnung kann in der Konfigurationsdatei abgeschaltet werden, wenn die Zeit außerhalb von VMS synchronisiert wird.




Pagination
Previous page
NewArecontIPCapture - Installation und Verwendung
Next page
NewBoschIPCapture - Installation und Verwendung