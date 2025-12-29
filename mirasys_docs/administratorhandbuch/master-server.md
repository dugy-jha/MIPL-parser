# Master-Server | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/master-server

Master-Server

In einem vernetzten System muss einer der Server als Masterserver eingerichtet werden.
Ein Masterserver ist der zentrale Server eines Überwachungssystems.
Alle anderen VMS-Server stellen eine Verbindung zu ihm her, und alle Clientanwendungen kommunizieren über den Masterserver.
Wenn der System nur einen Server enthält, dann ist dieser Server der Master Server.
Wenn es mehr als einen Server gibt, kann der Master Server frei eingestellt werden.
Es wird empfohlen, dass der Master Server nur für diesen Zweck in einem umfangreicheren System ein dedizierter Server ist .

HINWEIS: Auf Masterservern muss SQL Server Express 2014 oder ein anderer Microsoft SQL Server 2014 installiert sein.

Der Master-Server macht diese Dinge:

Es überprüft die Identität aller Programme und Benutzer, die versuchen, sich am System anzumelden (Authentifizierung).

Es speichert alle Systemkonfigurationsdaten.

Es speichert alle Benutzerdaten.

Es überwacht das System.

Es synchronisiert die Uhren auf allen Servern.

Es generiert Berichte.

Es speichert Watchdog-Ereignisse.

Es speichert Alarme.

Es speichert Audit-Trails.

Pagination
Previous page
VMS-Server
Next page
Client-Programme