# OnvifIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/onvifipcapture-installation-und-verwendung

OnvifIPCapture - Installation und Verwendung

In allen Komprimierungsmodi verwendet der Treiber RTSP/RTP/UDP/IP-Protokolle für den Videoempfang. Das HTTP-Protokoll wird für das Setzen/Abrufen von Parametern verwendet.

Wenn sich eine Firewall zwischen VMS und den Kameras befindet, müssen die folgenden RTSP/UDP/HTTP-Ports geöffnet sein:HTTP: default port is 80,

RTSP: Der Standard-Port ist 554,

UDP: Zwei aufeinanderfolgende Ports pro Unicast-Audio- oder Videostream in einem Portbereich von 3556 bis 4556 benötigt werden.

Wenn beispielsweise 4 IP-Kameras in einem VMS vorhanden sind, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Für das Multicast-Streaming sind ebenfalls zwei aufeinander folgende Ports pro Audio- oder Videostream erforderlich, aber die Anzahl der Ports hängt von den Geräteeinstellungen oder der XML-Konfiguration ab. Das Gerät kann zum Beispiel so konfiguriert sein, dass alle Streams nur an einen einzigen Port gesendet werden. Die Ports 40000-40001 sollten geöffnet werden, wenn für diese Einstellung der Port 40000 angegeben ist.

Beschränkungen

Der Befehl PTZ Area Zoom wird standardmäßig mit dem Befehl PTZ Center kombiniert, sofern unterstützt

Der PTZ-Center-Befehl wird mit geringer Genauigkeit ausgeführt, da die Genauigkeit stark vom Kameramechanismus, den vertikalen und horizontalen Blickwinkeln und den optischen Aberrationen (z. B. Verzerrungen) des aktuellen Objektivs abhängt. Es gibt derzeit keine Möglichkeit, diese Einstellungen einzugeben und zu speichern.

Der Treiber benötigt ein Medienprofil, um Voreinstellungen vom IP-Gerät zu empfangen. Sie können also geladen werden, nachdem der Videostream abonniert wurde.

Der Treiber verwendet Zeitstempel zur Authentifizierung auf dem Gerät gemäß den ONVIF-Spezifikationen. Daher sollten die Zeit auf dem ONVIF-kompatiblen Gerät und die Zeit auf dem PC, auf dem der VMS Recorder installiert ist, vor der Verwendung des Geräts synchronisiert werden.

Der Treiber unterstützt keine Unicode-Positionsnamen.

Die Mehrfach-Streaming-Funktion kann abhängig vom verwendeten Gerät Einschränkungen haben (z.B. kann die Auflösung auf Encoder1 nicht größer sein als die Auflösung auf Video-Encoder2). Bitte lesen Sie das Gerätehandbuch, um diese Einschränkungen zu erfahren.

Geräte mit mehreren Kanälen können unterschiedliche Funktionen für verschiedene Kanäle unterstützen. Beispielsweise unterstützt der erste Kanal einen H.264- und MPEG-4-Stream mit einer Auflösung von 1920x1080 und der zweite Kanal unterstützt nur die H.264-Kodierung, aber mit einer größeren Auflösung von 4096x2160. Die VMS-Architektur erlaubt es nicht, unterschiedliche Fähigkeiten für verschiedene Kanäle zu übergeben, daher werden die Fähigkeiten aller Kanäle kombiniert (d. h. MPEG-4-Kodierung und 4096x2160-Auflösung sind für beide Kanäle im obigen Beispiel verfügbar).

Der Treiber wählt automatisch eine geeignete Option aus, wenn der Benutzer versucht, einen Optionswert anzuwenden, der vom aktuellen Videokanal nicht unterstützt wird.

In einigen Fällen kann der Benutzer mit dem Problem „Kein Signal“ konfrontiert werden, weil das ONVIF-konforme Gerät falsch konfiguriert wurde (die Meldung „ter:Action > ter:ConfigurationConflict“ wird in der Protokolldatei angezeigt). In diesem Fall sollte der Benutzer die Einstellungen in VMS entsprechend den Fähigkeiten des Geräts korrigieren, wenn Mehrfach-Streaming aktiviert ist. Wenn die Option Mehrfaches Streaming nicht verwendet wird, nehmen Sie bitte minimale Einstellungen für zusätzliche Streams über das Web-Interface vor oder deaktivieren Sie sie ganz.

ONVIF-konforme Geräte können möglicherweise nicht von „Single Stream“ auf „Triple Stream“ umschalten, ohne die Einstellungen für den zweiten Stream zu übernehmen. Mit anderen Worten: Der Remote-Stream wird möglicherweise nicht korrekt eingerichtet, wenn der Live-Stream nicht gestartet wurde, nachdem die Funktion „Multiple Streaming“ aktiviert wurde.

