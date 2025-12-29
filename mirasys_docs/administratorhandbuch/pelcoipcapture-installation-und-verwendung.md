# PelcoIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/pelcoipcapture-installation-und-verwendung

PelcoIPCapture - Installation und Verwendung

Der Treiber verwendet RTSP/RTP/UDP/IP-Protokolle für den Empfang von MPEG-4- und H.264-Videos.

Das HTTP-Protokoll wird für das Einstellen/Abrufen von Parametern, den Empfang von JPEG-Videos und für die PTZ-Funktionalität verwendet.

Wenn sich zwischen VMS und den Kameras eine Firewall befindet, müssen die folgenden RTSP/UDP/HTTP Ports geöffnet sein:

HTTP: Der Standardport ist 80 für Sarix-Kameras und 49152 für Nicht-Sarix-Kameras,

RTSP: Hafen 554,

UDP: Pro Videostream sind zwei aufeinander folgende Ports im Portbereich 3556 bis 4556 erforderlich.

TCP: 3549 ist der Standardanschluss für GENA DigitalInputs-Meldungen.

Bitte beachten Sie auch die PelcoIPCapture.xml, Abschnitt DigitalIOListener, Anschlusswert

Beispiel: Wenn ein VMS über 4 Pelco-Kameras verfügt, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Für Sarix, Endura und die neueste Serie der Treiber von vesrion 1.8.0.0 wird die GENA-Benachrichtigungsarchitektur verwendet. Der Treiber konfiguriert automatisch die Windows Firewall, um eingehende Verbindungen zum DigitalIOListener-Port zuzulassen. Siehe auch addFirewallRule Option.

Im Abschnitt „DigitalIOListener“ können die Optionen „address“ und „port“ verwendet werden, um die externe IP-Adresse und den Port anzugeben, falls eine Weiterleitung vom externen Netzwerk auf denselben TCP-Port erfolgt.

Einschränkungen

Die Konfiguration von Qualität und Auflösung für den JPEG-Codec wird für Nicht-Sarix-Kameras nicht unterstützt. Alle JPEG-Bilder werden in 4CIF empfangen. Die SystemManager-Kameraeinstellungen werden in diesem Fall ignoriert.

Pelco Sarix-Kameras erlauben standardmäßig den Zugriff auf sie über SOAP-Anfragen ohne Benutzerauthentifizierung. So kann jeder nicht autorisierte Benutzer Pelco Sarix-Kameras abonnieren und konfigurieren. Um ein solches Verhalten zu vermeiden, setzen Sie bitte die Einstellung „Öffentliche Benutzerzugriffsebene“ auf der Registerkarte „Benutzer“ im Web-Interface auf „Deaktiviert“.

Die Firmware-Version kann nicht von Pelco IP-Kameras abgerufen werden. Dies ist eine Funktion der Pelco-API.

Pelco-Kameras wenden die Einstellungen für den Videostrom etwa 30 Sekunden lang an. Daher können die Funktionen CCRiA und CCFiA nicht für Pelco IP-Kameras implementiert werden.

Sarix MPEG-4 Encoder unterstützt keine Auflösungen über 704x576. Der Treiber setzt die Auflösung automatisch auf 704x576, wenn der Benutzer versucht, eine höhere Auflösung anzuwenden.

Der Treiber kann von Zeit zu Zeit die Anzahl der Ein- und/oder Ausgänge der IP110-Kamera nicht empfangen. Um dieses Problem zu beheben, versuchen Sie, die Kamera aus der Kameraliste zu entfernen und sie dann wieder hinzuzufügen.

Die tatsächliche Framerate für die JPEG-Komprimierung kann geringer sein als die erforderliche Framerate, da die Erfassung von Bildern über HTTP Verzögerungen aufweist.

Die IO-Funktionalität für SARIX-Kameras funktioniert im Moment nicht richtig. Die Zustände der Eingänge können nicht abgefragt werden. Die Ausgabekomponente funktioniert nicht ordnungsgemäß, da die Eingangszustände unbekannt sind.

