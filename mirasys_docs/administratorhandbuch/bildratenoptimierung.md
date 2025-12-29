# Moxa-Einstellungen | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/bildratenoptimierung

Moxa-Einstellungen
Moxa PTZ-Bearbeitung aktivieren

In den Eigenschaften der System Manager-Rolle / VMS-Server-Einstellungen kann die Bearbeitung der Moxa-PTZ-Einstellungen für die Benutzergruppe ausgewählt werden. Wenn Moxa-PTZ-Steuerung aktivieren nicht ausgewählt ist, sind die Moxa-PTZ-Einstellungen unter Kameraeinstellungen sichtbar, können aber nicht geändert werden.

Moxa PTZ-Einstellungen

In den Kameraeinstellungen ist eine zusätzliche Registerkarte für Moxa-Einstellungen für Kameras verfügbar, für die Moxa-PTZ-Treibereinstellungen konfiguriert wurden oder wenn die Moxa-Bearbeitung für die Benutzergruppe aktiviert ist.

Gerät

Aktivieren Sie die Moxa PTZ-Einstellungen für die Kamera

Wenn die Kamera keine PTZ-Einstellungen hat, öffnen Sie die Registerkarten Gerät und PTZ-Steuerung mit den Standardwerten.

Wenn die Kamera über Moxa-PTZ-Einstellungen verfügt und Aktivieren nicht ausgewählt ist, werden beim Speichern der Einstellungen die Moxa-PTZ-Einstellungen von der Kamera entfernt

Adresse geben Sie die IP- oder DNS-Adresse des MOXA-Geräts ein.

Portindex ist der Index des seriellen Ports (1 - 255) im MOXA-Gerät, an dem die PTZ-Kamera angeschlossen ist.

Timeout/ms ist der Timeout in Millisekunden für die Kommunikation mit dem MOXA-Gerät (5000 ms als Standard)

Protokoll ist das Kommunikationsprotokoll mit der PTZ-Kamera aus der folgenden Aufzählung:

{ "PelcoD", "BoschOSRD" }

Standardwert ist "PelcoD".

PTZ-Steuerung

Kameraindex - Adresse der analogen PTZ-Kamera, die in der Kamera eingestellt ist (normalerweise sind es Hardware-Jumper) (0 - 255)

Baudrate - Baudrate der seriellen Schnittstelle in Bits pro Sekunde. MOXA unterstützt die folgenden Baudraten:

{ 50, 75, 110, 134, 150, 300, 600, 1200, 2400, 4800, 6400, 7200, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600 }.

Der Standardwert ist 38400 bps.

Datenbits - (Byte) - Wert aus dem folgenden Satz:

{5, 6, 7, 8 }

Der Standardwert ist 8.

Stoppbit - (Byte) - Wert aus dem folgenden Satz:

{ 1, 2 }

Standardwert ist 1.

Parität - Wert aus der folgenden Aufzählung:

{ "None" = 0, "Even" = 1, "Odd" = 2, "Mark" = 3, "Space" = 4 }

Standardwert ist "Keine".

Flusskontrolle - Wert aus der folgenden Aufzählung:

{ "Keine" = 0, "RTS / CTS" = 1, "XON / XOFF" = 2, "Beide" = 3 }

Standardwert ist "Keine".




Pagination
Previous page
Fortschrittlich
Next page
Bewegungserkennung