Der Treiber wendet die Einstellungen für verschiedene Streams nacheinander an, nicht gleichzeitig. Daher kann das Starten zusätzlicher Streams mehr Zeit in Anspruch nehmen als das Starten nur des Aufzeichnungsstreams.

Der Treiber verwendet die PTZ-Dienstversion 2.0 gemäß den ONVIF-Spezifikationen. Alte Geräte können jedoch die frühere Version 1.0 des PTZ-Dienstes verwenden, so dass der Treiber die PTZ-Funktionen nicht korrekt erkennt. Bitte verwenden Sie in diesem Fall die XML-Konfigurationsdatei, um die richtige PTZ-Service-Version anzugeben.

Der Treiber verwendet den Pull-Point-Mechanismus, um die Zustände der digitalen Eingänge zu empfangen und den Bewegungserkennungsstrom zu überwachen. Wenn ein ONVIF-konformes Gerät diesen Mechanismus unterstützt, sollte es die Fähigkeit WSPullPointSupport in tds:GetCapabilitiesResponse gemäß Abschnitt 9.9 der ONVIF-Core-Spezifikation einstellen. Die digitalen Eingänge und die VMD-Funktionalität werden nicht erkannt, wenn diese Fähigkeit auf „nicht unterstützt“ gesetzt ist.

Einschränkungen der Audiofunktionalität

Der Treiber verwendet die Audiofunktionalität „wie sie ist“ ohne Anpassung der Audioparameter (z. B. Ausgangsverstärkung). Für die herstellerspezifischen Parameter wie „Eingangs-/Ausgangsintervall“ oder „Ausgangsdauer“ gibt es in den ONVIF-Spezifikationen keine entsprechenden Optionen. Bitte konfigurieren Sie diese Parameter vor der Verwendung der Kamera manuell über das Web-Interface.

Einschränkungen der Multicast-Erfassung

Die Multicast-Erfassung kann über die XML-Konfigurationsdatei mit der Option StreamingMode aktiviert werden. Diese Option wird beim Start des Streams gelesen, so dass eine Aktualisierung der Geräteeinstellungen ausreicht, um die geänderte StreamingMode-Option zu verwenden.

Bitte beachten Sie, dass VMS seit Version 7.4.1 über eine Optimierung für den Neustart von Kanälen verfügt, so dass es in diesem Fall erforderlich ist, eine der Videooptionen für jeden Kamerastream zu ändern, um sie neu zu starten. Die Audioeinstellungen sollten ebenfalls aktualisiert werden, um die Option zu verwenden.

Die Treiberinstanz kann so konfiguriert werden, dass sie als primäre Instanz oder als Listener verwendet wird. Die primäre Instanz ist in der Lage, die IP-Geräteeinstellungen zu ändern und zusätzliche Funktionen zu nutzen. Listener-Instanzen sind in der Lage, Video- und Audioströme per Multicast zu empfangen und ermöglichen die Nutzung der digitalen E/A- und VMD-Funktionen.

Der Treiber wählt eine Kombination von Videoquellen, Video-Encodern und Medienprofilen während der Erkennung von Fähigkeiten aus. Es ist erforderlich, dass sowohl die primäre als auch die Listener-Instanz dieselbe Kodierung auswählen, damit sie dasselbe Medienprofil auswählen können. Andernfalls wird die Listener-Treiberinstanz versuchen, ein anderes Profil zu abonnieren und einen anderen Multicast-Stream oder überhaupt keine Daten empfangen.

Der Listener-Recorder ändert keine Konfiguration auf der Seite des ONVIF-konformen Geräts. Wenn zum Beispiel kein Medienprofil auf der Kamera vorhanden ist, wird es nicht erstellt und der Treiber kann den Video- oder Audiostrom nicht empfangen. Das ONVIF-Gerät sollte vor der Verwendung in der Listener-Konfiguration zum primären Rekorder hinzugefügt werden.

Die zusätzlichen Streams (Live und Remote) sind nur dann aktiv, wenn sie in Clients geöffnet sind. Um die aktualisierten Multiple Streaming-Einstellungen zu verwenden, müssen diese Streams für den primären Rekorder gestartet (oder geöffnet gehalten) werden, nachdem die Stream-Einstellungen im VMS geändert wurden. Andernfalls werden die neuesten Stream-Einstellungen nicht auf die Kamera angewendet.

Sie sollten sicherstellen, dass nur ein Rekorder die Einstellungen von ONVIF-kompatiblen IP-Geräten ändert. Andere Rekorder, die diese Geräte verwenden, sollten sich im Listener-Modus befinden.

