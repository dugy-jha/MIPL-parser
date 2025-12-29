# WisenetIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/wisenetipcapture-installation-und-verwendung

WisenetIPCapture - Installation und Verwendung

In allen Komprimierungsmodi verwendet der Treiber RTSP/HTTP/HTTPS(TLS)/RTP/UDP/IP-Protokolle für den Videoempfang. Das HTTP/HTTPS-Protokoll wird auch zum Setzen/Abrufen von Parametern verwendet.

Wenn sich zwischen DVMS und den Kameras eine Firewall befindet, müssen die folgenden RTSP/UDP/HTTP/HTTPS-Ports geöffnet sein:

HTTP: Der Standard-Port ist 80,

HTTPS: Der Standard-Port ist 443,

RTSP: Der Standard-Port ist 554,

UDP: Zwei aufeinanderfolgende Ports (beginnend mit dem geraden Wert) pro Unicast-Audio- oder -Videostream in einem Portbereich von 3556 bis 4556.

Für die Kommunikation über HTTPS (TLS) muss RTSP über HTTP-Transport gewählt werden, der als
für HTTP und für HTTPS.

Wenn zum Beispiel 4 IP-Kameras in einem DVMS vorhanden sind, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet werden. Wenn ein Port nicht frei ist, wird das Portpaar übersprungen.

Für das Multicast-Streaming sind ebenfalls zwei aufeinander folgende Ports pro Audio- oder Videostream erforderlich, aber die Anzahl der Ports hängt von den Geräteeinstellungen oder der XML-Konfiguration ab.

Das Gerät kann z. B. so konfiguriert werden, dass alle Datenströme nur an einen einzigen Anschluss gesendet werden. Die Ports 40000-40001 sollten geöffnet werden, wenn für diese Einstellung der Port 40000 angegeben wird.

Beschränkungen

Die Nummernschilderkennung wird direkt in dem auf der Kamera installierten VaxALPR-Plugin gemäß dem Handbuch „VaxALPR On-Camera Software“ konfiguriert. Software-Setup und Kamerakonfiguration. Hanwha Handbuch“. Es gibt keine Möglichkeit, die Genauigkeit der LPR über XML einzustellen.

Es wird empfohlen, Kameras mit Whisenet 5 und Wisenet 7 Prozessoren für das Vaxtor ALPR Plugin (VaxALPR) zu verwenden.

Bezüglich des TLS-Zertifikats: Wenn eine RTSP-Verbindung über HTTPS (TLS) hergestellt wird, gibt die Kamera ihr öffentliches Zertifikat während des Handshake-Verfahrens weiter, daher muss der Client das öffentliche Zertifikat der Kamera nicht speichern oder besitzen.

Geben Sie keinen leeren Benutzernamen für die Autorisierung ein. Wenn der Benutzername leer ist, werden die Autorisierungs-Header nicht zu den HTTP-Anfragen hinzugefügt.

Die Kamera kann eine nicht gedrehte Auflösung zurückgeben, wenn die Option „Fluransicht“ auf 90 oder 270 Grad eingestellt ist (z. B. 800x448 anstelle der tatsächlichen Auflösung von 448x800). In diesem Fall wird der Stream mit der korrekten (gedrehten) Auflösung empfangen.

Datenschutzmasken werden auf der Grundlage der maximalen Auflösungsgröße gemäß den SUNAPI-Spezifikationen angewendet. Daher kann es vorkommen, dass sie nicht mit den angezeigten Positionen übereinstimmen, wenn ein beschnittenes Bild oder ein Bild mit einem anderen Seitenverhältnis verwendet wird. Dies ist ein normales Verhalten. Bitte verwenden Sie die maximale Auflösung in den Anwendungen System Manager/Spotter Admin für die Bearbeitung von Privatsphärenmasken.

Bei der SNB-9000-Kamera (Firmware-Version 1.02_160215) können während der Anwendung der Konfiguration durch den Treiber mehrmals Privatsphärenmasken erscheinen und verschwinden. Dies ist ein kamerabezogenes Problem, das dem Hanwha Techwin-Support gemeldet wurde, der jedoch im Moment keine neue Firmware-Version plant.

