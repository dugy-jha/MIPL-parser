# Aktionstypen und Einstellungen | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/aktionstypen-und-einstellungen

Aktionstypen und Einstellungen

Die folgende Liste enthält die Standardaktionstypen und ihre Parameter. Einige der oben aufgeführten Aktionstypen sind möglicherweise nicht auf allen Systemen verfügbar.

Zusätzlich zu den Standardaktionen kann das System Alarmaktionen enthalten, die über Module von Drittanbietern installiert werden.

Kameraaufnahme

Die Kameraaufzeichnung ist die Standardaktion für Kameras. Wenn ein Alarm ausgelöst wird, der diesen Aktionstyp enthält, werden die durch den Alarmtyp definierten Aufnahmeeinstellungen anstelle der Standardeinstellungen der Kamera verwendet.

Wenn in Spotter Alarm-Popup-Fenster für das Benutzerprofil aktiviert sind, werden Geräte, die mit der Aktion Kameraaufzeichnung verwendet werden, in der Alarm-Popup-Ansicht angezeigt, wenn der Alarm ausgelöst wird.

Die Aktion umfasst die folgenden Felder und Parameter:

Referenzbild

Dieses statische Feld enthält das Referenzbild (Image) der Kamera (A).

Kameraeinstellungen verwenden

Durch Aktivieren dieses Kontrollkästchens wird die Alarmaufzeichnung mit der kameraspezifischen Einstellung für Auflösung und Aufzeichnungsrate durchgeführt (B).

Auflösung

Verwenden Sie den Schieberegler, um die Auflösung einer IP-Kamera während der Alarmaufzeichnung zu ändern. Der Schieberegler ist nur für IP-Kameras aktiv (C).

Aufzeichnungsrate

Verwenden Sie den Schieberegler, um die IPS-Rate der Kamera während der Alarmaufzeichnung zu ändern. Der Schieberegler ist inaktiv, wenn das Kontrollkästchen Kameraeinstellungen verwenden markiert ist (D).

Aufzeichnung vor der Veranstaltung

Markieren Sie dieses Kontrollkästchen, um die Aufzeichnung vor dem Ereignis einzuschalten. Die Dauer der Aufzeichnung vor der Veranstaltung kann mit dem Schieberegler Aufzeichnung vor der Veranstaltung eingestellt werden (E).

Aufzeichnung nach der Veranstaltung

Aktivieren Sie dieses Kontrollkästchen, um die Aufzeichnung nach der Veranstaltung aktivieren. Die Dauer der Aufzeichnung nach der Veranstaltung kann mit dem Schieberegler Aufzeichnung nach der Veranstaltung eingestellt werden (F).

Aufnahmezeit vor und nach dem Ereignis

Diese Schieberegler können verwendet werden, um die Aufzeichnungsdauer vor und nach dem Ereignis für die Aktion einzustellen. Die Schieberegler sind nur aktiv, wenn die Aufzeichnung vor und/oder nach dem Ereignis aktiviert wurde (G).

Alle Geräte (Kameras und Mikrofone) sind mit dem Alarm verbunden und haben ihre Aufzeichnung vor und nach dem Ereignis aktiviert, um die gleiche Aufzeichnungsdauer vor und nach dem Ereignis zu teilen.

Audio Aufnahme

Die Audioaufzeichnung ist die Standardaktion für Mikrofone. Wenn ein Alarm ausgelöst wird, der diesen Aktionstyp enthält, werden die vom Alarmtyp definierten Aufnahmeeinstellungen anstelle der Standardeinstellungen des Mikrofons verwendet.

Wenn in Spotter Alarm-Popup-Fenster für das Benutzerprofil aktiviert sind, werden Geräte, die mit der Aktion Audioaufnahme verwendet werden, in der Alarm-Popup-Ansicht angezeigt, wenn der Alarm ausgelöst wird.

Die Aktion umfasst die folgenden Felder und Parameter:

Aufzeichnung vor der Veranstaltung

