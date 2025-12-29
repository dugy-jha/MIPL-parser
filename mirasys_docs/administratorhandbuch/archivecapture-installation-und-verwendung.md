# ArchiveCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/archivecapture-installation-und-verwendung

ArchiveCapture - Installation und Verwendung

Der Pfad für das Archiv wird in das Adressfeld (automatisches Suchfenster) eingegeben.

Die Treiberkonfiguration erfolgt über ArchiveCapture.xml:

Schleifenfunktion

Zeit der ursprünglichen (aufgenommenen) Bilder

Bildrate (konfigurierbar oder Standard)

Zeitlimits für die Aufnahme aus dem gespeicherten Archiv

Aktivieren/Deaktivieren von Videokanälen

Die Abschnitte „Kanäle“ und „Limit“ können komplett deaktiviert werden (Attribut enabled=„0“)

Ohne ArchiveCapture.xml werden die Standardwerte verwendet.

Die Einstellungen der XML-Datei werden nur während der Archivsuche angewendet.

PAUSE, CONTINUE und NEXT_FRAME sind implementiert über CIPVideoCapture::SetExtendedProperty(const char* const aProperty, void* aValue, unsigned long aChannelId) wobei:
aProperty- Befehl, kann sein "PAUSE", "CONTINUE" and "NEXT_FRAME"
aValue- für zukünftige Bedürfnisse, sollte NULL sein
aChannelId- Kanal-ID




Pagination
Previous page
Treiberinstallation und -verwendung
Next page
CanonIPCapture - Installation und Verwendung