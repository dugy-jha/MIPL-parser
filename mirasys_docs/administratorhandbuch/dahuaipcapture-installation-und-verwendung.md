# DahuaIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/dahuaipcapture-installation-und-verwendung

DahuaIPCapture - Installation und Verwendung

Der Treiber verwendet RTSP/RTP/UDP/IP-Protokolle für den Videoempfang in allen Komprimierungsmodi.

Das HTTP-Protokoll wird für das Setzen/Abrufen von Parametern verwendet. Wenn sich eine Firewall zwischen DVMS und den Kameras befindet, müssen die folgenden RTSP/UDP/HTTP-Ports geöffnet sein:

HTTP: Der Standard-Port ist 80,

RTSP: Hafen 554,

UDP: zwei aufeinanderfolgende Ports pro Videostream werden in einem Portbereich von 3556 bis 4556 benötigt.

Wenn beispielsweise 4 Dahua IP-Kameras in einem DVMS vorhanden sind, werden die Ports 3556, 3557, 3558, 3559, 3560, 3561, 3562 und 3563 verwendet. Wenn ein Port nicht frei ist, wird er übersprungen.

Beschränkungen

Für mehrere Streaming-Funktionen können je nach verwendetem Gerät Einschränkungen gelten (z. B. kann die Auflösung des Extra-Streams nicht höher sein als die des Video-Mainstreams). Bitte lesen Sie das Handbuch des Geräts, um diese Einschränkungen zu erfahren.

Die Funktion CCRiA (Can Change Resolution in Alarm) wird nicht unterstützt, da die Anwendung einer neuen Auflösung länger dauert als der Timeout für den Signalverlust.

Kameras mit zwei abhängigen Sensoren, zum Beispiel DH-SDT4E425-8P-GB-APV1, werden nicht vollständig unterstützt.
Unser VMS unterstützt keine unterschiedlichen Auflösungen für verschiedene Kanäle desselben Geräts. Alle Kanäle haben die gleiche Auflösungsliste, aber es können nur unterstützte Auflösungen verwendet werden.
Das Gleiche gilt für die Änderung der Auflösung in der Alarmfunktionalität.

Wenn Dahua/Stanley-Geräte die Auflösung oder Framerate nicht korrekt ändern, aktualisieren Sie sie bitte auf eine neue Firmware. Der Treiber gibt die folgende Meldung in der Datei DVRLog.txt aus:

„Kann keine Videokanäle für Gerät <ip>:80 konfigurieren, Ergebniscode: 12002 (Request timeout).“ „Das Gerät akzeptiert möglicherweise keine neuen Videoeinstellungen ohne korrekten Bitratenparameter. Die Kamera sendet einen falschen Bitratenbereich, und der Treiber berechnet eine inakzeptable Bitrate nach Qualität und versucht, sie sowohl im CBR- als auch im VBR-Modus anzuwenden. Es ist möglich, den Bitratenbereich mit der folgenden Option in der Datei DahuaIPCapture.xml zu überschreiben <BitrateMap enabled=„yes“ Der Treiber verfügt über eine interne Bitratenkarte für die meisten Auflösungen bis zu 1920x1080 nur für den H.264-Codec. Es ist möglich, weitere Bitraten für höhere Auflösungen und den JPEG-Codec hinzuzufügen, wie in den Beispielen im XML des Treibers gezeigt.

Das Dahua-Gerät wird möglicherweise mit einer niedrigeren maximalen Bildrate hinzugefügt, als einige Auflösungen unterstützen. Bitte aktualisieren Sie die Firmware. Wenn dies nicht möglich ist, entfernen Sie das Dahua-Gerät aus DVMS, legen Sie die erforderlichen Videoeinstellungen über die Weboberfläche fest, und fügen Sie es erneut hinzu.

Wenn das Dahua-Gerät viele „400“ oder „500“ HTTP-Fehler als Antwort zurückgibt, aktualisieren Sie es bitte auf eine neue Firmware. Falls das Firmware-Update nicht verfügbar ist, gibt es mehrere Parameter in der Datei DahuaIPCapture.xml:

<UseEventManager>false</UseEventManager> So deaktivieren Sie die „EventManeger“-Abfrageanforderungen

<InputCheckTimeout>1000</InputCheckTimeout> Zum Einstellen des Intervalls zwischen den Anfragen für digitale Eingänge, nur wenn die Option <UseEventManager>false</UseEventManager> deaktiviert ist

<Control digitalInputs="false" motionDetection="false" /> So deaktivieren Sie die digitalen Eingänge und die Bewegungserkennung der Kamera-Hardware

Einschränkungen der Audiofunktionalität:

Der Treiber verwendet die Audiofunktionalität „wie sie ist“, ohne dass die Audioparameter (wie die Ausgangsverstärkung) angepasst werden. Bitte konfigurieren Sie diese Parameter über das Web-Interface.

Der Treiber unterstützt die Audiokodierungen G.711 und G.726. Die AAC-Kodierung wird nicht unterstützt.

