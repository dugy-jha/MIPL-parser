# Installieren externer Treiberpakete | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/installieren-externer-treiberpakete

Installieren externer Treiberpakete

Um IP-Kameras, digitale E/A-Geräte oder Textdaten im VMS-System zu verwenden, muss der Treiber für jedes Gerät auf dem Server installiert werden.
Die Software enthält alle Treiber und Plugins, die in den vorherigen Versionen der Software enthalten waren.
Jedoch Bei Bedarf können neue Treiber und Plugins manuell installiert werden.
Um einen neuen Treiber zu installieren, benötigen Sie ein gerätespezifisches Treiberinstallationspaket.
Das Treiberinstallationspaket ist ein komprimierter (gezippter) Ordner, der die Treiberdateien enthält.
Bei der Installation eines Treibers Installationspaket, vergleicht das System die Dateien im Installationspaket mit den vorhandenen Dateien auf den Servern.
Normalerweise installiert es die Dateien nur dann, wenn sie auf den Servern nicht vorhanden sind oder wenn die Dateien im Installationspaket neuer sind als die Dateien auf den Servern .
Sie können das System jedoch bei Bedarf dazu zwingen, eine beliebige Treiberversion zu installieren.

Notiz: Wenn Sie einen bereits vorhandenen Kameratreiber aktualisieren möchten, entfernen Sie die Kamera aus dem System, bevor Sie den Treiber aktualisieren.Nach dem Entfernen der Kamera installieren Sie die Treiberdatei, danach können Sie die Kamera neu installieren.Nach der Installation eines neuen Treibers müssen Sie konfigurieren die Geräte, die den Treiber verwenden.

So installieren Sie ein Treiberpaket:

Öffnen Sie auf der Registerkarte System unter Add-Ins die Option Treiber installieren.

Wählen Sie das Laufwerk aus, auf dem sich das Treiberpaket befindet, suchen Sie das Treiberpaket (.zip-Datei) und wählen Sie es aus. Das Dialogfeld Treiber installierenwird angezeigt.

3. Wählen Sie die Server aus, auf denen Sie den Treiber installieren möchten.

4. Wenn Sie das System zwingen möchten, die Treiberpaketversion zu installieren, wählen Sie  Treiber installieren, auch wenn dieselbe oder eine neuere Version vorhanden ist.

5. Klicken Sie auf Install. Die Spalte Status zeigt den Text Installed an, wenn der Treiber erfolgreich installiert wurde. Wenn der Treiber nicht installiert ist, zeigt die Spalte eine Fehlermeldung an.

6. Klicken Sie auf Schließen, um das Dialogfeld zu verlassen.

Hinweise:

Wenn Sie Treiber für andere Hardware als IP-Kameras aktualisieren müssen, wenden Sie sich bitte an den Systemlieferanten.

Ein 32-Bit-System erfordert ein 32-Bit-Treiberpaket und ein 64-Bit-System erfordert ein 64-Bit-Treiberpaket.

Pagination
Previous page
Mirasys Kamera-Treiber
Next page
Treiberinstallation und -verwendung