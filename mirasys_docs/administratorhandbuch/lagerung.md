# Lagerung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/lagerung

Lagerung

In den Speichereinstellungen können Sie die Speicherzeit der aufgezeichneten Video-, Audio- und Textdaten sowie Alarmdaten festlegen.

Darüber hinaus können Sie nach dem Hinzufügen einer Festplatte zu einem Server diese über die Speichereinstellungen als zusätzlichen Datenspeicher festlegen.

Die Speichereinstellungen werden auch verwendet, um die automatische Archivierungsfunktion zu konfigurieren, die es ermöglicht, täglich oder wöchentlich Sicherungskopien der serverspezifischen Video-, Audio- und Textdaten zu erstellen.

Video-, Audio-, Textdaten und Alarmaufzeichnungen werden aufbewahrt, bis ihr definiertes Maximum-Datum überschritten oder der zugewiesene Speicherplatz erschöpft ist.

Speicherplatz hinzufügen

Wenn zusätzlicher Speicherplatz benötigt wird, können Sie neue Festplatten hinzufügen oder ein Netzlaufwerk für die Datenspeicherung (z. B. NAS-Unterstützung) zuordnen.

Wie im Bild zu sehen, können mehrere Netzwerkspeicherlaufwerke und lokale Laufwerke gleichzeitig verwendet werden.

Notiz: Beim Hinzufügen von Speicherlaufwerken zum alten Mirasys-Dateisystem (VMS-Serverversion 7.5.x oder früher) wird empfohlen, dass die Speicherlaufwerke alle die gleiche Kapazität haben, und jede einzelne Festplatte sollte weniger als 10 TB groß sein, und die Gesamtgröße pro VMS Server sollte weniger als 25 TB groß sein.

Die Verwendung mehrerer Speicherplatten hat den Vorteil, dass das Schreiben von Material auf alle Laufwerke verteilt werden kann, wodurch es unwahrscheinlicher wird, dass ein Verlust eines einzelnen Materiallaufwerks große Teile des gespeicherten Materials auslöscht.

So fügen Sie eine Festplatte hinzu:

Installieren Sie die neue Festplatte.

Klicken Sie in Speichereinstellungen auf Festplatte hinzufügen.

Das Dialogfeld Datenträger hinzufügen wird angezeigt.Die Minimaler freier Speicherplatz auf der neuen Diskettenbox zeigt, wie viel freien Speicherplatz die neue Diskette haben muss.

Wählen Sie die Festplatte aus der Liste aus und klicken Sie auf OK.

So ordnen Sie ein Netzlaufwerk zu:

Aktivieren Sie in  Speichereinstellungen  das Kontrollkästchen  Netzlaufwerk .

Klicken Sie bei Bedarf auf Netzlaufwerk definieren

um den Konfigurationsbildschirm für Netzlaufwerke zu öffnen.

Geben Sie den Benutzernamen und das Passwort des Netzlaufwerks in die Felder Benutzername und Passwort ein.

Geben Sie den Speicherort des Netzlaufwerks in das Feld Netzlaufwerkspfad ein.

Klicken OK

Verwenden Sie den Schieberegler Zugewiesener Speicherplatz, um den Speicherplatz einzustellen, der auf dem Netzlaufwerk für die Datenspeicherung reserviert ist.

So ordnen Sie mehrere Netzlaufwerke zu:

Installieren und konfigurieren Sie den Netzwerkspeicher so, dass er als lokal zugeordnetes Laufwerk funktioniert (verwenden Sie beispielsweise iSCSI-Initiator oder ähnliches).

Klicken Sie in Speichereinstellungen auf Festplatte hinzufügen

Das Dialogfeld Datenträger hinzufügen wird angezeigt.

Die Speichergröße kann für iSCSI-Festplatten nicht konfiguriert werden.

Klicken Sie auf OK, um die Einstellungen zu speichern. Wiederholen Sie dies für andere Festplatten.

Speichereinstellungen für Video-, Audio- und Textdaten
Minimum

Um Aufzeichnungen von einem oder mehreren Video-, Audio- oder Textdatenkanälen zu priorisieren, stellen Sie sicher, dass die Mindestwerte für andere Kanäle ausreichend niedrig sind.

Stellen Sie dann den Wert für den oder die Kanäle mit hoher Priorität höher ein.

Wenn Sie Automatisch wählen, löscht das System Aufnahmen von Kanälen, die den meisten Speicherplatz beanspruchen.

Maximal

Das System prüft die Aufzeichnungen täglich und löscht diejenigen, die älter als die maximale Anzahl von Tagen sind.

