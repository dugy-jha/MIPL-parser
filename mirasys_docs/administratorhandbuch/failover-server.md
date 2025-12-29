# Failover-Server | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/failover-server

Failover-Server

Mirasys VMS unterstützt Failover-Videoserver als Mirasys VMS-Option.

Failover-Server sind VMS-Server im passiven Standby-Modus, bis das System erkennt, dass einer der aktiven Videoaufzeichnungs-VMS-Server ausgefallen ist; An dieser Stelle tritt ein Failover-Server an die Stelle des defekten Servers.

Der ausgefallene Server kann repariert und als neuer Failover-Server ersetzt werden, während der an seine Stelle getretene Failover-Server als aktiver Server weiterarbeiten kann.

Hinweis: Wenn ein Failover-Server einen aktiven Server ersetzt, sind alle nicht integrierten Spotter-Plugins (wie Grafana oder List Management Application) nicht im Switch enthalten und müssen nach einer Serverwiederherstellung manuell neu installiert werden. 

Aufzeichnungs- und Failover-Server sollten ein ähnliches Hardware-Setup aufweisen und die Zuweisungen von Laufwerksbuchstaben und Versionsnummern gemeinsam nutzen.

Analoge Kameras, die an die Capture-Karte eines Servers angeschlossen sind, werden nicht an den Failover-Server übertragen. Beim Wechsel werden nur zuvor zugewiesene IP-Kameras neu zugewiesen.

Failover-Funktionalität

Beim Hinzufügen eines neuen Servers zum System kann der Administrator auswählen, ob der hinzugefügte Server ein Standardserver oder ein Failover-Server ist.

Es kann eine beliebige Anzahl von Failover-Servern (0-n) geben.

Wenn der Server der Standardserver ist, kann der Administrator wählen, ob dieser bestimmte Server zur Failover-Überwachung hinzugefügt wird, d. h. bei einem Serverausfall (Hardware oder Software) wird dieser Server auf den verfügbaren Failover-Server migriert.

Es ist wichtig zu beachten, dass der Master-Server auf einer anderen Hardware installiert werden muss als auf derjenigen, die mit Aufzeichnungslizenzen oder Failover-Lizenzen betrieben wird.

Das minimale Hardware-Setup besteht aus drei Servern: einem Master-Server, einem VMS-Server für die Videoaufzeichnung und einem Standby-Failover-Server.

Die Failover-Migration wird unter den folgenden Bedingungen ausgelöst:

Der Master Server hat die Verbindung zu einem VMS Server verloren und das vom Administrator eingestellte Timeout ist erreicht

Ein VMS-Server hat dem Master-Server mitgeteilt, dass die Verbindung zu allen Materialplatten (Aufzeichnungsspeicher) auf dem Server fehlgeschlagen ist

Eine manuelle Datenwiederherstellung von Serverfestplatten kann versucht werden, wenn die Festplatten noch funktionsfähig sind

Der Watchdog-Dienst eines Servers hat den Master-Server darüber informiert, dass er den Aufzeichnungsdienst nicht initialisieren kann

Die Aufzeichnung erfolgt kontinuierlich, nachdem der Failover-Server übernommen wurde, um das System betriebsbereit zu halten.

Die einzige Ausnahme ist die Timeout-Zeit zwischen Trennen und Failover-Trigger. Der Administrator konfiguriert dies.

Nachdem ein Failover-Server die Aufzeichnungsrolle eines ausgefallenen Servers übernommen hat, wird automatisch eine Systemsicherung erstellt, um eine neue Baseline festzulegen.

Während des Failover-Wiederherstellungsprozesses und der folgenden Systemsicherung:

Benutzer können keine manuellen Sicherungsvorgänge durchführen

Alle folgenden defekten Server werden einer Failover-Warteschlange hinzugefügt

Die Failover-Warteschlange wird behandelt, nachdem die Failover-Wiederherstellung abgeschlossen wurde.

Pagination
Previous page
Verwenden von TruCast
Next page
Mindestanforderungen