# Einstellungen für die List Management | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/einstellungen-fur-die-list-management

Einstellungen für die List Management

Die Listenverwaltung ermöglicht es, Identitäten und Listen zu definieren, so dass die erlaubten oder nicht erlaubten Identitäten festgelegt werden können.

Die Einstellungen definieren und verwalten die Einstellungen für die Identitäts- und Listenverwaltung. Mit den Einstellungen können Sie:

Hinzufügen, Bearbeiten und Löschen von Identitäten mit Nummernschildern und Gesichtsbildern

Hinzufügen, Bearbeiten und Löschen von Listen und Verwalten von Listeninhalten

Import und Export von Listen und Identitäten

Konfigurieren von Speichergrenzen für LPR- und FR-Ereignisdatenbanken

Aktivieren und Definieren der Integration und ihrer Einstellungen

Die Systemmanager-Anwendung bietet mehrere Dialoge für den Zugriff und die Änderung von Daten und Einstellungen des Listenverwaltungsdienstes. Die Dialoge finden Sie im Abschnitt "Systemeinstellungen".

Die Integration erfordert eine LPR- und FR-Integrationslizenz.

Einstellungen für die Listenverwaltung

So öffnen Sie das Dialogfeld Einstellungen für die Listenverwaltung:

Gehen Sie auf die Registerkarte System

Doppelklicken Sie unter Systemeinstellungen auf den Baumknoten Listenverwaltungseinstellungen, wie in der Abbildung unten dargestellt:

Wenn Sie auf Listenverwaltungseinstellungen doppelklicken, wird der Dialog geladen, die Einstellungen werden vom Listenverwaltungsdienst angefordert und bei Erfolg angezeigt. Wenn das Laden fehlschlägt, wird dem Benutzer eine Fehlermeldung angezeigt, und der Dialog wird geschlossen.

Dialogfeld "Listenverwaltungseinstellungen

In dem Dialog finden Sie die folgenden Registerkarten:

Identitäten - Liste der Identitäten und deren Einstellungen

Listen - Identitätslisten und deren Einstellungen

Import/Export - Import/Export-Funktionalität zum Wiederherstellen/Speichern von Listenverwaltungsdaten im CSV-Textformat

Datenbankeinstellungen - Parameter, die sich auf die Datenbank des Listenverwaltungsdienstes beziehen

Integrationseinstellungen - Aktivierung der Integration und Integrationseinstellungen

Alle Änderungen, die Sie in diesen Dialogregistern vornehmen, können durch Klicken auf die Schaltfläche OK gespeichert werden.

Wenn Sie die Änderungen nicht behalten wollen, können Sie den Dialog mit der Schaltfläche Schließen oder Abbrechen schließen.

Nachfolgend finden Sie eine detaillierte Beschreibung der einzelnen Registerkarten.

Registerkarte "Identitäten

Auf der Registerkarte "Identitäten" können Sie Operationen mit Identitäten durchführen:

Registerkarte "Identitäten

Die Auswahl von Identitäten erfolgt mit der linken Maustaste. Wenn Sie mehrere Identitäten auswählen müssen (mehrere Zeilen in der Liste), können Sie die linke Maustaste + Strg/Umschalttaste verwenden. Bei Mehrfachauswahl können Sie die ausgewählten Identitäten in den Zustand "aktiv" oder "nicht aktiv" versetzen, indem Sie auf die Kontrollkästchen in der Spalte "Aktiv" klicken.

Oberhalb der Liste der Identitäten befindet sich das Feld "Suchen": Wenn Sie hier etwas eingeben, wird die Liste der Identitäten automatisch gefiltert, wenn der Text in Identitätsnamen oder -kennzeichen enthalten ist.

Mit den Schaltflächen Hinzufügen und Entfernen unterhalb der Identitätsliste können Sie ausgewählte Identitäten hinzufügen oder entfernen.

Im Bereich Identitätsdetails können Sie detaillierte Informationen zur Identität anzeigen, aber alle diese Felder sind schreibgeschützt. Um die ausgewählte Identität zu ändern, können Sie auf die Schaltfläche Ändern klicken oder mit der Maustaste darauf doppelklicken.

Wenn Sie eine Identität hinzufügen oder ändern, wird das folgende Dialogfeld angezeigt:

Dialog zum Hinzufügen/Ändern der Identität

Sie können alle Felddaten ändern oder Bilder von Gesichtern oder Fahrzeugen (Nummernschildern) hinzufügen/entfernen.

Um ein Gesichtsbild hinzuzufügen, klicken Sie auf die Schaltfläche "Neues Gesichtsbild hinzufügen" und der folgende Dialog wird geöffnet:

Dialog zum Hinzufügen/Ändern der Identität

Für eine Identität können mehrere Gesichtsbilder definiert werden. Alle Gesichtsbilder werden beim Identitätsabgleich verwendet, so dass die Verwendung mehrerer Gesichtsbilder für eine Identität die Zuverlässigkeit der Gesichtserkennung erhöhen kann.

Hier können Sie einen Gesichtsbildnamen eingeben und eine Gesichtsbilddatei auswählen. Nach der Auswahl der Datei wird das Bild geladen, und die Merkmalsvektordaten des Bildes werden berechnet.

Um den Vektor der Gesichtsmerkmale zu berechnen, muss mindestens ein Gesichtserkennungsdienst gestartet und im VMS registriert sein

Um ein Gesichtsbild zu entfernen, müssen Sie es im Kombinationsfeld auswählen und auf die Schaltfläche Ausgewähltes Gesichtsbild entfernen klicken.