Die Liste der unterstützten Bildwiederholraten kann für verschiedene Codecs für Sarix-Kameras unterschiedlich sein. Wenn der Benutzer versucht, einen nicht unterstützten Wert für die Bildrate anzuwenden, wird der nächsthöhere Wert für die Bildrate verwendet (z. B. wird der Wert 7,5 anstelle des nicht unterstützten Wertes 6 verwendet). Wenn der Benutzer versucht, einen höheren Wert als den maximal unterstützten Wert anzuwenden, wird automatisch der maximale Wert angewendet. Eine Liste der unterstützten Bildratenwerte finden Sie in der Webschnittstelle der Kamera.

Der Parameter Geschwindigkeit wird von Pelco PTZ IP-Kameras für die folgenden PTZ-Funktionen nicht unterstützt:

Fokussieren;

Zoomen;

Änderung der Blende;

Anfahren der voreingestellten Position. Der Treiber verwendet diese Funktionen also so, wie sie sind: Die Kamera verarbeitet sie in allen Fällen mit konstanter Geschwindigkeit.

Die Spectra HD-Kamera sendet den H.264-Videostrom mit einer niedrigeren Bildrate als erforderlich (z. B. 1 fps anstelle von 4 fps), wenn der Wert der Bildrate gerade ist. Die meisten ungeraden Werte (außer 1 und 25) werden korrekt verarbeitet. Dies ist ein Firmware-Problem.

Der Treiber ist nicht in der Lage, die SOAP-Antwort der Kamera zu parsen, wenn nicht standardisierte Symbole (wie Umlaute oder Hieroglyphen) in den Konfigurationsnamen verwendet werden. Die Verwendung dieser Symbole kann zu fehlerhaftem Verhalten des Treibers führen. Vermeiden Sie daher die Verwendung dieser Symbole bei der Konfiguration von Sarix-Kameras über die Webschnittstelle.

Pelco 1080p-Kameras senden möglicherweise keinen H.264-kodierten Videostrom mit 1080p-Auflösung bei niedrigen Bildraten (von 1 bis 4). Dies ist ein bekanntes Problem der Pelco-Firmware. Einzelheiten finden Sie in der Pelco Knowledge Base: <http://www.pelco.com/sites/global/en/sales-and-support/faq/faq_main.page?AID=12392>.

Um das Problem in der VMS-Software zu lösen, verwenden Sie bitte die niedrigste Qualität für diese Einstellungen.

Der GetAlarmStates-Aufruf, der für die Abfrage der digitalen Eingänge verwendet wird, ist veraltet und wird vom Pelco-Support-Team nicht für die kommerzielle Nutzung empfohlen. Die Abfrage der digitalen Eingänge alle 2 Sekunden kann dazu führen, dass sich die Kamera nach 2-3 Tagen Betrieb aufhängt. Daher ist die Funktion der digitalen Eingänge standardmäßig deaktiviert, kann aber über die XML-Konfigurationsdatei aktiviert werden, falls sie benötigt wird.  It may be required to re-add the camera after configuration file change.

Port 3549 sollte für eingehende Verbindungen in der Windows-Firewall für die DigitalIO-Funktionalität für die Serien Sarix, Endura und höher zugelassen werden. Siehe auch PelcoIPCapture.xml, Abschnitt DigitalIOListener, Port-Wert.

Ältere Versionen der Kameras haben ein Problem, wenn die Digital Outputs-Anforderungen sehr häufig gesendet werden. Wenn der Benutzer eine häufige Änderung des Ausgangs konfiguriert (häufiger als ein Wechsel pro Minute), kann die Kamera nach einigen Tagen hängen bleiben. Um dieses Problem zu vermeiden, deaktivieren Sie bitte die Funktion der digitalen Ausgänge in der Treiberkonfigurationsdatei.

Pelco Optera Serie Panorama-IP-Kameras (IMM12018, IMM12027 und IMM12036 Modelle) haben eine spezielle Implementierung von Stream Dewarping, die noch nicht in den nativen Treiber integriert wurde.

Bitte verwenden Sie stattdessen den ONVIF IP Capture-Treiber für diese Geräteserie.

Pagination
Previous page
OnvifIPCapture - Installation und Verwendung
Next page
PSIAIPCapture - Installation und Verwendung