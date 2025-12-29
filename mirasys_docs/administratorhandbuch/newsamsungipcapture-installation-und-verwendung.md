# NewSamsungIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/newsamsungipcapture-installation-und-verwendung

NewSamsungIPCapture - Installation und Verwendung

In allen Komprimierungsmodi verwendet der Treiber RTSP/RTP/UDP/IP-Protokolle für den Videoempfang. HTTP/HTTPS-Protokolle werden für das Setzen/Abrufen von Parametern verwendet.

Wenn sich eine Firewall zwischen VMS und den Kameras befindet, müssen die folgenden Ports geöffnet werden:

HTTP: Der Standard-Port ist 80,

HTTPS: Der Standard-Port ist 443,

RTSP: Hafen 554,

UDP: Zwei aufeinanderfolgende Ports pro Videostream in einem Portbereich von 3556 bis 4556 benötigt werden.

Beispiel: Wenn ein VMS über 4 Samsung IP-Kameras verfügt, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Die Datei NewSamsungIPCapture.xml wird verwendet für:

Konfiguration des Fahrerverhaltens:

Unicast

Multicast:Primary

Multicast:Listener

Einstellungen der Videokanäle:

Videokanal-Protokoll (RTP over UDP, RTP over RTSP)

Bitrate-Modus (CBR/VBR)

Beschränkungen

Die Fähigkeiten von Samsung-Kameras können für frühere Firmware-Versionen nicht abgerufen werden. Alle Kamerafunktionen (mit Ausnahme des Kameramodellnamens) für diese Kameras sind im Treiber fest einprogrammiert. Daher sollten alle Kameras auf die neueste Firmware-Version aktualisiert werden.

Samsung-Kameras unterstützen die Konfiguration von Eingängen über CGI-Befehle nicht. Der Eingang ist standardmäßig als „deaktiviert“ konfiguriert. Bitte setzen Sie die Eingangskonfiguration im Web-Interface auf „NO“ (d. h. „Normal Open“), bevor Sie die Kamera zum VMS hinzufügen.Samsung camera frame rates may differ from settings (+/- 3 fps) 

Treiber speichert Voreinstellungsnamen in XML-Datei (Unicode-Namen werden unterstützt)

Die Samsung PTZ-Geräte unterstützen keinen Geschwindigkeitsparameter für den Befehl „move to preset“. Daher ist die Geschwindigkeit für die Bewegung zum Preset immer gleich.

Bei Samsung-Kameras wird die Konfiguration jeder Privatzone durch eine separate Anforderung (Hinzufügen/Entfernen) vorgenommen. Um die Position der Zone zu ändern, müssen wir die vorherige Konfiguration entfernen und eine neue Position durch verschiedene Anfragen hinzufügen. Jede Anforderung zum Hinzufügen/Entfernen wird von der Kamera innerhalb von 0,6 bis 0,8 Sekunden verarbeitet. Die Aktualisierung der Positionen von 10 Privatzonen kann also bis zu 16 Sekunden dauern.

Zeitzonen für eingestellte Kameras können bei der Zeitsynchronisation falsch eingestellt sein.

Das IP-Gerät sollte vom Benutzer auf folgende Weise manuell konfiguriert werden, wenn der Benutzer die Edge-Speicherfunktion verwenden möchte:

Es gibt keine Möglichkeit zu wissen, ob gerade eine Datei geschrieben wird. Stellen Sie daher die Option „Post-Alarm-Dauer“ nicht auf eine lange Zeitspanne ein, da dies dazu führen kann, dass der Treiber dieses Intervall überspringt.

Es wird empfohlen, die Option „1 fps zwangsweise aufnehmen“ zu deaktivieren. Diese Option kann jedoch bei einigen Einstellungen des aufgezeichneten Profils deaktiviert sein (Einzelheiten finden Sie im Handbuch der Kamera). Sie können in diesem Fall ein separates Videoprofil für die Aufnahme von Videos für HD- und Full-HD-Kameras verwenden.

Es wird empfohlen, die automatische SD-Reinigung zu verwenden, um den erforderlichen Speicherplatz für Videoaufnahmen zu erhalten.