Wenn Sie Automatisch wählen, werden die Aufnahmen nur gelöscht, wenn der freie Speicherplatz nicht ausreicht.




Notiz: Wenn die Mindestwerte für einige Kanäle zu hoch sind, während sie gleichzeitig für andere Kanäle nicht eingestellt sind, löscht das System Aufzeichnungen von den Kanälen ohne eingestelltes Minimum.

Alarmgrenzen
Minimum

Das System löscht Alarme, die älter als der Mindestwert sind.

Wenn Sie Automatisch wählen, werden die Aufnahmen nur gelöscht, wenn der freie Speicherplatz nicht ausreicht.

Maximal

Das System prüft die Alarmaufzeichnungen täglich und löscht sie, die älter als die maximale Anzahl an Tagen sind.

Wenn Sie Automatisch wählen, werden die Aufnahmen nur gelöscht, wenn der freie Speicherplatz nicht ausreicht.

Log-Einträge

Dieser Wert gibt an, wie viele Alarmereignisse maximal im Alarmprotokoll gespeichert werden.

Das System prüft stündlich die Anzahl der Logeinträge und löscht bei Überschreitung die ältesten Einträge.

% maximal

Dieser Wert gibt an, wie viel Speicherplatz Alarmaufzeichnungen vom gesamten Speicherplatz verwenden dürfen.

Solange nicht der gesamte Speicherplatz belegt ist, können Alarmaufzeichnungen mehr Speicherplatz als diesen Wert beanspruchen.

Das System löscht zuerst die ältesten Alarmaufzeichnungen, bevor es andere Video- oder Audioaufzeichnungen löscht, wenn der gesamte Speicherplatz belegt ist.

Automatisches Löschen von Video-, Audio- und Textdaten

Nach Überschreiten der definierten maximalen Speicherzeit werden gespeicherte Video-, Audio-, Text- und Alarmdaten automatisch gelöscht – die maximale Speicherzeit für Daten, die das System täglich prüft.

Da die Größe eines gespeicherten Datenstroms aufgrund von Bewegungen im Videobild, Änderungen der Audiopegel oder der Anzahl von Textdatenereignissen erheblich variieren kann, kann es schwierig sein, den Speicherplatzbedarf genau vorherzusagen.

Daher kann es das System manchmal für erforderlich halten, freien Speicherplatz zu gewährleisten, indem es altes Material unabhängig von der maximalen Speicherzeit automatisch löscht.

Wenn Daten gelöscht werden müssen, um freien Speicherplatz zu gewährleisten, läuft der Löschvorgang nach folgendem Muster ab:

In einfachen Worten läuft dieser Aufbewahrungsprozess so ab, wenn FS eine neue kostenlose Datei benötigt:

Überprüfen Sie die Alarmquote. Wenn die Alarmmaterialdateien mehr zählen als die Quote (% von allen Daten), bereinigen wir die älteste Alarmdatei und verwenden sie wieder

Überprüfen Sie die Mindesteinstellungen für Alarmdaten – wenn Alarmkanäle Daten enthalten, die die Mindestalarmeinstellungen überschreiten – nehmen wir die älteste Datei von diesen, bereinigen sie und verwenden sie erneut

Überprüfen Sie die Mindesteinstellungen für alle Materialkanäle (Video, Audio, Daten) – wenn einige Kanäle Daten enthalten, die die Mindesteinstellungen überschreiten – nehmen wir die älteste Datei von diesen, bereinigen sie und verwenden sie wieder

Überprüfen Sie die älteste Datei von Kanälen mit automatischen Min-Einstellungen, wenn sie vorhanden sind. Wenn ja, nehmen wir die älteste Datei von diesen, bereinigen sie und verwenden sie erneut

Wenn immer noch nichts gefunden wird – wir nehmen einfach die älteste Datei aus allen Kanälen (Material und Alarm), bereinigen sie und verwenden sie erneut

Außerdem haben wir eine Hintergrundaufgabe, die Materialdateien gemäß den maximalen Einstellungen bereinigt.

Die Startperiode wird von allen Kanälen (Material und Alarm) auf eine minimale maximale Einstellung eingestellt.

Notiz: Um sicherzustellen, dass die Notwendigkeit einer automatischen Löschung aufgrund von Speicherplatzmangel minimiert wird, ist es gut, die Festplattennutzung regelmäßig zu überwachen und die maximale Speicherzeit und den zugewiesenen Speicherplatz zu ändern.

Es ist ratsam, manuelle oder automatische Archivierungstools zu verwenden, um sicherzustellen, dass keine relevanten Daten bei Speicherplatzproblemen gelöscht werden.