Sichtschutzmasken werden für PTZ-Geräte nicht unterstützt, da Mirasys VMS keine Möglichkeit hat, die Position der Maske mit Hilfe von Kugelkoordinaten festzulegen.

Einige Kameras wie die PNM-9030V unterstützen Privacy Masking nur für den Übersichtskanal. Die übrigen Kanäle zeigen einen Teil des Übersichtskanals an und haben keine Möglichkeit, eigene Masken einzurichten.

Da VMS keine Möglichkeit hat, die Funktionen für jeden Videokanal einzeln einzurichten, haben alle Kamerakanäle die gleiche (maximale) Anzahl von verfügbaren Masken. Allerdings funktionieren die Masken in diesem Fall nur für den Übersichtskanal. Die Einstellungen für Privatsphärenmasken für andere Kanäle werden ignoriert.

Das Beispiel des Wisenet PNM-9030V unterstützt die Funktion der Privatsphärenmaskierung nur für den Kanal „Übersicht“.

Das Bild für die anderen Kanäle unterstützt keine Privacy-Masking-Funktion. Daher können alle Objekte, die im Bild des Kanals „Übersicht“ durch Masken verdeckt sind, auf den anderen Kanälen leicht gesehen werden.Dies ist das Konzept von Hanwha und wird in den Spezifikationen der Kamera erwähnt.

Die SNB-9000-Kamera (Firmware-Version 1.02_160215) kann den Codec nicht per SUNAPI-Aufruf ändern.

Dies ist ein kamerabezogenes Problem, das dem Hanwha Techwin-Support gemeldet wurde. Allerdings gibt es derzeit keine Pläne für die Veröffentlichung einer neuen Firmware-Version.

Bitte ändern Sie den Codec manuell über das Web-Interface, falls Sie Probleme mit der Anwendung der Videoeinstellungen haben sollten.

Die SNB-9000-Kamera ändert die Auflösung bei Alarm (CCRiA-Funktion) innerhalb von 8 Sekunden. Dieses Verhalten wird durch verschiedene Verzögerungen auf der Kameraseite während der Neuübertragung des Streams verursacht und kann auf der Treiberseite nicht verbessert werden. Die Änderung der Bildrate im Alarmfall (CCFiA) dauert aufgrund des ähnlichen Kameraverhaltens 2 Sekunden.

Bitte beachten Sie diese Einschränkungen, wenn Sie CCRiA/CCFiA-Funktionen mit dieser Kamera in Ihrem Setup verwenden möchten.

Der Treiber erlaubt nicht die Verwendung der PTZ-Funktionalität für Kameras mit „Cropped image“-Funktionen (wie SNB-9000 oder SNV-8080 Kameras).

Die Kameras mit motorisierten Fokus/Zoom-Objektiven unterstützen kein kontinuierliches Zoomen/Fokussieren wie PTZ-Kameras. Die Zoom-/Fokusänderung wird als schrittweise Einstellung im Web-Interface verwendet. Daher erfolgt die Zoom-/Fokusänderung diskret. Der Treiber sendet auch weiterhin wiederholbare Schrittbefehle, während die Zoom-/Fokustaste gedrückt wird, um eine kontinuierliche Bewegung zu emulieren.

Hanwha-Box-Kameras (mit 'B'-Zeichen im Modell, wie XNB-xxxx oder QNB-xxxx) unterstützen die Funktion Externes PTZ, die es ermöglicht, die Kamera mit der PT-Plattform zu verwenden. Leider gibt es keine Möglichkeit, über HTTP-API-Aufrufe zu erkennen, ob die Kamera mit der PT-Plattform verbunden ist oder nicht, so dass Box-Kameras mit Unterstützung der externen PTZ-Funktion als PTZ-Kameras erkannt werden. Dies ist eine Einschränkung der HTTP-API/Kamerahardware.

Die Geräte von Hanwha haben die folgenden Einschränkungen für die Namen der voreingestellten Positionen:

