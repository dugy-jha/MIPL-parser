# Markieren | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-benutzerhandbuch/V9.9/markieren

Markieren

Die Metadaten-Objekte für LPR- und FR-Ereignisse enthalten Bounding-Box-Elemente und Beschriftungen (Identitätsname in FR-Metadaten und Kennzeichen im Falle von LPR-Metadaten). Diese Begrenzungsrahmen und Beschriftungen können in der Spotter-Anwendung angezeigt werden, wenn das VCA-Visualisierungs-Plugin aktiviert ist und der Benutzer die Anzeige von VCA im Bedienfeld der Videoansicht auswählt.

VCA-Visualisierungsanforderungen

Spotter muss Metadaten erhalten, um Objekte zu visualisieren.

Die Lizenz muss über VCA-Kanäle verfügen.

VCA muss für die Kamera in den Systemmanager-Einstellungen aktiviert sein, oder es muss die Kennzeichen- oder Gesichtserkennung verwendet werden.

Die Datenbank muss installiert sein (für die Wiedergabe von Metadaten)

Für optimale Ergebnisse sollte die hermeneutische Bewegungserkennung verwendet werden.

Es können sowohl VCA Core- als auch Mirasys-Metadaten verwendet werden, obwohl es einige Unterschiede bei der Erkennung von Objekten geben kann

​​​Visualisierung

Hervorheben von sich bewegenden Objekten wie Autos und gehenden Personen 

Zeigt die Spur, die das Objekt auf dem Kamerabildschirm genommen hat 

Textinformationen anzeigen zeigt Textinformationen zu dem verfolgten Objekt an

VCA-Zonen und -Linien anzeigen, nachdem sie mit dem VCA-Konfigurator konfiguriert worden sind

Einen VCA-Ereigniszähler nur für den Client anzeigen

Alle Zähler auf einem Kamerabildschirm zurücksetzen

Die VCA-Visualisierung kann für alle Kameras über das Registerkartenmenü aktiviert werden.

VCA-Visualisierungszustände werden im Speicher gehalten und auf einem lokalen PC für jeden Benutzer gespeichert

Der VCA-Zustand der Kamera wird gespeichert, so dass beim Öffnen der Kamera die zuvor verwendeten VCA-Zustände wiederhergestellt werden

Die VCA-Visualisierung kann auch mit AVM ein- und ausgeschaltet werden.

Die reinen Client-VCA-Zähler sind lokal in der Spotter-Anwendung und nicht in die Mirasys Reporting+ Anwendung integriert. Sie sind für kurzfristige Berichte gedacht und können durch Anklicken des Zählers auf dem Kamerabildschirm zurückgesetzt werden.

Intelligente Visualisierung von Erkennungsmetadaten

Es gibt zwei "Hervorheben"-Menüpunkte für die Visualisierung bewegter Objekte "Kennzeichen" und "Gesicht" (Zeichnungsränder und Name/Kennzeichen):

Nummernschilder anzeigen

Gesichter anzeigen

Die Menüpunkte sind nur aktiviert, wenn die Kamera für eine VCA-Erkennung konfiguriert ist.

Einstellungen für die VCA-Visualisierung in Spotter

Die Linienfarbe kann geändert werden

Die Linienstärke kann geändert werden

Die maximale Länge der Linie kann geändert werden

Die Zonenfarbe kann geändert werden

Erweiterte Einstellungen

In den erweiterten Einstellungen gibt es eine Einstellung, die VCA für alle Kameras zulässt, auch wenn VCA nicht für die Kamera konfiguriert ist. Dies ist nützlich, wenn Metadaten von Drittanbietersystemen (z. B. von Datentreibern) empfangen werden, die die VCA des Rekorders nicht verwenden.




Pagination
Previous page
Bildsteuerungen
Next page
Sicht