Hinweis Sie können ein Watchdog-Ereignis festlegen, das Sie benachrichtigt, wenn der Speicherplatz knapp wird.

Archivierung

Sie können das System so einstellen, dass Video-, Audio- und Textdaten täglich oder wöchentlich automatisch archiviert werden.

Die Archivdateien können automatisch auf den Festplatten des Servers oder einem Netzlaufwerk erstellt werden.

Die Archivdateien können auf jedem Spotter-Client geöffnet werden.

Notiz: Archivdateien können sehr groß sein und daher den Speicherplatz schnell füllen. Archivdateien sollten regelmäßig von den Serverfestplatten oder Netzlaufwerken kopiert und entfernt werden, auf denen sie automatisch gespeichert werden.

So legen Sie einen automatischen Archivierungszeitplan fest:

Klicken Sie im Bereich  Datenspeicherung  auf die Geräte, die Sie in den automatischen Archivierungsprozess einbeziehen möchten.  
HinweisWählen Sie benachbarte Geräte oder Ordner aus, halten Sie die UMSCHALTTASTE gedrückt und klicken Sie dann auf das erste und letzte Gerät, das Sie auswählen möchten.

Um ein Gerät zu einer Auswahl hinzuzufügen oder aus einer Auswahl zu entfernen, halten Sie die STRG-Taste gedrückt und klicken Sie dann auf das Gerät, das Sie hinzufügen oder entfernen möchten.
Hinweis: Durch Auswählen einer Gerätegruppe (Ordner) wird auch deren Inhalt ausgewählt.

Markieren Sie das Kontrollkästchen Archiv.

Klicken Sie auf Archiveinstellungen ändern

Legen Sie das Archivpasswort fest, indem Sie auf Archivpasswort ändern klicken

Wählen Sie aus, ob das Archiv täglich oder wöchentlich erstellt werden soll, indem Sie Täglich oder Einmal pro Woche auswählen

Wenn Sie die tägliche Archivierung festlegen, verwenden Sie das Dropdown-Menü Archivierungszeit, um die Uhrzeit auszuwählen, zu der die Archivdateien erstellt werden.

Wenn Sie die wöchentliche Archivierung festlegen, verwenden Sie die Dropdown-Menüs Archivierungs-Wochentag und Archivierungszeit, um das Datum und die Uhrzeit auszuwählen, an denen die Archivdateien erstellt werden.

Verwenden Sie den Schieberegler Archivierter Zeitraum, um den Zeitraum festzulegen, der in den Archivdateien verwendet wird.

Wählen Sie aus, ob die Archive auf einem lokalen Laufwerk (auf dem Server) oder einem Netzlaufwerk erstellt werden sollen, indem Sie das VMS-Serververzeichnis  oder Netzwerkverzeichnis auswählen.

Klicken Sie auf die Schaltfläche  Verzeichnis  wechseln oder  Netzlaufwerk  wechseln, um das Verzeichnis zum Speichern der Archive festzulegen.

Klicken Sie auf OK, um den Archivierungszeitplan festzulegen

Verwenden Sie den Betriebssystem-Cache

DVMS 8. x und neuer haben die Möglichkeit, die Verwendung des Betriebssystem-Cache beim Zugriff auf die physische Festplatte zu aktivieren.

DVMS 9.4 und neuer haben die Möglichkeit, die maximale OS-Cache-Größe festzulegen.

Jede Software kann im Direktzugriffsmodus auf die Festplatte zugreifen, wenn das Betriebssystem kein Caching verwendet und den Betriebssystem-Cache verwendet.

Der letzte hilft, mit instabiler Last auf der Festplatte umzugehen und die am häufigsten verwendeten Teile der Daten zwischenzuspeichern.

Windows Server- und Windows-Desktopversionen haben unterschiedliche Prioritäten für Anwendungen – Windows-Dienste priorisieren Hintergrunddienste und Desktopversionen priorisieren UI-Anwendungen.

Außerdem verwendet Windows Server mehr Systemressourcen, um z. HDD-Zugriff und kann dafür bis zu 90 % des Arbeitsspeichers verwenden.

Um Situationen zu vermeiden, in denen der gesamte RAM vom Dateisystem-Cache belegt ist, verfügt DVMS 9.4 und neuer über eine Option, um die maximale Größe des Betriebssystem-Cache zu begrenzen.

Die Einstellung für den maximalen OS-Cache ist bis zum Neustart des PCs gültig, sodass sie bei jedem Start des Rekorders festgelegt werden.




Pagination
Previous page
ONVIF Profil M Benutzerdefinierte Alarmauslöser
Next page
Textkanäle