Samsung-Kameras der Serie 7000 haben ein Problem mit der Aufzeichnung von Videodaten nach Ereignissen. Die Kamera zeichnet nichts auf, obwohl Ereignisse, die für die Aufzeichnung konfiguriert wurden, signalisiert werden. Die Kamera beginnt mit der Aufzeichnung von Videos nach einem Neustart oder manchmal nach dem Zurücksetzen der Kameraeinstellungen auf die Werkseinstellungen. Dies ist ein Kameraproblem.

Alte Samsung-Kameramodelle wie SNP-570 und SND-460, die das STW SDK verwenden (STW-Kameras in den nächsten Hinweisen) und deren Firmware-Version älter als 1.3.5 ist, unterstützen das Abrufen der Kameraeigenschaften nicht. Diese Kameras werden als „Samsung IP-Kamera“ erkannt und funktionieren nur im PAL-Videomodus.

Samsung STW-Kameras unterstützen den Befehl „Ausgang ausschalten“ nicht. Die Ausgänge werden von der Kamera automatisch gemäß den Ausgabeeinstellungen im Web-Interface ausgeschaltet.

Samsung STW-Kameras senden MPEG-4-Streams mit 12,5 FPS für die Einstellungen 10 und 15 FPS.

Samsung STW-Kameras verringern den Videoqualitätswert für MPEG-4-Codec automatisch während der Bewegung. Dies ist eine Funktion der Kamera (laut Informationen von Samsung Techwin Support).

Die Bildrate schwankt im MPEG-4-Komprimierungsmodus für Samsung STW-Kameras. Dies wird durch den Empfang von RTP-Paketen mit falscher Sequenznummer verursacht. Dies ist ein Kameraproblem.

Ein Videostream von Samsung STW-Kameras weist FPS-Schwankungen auf, wenn die Belichtungseinstellungen für die Kamera ungültig sind. Um die Einstellungen zu korrigieren, verwenden Sie die Schaltfläche „Kamera-Setup“ auf der Seite Live-Ansicht im Web-Interface.

Samsung STW-Kameras gehen in einen deaktivierten Zustand über (HTTP-Antworten mit Statuscode 500 für alle Anfragen), nachdem die Verbindung für kurze Zeit unterbrochen und dann wiederhergestellt wurde. Das Problem wird mit einer Wahrscheinlichkeit von 30 % nur für den MJPEG-Codec reproduziert.

Die FPS-Einstellungen werden für MJPEG-Videostreams nicht korrekt angewendet. Dieses Kameraproblem tritt bei Samsung STW-Kameras mit Firmware-Version 1.3.5 oder früher auf. Daher können die tatsächlichen FPS für den MJPEG-Videostream niedriger sein als erforderlich.

Der MJPEG-Stream stoppt nach einer langen Betriebszeit (z. B. bei Tests über Nacht). Dies liegt daran, dass die Kamera HTTP-Antworten mit dem Statuscode 500 für alle Anfragen zurückgibt. In diesem Fall sollte die Kamera manuell neu gebootet werden. Dieses Problem tritt tatsächlich bei Samsung STW-Kameras auf.

Die SNP-1000A-Kamera sendet einen MJPEG-Stream mit 8-9 FPS bei 10 FPS und D1-Auflösungseinstellungen. Dies ist ein Firmware-Problem.

Die SNP-1000A-Kamera verarbeitet keine HTTP-Anfragen mehr, nachdem die Netzwerkverbindung unterbrochen und wiederhergestellt wurde (z. B. nach „Kein Signal“ während 2 Minuten). Dies liegt daran, dass die Kamera HTTP-Antworten mit dem Statuscode 403 für alle Anfragen zurückgibt. In diesem Fall sollte die Kamera manuell neu gebootet werden.

SNP-1000A- und SNC-550-Kameras unterstützen keine MPEG-4-RTP-Dienste. Für diese Kameras ist nur MJPEG-Videostream verfügbar.

Die SNP-1000A-Kamera schwenkt zwischen 0 Grad und 350 Grad. Gradwerte zwischen 351 und 359 Grad sind nicht verfügbar - dies ist eine Funktion der Kamera.

