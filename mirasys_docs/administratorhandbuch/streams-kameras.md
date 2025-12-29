# Streams (Kameras) | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/streams-kameras

Streams (Kameras)
Standardmäßig empfängt Mirasys VMS einen Stream in Aufzeichnungsqualität von der Kamera. 
 Der Mirasys VMS-Server sendet den Aufzeichnungsstream standardmäßig an Mirasys Spotter
Codec

Der Codec wird für die Übertragung des Videos zwischen dem Server und den Client-Anwendungen und im Fall von IP-Kameras für die Übertragung des Videos zwischen der IP-Kamera und dem Server verwendet.
 Im Fall von analogen Kameras ist der vom System verwendete Codec JPEG.
Bei IP-Kameras kann jeder Codec ausgewählt werden, der sowohl von der Kamera als auch von der Serversoftware unterstützt wird.
Die von der Serversoftware unterstützten Codecs sind JPEG, MPEG-4, H.264, H.265 und Mobotix MxPEG.

Bitrate mode. 

Diese Einstellung steuert, ob die variable Bitrate (VBRMax) oder die konstante Bitrate (CBR) verwendet wird.

Qualität

Stellen Sie diesen Wert zwischen 0%-100% ein. Ein höherer Wert bedeutet eine bessere Bildqualität, aber auch eine große Bilddatengröße.
 Um die Bilddatengröße zu verringern, stellen Sie den Wert niedriger ein. Eine niedrigere Einstellung des Werts verringert jedoch auch die Qualität der Bilder. 
50 % sind in der Regel ausreichend. Wählen Sie für drahtlose Verbindungen und Verbindungen mit geringer Bandbreite 0 % aus.

Auflösung

 Bei automatisch konfigurierten IP-Kameras werden genau die vom Kameramodell unterstützten Bildauflösungen angezeigt.

Rekordrate

Die Aufzeichnungsrate definiert, wie viele Frames die Kamera an das VMS sendet und wie viele Frames aufgezeichnet werden.
Die maximale Rate hängt vom Videostandard und vom Kameratyp ab.
Multiple Streaming (Multi-Streaming)

Mehrfach-Streaming (Multi-Streaming)

Pagination
Previous page
Allgemeine Einstellungen
Next page
Multi-Streaming (Kameras)