Es ist erforderlich, die IP-Adresse des Netzwerkadapters anzugeben, über den die Kamera angeschlossen ist, um das Multicast-Streaming korrekt zu empfangen, falls mehr als ein Netzwerkadapter vorhanden ist. Wenn keine Option konfiguriert ist, wird der in Windows als Standard markierte Netzwerkadapter verwendet.

Der Treiber kann eine Meldung über eine ungültige Multicast-Konfiguration schreiben (z.B.:  ter:InvalidArgVal > ter:InvalidMulticastSettings). Diese Meldung bedeutet, dass ein Fehler in der Multicast-Konfiguration vorliegt und der Video- oder Audiostream nicht gestartet werden kann.

Bitte geben Sie den Abschnitt Multicast in der XML-Konfigurationsdatei an, um das Problem zu lösen, oder passen Sie die Werte an, wenn dieser Abschnitt bereits vorhanden ist.

Einige ONVIF-konforme IP-Geräte (z. B. Axis) ermöglichen es, den Videostream beizubehalten, während der Client seine Videoparameter ändert. Infolgedessen wird ein solches Gerät den aktiven Stream für die Multicast:Listener-Instanz mit den vorherigen Einstellungen beibehalten und einen anderen Stream für die Multicast:Primary-Instanz mit den aktualisierten Einstellungen starten.

Es ist erforderlich, die Überwachung der Videooptionen auf der Hörerseite mit dem Parameter VideoSettingsMonitoringInterval zu aktivieren. Weitere Einzelheiten sind den Kommentaren in der Konfigurationsdatei zu entnehmen.

Einschränkungen der Video-Bewegungserkennung

Das Gerät sollte den Themensatz 'tns1:VideoSource/MotionAlarm' unterstützen, um die Bewegungserkennungsfunktion zu unterstützen. Benutzerdefinierte Themensätze wie „tns1:VideoAnalytics/tnssamsung:MotionDetection“ können ebenfalls unterstützt werden, funktionieren jedoch nur bei Geräten mit einem Kanal, da diese Themensätze keine Videoquellen- oder Kanalkennungen als Quelldaten in Ereignisbenachrichtigungen enthalten.

Es sind keine IP-Geräte-bezogenen Bewegungserkennungseinstellungen in VMS verfügbar. Daher sollten die Bewegungserkennungseinstellungen (Bereiche, Empfindlichkeit, Objektgröße usw.) auf dem IP-Gerät manuell konfiguriert werden, bevor diese Funktion im VMS verwendet wird.

Die Bewegungserkennung kann mit Multicast-Streaming verwendet werden. Die Option „Rekorder- und Kamerahardware“ sollte sowohl auf dem primären als auch auf dem Listener-Rekorder aktiviert sein, damit der Videostream korrekt angehalten/fortgesetzt werden kann.

Es gibt keine Möglichkeit, den Zeitpunkt der Anwendung von Video-Optionen ohne Änderung der Kamerakonfiguration zu erkennen. Der Treiber fügt die Unterstützung von CFiA/CRiA-Funktionen für alle Geräte hinzu, kann aber nicht garantieren, dass die Kamera die Optionen schnell genug per Alarm umschaltet.

Bitte probieren Sie die CFiA/CRiA-Funktion in einem Testaufbau aus, bevor Sie sie mit Sicherheitssystemen verwenden.

Sonstige Hinweise

Der Treiber verwendet seit der Treiberversion 1.5.0.0 standardmäßig den Transport „RTP over RTSP“ für das Video-/Audio-Streaming.

Die digitalen Eingänge, die vom ONVIF-konformen Gerät zurückgegeben werden, sind nach Token-Namen sortiert, um sicherzustellen, dass sie vom Gerät bei der ersten Statusabfrage nicht neu geordnet werden. Daher können die realen Eingangsnummern von den VMS-Werten abweichen (z. B. „1“, „2“, ..., „10“ wird als „1“, „10“, „2“, ..., „9“ sortiert).

Die Funktion „Optionen bei Alarm ändern“ (CRiA/CFA) kann nur im „aktiven“ Steuerungsmodus verwendet werden. Im „Passiv“-Modus ändert der Treiber keine Optionen der IP-Kamera, so dass der Stream ohne Änderung der Auflösung oder der Bildrate weiterläuft.

Windows XP wird seit Treiberversion 1.5.0.0 nicht mehr unterstützt.




Pagination
Previous page
NewSonyIPCapture - Installation und Verwendung
Next page
PelcoIPCapture - Installation und Verwendung