Die SNP-1000A-Kamera unterstützt keine kontinuierlichen Bewegungsbefehle. Der Treiber implementiert eine Emulation des kontinuierlichen Bewegungsmechanismus. Dieser Mechanismus reduziert die folgenden Probleme:

Kamerabewegungen werden diskret sein.

Der MJPEG-Stream stoppt manchmal für ein paar Sekunden, wenn sich die Kamera mit höchster Geschwindigkeit bewegt. Wahrscheinlich ist die Kamera-Firmware nicht in der Lage, den Videostream und eine Vielzahl von Bewegungsbefehlen gleichzeitig zu verarbeiten.

Die Kamera bewegt sich fälschlicherweise in der unteren Position, wenn sie versucht, nach unten zu fahren. Die Kamera kehrt die vertikale Skala um und bewegt sich nach oben, wenn der Befehl „nach unten bewegen“ empfangen wird und die Kamera die untere Position passiert. Der nächste Befehl „Abwärtsbewegung“ wird jedoch nicht invertiert und die Kamera bewegt sich wieder in die untere Position.

Die Speicherung der Vorposition funktioniert bei der SNP-1000A-Kamera mit der aktuellen Firmware-Version nicht. Eine Aktualisierung der Firmware ist erforderlich.

Die Kameras der Serie 7002 haben eine Begrenzung für die Anzahl der aktiven Profile. Die Anzahl der aktiven Videoströme ist auf 2 begrenzt, wenn jeder von ihnen eine Auflösung von 1024x768 oder mehr verwendet. Daher kann es sein, dass die Funktion für mehrfaches Streaming bei diesen Kameras nicht korrekt funktioniert.

Der Treiber unterstützt nur G.711-Audiocodierung. Daher sollte die G.711-Kodierung manuell über das Web-Interface ausgewählt werden, wenn die Kamera mehr als eine Audiokodierung unterstützt.

VMS unterstützt keine Privatzonen für PTZ-Kameras. Die Unterstützung von Privatzonen wird also erkannt, wenn die Kamera keine Schwenk-/Neigebewegung unterstützt.

Samsung-Geräte mit WR3.0-Softwareplattformversion haben ein Problem bei der SSL-Implementierung, das die Verwendung von POST-Befehlen nicht zulässt. Daher kann die Privacy-Zones-Funktion nicht verwendet werden, wenn die HTTPS-Unterstützung aktiviert ist. Samsung hat versprochen, dieses Problem in der nächsten Firmware-Version zu beheben.

Samsung-Geräte mit WR3.0-Softwareplattformversion senden Videostreams mit niedriger Bildrate (z. B. 2-3 statt 20), wenn der Audiostream vor dem Videostream abonniert wurde. Dieses Verhalten wird durch die Implementierung des RTSP-Moduls auf der Kameraseite verursacht. Bitte speichern Sie die Kameraeinstellungen erneut, ohne sie zu ändern, um die Kamera in den normalen Streaming-Modus zu versetzen.

Bei der Verwendung von Einstellungen für konstante Bitraten (CBR) für Samsung-Geräte mit Profilunterstützung wird die VMS-Qualität anhand der folgenden Grenzwerte in Prozentwerte für die Bitrate umgerechnet:

2Mbps - 15Mbps für eine Auflösungsbreite von 1600px und mehr;

1024Kbps - 10Mbps für Auflösungsbreiten zwischen 1024px und 1600px;

512Kbps - 5Mbps für Auflösungsbreiten zwischen 640px und 1024px;

64Kbps - 2Mbps für eine Auflösungsbreite von weniger als 640px.

Die korrekte VMS-Qualität sollte so eingestellt werden, dass sie zur erforderlichen Netzwerkbandbreite passt. Andere Kameras verwenden die Standardqualitätseinstellungen, nicht die Bitrate.

Die Bitrate kann auf 6 Mbps begrenzt werden, wenn das Videoprofil im Aufnahmemodus für die interne Flash-Karte (Edge Storage) konfiguriert ist. Der Treiber ändert den Wert der GOP-Größe für Videoprofile, die im Aufnahmemodus konfiguriert sind, nicht. Um diese Einschränkung zu vermeiden, konfigurieren Sie bitte ein separates Profil für internes Aufnahmematerial über das Web-Interface der Kamera (im Abschnitt „Videoprofil“).

