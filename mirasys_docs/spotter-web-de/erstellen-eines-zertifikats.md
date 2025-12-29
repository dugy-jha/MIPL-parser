# Erstellen eines Zertifikats | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-web-de/V9.9/erstellen-eines-zertifikats

Erstellen eines Zertifikats
Neues Zertifikat erstellen

Navigieren Sie zu Win-acme

Klicken Download

Laden Sie das neueste Paket herunter

Kopieren und extrahieren Sie das Paket auf den PC, auf dem Spotter Web installiert ist

Klicken wacs.exe

Geben Sie N  ein und drücken Sie ENTER

Überprüfen Sie, ob das Tool die Website erkennt, wählen Sie die richtige Nummer aus und drücken Sie ENTER

Wenn das Tool Binging nicht finden kann, überprüfen Sie, ob Sie die Website-Adresse in der Bindung hinzugefügt haben. Siehe Abschnitt Anwenden des Zertifikats auf das Spotter-Web.

Überprüfen Sie, ob das Werkzeug die richtige Adresse anzeigt, wählen Sie die angezeigte Nummer aus und drücken Sie ENTER

Antwort Yto Frage Continue with this selectionund drücken Sie die ENTER

10. Antwort Y to Frage Open in default application und drücken Sie die ENTER

11. Stimmen Sie dem Begriff zu, indem Sie Y eingeben und ENTER drücken

12. Danach können Sie eine E-Mail hinzufügen, wo Sie Updates zu Problemen und Missbrauch erhalten.

Wenn dies erledigt ist, erstellt das Tool ein Zertifikat für diese Domänenadresse. Jetzt können Sie das Tool schließen, indem Sie Q eingeben und ENTER.
 drücken

Anwenden des Zertifikats auf das Spotter-Web

Um das Let’s Encrypt-Zertifikat für Spotter Web zu verwenden, müssen Sie den Hostnamen für die Adresse sub.domain.com ändern.

Offen Internet Information Services Manager

Offen SpotterWeb Site

Auswählen Bindings

Klicken Bearbeiten

Geben Sie den richtigen Hostnamen ein

Klicken Sie auf . Wählen Sie , um das von Let´s encrypt  erstellte Browserzertifikat zu öffnen

Klicken OK

Wenn Sie die Website erneut öffnen, können Sie sehen, dass sie verschlüsselt ist, und Sie können die Website sicher verwenden.

Pagination
Previous page
Anforderungen