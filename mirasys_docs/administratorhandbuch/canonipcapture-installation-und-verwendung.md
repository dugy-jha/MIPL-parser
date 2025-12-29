# CanonIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/canonipcapture-installation-und-verwendung

CanonIPCapture - Installation und Verwendung

In allen Komprimierungsmodi verwendet der Treiber die RTSP/RTP/UDP/IP-Protokolle für den Empfang des Videostroms und des Eingangsstatus.

Das HTTP-Protokoll wird für das Setzen/Abrufen von Parametern verwendet.

Wenn sich eine Firewall zwischen VMS und den Kameras befindet, müssen die folgenden RTSP/UDP/HTTP-Ports geöffnet werden:

HTTP: Standard-Ports sind 80,

RTSP: Connection 554,

UDP: Zwei sequentielle Ports pro Videostrom und zwei sequentielle Ports pro Metadatenstrom (Eingangszustände) werden in einem Portbereich von 3556 bis 4556 benötigt.

Beispiel: Wenn ein DVMS über 2 IP-Kameras verfügt, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Die Datei CanonIPCapture.xml wird zur Konfiguration des Treiberverhaltens verwendet:

Unicast

Multicast:Primary

Multicast:Listener

Parameter für die PTZ-Geschwindigkeitsbegrenzung:

PanSpeed (1 - 100%, Grenzgeschwindigkeit für gewünschten Prozentwert)

TiltSpeed (1 - 100%, Grenzgeschwindigkeit für gewünschten Prozentwert)

ZoomSpeed (1 - 100%, Grenzgeschwindigkeit für gewünschten Prozentwert)

PTZQueueSize (PTZ-Warteschlangengröße, kann für langsame Kameras optimiert werden)

Beschränkungen

Ältere Canon Kameras mit Firmware 1.0.3 oder früher können bei jeder Auflösungsänderung neu starten. Dies kann 1-5 Minuten dauern.

VB-S-Kameras haben 2 H.264-Streams, die für die Aufzeichnung und die Live-Übertragung im VMS verwendet werden können. Andere Serien haben nur einen H.264-Kanal.

VB-S-Kameras haben eine Beschränkung auf eine maximale Framerate von 15 für ausgewählte Auflösungen. Wenn eine dieser Kombinationen eingestellt ist, wird die Bildrate geändert, auch wenn die DVMS-Einstellungen anders sind:

1920x1080 - Alle Größen

Alle Größen - 1920x1080

1280x960 - 1280x960

1280x720 - 1280x720

Die Kamera der Serien VB-M, VB-H und VB-S unterscheidet sich von der herkömmlichen Bewegungserkennung. Die Erkennung erstellt ein statisches „Hintergrundbild“ und vergleicht jede Szenenänderung innerhalb des Erfassungsbereichs mit diesem Bild.
Die Kamera sendet eine „Ereignis EIN“-Statusmeldung, wenn das Objekt in den Erfassungsbereich eintritt, und sendet einen „Ereignis AUS“-Status, wenn ein Objekt aus dem Erfassungsbereich herauskommt und die Szene wieder in das ursprüngliche „Hintergrundbild“ geändert wird.“
Wenn der Status „Ereignis EIN“ über einen Zeitraum von 5 Minuten anhält, betrachtet die Kamera dies als einen neuen Hintergrund, sendet den Status „Ereignis AUS“ und kehrt in den Standby-Modus der Alarmerkennung zurück.

Unicast mode: Der Treiber ändert die Kameraeinstellungen entsprechend den DVMS-Einstellungen und empfängt Audio- und Videodaten von der Kamera über eine Unicast-Verbindung.

Multicast:Primary: Der Treiber ändert die Kameraeinstellungen entsprechend den DVMS-Einstellungen und empfängt Audio- und Videodaten von der Kamera über eine Multicast-Verbindung.

Multicast:Listener: Der Treiber ändert keine Kameraeinstellungen, sondern empfängt lediglich Audio- und Videodaten von der Kamera über die Multicast-Verbindung.

Wenn die Kamera in mehreren DVMS-Instanzen verwendet werden soll, sollte ein DVMS auf Multicast:Primary und die anderen auf Multicast:Listener eingestellt werden.

Mehrere Multicast:Primary-Konfigurationen oder Multicast:Primary- und Unicast-Konfigurationen sind nicht zulässig; in anderen Fällen sollte die Kamera mit ständigen gleichzeitigen Einstellungsänderungen überlastet werden.

CCFIA und CCRIA sind für die VB-M-Serie deaktiviert, da Kameras dieser Serie nach einer Änderung der Einstellungen einen Neustart erfordern.

Pagination
Previous page
ArchiveCapture - Installation und Verwendung
Next page
DahuaIPCapture - Installation und Verwendung