Markieren Sie dieses Kontrollkästchen, um die Aufzeichnung vor dem Ereignis einzuschalten. Die Dauer der Aufzeichnung vor der Veranstaltung kann mit dem Schieberegler Aufzeichnung vor der Veranstaltung eingestellt werden.

Aufzeichnung nach der Veranstaltung

Aktivieren Sie dieses Kontrollkästchen, um die Aufzeichnung nach der Veranstaltung aktivieren. Die Dauer der Aufzeichnung nach der Veranstaltung kann mit dem Schieberegler Aufzeichnung nach der Veranstaltung eingestellt werden.

Aufnahmezeit vor und nach dem Ereignis

Diese Schieberegler können verwendet werden, um die Aufzeichnungsdauer vor und nach dem Ereignis für die Aktion einzustellen. Die Schieberegler sind nur aktiv, wenn die Aufzeichnung vor und/oder nach dem Ereignis aktiviert wurde.

Alle Geräte (Kameras und Mikrofone), die mit dem Alarm verbunden sind und deren Aufzeichnung vor und nach dem Ereignis aktiviert ist, um die gleiche Aufzeichnungsdauer vor und nach dem Ereignis zu teilen.

Digitaler Ausgang

Der digitale Ausgang ist die Standardaktion für digitale E/A-Geräte. Wenn ein Alarm ausgelöst wird, der diesen Aktionstyp enthält, wird das E/A-Gerät aktiviert.

Auch wenn die Schieberegler Aufnahmezeit vor und nach dem Ereignis für den Aktionstyp angezeigt werden, haben sie keinen Einfluss auf die Funktionalität der Aktion.

PTZ (Dome) Voreingestellte Position

Die Aktion PTZ voreingestellte Position kann verwendet werden, um eine PTZ-Kamera auf eine bestimmte voreingestellte Position einzustellen.

Wenn ein Alarm ausgelöst wird, der diesen Aktionstyp enthält, bewegt sich die PTZ-Kamera automatisch in die ausgewählte voreingestellte Position.

Informationen zum Festlegen von voreingestellten PTZ-Kamerapositionen finden Sie im Mirasys VMS Spotter-Benutzerhandbuch.

Es sollte beachtet werden, dass diese Aktion die PTZ-Kamera in eine voreingestellte Position bewegt, aber nicht dazu führt, dass der Video-Feed von der PTZ-Kamera in der Alarmansicht in der Client-Anwendung angezeigt wird, es sei denn, es wurden andere Alarmaktionen wie Kameraaufzeichnung durchgeführt für die PTZ-Kamera ausgewählt.

Die Aktion umfasst die folgenden Felder und Parameter:

Position

Verwenden Sie das Dropdown-Menü, um die voreingestellte Position auszuwählen, in die sich die PTZ-Kamera während des Alarms bewegt.

Auch wenn die Schieberegler Aufnahmezeit vor und nach dem Ereignis für den Aktionstyp angezeigt werden, haben sie keinen Einfluss auf die Funktionalität der Aktion.

PTZ (Dome) Kameratour

Die Aktion PTZ-Kameratour kann verwendet werden, um eine PTZ-Kamera so einzustellen, dass sie eine vorprogrammierte PTZ-Kameratour startet. Wenn ein Alarm ausgelöst wird, der diesen Aktionstyp enthält, wird die ausgewählte PTZ-Kameratour gestartet. Informationen zum Festlegen von voreingestellten PTZ-Kameratour finden Sie im Mirasys VMS Spotter-Benutzerhandbuch.

Es sollte beachtet werden, dass diese Aktion die PTZ-Kameratour startet, aber nicht dazu führt, dass der Video-Feed von der PTZ-Kamera in der Alarmansicht in der Client-Anwendung angezeigt wird, es sei denn, andere Alarmaktionen, wie z. B. Kameraaufzeichnung, wurden für ausgewählt PTZ-Kamera.

Die Aktion umfasst die folgenden Felder und Parameter:

Program

Verwenden Sie das Dropdown-Menü, um die PTZ-Kameratour auszuwählen, die beginnt, wenn der Alarm ausgelöst wird.

