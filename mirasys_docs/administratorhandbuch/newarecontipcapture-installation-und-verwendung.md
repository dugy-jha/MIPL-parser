# NewArecontIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/newarecontipcapture-installation-und-verwendung

NewArecontIPCapture - Installation und Verwendung

Der Treiber für den H.264-Komprimierungsmodus verwendet RTSP/RTP/UDP/IP-Protokolle für den Videoempfang bei üblichen Bildraten. Das HTTP-Protokoll wird zum Einstellen/Abrufen von Parametern, zum Empfangen von MJPEG/H.264-Streams bei langsamen Bildraten der Kamera und zum kontinuierlichen Empfangen von MJPEG verwendet.

Wenn sich zwischen VMS und den Kameras eine Firewall befindet, müssen die folgenden RTSP/UDP/HTTP-Ports geöffnet sein:

HTTP: Der Standard-Port ist 80,

RTSP: Der Standard-Port ist 554,

UDP: Zwei aufeinanderfolgende Ports pro Videostream werden in einem Portbereich von 3554 bis 4556 benötigt.

Der Treiber kann mithilfe einer XML-Konfigurationsdatei konfiguriert werden, um die folgenden Parameter einzustellen:

Innenbeleuchtungskompensationswert

Kanalspezifische Parameter:

MaxFrameRate - maximale Bildrate bei voller Auflösung

MaxFrameRateHalf - maximale Bildrate bei halber Auflösung

RTP über RTSP-Transportprotokoll

RTP-Blockgröße (falls für den jeweiligen Router erforderlich)

BitrateMode (CBR, VBR oder Auto - die letzte Option weist den Treiber an, die Qualitätsänderung bei der Kamera zu überspringen)

BitrateMin (Mindestbitrate für CBR)

BirateMax (maximale Bitrate für CBR)

KeyFrameIntervalMs (Intra-Frame-Intervall in ms, 0 - all intras)

IndoorLightFrequency - Lichtfrequenz

Beschränkungen

Der Wert für die maximale Bildrate wird nach der „geheimen“ Formel von Arecont berechnet. Die tatsächliche Bildrate kann niedriger sein als angegeben - sie hängt von den Netzwerkbedingungen ab.

Einige Bildauflösungen können von den Einstellungen abweichen, z.B. 1600x1200 wird zu 1600x1184. Dies liegt daran, dass die Auflösung der Arecont-Kamera für den Vollmodus durch 32 und für den Halbmodus durch 64 teilbar sein muss.

Die maximale Auflösung von Arecont wird an der Kamera eingestellt. VMS verwendet sie und die Hälfte davon. Um die maximale Auflösung zu ändern, müssen Sie sie auf der Kamera ändern und dann eine Kamera zum VMS hinzufügen.

Arecont-Kameras haben nur zwei volle Bildauflösungen - die maximale Sensorauflösung und die Hälfte davon. Die anderen Auflösungen sind von der maximalen Auflösung abgeschnitten und werden im Treiber nicht verwendet.

AV8185 und AV8180 haben kein IO (die Angaben in der Dokumentation sind falsch).

AV3135 hat zwei Sensoren - Tag und Nacht. Beide arbeiten mit bestimmten Auflösungen. VMS zeigt Auflösungen für den Tagmodus an; die tatsächliche Bildauflösung kann von den Einstellungen abweichen.

Arecont-Kameras können die Bildauflösung dynamisch ändern. Die tatsächliche Bildauflösung kann von den Einstellungen abweichen.

DVMS unterstützt nur maximal 30 fps, so dass alle Arecont-Kameras diese Einschränkung haben (auch wenn sie mehr als 30 fps unterstützen).

Bei Arecont 4-Kanal-Kameras kann es Probleme geben, wenn H.264 + MJPEG verwendet wird. Es ist besser, ein Kompressionsformat für alle Kanäle zu verwenden.




Pagination
Previous page
NewActiIPCapture - Installation und Verwendung
Next page
NewAxisIPCapture - Installation und Verwendung