Es sind nur alphanumerische Zeichen (A-Z, a-z, 0-9) erlaubt;

Die Länge des Voreinstellungsnamens ist auf 12 Symbole begrenzt.

Als Ergebnis speichert der Treiber seit Version 1.0.2.0 die Preset-Positionen in '*.preset' XML-Dateien. Falls die Datei keine Preset-Positionen enthält, versucht der Treiber, aktuelle Informationen über Preset-Positionen aus dem Wisenet IP-Gerät zu laden.

Die Verwendung der XML-Speicherung ermöglicht auch die Verwendung von Unicode-Symbolen in voreingestellten Positionsnamen.

Der Wert für die GOV-Länge wird für das Aufnahmeprofil automatisch auf die Hälfte der aktuellen Bildrate (d. h. 2 Schlüsselbilder pro Sekunde) festgelegt und kann nicht über die Webschnittstelle oder über HTTP-API-Befehle angepasst werden. Wählen Sie ein anderes Profil als „Aufnahme“-Profil, wenn diese Einschränkung für Ihre Konfiguration nicht geeignet ist.

Das Multisensor-Wisenet IP-Gerät kann für verschiedene Kanäle unterschiedliche Auflösungsmöglichkeiten haben. Zum Beispiel unterstützt das PNM-9030V-Beispiel 6096x2540 und 2688x1120 Auflösungen für den ersten Kanal, bis zu 2592x1944 Auflösungen für die nächsten 4 Kanäle und bis zu 1920x1080 für den 6. und 7.

Leider hat das VMS keine Möglichkeit, verschiedene Auflösungen für verschiedene Kanäle festzulegen - dies ist eine Einschränkung der Softwarearchitektur. Mit anderen Worten, alle Auflösungen (6096x2540, 2688x1120 und 2592x1944) werden für alle Kanäle verfügbar sein.

Falls die gewählte Auflösung vom Kanal nicht unterstützt wird, wird stattdessen die nächsthöhere oder maximale Auflösung verwendet. In unserem Beispiel wird im Falle der Auswahl von 2592x1944 die Auflösung 2688x1120 für den ersten Kanal und 1920x1080 für den siebten Kanal verwendet.

Der Audiokanal verwendet dasselbe Videoprofil, das auch für den Empfang des Aufzeichnungsvideostroms verwendet wird.

Dies kann zu Konflikten in der Multicast-Konfiguration führen, die vom Videokanal (aus der dynamischen UI-Konfiguration) und vom Audiokanal (aus der XML-Datei geladen) angewendet wird.

Der Audiokanal ändert also die Multicast-Konfiguration nur dann, wenn sie noch nicht vom Videokanal geändert wurde. Ansonsten wird die bestehende Multicast-Konfiguration für das Multicasting des Audiostroms verwendet.

Das Videoprofil des Geräts wird für den Empfang und das Senden von Audio verwendet. Jede Änderung der Videoprofileinstellung, die zu einem Neustart der RTSP-Sitzung führt, kann auch ein erneutes Abonnieren des Audiostroms verursachen.

DVMS hat keine Möglichkeit, die Audioeinstellungen im System Manager zu konfigurieren, daher sollten diese Einstellungen über eine XML-Konfigurationsdatei konfiguriert werden.

Standardmäßig wird nur der Audio-Encoder (Option <Encoding>) angegeben: AAC für den Audioeingang und G.711 für den Audioausgang. Die anderen Audio-Optionen (einschließlich Lautstärke/Verstärkung) sind so konfiguriert, dass sie die Werte verwenden, die derzeit im Web-Interface der Kamera ausgewählt sind.

Wisenet-Kameras können eine Begrenzung der Bildrate aufweisen, die von der Anzahl der gleichzeitig gestreamten Profile abhängt:

Die neue Q-Serie unterstützt 1920x1080 Streams mit insgesamt 45 fps. Die Kamera QND-6082R unterstützt beispielsweise bis zu 30 Bilder/s für H.264-Streams mit einer maximalen Auflösung von 1920x1080. Beim Streaming von einem einzigen Profil liefert die Kamera einen Stream mit 30 fps. Beim Streaming von 2 verschiedenen Profilen mit denselben H.264 1080p @ 30 fps Stream-Einstellungen streamt die Kamera jedoch jedes Profil nur mit 22 fps.New L-series can support 1920x1080 stream by total 30fps.

