# Einstellungen für Speicherschließfach | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/einstellungen-fur-speicherschliefach

Einstellungen für Speicherschließfach

Storage Locker Settings enthält die folgenden Werte:

Dateipfad:

Definiert den Speicherort von Storage Locker.
Als Standardspeicherort befindet sich Storage Locker auf dem Master-Server.

Dateipfad ändern

Bitte beachten Sie, dass die alten Locker-Daten des Speichers nicht an den neuen Speicherort kopiert werden

Klicken Sie auf Dateipfad für die Datenspeicherung festlegen

2. Wählen Sie einen neuen Standort und klicken Sie auf OK

Dateipfad importieren:

Wenn jemand Exporte hat, die zum Speicherschließfach hinzugefügt werden müssen, sollten diese Exporte in einem Ordner abgelegt werden, der in den Speicherschließfacheinstellungen als "Dateipfad importieren" definiert ist. Wie benutzt man:

Alle Importdaten müssen sich in einem eigenen Ordner befinden, Dateien, die direkt im Importordner abgelegt werden, werden ignoriert

Jeder Importordner kann mehrere Unterordner haben

Bilder und Clips können in einem Ordner abgelegt werden, Storage Locker importiert sie einzeln

SEF-Archive sollten sich in einem eigenen Ordner befinden und nicht mit anderen Daten (wie Bildern, Clips usw.)

Importdaten sollten alle auf einmal kopiert werden, wenn etwas hinzugefügt werden soll - es sollte mit eigenem Ordner kopiert werden, Dateien, die zu bestehenden Ordnern hinzugefügt werden, werden nicht unterstützt (diese Dateien werden nicht verarbeitet)

Die Aufbewahrungszeit für Daten

Die Aufbewahrungszeit für Datensätze definiert, wie lange Storage Locker Daten aufbewahrt, die in keinem Vorfallbericht verwendet werden

Die Aufbewahrungszeit für Daten, die in den Vorfallberichten verwendet werden

Die Aufbewahrungszeit für Daten, die in Vorfallberichten verwendet werden, definiert, wie lange Storage Locker Daten aufbewahrt, die in jedem Vorfallbericht verwendet werden

Schritte zum Zuordnen eines Netzlaufwerks, das für Storage Locker-Daten verwendet werden kann


Erstellen Sie eine Stapeldatei (siehe Details zur Stapeldatei) und speichern Sie sie am gewünschten Ort. In meinem Fall habe ich diese Batchdatei unter C:\temp mit dem Namen „SysinternalSuite.bat“ gespeichert.

Laufcd C:\temp\SysinternalsSuite psexec -i -s cmd.exe /c net use S: "\\172.17.100.10\storageforvms" /user:vms sharepassword /persistent:Yes

offenTask Scheduler

klickenCreate Task

3. Name eingeben

4. Ermöglichen Run whether the user is logged on or not

5. Ermöglichen Run with highest privilege

6. Offen Triggers

7. Klicken New

8. wählen At startup from the Begin the task dropdown list

9. KlickenOK

10. oppen Actions

11. Klicken New

12. Durchsuchen Sie den Speicherort des Skripts und wählen Sie Skript aus

13. Klicken OK

14. oppenConditions

15. Deaktivieren tart the task only if the computer is on AC power and Wake the computer to run this task

16. Klicken OK

Beachten Sie, dass in Mein PC das neu erstellte zugeordnete Laufwerk für ALLE Benutzer dieses Systems angezeigt wird, aber sie sehen es als „Getrenntes Netzwerklaufwerk (X:)“ angezeigt.( Wenn das Laufwerk passwortgeschützt ist, wird der Benutzer aufgefordert, das Passwort einzugeben, nachdem er auf die Schaltfläche OK geklickt hat.)

Öffnen Sie nun den System-Manager, navigieren Sie zu den Storage Locker-Einstellungen und beobachten Sie, dass das zugeordnete Laufwerk in der Liste angezeigt wird.

Laufwerk aus der Liste auswählen

Klicken OK




Pagination
Previous page
Reihenfolge der Werte ändern
Next page
Storage Locker Einstellungen