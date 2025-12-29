# Installation - Spotter Web | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-web-de/V9.9/installation-spotter-web-german

Installation - Spotter Web
❗️Wenn Sie Spotter Web verwenden möchten, MUSS der Master-Server V9.4 oder neuer sein!.
Einschränkungen des Betriebssystems

Wenn SpotterWeb auf einem Client-Betriebssystem installiert ist, können maximal 10 gleichzeitige Verbindungen bestehen: https: //docs.microsoft.com/en-us/iis/troubleshoot/request-restrictions

Für jede SpotterWeb-Anmeldung werden 3 Verbindungen hergestellt: HTTP, SignalR for events and WebSocket for streaming. So können sich beispielsweise bei Windows 10 Professional nur 3 Clients gleichzeitig anmelden.

Es gibt keine ähnlichen Einschränkungen im Server-Betriebssystem, daher wird dringend empfohlen, SpotterWeb auf dem Windows-Server-Betriebssystem zu installieren.

Bei der Installation von SpotterWeb auf dem Client-Betriebssystem gibt das Installationsprogramm eine Warnung zu den Einschränkungen des Betriebssystems/IIS aus.

Spotter-Web-Installation

Starten Sie die Installation, indem Sie auf das SpotterWeb-Installationspaket klicken

Klicken Install

Bestätigen Sie die Benachrichtigung über die Einschränkung des Betriebssystems

Klicken Next

Verwenden Sie den Standardinstallationsordner und klicken Sie auf Next

Stellen Sie die Master-Server-Adresse (den Computernamen des Master-Server-PCs) ein.

Verwenden Sie standardmäßig Master-Server-Port und Master-Server-HTTP-Port

Klicken Next

Legen Sie die SpotterWebsite-Adresse (den Computernamen des Master-Server-PCs) fest.

Verwenden Sie den Standardport  Spotter Web HTTPS  (443) 

Prüfen Sie, ob Set Firewall-Ausnahmen aktiviert ist

Klicken Next

Klicken Install

Klicken Finish

Klicken Sie auf Close, um die Installation abzuschließen




Pagination
Previous page
Über Spotter Web
Next page
Anmeldung