Gesichtsbild als Standard festlegen

Ein Gesichtsbild ist das Standardbild, das in allen Plugins und Identitätslisten als Miniaturbild verwendet wird. Um das Gesichtsbild als Standard festzulegen, müssen Sie das Gesichtsbild im Kombinationsfeld auswählen und auf die Schaltfläche Ausgewähltes Gesichtsbild als Standard festlegen klicken:

Ausgewähltes Gesichtsbild als Standard festlegen
Fahrzeuge hinzufügen oder entfernen

Sie können Fahrzeuge hinzufügen oder entfernen. Um ein Fahrzeug hinzuzufügen, klicken Sie auf die Schaltfläche Neues Fahrzeug hinzufügen, woraufhin sich der folgende Dialog öffnet:

Dialogfeld "Fahrzeug hinzufügen

Im Dialogfeld Fahrzeug hinzufügen können Sie das Kennzeichen, die Vorwahl, den Hersteller, das Modell und die Fahrzeugfarbe eingeben. Um ein Fahrzeug zu entfernen, müssen Sie es im Kombinationsfeld auswählen und auf die Schaltfläche Ausgewähltes Fahrzeug entfernen klicken.

Registerkarte Listen

Auf der Registerkarte Listen können Sie Operationen mit Identitätslisten durchführen:

Registerkarte "Listen

Die Listenauswahl erfolgt mit der linken Maustaste. Wenn Sie mehrere Listen (mehrere Zeilen) auswählen müssen, können Sie die linke Maustaste + Strg/Umschalttaste verwenden. Bei Mehrfachauswahl können Sie die ausgewählten Listen durch Anklicken der Kontrollkästchen in der Spalte Aktiv in den Zustand aktiv oder nicht aktiv versetzen.

Mit den Schaltflächen Hinzufügen und Entfernen unter den Listen können Sie ausgewählte Listen hinzufügen oder entfernen.

Um die ausgewählte Identitätsliste zu ändern, können Sie auf die Schaltfläche Ändern klicken oder mit der Maustaste darauf doppelklicken.

Wenn Sie die Identitätsliste hinzufügen oder ändern, wird das folgende Dialogfeld angezeigt:

Dialogfeld zum Hinzufügen/Ändern von Listeneinstellungen

Sie können Identitäten in die Liste verschieben oder sie aus der Liste entfernen, den Namen der Liste und die Farbe festlegen.

Registerkarte "Import/Export

Auf der Registerkarte "Import/Export" können Sie Listenverwaltungsdaten aus einer CSV-Datei importieren oder Listenverwaltungsdaten in eine CSV-Datei exportieren:

Registerkarte Import/Export
Parameter für den Import

Die folgenden Parameter müssen für den Importvorgang festgelegt werden:

Dateipfad - Pfad zu der CSV-Datei, die die Listenverwaltungsdaten enthält

Importtyp - "Nur Identitäten" oder "Identitäten und Listen"

CSV-Begrenzer - "Komma" oder "Semikolon"

Elemente mit der gleichen Kennung - "Überspringen", "Überschreiben" oder "Neue" Kennung für sie erstellen

Wenn die richtigen Parameter ausgewählt sind, wird die Schaltfläche "Daten aus Datei importieren" aktiviert, und der Benutzer kann den Importvorgang starten. Während des Prozesses sehen die Benutzer den Fortschritt und das Ergebnis des Imports.

Parameter für den Export

Die folgenden Parameter müssen für den Exportvorgang festgelegt werden:

Ordnerpfad - Pfad zu dem Ordner, in den die Listenverwaltungsdaten exportiert werden und in dem die CSV-Datei erstellt wird

Exporttyp - "Nur Identitäten" oder "Identitäten und Listen"

CSV-Begrenzungszeichen - "Komma" oder "Semikolon"

Wenn die richtigen Parameter ausgewählt sind, wird die Schaltfläche "Daten in Datei exportieren" aktiviert, und der Benutzer kann den Exportvorgang starten. Während des Prozesses sehen die Benutzer den Fortschritt und das Ergebnis des Exports.

Registerkarte "Datenbankeinstellungen

Auf der Registerkarte "Datenbankeinstellungen" können Sie die Datenbankeinstellungen für den Listenverwaltungsdienst festlegen:

Registerkarte Datenbankeinstellungen
Registerkarte Integrationseinstellungen

Auf der Registerkarte Integrationseinstellungen können Sie Integrationseinstellungen für den Listenverwaltungsdienst vornehmen:

Registerkarte "Integrationseinstellungen

Hier können Sie Einstellungen für die Ereigniswarteschlange festlegen und die Integrationseinstellungen aktivieren/deaktivieren. Die Registerkarte ist nicht sichtbar, wenn die Lizenz die Listenmanagement-Integration nicht aktiviert.

Benachrichtigung über die Aktualisierung von Listenverwaltungsdaten

Wenn die Listenverwaltungsdaten in einer anderen Anwendung geändert wurden, empfängt der System Manager ein Ereignis mit aktualisierten Informationen und zeigt die folgende Meldung an:

Warnung vor Datenaktualisierung

Wenn Sie auf die Schaltfläche OK des Meldungsdialogs klicken, werden alle Einstellungsdialoge geschlossen, um die Daten aus dem Listenverwaltungsdienst neu zu laden. Alle Änderungen, die nicht gespeichert wurden, gehen dabei verloren.

Pagination
Previous page
Storage Locker Einstellungen
Next page
Sicherung