Auch wenn die Schieberegler Aufnahmezeit vor und nach dem Ereignis für den Aktionstyp angezeigt werden, haben sie keinen Einfluss auf die Funktionalität der Aktion.

Stellen Sie die Bewegungserkennungsmaske ein

Die Aktion Stellen Sie die Bewegungserkennungsmaske ein kann die Bewegungserkennungsmaske ändern, die von einer bestimmten Kamera während des Alarms verwendet wird. Wenn der Alarm auftritt, wird die für die bezeichnete Kamera verwendete Bewegungserkennungsmaske in die alarmspezifische Maske geändert. Nach Ende des Alarms stellt das System die Standardmaske wieder her.

Die Aktion umfasst die folgenden Felder und Parameter:

Masken

Verwenden Sie das Dropdown-Menü, um die Bewegungserkennungsmaske auszuwählen, die während des Alarms verwendet wird.

Auch wenn die Schieberegler 2Vor- und Nachaufzeichnungsdauer2 für den Aktionstyp angezeigt werden, haben sie keinen Einfluss auf die Funktionalität der Aktion.

E-Mail senden

Die Aktion E-Mail senden kann zum Senden von E-Mails an beliebige E-Mail-Adressen oder Gruppen verwendet werden, die in den E-Mail-Einstellungen auf der Registerkarte System konfiguriert wurden.

Sie können auswählen, welcher Empfänger oder welche Gruppe den Alarm erhalten soll.

Sie können auch ein oder mehrere unskalierte oder verkleinerte Bilder in die Alarm-E-Mail einfügen. Deaktivieren Sie dazu die Option Im Kurzformat senden und aktivieren Sie die Option Bilder anhängen

Danach können Sie eine Kamera, die Größe für die Bildskalierung, die gewünschte Anzahl von Bildern und den Zeitraum, aus dem die Bilder abgerufen werden, auswählen.

Die Anzahl der Bilder in dieser Konfiguration ist die maximal gelieferte Menge. Möglicherweise kommen weniger Bilder an

Das Anhängen von Bildern an Alarm-E-Mails kann zu hohem Datenverkehr führen, daher wird empfohlen, die Konfigurationseinstellungen zu testen, um die optimale Einstellung zu finden.

Wenn Sie Probleme haben, dass mit den Standardeinstellungen keine Bilder ankommen, wird empfohlen, mehr als ein Bild für die Einstellung „Maximale Bilder“ auszuwählen und die Schieberegler leicht anzupassen, um eine längere Zeit zu haben, in der die Bilder abgerufen werden.

Die Aktion umfasst die folgenden Felder und Parameter:

Format

Definiert das Nachrichtenformat als kurz oder normal.

Eine Kurznachricht enthält nur bis zu 160 Zeichen und kann keinen zusätzlichen Nachrichtentext oder Bildanhänge enthalten (siehe unten).

Nachricht

Dieses Feld enthält die Nachricht, die an die Empfänger gesendet wird, wenn der Alarm auftritt. Das Nachrichtenfeld ist nur aktiv, wenn das E-Mail-Format auf lang eingestellt ist.

Im Gegensatz zu anderen Alarmaktionen kann die Aktion E-Mail senden nur einmal für jeden Alarm ausgewählt werden. Nach der Auswahl verschwindet die Aktion aus der Liste der verfügbaren Aktionen.

Die Nachricht enthält den Alarmnamen im Titel.

Alarme deaktivieren

Die Aktion Alarme deaktivieren kann verwendet werden, um Deaktivierungsalarme basierend auf einem Alarm zu senden. Die Konfiguration kann so erfolgen, dass alle Alarme deaktiviert sind, Alarme mit niedriger und mittlerer Priorität oder Alarme mit niedriger Priorität.

Mit dieser Option können bestimmte Alarme aktiv bleiben, während andere unterdrückt werden.

Die Alarme werden nur deaktiviert, solange der Alarm, der sie deaktiviert, aktiv ist.

Pagination
Previous page
Hinzufügen eines neuen Weckers
Next page
ONVIF Profile M