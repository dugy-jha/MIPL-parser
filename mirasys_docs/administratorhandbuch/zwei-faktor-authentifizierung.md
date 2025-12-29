# Zwei-Faktor-Authentifizierung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/zwei-faktor-authentifizierung

Zwei-Faktor-Authentifizierung

Die Zwei-Faktor-Authentifizierung ist eine Funktion zur Verbesserung der Identifizierung des Benutzers, indem der Benutzername und das Kennwort sowie ein Code von einem externen physischen Gerät angefordert werden.

Dies macht es praktisch unmöglich, z.B. bestimmte Benutzergruppen (z. B. Systemadministratoren), um gemeinsame Zugangsdaten zu verwenden.

(Die Verwendung gemeinsamer Zugangsdaten würde es fast unmöglich machen, später z. B. bestimmte Benutzeraktionen aus den Audit-Logs zu überwachen.)

Aufstellen:

Der Admin aktiviert die 2-Faktor-Authentifizierung für die jeweilige Benutzergruppe.


Beim erstmaligen Einloggen des Benutzers in der Gruppe wird der Benutzer aufgefordert, den 2-Faktor-Authentifizierungs-Client (z. B. Authy, Google Authenticator, MS Authenticator (kostenlos erhältlich)) auf seinem mobilen Gerät zu verwenden bzw. zu installieren .

Das VMS und der Authentifizierungsclient werden dann mit der Software mit VMS synchronisiert.

Dies geschieht, indem der vom VMS generierte „geheime Schlüssel“ per QR-Code an die Authentifizierungssoftware übertragen oder direkt in die Software eingetippt wird.
Beispiel unten:


Danach generiert der Authentifizierungsclient automatisch neue Einmalpasswörter.

(Die Passwörter ändern sich regelmäßig und werden synchron gehalten, da die VMS-Uhren und die Authentifizierungs-App die gleiche Zeit haben.

Beachten Sie, dass dies keine direkte Datenkommunikationsverbindung zwischen der Software erfordert.)

Anmeldung:

Der Benutzer stellt VMS die Standard-Anmeldeinformationen zur Verfügung (Benutzername, Passwort)

Das VMS fordert für jede Anmeldung einen Authentifizierungscode von der Authentifizierungs-App an.

Der Benutzer gibt das Einmalpasswort aus der Authentifizierungs-App an. Der Benutzer gibt sie in den VMS-Client ein.

Instandhaltung:

Wenn der Benutzer seinen geheimen 2-Faktor-Schlüssel vergisst, kann der Administrator den Schlüssel dann über den Systemmanager zurücksetzen.

Nach dem Zurücksetzen des 2-Faktor-Geheimschlüssels muss der Benutzer den privaten Schlüssel bei der nächsten Anmeldung aktualisieren. (Siehe Schritt 2).







Pagination
Previous page
Erstellen einer kundenspezifischen Benutzergruppe
Next page
Domänenbasierte Benutzergruppen (Active Directory)