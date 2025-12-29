# Audit-Protokoll | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/audit-protokoll

Audit-Protokoll

Das Protokoll des Audit-Trails kann verwendet werden, um Informationen über die Benutzeraktivitäten des VMS-Systems zu suchen. Der Zugriff darauf erfolgt im System-Manager auf der Registerkarte "System" unter "Überwachung".

Audit-Trail-Protokoll

Im Audit Trail Log-Dialog kann der Administrator mit verschiedenen Suchparametern nach Audit Trail-Ereignissen suchen.




Die Ergebnisse werden in einer nach Zeit geordneten Ergebnisliste aufgeführt. Gefundene Audit-Trail-Ereignisse können nach anderen Audit-Trail-Ereignis-Informationen sortiert werden, indem Sie auf die Listenüberschriften klicken.

Suchparameter

Die folgenden Suchparameter können für die Suche nach Audit-Trail-Ereignissen verwendet werden.

Datum - Wählen Sie das Datum, an dem die Suche beginnen soll. Mit den Schaltflächen auf der linken und rechten Seite können Sie den Tag des Datums vergrößern oder verkleinern.

Zeit - Wählen Sie die Uhrzeit des Datums, zu der die Suche beginnen soll. Mit den Schaltflächen links und rechts können Sie die Stunde der Uhrzeit erhöhen oder verringern. Die Schaltflächen nach oben und unten erhöhen bzw. verringern die Minuten der Uhrzeit um zehn.

Benutzer - Benutzer, dessen Audit Trail-Ereignisse durchsucht werden sollen. Alle = Suche ohne Filterung der Benutzer.

Anwendung - Zu durchsuchende Anwendung. Alle = Suche ohne Filterung der Anwendungen.

Max result count - Maximale Anzahl, wie viele Audit-Trail-Ereignisse ab der Startzeit durchsucht werden sollen.

VMS Server -Die Dropdown-Liste VMS-Server zeigt alle möglichen Werte für VMS-Server an, die ausgewählt werden können.

Endzeit-Kontrollkästchen - Wenn dieses Kontrollkästchen aktiviert ist, können Sie das Enddatum und die Endzeit der Suche auf ähnliche Weise wie die Startzeit auswählen. Wenn es nicht markiert ist, wird die Endzeit nicht als Suchfilter verwendet (= Suche bis jetzt).

Audit-protokoll Veranstaltungen - Zu durchsuchender Vorgang: Es kann keiner, einer, viele oder alle Vorgänge ausgewählt werden. Wenn keine oder alle ausgewählt sind, wird ohne Filterung der Vorgänge gesucht. Die folgenden Schaltflächen können mit Vorgängen verwendet werden:

Ansicht der Vorgangsliste vergrößern

Alle auswählen

Alle abwählen

Ergebnisliste

Gefundene Audit-Trail-Ereignisse werden in der Suchergebnisliste aufgeführt. Die Liste enthält Informationen zu jedem Audit-Trail-Ereignis.

Zeit - Zeitpunkt der Benutzeraktion.

Benutzer - Benutzername, der die Benutzeraktion durchgeführt hat.

Anwendung - Anwendung, in der die Benutzeraktion durchgeführt wurde.

Ereignis - Name der Benutzeraktion. Wenn sich das Ereignis auf eine Kameraprüfung bezieht und der Bediener vor dem Zugriff auf das Wiedergabematerial einen Kommentar hinzufügen muss, enthält das Ereignis den Kommentar.

Ereignisstatus - ob der Vorgang erfolgreich war oder nicht.

Objekt - Das Objekt hängt von der Operation selbst ab. Wenn Sie zum Beispiel eine Kamera öffnen, wird der Name dieser Kamera angezeigt.

VMS Server - Zeigt an, auf welchem VMS-Server der Vorgang stattgefunden hat.

Audit-Protokoll-Export

Aufgelistete Audit-Trail-Ereignisse können durch Klicken auf die Schaltfläche unter der Ergebnisliste der Audit-Trail-Ereignisse in eine PDF-Datei als Audit-Trail-Bericht exportiert werden. Der Speicherort und der Name der exportierten Datei sowie der Kommentar für den Bericht können im Dialog zum Speichern des Berichts angegeben werden. Der Titel des Audit-Protokollberichts wird aus der Exportzeit und dem Benutzer, der den Bericht exportiert hat, erstellt. Der Bericht enthält alle Audit-Protokolleinträge mit denselben Informationen, die auch in der Ergebnisliste der Audit-Trail-Ereignisse aufgeführt sind.




Pagination
Previous page
Serverdiagnose
Next page
Lizenzen