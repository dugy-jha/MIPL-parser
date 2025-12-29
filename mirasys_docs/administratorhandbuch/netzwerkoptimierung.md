# Netzwerkoptimierung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/netzwerkoptimierung

Netzwerkoptimierung

TruCast kann verwendet werden, um die Netzwerklast in bestimmten Szenarien zu reduzieren.

Die Lastreduzierung erfolgt hauptsächlich, wenn sich der Server außerhalb des Standorts (remote) und der Viewing-Client vor Ort (lokal zu den Kameras) befindet.

In Beispielszenario 1 haben wir zwei Standorte, an denen die Aufzeichnung außerhalb des Standorts erfolgt und der Viewing-Client vor Ort ist. Im folgenden Diagramm erfolgt die Anzeige ohne TruCast, und das Video geht zuerst zum Server und dann vom Server zum Anzeige-Client.




Bei dieser Lösung wird der Verkehr zwischen den beiden Standorten erhöht.

Wenn der Stream mit TruCast direkt von der Kamera konsumiert wird, wird der Verkehr zwischen den beiden Standorten reduziert.




In Beispielszenario 2 befinden sich Kameras an zwei Standorten und anzeigende Clients an zwei Standorten.

Für den Site 2-Anwender ist der Einsatz von TruCast für die Kameras vor Ort sinnvoller.

Der Benutzer kann wählen, ob TruCast für alle Kameras oder nur für die Kameras vor Ort verwendet werden soll.

Für den Benutzer von Site 1 reduziert die Verwendung von TruCast nur den Datenverkehr vom Server zur nächsten Netzwerkverbindung.

Benutzer haben die vollständige Kontrolle darüber, welche Kameras typischerweise von TruCast verwendet werden.

Die Einstellung wird für jede Kamera und jeden Benutzer gespeichert und in Spotter-Layouts gespeichert.

Pagination
Previous page
Unterstützte Kameras
Next page
Multistreaming und TruCast für Netzwerkoptimierung und -speicherung