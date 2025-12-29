# Konfiguration der Bewegungserkennung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/bearbeiten-einer-maske

Konfiguration der Bewegungserkennung

Um auf die Konfiguration der Bewegungserkennung im System Manager zuzugreifen, gehen Sie zu VMS Servereinstellungen > Kameraeinstellungen > Bewegungserkennung.

Wählen Sie die Kamera im Dropdown-Menü Kamera aus.

Wählen Sie unter Maskeneinstellungen die Maske aus, die Sie konfigurieren möchten.
Sie können den Namen der Maske ändern.
Klicken Sie auf Maskenname ändern und geben Sie einen neuen Namen für die Maske ein.
Bitte beachten Sie, dass die Standardmaskenkonfiguration nicht geändert werden kann.

Zeichnen Sie die Maske über das Bild, um festzulegen, für welchen Bereich der Bewegungserkennungs-Feed berechnet werden soll. Verwenden Sie die Zeichenwerkzeuge auf der rechten Seite der Ansicht und malen Sie mit den Zeichenwerkzeugen die Bereiche rot an, in denen das System Bewegungen erkennen soll, und entfernen Sie das Rot aus den Bereichen, in denen Bewegungen ignoriert werden sollen.

Zeichenutensilien

Werkzeug

	

Name

	

Beschreibung



	

Bleistift

	

Verwenden Sie zum Einstellen des Bewegungserkennungsbereichs. Wählen Sie die Stiftgröße aus, indem Sie auf eine der Schaltflächen für die Werkzeuggröße klicken (groß, mittel, klein).



	

Radiergummi

	

Verwenden Sie diese Option, um ausgewählte Bereiche zu löschen, die Sie nicht einschließen möchten. Wählen Sie die Radiergummigröße aus, indem Sie auf eine der Schaltflächen für die Werkzeuggröße klicken (groß, mittel, klein).



	

Lasso

	

Wählen Sie mit geraden Linien Bereiche aus. Wenn das Stiftwerkzeug ausgewählt ist, fügt die Verwendung dieses Werkzeugs ausgewählten Bereichen hinzu. Wenn das Radiergummi-Werkzeug ausgewählt ist, wird dieses Werkzeug aus der Auswahl entfernt. Klicken Sie auf das Bild, bei dem Sie die Auswahl beginnen möchten. Klicken Sie erneut auf die Stelle, an der Sie die Linie verankern möchten, und ändern Sie die Richtung. Um die Auswahl abzuschließen, klicken Sie auf den Startpunkt. Der ausgewählte Bereich wird rot gestrichen oder die rote Farbe wird entfernt.



	

Füllen/Löschen

	

Wenn das Stiftwerkzeug ausgewählt ist, wird durch Klicken auf diese Schaltfläche der gesamte Bildbereich ausgewählt. Wenn das Radiergummi-Werkzeug ausgewählt ist, wird durch Klicken auf diese Schaltfläche alle Auswahlen entfernt.



	

Umkehren

	

Kehrt ausgewählte und nicht ausgewählte Bereiche um. Manchmal ist es einfacher, den Bereich auszuwählen, den Sie nicht maskieren möchten, und dann die Auswahl umzukehren.



	

Werkzeuggröße

	

Klicken Sie auf eine der Schaltflächen, um die Größe des Bleistifts oder Radierers auszuwählen (groß, mittel, klein).

Stellen Sie die Erkennungsempfindlichkeit mit dem Schieberegler ein.

Stellen Sie mit dem Schieberegler die Mindestmenge an Bewegung ein.

Wählen Sie die Bewegungserkennungsmethode. Sie können zwischen vergleichender, adaptiver oder hermeneutischer Bewegungserkennung wählen. Eine ausführlichere Beschreibung dieser Optionen finden Sie auf der vorherigen Seite.

Wählen Sie entweder den Standardwert für die Bewegungserkennungs-Bildrate oder verwenden Sie den Schieberegler.

Wählen Sie die Bewegungserkennungsplattform, entweder nur den VMS Server oder den VMS Server und die Kamerahardware.

Sobald die Konfiguration abgeschlossen ist, müssen die Bewegungserkennungsmasken mit Hilfe des Zeitplaners in Betrieb genommen werden. Um auf die Konfiguration der Bewegungserkennung im System Manager zuzugreifen, gehen Sie zu VMS Server Settings > Camera Settings > Scheduler. Eine Anleitung zur Verwendung des Schedulers finden Sie im nächsten Dokument.

Schalter

Um die Bewegungserkennung zu testen, können Sie den Zähler verwenden. Wenn Sie den Zähler aktivieren, wird das Video von der Kamera gestreamt und die Bewegungserkennung wird berechnet. Das Ergebnis der Bewegungserkennung wird oben auf dem Bild angezeigt. Der Zählerwert erhöht sich jedes Mal, wenn eine Bewegung erkannt wird, je nach Ihrer Konfiguration.

So verwenden Sie den Zähler:

Ermöglichen Schalter

Überprüfen Sie die Bewegungswerte

Das Kamerabild zeigt an, welcher Bereich des Kamerabildes eine Bewegungserkennungsaufzeichnung verursacht

Vor- und Nachaufzeichnungszeit

Wenn Sie Material vor und nach der Bewegung aufzeichnen möchten, verwenden Sie die Vor- und Nachaufzeichnung von Bewegung.

Jede Maske kann separat konfiguriert werden.

Die Werte reichen von 0s bis 60 Minuten.

Mit der Schaltfläche Vor- und Nachaufzeichnungszeit für alle Kameras kopieren können Sie die ausgewählten Werte auf alle Kameras übertragen.

Pagination
Previous page
Bewegungserkennung
Next page
Planer