Für die Verwendung von VBR mit Audio und Multiple Streaming sollte die Kamera über Firmware 2.x oder höher verfügen. Mit älterer Firmware funktioniert Video für Mehrfach-Streaming nicht.

Multicast ist für Samsung-Modelle mit altem SDK (Nicht-Profil-Kameras) nicht aktiviert. Alle diese Modelle arbeiten nur mit Unicast. Diese Kameras können nicht in mehreren VMS-Instanzen verwendet werden!

Unicast mode: Der Treiber ändert die Kameraeinstellungen entsprechend den VMS-Einstellungen und empfängt Audio- und Videodaten von der Kamera über die Unicast-Verbindung.

Multicast:Primary: Der Treiber ändert die Kameraeinstellungen entsprechend den VMS-Einstellungen und empfängt Audio- und Videodaten von der Kamera über die Multicast-Verbindung.

Multicast:Listener: Der Treiber wird die folgenden Kameraeinstellungen nicht ändern:

Qualität

Auflösung

Framerate

Für Multicast:Listener werden die folgenden Optionen auf die gleiche Weise konfiguriert wie für Multicast:Primary:

Option Mehrfaches Streaming

Videocodec für alle Streams

Wenn die Kamera in mehreren VMS-Instanzen verwendet werden soll, sollte ein VMS auf Multicast:Primary und die anderen auf Multicast:Listener eingestellt werden.

Mehrere Multicast:Primary-Konfigurationen oder Multicast:Primary- und Unicast-Konfigurationen sind nicht zulässig, da die Kamera sonst durch ständige gleichzeitige Änderungen der Einstellungen überlastet wird.

Multicast-Adresse und -Port sollten für jedes Profil auf der Webschnittstelle der Kamera eingestellt werden, andernfalls wird Multicast nicht funktionieren. Wenn Mehrfach-Streaming aktiviert ist, erstellt der Treiber ein MLIVE-Profil - Multicast-Adresse und -Port sollten auch für dieses Profil festgelegt werden.

Bereichszoom und Zentrierfunktion sind für Samsung-Kameras mit SUN API 2.0-Unterstützung verfügbar.

Die Änderung der Blende ist aufgrund von Kameraeinschränkungen langsam). Ein Klick - eine Änderung.

Wenn die Kamera bewegt (oder gezoomt) wird, werden automatische Blende und Autofokus angewendet.

Zur Unterstützung von Audio in Edge Feature ist VMS Version 7.4.3.71 oder höher erforderlich.

Die neuen Kameraserien (z. B. QNO/QNV/QND-7010R) haben Einschränkungen bei der Verwendung von 2 Megapixel und höheren Auflösungen für H.264-Streams:

Bei Auflösungen über 2MP (2592x1520 / 2560x1440 / 2304x1296) wird die maximale Bildrate auf die Anzahl der aktiven Streams aufgeteilt:

20 fps / 2 Streams = 10 fps pro Stream;

20 fps / 3 Streams = 6 fps pro Stream.

Ein Stream über 2MP + 2MP-Streams:

15 fps pro Stream für Dual-Streaming-Konfigurationen (Beispiel: 2592x1520 @ 20fps + 1920x1080 @ 20fps)

10 fps pro Stream für Dreifach-Streaming-Konfigurationen (Beispiel: 2592x1520 @ 20 fps + 1920x1080 @ 20 fps + 1920x1080 @ 20 fps)

Nur 2MP (1920x1080) Streams:

Keine Begrenzung für 2 Streams (20 fps pro Stream)

15 fps pro Stream für 3 Streams

Die Funktion zum Ändern von Optionen durch Alarm (CCFiA/CCRiA) ist für Geräte verfügbar, die einen Wechsel der Optionen schneller als 2 Sekunden ermöglichen. Die Geräte, die vor dem Jahr 2015 veröffentlicht wurden, unterstützen diese Funktion nicht.

Windows XP wird seit der Treiberversion 2.2.18.1 nicht mehr unterstützt.




Pagination
Previous page
NewPanasonicIPCapture - Installation und Verwendung
Next page
NewSiquraIPCapture - Installation und Verwendung