Bei einigen Firmware-Versionen kann es vorkommen, dass Two-Way-Audio nach einer Netzwerkunterbrechung nicht funktioniert. Bitte entfernen Sie das Gerät aus DVMS, starten Sie es neu und fügen Sie es erneut hinzu. Um diese Funktion für ein bestimmtes Gerät zu deaktivieren, setzen Sie die folgende Option: <TwoWayAudio>NO</TwoWayAudio>

Einschränkungen bei der Multicast-Erfassung:

Die Multicast-Erfassung kann über eine XML-Konfigurationsdatei mit der Option RTPMode aktiviert werden. Diese Option wird beim Start des Streams gelesen, so dass eine Aktualisierung der Geräteeinstellungen ausreicht, um die geänderte RTPMode-Option zu aktivieren.

Der Benutzer sollte sicherstellen, dass nur ein Rekorder die Einstellungen von IP-Geräten ändert. Andere Rekorder, die diese Kamera verwenden, sollten keine Einstellungen ändern.
Bitte deaktivieren Sie die Änderung der Kameraeinstellungen mit der folgenden Option <ChangeSettings>false</ChangeSettings>
In diesem Modus ändert der Treiber die folgenden Kameraeinstellungen nicht:
= Quality
= Resolution
= Framerate

<ChangeSettings>true</ChangeSettings>
Der Treiber ändert die Kameraeinstellungen entsprechend den DVMS-Einstellungen und empfängt Audio- und Videodaten von der Kamera über eine Multicast-Verbindung. Bitte konfigurieren Sie diesen Modus nur für den primären Rekorder.

Für den sekundären Rekorder werden die folgenden Optionen genauso konfiguriert wie für den primären Rekorder:
= Mehrere Streaming-Optionen
= Video Codec für alle Streams

Verschlüsseltes Streaming weist bekannte Probleme und Einschränkungen auf:

Der Dahua IP Capture-Treiber unterstützt den Empfang verschlüsselter Videoströme von den IP-Geräten. Die Verarbeitung des verschlüsselten Streams basiert auf 3 Dahua-Bibliotheken (NetSDK und PlaySDK von Dahua)

Die Stream-Verschlüsselung sollte über die Web-UI aktiviert werden, bevor sie im Mirasys VMS verwendet wird. Um sie zu aktivieren, gehen Sie zu den Geräteeinstellungen, wählen Sie die Gruppe „System“ und dann die Untergruppe „Sicherheit“ oder „Safety“ (der Name kann bei verschiedenen Geräten unterschiedlich sein). Wählen Sie im Einstellungsdialog die Registerkarte ÑSystemdienstì und aktivieren Sie das Kontrollkästchen ÑAudio- und Videoübertragungsverschlüsselungì.

Wenn das IP-Gerät die Stromverschlüsselung unterstützt, fügt das System den Transport „AES-256 verschlüsselt“ hinzu und wählt ihn als Standardtransport aus. Wenn Sie keine Stromverschlüsselung benötigen ñ wählen Sie einfach einen anderen Transport entsprechend Ihren Anforderungen.

Der AES-256-Algorithmus wird für die Stream-Verschlüsselung gemäß dem GDPR-Spezifikationsdokument von Dahua verwendet. Es wird die Key-Frame-Verschlüsselung verwendet. Mit anderen Worten:
= Die Stream-Verschlüsselung kann für H.265-, H.264- und MPEG-4-Kodierungen verwendet werden;
= Der MJPEG-Stream kann nicht verschlüsselt und unverändert über SDK-Bibliotheken empfangen werden.

MPEG-4-Verschlüsselung wird unterstützt. Es war jedoch kein Gerät verfügbar, um dies in Mirasys zu testen. Daher wurde die Implementierung auf der Grundlage der SDK-Dokumentation vorgenommen, aber nicht getestet.

Die Audioverschlüsselung ist über NetSDK verfügbar, wurde aber nicht in den Treiber implementiert.

Die Verschlüsselung wird für Multicast-Streaming nicht unterstützt.

Für einen schnellen Start der Videoaufzeichnung im Multicast-Modus ist es möglich, Adressen und Ports auf dem Gerät und in der Treiber-XML-Datei zu konfigurieren und die Anpassung der Videoeinstellungen durch die folgende Option <ChangeSettings>false</ChangeSettings> zu deaktivieren.

Der Zoom funktioniert bei der Stanley IPC-STAN-6100IRV Kamera möglicherweise nicht richtig. Dies ist ein Problem der Kamera-Firmware.

Der Treiber unterstützt keinen Unicode in PTZ-Voreinstellungsnamen (Präposition).

Bitte versuchen Sie nicht, die Kamera mit der Option <Alle Treiber> und den <Standard>-Anmeldeinformationen oder einem falschen Kennwort zu suchen - dies kann das Benutzerkonto sperren. Bitte fügen Sie das Gerät stattdessen mit einem einzigen „DahuaIPCapture“-Treiber hinzu.

Dieser Treiber unterstützt nicht Windows XP.

Pagination
Previous page
CanonIPCapture - Installation und Verwendung
Next page
EHIIPCapture - Installation und Verwendung