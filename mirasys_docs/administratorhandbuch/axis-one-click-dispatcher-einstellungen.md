# Axis One-Click-Dispatcher-Einstellungen | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/axis-one-click-dispatcher-einstellungen

Axis One-Click-Dispatcher-Einstellungen
Installationsschritte

Installieren Sie den O3C-Server wie im Handbuch „AXIS O3C Server Reference“ beschrieben. Windows and Linux Versions" (Technical Reference Document. AXIS One-Click Cloud Connection Server 2.30.0), part 2.2.2.

Wichtige Dinge:

Installieren Sie den O3C-Server wie im Handbuch „AXIS O3C Server Reference“ beschrieben. Windows and Linux Versions" (Technical Reference Document. AXIS One-Click Cloud Connection Server 2.30.0), part 2.2.2.

Wichtige Dinge:

setup provider certificate authority:

Directory in which the CA should be set up [default: ca]: (by default ca)

Passphrase for the CA key (DO NOT FORGET THIS!) [default: N/A]: pAs_sw! ord (some password)

Valid time, in days [default: 7300]: 100 (any number)

Issue a server certificate:

Path to the CA directory [default: ca]: (as above)

Passphrase for the CA key [default: N/A]: pAs_sw! ord (as above)

Subject Alternative Names (separated by comma) [default: N/A]: 172.17.102.56 (very important!!! Should be equal IP address of O3C server)

Valid time, in days [default: 398]: 100 (as above)

Result:

Concatenated server certificate and key saved to: ca/issued/stserver_EA363E5578E696E7.pem

Register O3C server as service in Windows SCM: there is needed the Power Shell tool for Windows! And for install call:

.\setup_service.ps1 add -c C:\o3c-server\o3c-server.conf

Configure o3c-server.conf

listen_client = 172.17.102.56:80

IP and port where the server will wait for the client (the camera) connections

stserverid = test_o3c_server

Any string

cert_file = C:\o3c-server\stserver_EA363E5578E696E7.pem

issued server certificate created after command: "pkitool issue-server-cert"

provider_ca = C:\o3c-server\stserver_ca.crt

CA certificate from ca directory created after the command: "pkitool setup-provider-ca"

provider_name =

can be left blank

credentials = root:root

for device access requests

O3C-server service

By default, the service is called Axis O3C Server in Services or O3C-server in command prompt.

Starten Sie den O3C-Serverdienst

Aktivieren Sie die Ein-Klick-Technologie auf der Kamera, wie in Teil 4.1 des Handbuchs beschrieben.

Firewalls deaktivieren oder O3C-Server zu den Ausnahmen hinzufügen

Registrieren Sie die Kamera wie in Teil 4.2 der Anleitung beschrieben.

http://172.17.102.56/admin/dispatch.cgi?action=register&user=adp_mirasys_100&pass=GQ41lSRbbEb4w3sorkN8&mac=B8A44F17AAFA&oak=8A22D6434817&server=172.17.102.56:80

where:user=adp_mirasys_100, pass=GQ41lSRbbEb4w3sorkN8 - Mirasys credentials (Provider name and password) from Axismac=B8A44F17AAFA, oak=8A22D6434817 - MAC address and OAK key from the camera

Um die MAC-Adresse zu finden, verwenden Sie im Browser die folgende Zeichenfolge: http://172.17.100.84/axis-cgi/admin/param.cgi?action=list&group=Network

server=172.17.102.56:80 - as "listen_client" in o3c-server.conf

Überprüfen Sie, ob die Kamera mit dem O3C-Server verbunden war: Rufen Sie im Browser den String auf: http://172.17.102.56:80/admin/status.cgi 172.17.102.56 - IP-Adresse des O3C-Servers

Und überprüfen Sie, ob ein Kommentar zum verbundenen Client wie folgt vorhanden ist: "id=4.b8a44f17aafa srcaddr=172.17.100.84:34148 accepted=1 v=2 rx=0 tx=0 connected=2022-01-10T12:45:40.875571Z

Gesamtzahl der Kunden: 1"

PS: Die Kamera versucht alle 20 Sekunden, sich mit dem Server zu verbinden

7. Überprüfen Sie, ob wir Optionen von der Kamera erhalten können: Dazu mussten die Proxy-Einstellungen für den Browser konfiguriert werden -

8. Öffnen Sie die Internetoptionen des Systems

9. Wählen Sie die Registerkarte Verbindungen -> Wählen Sie die Schaltfläche LAN-Einstellungen -> um "Proxy-Server für LAN verwenden (...)" zu aktivieren und geben Sie die Proxy-IP-Adresse und den Port ein. (im aktuellen Fall gibt es eine lokale IP-Adresse und Port 80)

10. Danach können wir die Kamerafunktionen im Browser abrufen:

http://b8a44f17aafa/axis-cgi/param.cgi?action=list&group=root.RemoteService where b8a44f17aafa - MAC address of the camera

Filter for wireshark for Axis P1375:

((ip.src == 172.17.100.84) && (ip.dst == 172.17.102.56)) || ((ip.src == 172.17.102.56) && (ip.dst == 172.17.100.84))

Add Axis One-Click Camera

Open System tab

Go to System Settings and open Axis one-click dispatcher settings

Enter all necessary details and click OK

4. Open the VMS Servers tab

5. Click Hardware

6. Click Add Axis One-Click Camera icon

7. Enter Axis One-Click Camera details and click OK

After clicking the OK, the camera query starts

When the camera query is finished, the device will be added to the hardware list

8. Click OK to finalize







Pagination
Previous page
Systemadressen
Next page
VMS-Server aktualisieren