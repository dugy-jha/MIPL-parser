# Allgemein | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/allgemein

Allgemein

VMS-Servername

Beschreibung

Passwort

Protokoll

Multicast-Adresse

VMS-Server-Failover-Einstellungen

Multicast-Adresse

Wenn ein einzelner Workstation-Stream mehrmals geöffnet wird, werden der Server – und das Netzwerk – unnötig belastet, da jeder Stream als separate Einheit behandelt wird.
Multi-Casting ermöglicht das gleichzeitige Öffnen und Senden eines einzelnen Streams an mehrere Workstations.
Bei Verwendung von Multi -casting wird der Stream für jeden Videokanal nur einmal an das LAN gesendet.
Alle Anwendungen im LAN können den einzelnen Stream empfangen, sodass die Nutzung der Netzwerkbandbreite geringer ist als beim separaten Senden eines Streams für jede Anwendung.
Die Funktion muss konfiguriert werden im System Manager und über die Netzwerkeinstellungen.
Bitte wenden Sie sich an Ihren Netzwerkinfrastrukturdienst, um Informationen zum Aktivieren der Multicasting-Unterstützung auf Netzwerkebene zu erhalten.

So konfigurieren Sie Multicasting in System Manager:

Ändern Sie in den allgemeinen Einstellungen des Servers das Protokoll von TCP (Standard) auf RTP Multicast.

Bearbeiten Sie die Multicast-Adresse.

Wiederholen Sie die Schritte 1-2 für alle erforderlichen Server im System. Notiz: Jede Multicast-Adresse muss separat sein.

VMS-Server-Failover-Einstellungen

Beim Hinzufügen eines neuen Servers zum System kann dieser als Failover-Server definiert werden.
Ein Failover-Server ist ein Backup-Server, der alle Serveraufgaben übernehmen soll, von denen festgestellt wurde, dass sie unter Failover-Schutz stehen.


Failover-Server müssen das gleiche Dateisystem (dasselbe Laufwerk) haben Buchstaben) als VMS-Server unter Failover-Schutz, und sie können nur für Backup-Zwecke von IP-Kameras verwendet werden unzugänglich sind, wurden sie in den Ordner  „Ausgefallene VMS-Server“ verschoben.


Jeder verfügbare Failover-Server übernimmt die Verantwortung für den ausgefallenen Server.
Failover-Einstellungen können über die allgemeinen Einstellungen des ausgewählten Servers gesteuert werden.
Der Failover-Übergang wird durchgeführt, wenn alle Materialfestplatten defekt sind oder der Server länger als eine definierte Zeit nicht erreichbar ist.

Wenn beispielsweise unter Failover-Schutz länger als 2 Stunden nicht zugegriffen werden kann, wird die Failover-Umschaltung ausgeführt.

Failover verzögern, um Datenverlust zu vermeiden

Der Failover-Prozess wurde aktualisiert, um Datenverluste während des Failover-Prozesses, z. B. während der Aktualisierung des Rekorders zu verhindern.

Beim Kopieren von Material aus dem Failover-Recorder prüft der wiederhergestellte Recorder zuerst seine aufgezeichneten Daten und kopiert dann nur fehlendes Material (einschließlich Video, Audio, Textdaten, Metadaten und ANPR-Daten).

Diese Funktion kann im Dialogfeld System-Manager > VMS-Server allgemein (Kontrollkästchen Auf den Rekorder warten, um Einstellungen zu übernehmen) aktiviert werden.

Delay Failover kann nur für Rekorder ab V9.7 aktiviert werden, da Rekorder vor V9.7 keine selektive Materialkopie unterstützen und sich die Daten überschneiden.




Pagination
Previous page
VMS-Servers
Next page
Port-Weiterleitung