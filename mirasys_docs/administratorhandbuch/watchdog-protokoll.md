# Watchdog-Protokoll | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/watchdog-protokoll

Watchdog-Protokoll

Standardmäßig zeigt das System die Watchdog-Protokolle von allen Servern an.
 Sie können jedoch einen oder mehrere Server aus der Liste auf der linken Seite auswählen.
Sie können die Protokolle sortieren, indem Sie auf die Spaltenüberschriften klicken.
Um die Liste zu aktualisieren, ohne das Fenster zu schließen, klicken Sie auf die Schaltfläche Aktualisieren.

Zusätzliche Watchdog-Zustellungsmethoden

Die Watchdog-Funktionalität umfasst drei neue Protokolle: TCP, SMS (erfordert ein externes SMS-Modul) und anpassbares E-Mail-Formular.

Jedes neue Protokoll hat seinen Treiber:

C:\Programme\DVMS\DVR\WDEventProviders\

WDEventProviderSMS.xml

WDEventProviderSMTP.xml

WDEventProviderTCP.xml

Derzeit müssen diese Dateien manuell bearbeitet werden. Jede XML-Datei enthält die Dokumentation zu den Konfigurationsoptionen.
Die neuen Konfigurationsoptionen umfassen gefilterte und bedingte Warnungen (z. B. „Warnung X nur einmal alle 60 Minuten senden“ oder „Warnung X nur senden, wenn Bedingung Y nicht innerhalb von zwei Minuten erfüllt wird“). und ein anpassbares Warnmeldungsformat.
 Nachdem die Dateien bearbeitet wurden, muss Watchdog neu gestartet werden, damit die Änderungen wirksam werden.

Notiz Diese Funktion wird nur für fortgeschrittene Benutzer empfohlen. XML-Dateien sind sehr anfällig für Rechtschreibfehler und Tippfehler bei Zeichenfolgen und Schlüsseln.
 Selbst ein winziger Fehler kann schwerwiegende Fehler verursachen. Mirasys übernimmt keine Verantwortung für XML-Fehler, die durch das Bearbeiten der Dateien verursacht werden.

Pagination
Previous page
Watchdog-Einstellungen
Next page
Add-Ins