# VMS-Server aktualisieren | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/vms-server-aktualisieren

VMS-Server aktualisieren

Über die Option Update VMS Servers ist es möglich, den lokalen Server und alle angeschlossenen VMS-Server aus der Ferne zu aktualisieren

Um Server zu aktualisieren, wählen Sie zuerst die Installationsdatei mit der Schaltfläche 

aus. 

Die Liste wird aktualisiert, um anzuzeigen, welche Server mit der ausgewählten Installationsdatei aktualisiert werden können.

Notiz: Bei einem Upgrade der Hauptversion, beispielsweise von VMS 6. x auf 7. x, ist es normalerweise erforderlich, zuerst die Serverlizenzen zu aktualisieren und erst danach die VMS-Software. Der Dialog „VMS-Server aktualisieren“ informiert den Benutzer wenn vor dem Software-Update ein Lizenz-Upgrade erforderlich ist.Wählen Sie als Nächstes aus, welche Server Sie aktualisieren möchten und ob Sie vor dem Update eine Sicherung durchführen möchten.

Durch Auswahl der Schaltfläche  starten

Sie das Update und ein Update-Fortschrittsdialog wird angezeigt:

Dieser Dialog kann jederzeit geschlossen werden, ohne die Server-Updates zu beeinflussen.

Notiz:

Der Fortschrittsdialog zeigt möglicherweise keine Statusinformationen für die Übertragung der Installationsdatei und den Aktualisierungsfortschritt an, wenn die Netzwerkverbindung langsam oder zeitweilig ist.

Dies ist kein Grund zur Beunruhigung; In den meisten Fällen wird das Update erfolgreich sein, es kann jedoch lange dauern (20 - 30 Minuten).

Es wird empfohlen, sich auf die Möglichkeit des Fernzugriffs auf solche Server vorzubereiten.

Wenn ein lokaler Server zum Aktualisieren ausgewählt wurde, würde der Systemmanager automatisch geschlossen, nachdem dieser Dialog angezeigt wurde.

In seltenen Fällen erfordern einige Server einen Systemneustart nach einem Remote-VMS-Softwareupdate, wenn die Verbindung zwischen dem Masterserver und dem VMS-Server nach dem Update nicht wiederhergestellt wird.

Es wird empfohlen, die Verbindung zu VMS-Servern nach dem Update zu überwachen.

Seit Version 7.4.3 unterstützt Mirasys VMS 64-Bit-Server. Das Upgrade von 32-Bit (x86) auf 64-Bit kann genau durch die Installation einer beliebigen DVMS-Version erreicht werden.

Nach dem Update zeigt die Systemsteuerung von Windows DVMS-x64 für 64-Bit-DVMS an.

Pagination
Previous page
Axis One-Click-Dispatcher-Einstellungen
Next page
Einstellungen für die Meldung von Vorfällen