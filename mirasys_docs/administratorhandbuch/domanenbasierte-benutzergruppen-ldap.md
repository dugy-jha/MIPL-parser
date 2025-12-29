# Domänenbasierte Benutzergruppen (Active Directory) | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/domanenbasierte-benutzergruppen-ldap

Domänenbasierte Benutzergruppen (Active Directory)

Das System unterstützt die Integration von Benutzerrechten auf Domänenebene (Microsoft Active Directory, LDAP), wodurch Benutzer aus Domänengruppen synchronisiert werden können.

Domänenbasierte Benutzer können sich mit ihren Domänenbenutzernamen und Passwörtern beim VMS-System anmelden.

Standardmäßig werden Benutzergruppenrechte alle 30 Minuten mit ihrer übergeordneten Domäne synchronisiert.

Bitte wenden Sie sich an Ihren Systemlieferanten, wenn Sie das Standardintervall ändern müssen.

Diese Funktion erfordert ein Lizenzupdate.

Hinzufügen einer neuen domänenbasierten Benutzergruppe zum System

Klicken Sie in der oberen linken Ecke der Registerkarte Benutzer auf Benutzergruppen aus einer externen Quelle importieren.
Der Master-Server muss mit einer Domäne verbunden sein, damit die Schaltfläche angezeigt wird.
Wenn der Server nicht mit einer Domäne verbunden ist, ist die Schaltfläche nicht sichtbar.

Geben Sie den Namen der Domäne in das Dialogfeld Domänenname ein.

Wählen Sie aus, ob Sie alle Benutzergruppen abrufen oder nach bestimmten Gruppen suchen möchten.
Wenn Sie nach bestimmten Gruppen nach Namen suchen möchten, können Sie ein Suchkriterium hinzufügen, das darauf basiert, dass die Textzeichenfolge dem Gruppennamen entspricht, im Gruppennamen enthalten ist oder der Gruppenname in der Textzeichenfolge beginnt oder endet.

Wählen Sie aus, ob offene Benutzergruppen übersprungen oder eingeschlossen werden sollen.

Wählen Sie aus, ob vorherige Suchergebnisse gelöscht oder beibehalten werden sollen.

Aktivieren Sie Sichere (SSL)-Verbindung verwenden. Wenn benötigt

Klicken Sie auf Ok.

Wählen Sie im Fenster Benutzergruppen importieren die Benutzergruppen aus, die Sie aus der Domäne importieren möchten.

Klicken Sie auf Ok, um die ausgewählten Gruppen zu importieren.

Bearbeiten Sie die importierten Benutzergruppen, um ihre Benutzerrollen wie unten beschrieben festzulegen.




Pagination
Previous page
Zwei-Faktor-Authentifizierung
Next page
Aktive Stunden - Zeitplan für den Zugang von Benutzergruppen