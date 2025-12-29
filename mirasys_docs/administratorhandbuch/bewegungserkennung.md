# Bewegungserkennung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/bewegungserkennung

Bewegungserkennung

Mit unserer Bewegungserkennungsfunktion können Sie festlegen, welche Aufzeichnungen in unserem Dateisystem gespeichert werden und zur Auslösung von Alarmen verwendet werden können.

Um mit der Bewegungserkennung zu beginnen, müssen Sie Bewegungsmasken konfigurieren, die dann verwendet werden, um zu definieren, ob eine Bewegung auf der Kamera oder im Videostream erkannt wird.

Mithilfe des Schedulers können Sie entscheiden, welche Bewegungsmasken bei der Speicherung von Aufzeichnungen im Dateisystem verwendet werden sollen.

Die durch die Bewegungserkennung erhaltenen Informationen können in den Alarmeinstellungen verwendet werden, um Alarme auszulösen. In den Einstellungen für die Alarmauslösung legen Sie fest, welche Bewegungsmaske für die Bewegungserkennung als Alarmauslöser verwendet werden soll.

Um auf die Konfiguration der Bewegungserkennung im System Manager zuzugreifen, gehen Sie zu VMS Server Settings > Camera Settings > Motion Detection.

Empfindlichkeit und Quantität

Das System erkennt Bewegung, wenn:

Pixel ändern sich mehr als das eingestellte Limit (Empfindlichkeit).

Die angegebene Pixelanzahl ändert sich (Menge).

Wenn im Bild viele Hintergrundgeräusche vorhanden sind, z. B. Änderungen der Lichtverhältnisse, verringern Sie die Empfindlichkeit, indem Sie den Schieberegler nach links ziehen, oder erhöhen Sie die Mengenbegrenzung, indem Sie den Schieberegler nach rechts ziehen.

Methoden zur Bewegungserkennung
Vergleichende Erkennung

Die vergleichende Erkennung vergleicht ein Bild mit dem vorherigen Bild und kann unter den meisten Bedingungen eingesetzt werden.

Wenn die Unterschiede die eingestellten Grenzwerte überschreiten, erkennt das System eine Bewegung.

Bei viel Bewegung im Hintergrund, z. B. bei Regen, sich bewegenden Blättern oder wechselnden Lichtverhältnissen, sollten Sie die adaptive Bewegungserkennung verwenden.

Adaptive Erkennung

Die adaptive Erkennung vergleicht jedes Bild mit einem Hintergrundbild.

Das System lernt automatisch das Hintergrundbild und interpretiert z. B. bewegte Blätter nicht als Bewegung.

Wenn sich mehr als die Hälfte der Pixel in einem Bild ändert, schließt das System daraus, dass sich die Lichtverhältnisse geändert haben, und setzt das Referenzbild zurück und beginnt erneut mit dem Lernen.

Hermeneutische Entdeckung

Die hermeneutische Erkennung ist ein ausgeklügeltes Bewegungserkennungssystem für schwierige Wetterbedingungen wie starken Regen, „verrauschte“ Hintergrundbilder und Situationen, in denen externe Video-Content-Analysetools (VCA) verwendet werden.

Die hermeneutische Erkennung erfordert mehr Verarbeitungsressourcen als die anderen Erkennungsmethoden.

Bildrate der Bewegungserkennung

Mit der Bildrate für die Bewegungserkennung wird die für die Bewegungserkennung verwendete Bildrate festgelegt.

Es wird im Allgemeinen empfohlen, die Standard-Bildrate zu verwenden.

Bei IP-Kameras verwendet die Bewegungserkennung Intra-Frames und entspricht der Intra-Frame-Rate. Normalerweise ist dies ein Bild pro Sekunde.

Pagination
Previous page
Moxa-Einstellungen
Next page
Konfiguration der Bewegungserkennung