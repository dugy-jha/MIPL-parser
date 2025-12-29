# Multistreaming und TruCast für Netzwerkoptimierung und -speicherung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/multistreaming-und-trucast-fur-netzwerkoptimierung

Multistreaming und TruCast für Netzwerkoptimierung und -speicherung

Da es auch möglich ist, für TruCast einen anderen Stream als den Aufzeichnungsstream zu verwenden, sollte dies bei der Planung der Netzwerkkapazität berücksichtigt werden.

Beispielsweise können Benutzer Live-Bilder mit TruCast mit einer höheren Bildrate (z. B. 25 fps) anzeigen und immer mit einer niedrigeren Bildrate (z. B. acht fps) aufnehmen.

Dies reduziert den Speicher- und Netzwerkbedarf erheblich.

  Auswirkungen von TruCast auf die Bildverzögerung

Da der TruCast-Stream nicht zum VMS-Server und zurück wandert, ist die Verzögerung von der Kamera zum Client etwas geringer, aber der Unterschied zum vom Server empfangenen Stream ist nicht groß, nur wenige Millisekunden.

Der Unterschied in der Zweistrom-Mode ist im wirklichen Leben kompliziert zu beobachten.

   Von TruCast Streaming  nicht unterstützte Funktionen

TruCast unterstützt keine PTZ-Steuerung oder Audio

Außerdem unterstützt TruCast derzeit nur Live-Bilder. Die Wiedergabe (aufgezeichnete Bilder) wird derzeit immer vom Server empfangen.

  Lizenzen

TruCast erfordert die VMS-Lizenz, damit die TruCast-Funktion und die TruCast-Client-Treiberkennungen verwendet werden.

Diese TruCast-Treiberlizenzen und die TruCast-Funktion sind in der Produktversion Mirasys V9 immer aktiviert.

  Mehrere Zuschauer

Da jeder TruCast-Viewer einen individuellen neuen Stream von der Kamera zum Client öffnet, sollten Anwender testen, wie viele Streams zuverlässig von den verwendeten Kameras geöffnet werden können. In der Praxis funktionieren normalerweise 3-5 Streams ok.

  Client-Treiber installieren

Vor der Verwendung von TruCast müssen die erforderlichen Client-Treiber mit der System Manager-Anwendung installiert werden, wenn sie nicht mit der ursprünglichen Systeminstallation installiert wurden.

Die Client-Treiberpakete sind im gesamten Setup-Paket von Mirasys verfügbar. Sie werden mit der Dateinamenerweiterung „.sdi“ benannt.

Diese Treiber werden auf der ersten Seite der System Manager-Anwendung installiert, „Client-Treiber installieren“.

Die neuen Treiber können hinzugefügt werden, indem Sie auf die Schaltfläche „Neuen Client-Treiber installieren“ klicken und die SDI-Pakete auswählen.

Klicken Sie anschließend auf die Schaltfläche „OK“.

Nach der Installation der Treiber müssen diese noch auf die anzeigenden Spotter-Clients heruntergeladen werden. Dies geschieht, wenn der Spotter vom Desktop aus neu gestartet wird.

Nachdem Spotter die neuen Treiber heruntergeladen hat, ist das System für die Verwendung von TruCast bereit.

Bitte beachten Sie, dass nur die Kameras, deren Client-Treiber installiert wurde, als TruCast aktiviert angezeigt werden.

   Multi-Streaming konfigurieren 

TruCast kann jeden Stream von der Kamera, der Aufzeichnung, Live-Anzeige oder Remote-Streams verwenden.

Das Multi-Streaming wird normalerweise im System Manager - Kameras aktiviert und konfiguriert.

In den Spotter-Client-Einstellungen - Streaming - Multi-Streaming kann der Benutzer auswählen, welcher der Streams zum Anzeigen verwendet wird. Dieselbe Einstellung wird für die Standard- und TruCast-Anzeige verwendet.

TruCast-Standardeinstellung

Die Standardeinstellung für alle Kameras, die noch nicht für TruCast verwendet wurden, kann in den Spotter-Einstellungen - Streaming - TruCast-Standardwert definiert werden.

Die möglichen Werte sind

Immer vom VMS-Server streamen

Streamen Sie normal vom VMS-Server, wechseln Sie jedoch zu TruCast, wenn die Verbindung zum Server unterbrochen wird

Immer mit TruCast streamen

Pagination
Previous page
Netzwerkoptimierung
Next page
Verwenden von TruCast