Das Mirasys VMS hat ein Problem mit der Dekodierung von G.726-Audiostreams von verschiedenen Samples wie Wisenet XND-8080R. Das Problem wird in den nächsten Treiberversionen behoben. Bitte verwenden Sie G.711 oder AAC-Kodierung, falls Sie Probleme mit der G.726-Audiodekodierung haben.

Der Treiber unterstützt nur die neue Version der Edge-Storage-Funktion, die seit VMS Version 8.0 verfügbar ist. Die Edge-Storage-Funktion wird bei früheren DVMS-Versionen nicht erkannt.

Die Wisenet SNF-8010 Kamera hat ein Problem mit der Suche nach aufgezeichneten Datenintervallen: Sie erkennt nur Intervalle, deren Beginn und Ende innerhalb des gewünschten Zeitraums liegen. Andere Kameramuster erkennen auch Überschneidungen (d. h. die Startzeit der Aufzeichnung liegt vor dem angeforderten Zeitraum, und die Endzeit liegt innerhalb oder nach dem Zeitraum).

Die SNF-8010-Kamera ist bereits abgekündigt (seit 2018), so dass das Problem auf der Kameraseite nicht behoben werden kann. Mirasys hat auch keine Pläne, dem Treiber eine separate Verarbeitungslogik für einzelne Modelle hinzuzufügen.

Die verschiedenen Multisensorgeräte unterstützen die Aufzeichnung von Material über eine begrenzte Anzahl von Kanälen.

Das Beispiel des PNM-9030V erlaubt beispielsweise nur die Aufzeichnung von Videos über den Kanal „Übersicht“.

In diesem Fall verwendet der Treiber die Edge-Storage-Funktion nur für Kanäle, die in der Attributgruppe „Aufzeichnung“ die Fähigkeit „Aufzeichnung“ aufweisen.

Die SUNAPI v2.x-Spezifikationen haben die folgenden Einschränkungen für HTTP- und RTSP-Anfragen im Zusammenhang mit der Verarbeitung von Speicherfunktionen:

Die Millisekunden sind nicht verfügbar;

Die Zeit sollte bei allen Anfragen im lokalen Format angegeben werden (keine UTC-Unterstützung);

Die vom Gerät zurückgegebenen Zeitintervalle sind ebenfalls in Ortszeit. 

Diese Einschränkungen können die folgenden Probleme verursachen:

Da die Zeitauflösung eine Sekunde beträgt, kann der Wechsel zwischen Aufzeichnungs- und Kantenmaterial und umgekehrt zu wiederholbaren Fragmenten führen, die nicht länger als eine Sekunde dauern, oder es können Daten fehlen, die nicht länger als eine Sekunde sind;

Die Umrechnung zwischen Ortszeit und UTC-Zeit kann zu Problemen bei der Materialauswahl während der Umstellung auf oder von der Sommerzeit (DST) führen;

Ein Wechsel der Zeitzone kann dazu führen, dass beim Intervallempfang ein falsches Zeitintervall gewählt wird;

Die Wisenet-Geräte unterstützen nur eine RTSP-Verbindung für die gleichzeitige Wiedergabe. Im Falle der Verwendung eines Geräts mit mehreren Kanälen werden die verlorenen Daten also nacheinander von der SD-Karte des Geräts empfangen: alle Intervalle von allen Kanälen werden in eine einzige Warteschlange gestellt und nur dann aus der Warteschlange extrahiert, wenn gerade keine anderen Intervalle verarbeitet werden.

Der Treiber kann mit Windows 7 oder neueren Betriebssystemen verwendet werden. Ältere Betriebssysteme werden nicht unterstützt.

Pagination
Previous page
VivotekIPCapture - Installation und Verwendung
Next page
Installieren von Metadatentreibern