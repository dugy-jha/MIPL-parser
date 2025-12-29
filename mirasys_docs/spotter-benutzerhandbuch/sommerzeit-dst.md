# Sommerzeit (DST) | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-benutzerhandbuch/V9.9/sommerzeit-dst

Sommerzeit (DST)

In diesem Leitfaden wird erläutert, wie Sie bei der Verwendung unserer Videoverwaltungssoftware (VMS) mit möglichen Problemen umgehen, die durch die Sommerzeitumstellung verursacht werden. Außerdem enthält er Anweisungen zum Abrufen von aufgezeichnetem Filmmaterial während der Sommerzeitumstellung, insbesondere in der ersten Stunde nach der Zeitumstellung.

Einführung

Bei der Sommerzeit werden die Uhren im Frühjahr um eine Stunde vorgestellt („spring forward“) und im Herbst um eine Stunde zurückgestellt („fall back“). Der genaue Zeitpunkt der Umstellung ist von Land zu Land und von Region zu Region unterschiedlich, aber das allgemeine Prinzip bleibt weltweit gleich.

:light_bulb_on:

Unser VMS speichert Filmmaterial in koordinierter Weltzeit (UTC).

Die UTC wird von der Sommerzeitumstellung nicht beeinflusst. Dadurch wird sichergestellt, dass kein aufgezeichnetes Material verloren geht oder dupliziert wird.

Auswirkungen der Sommerzeit auf Videoüberwachungssysteme

Die Umstellung auf die Sommerzeit kann bei der Durchsicht des Filmmaterials Verwirrung stiften, da sich die Ortszeit des Systems ändert, auch wenn die UTC-Zeit gleich bleibt.

Zwar geht kein Filmmaterial in UTC verloren oder wird dupliziert, doch kann die Änderung der Ortszeit die Darstellung für die Benutzer beeinflussen:

Die übersprungene Stunde kann dazu führen, dass die Benutzer denken, dass Filmmaterial fehlt.

Die wiederholte Stunde kann Verwirrung stiften, da sie zwei Sätze von Filmmaterial mit demselben lokalen Zeitstempel erzeugt.

Frühling vorwärts

Während der Sommerzeitumstellung im Frühjahr werden die Uhren um eine Stunde vorgestellt, wobei eine bestimmte Stunde übersprungen wird. Da unser System mit UTC arbeitet, wird diese Stunde nicht erfasst, da sie in der lokalen Zeit nicht existiert.

:light_bulb_on:

Für die Stunde, die während der Umstellung auf die Sommerzeit übersprungen wird, wird kein Video aufgezeichnet (die genaue Stunde hängt von der lokalen Zeitzone ab).

Die Benutzer können das fehlende Filmmaterial wahrnehmen, aber die übersprungene Stunde existiert einfach nicht in der lokalen Zeit des Systems.

Materialabruf beim Spring Forward

Bei der Zeitumstellung im Frühjahr ist zu beachten, dass die übersprungene Stunde nicht im System vorhanden ist. Das letzte verfügbare Filmmaterial vor der Zeitumstellung ist kurz vor der Umstellung auf die Sommerzeit, und das nächste verfügbare Filmmaterial ist eine Stunde später. Für die übersprungene Stunde gibt es kein Filmmaterial, das abgerufen werden könnte.

:light_bulb_on:
Vorwärts springen

Die bestimmte Stunde, die übersprungen wird, hat kein Filmmaterial. Diese Stunde hängt von der Zeitzone ab, in der sich das System befindet.

Abrufen von Aufnahmen: Das letzte verfügbare Filmmaterial vor der Zeitumstellung liegt kurz vor der übersprungenen Stunde, und das nächste verfügbare Filmmaterial wird nach der übersprungenen Stunde fortgesetzt.

Herbst zurück

Im Herbst werden die Uhren um eine Stunde zurückgestellt, wodurch eine bestimmte Stunde wiederholt wird. Da unser System in UTC arbeitet, bedeutet dies, dass für die wiederholte Stunde zwei getrennte Sätze von Filmmaterial aufgezeichnet werden.

Bei Verwendung der Zeitauswahl der Spotter-Anwendung für die doppelte Stunde werden alle Zeitanfragen in die zweite Stunde umgerechnet. Das bedeutet, dass bei der Verwendung der Spotter-Zeitleiste die Wiedergabe das Material abspielt und die Suche ab der zweiten Stunde erfolgt.

Um auf die Materialien der ersten Stunde zuzugreifen, können die Bediener die Wiedergabe ab der Stunde vor der Sommerzeitumstellung vorwärts oder ab der Stunde der Sommerzeitumstellung rückwärts starten.

Anweisungen für die Materialbeschaffung während des Fall Back

Für den Fall-Back-Übergang werden zwei separate Stunden aufgezeichnet. Diese zwei separaten Stunden können anhand des Zeitstempels des Systems unterschieden werden. Sie können sich vergewissern, dass auf die richtige Stunde zugegriffen wird, indem Sie das Systemprotokoll oder das Wasserzeichen überprüfen, das die tatsächliche Zeit der Aufzeichnung angibt.

Überprüfen Sie die Systemprotokolle und Ereignisprotokolle, um die genauen Zeiten zu ermitteln, zu denen das System seine Uhr eingestellt hat.

Bei Verwendung der Zeitauswahl der Spotter-Anwendung für die doppelte Stunde werden alle Zeitanfragen in die zweite Stunde umgerechnet. Das bedeutet, dass bei der Verwendung der Spotter-Zeitleiste die Wiedergabe das Material abspielt und die Suche ab der zweiten Stunde erfolgt.

Um auf die Materialien der ersten Stunde zuzugreifen, können die Bediener die Wiedergabe ab der Stunde vor der Sommerzeitumstellung vorwärts oder ab der Stunde der Sommerzeitumstellung rückwärts starten.

:light_bulb_on:
Zurückstellen

Die jeweilige Stunde wird zweimal aufgezeichnet, einmal vor und einmal nach der Rückstellung der Uhr.

Aufzeichnungen abrufen: Unterscheidung zwischen zwei aufgezeichneten Stunden. Überprüfen Sie das Systemprotokoll oder das Wasserzeichen, um zwischen den beiden Aufzeichnungen der wiederholten Stunde unterscheiden zu können.

Wenn Sie die Spotter-Anwendung für die Wiedergabe verwenden, beachten Sie, dass alle Zeitanfragen während der doppelten Stunde standardmäßig auf das zweite Auftreten dieser Stunde verweisen.

Um das Filmmaterial aus der ersten Stunde der doppelten Stunde abzurufen, können Sie:

Starten Sie die Wiedergabe ab der Stunde vor der Sommerzeitumstellung.

Rückwärtswiedergabe ab der Stunde nach der Umstellung der Sommerzeit verwenden.

Best Practices für die Handhabung von DST-Übergängen in Mirasys VMS

Um Verwirrung zu vermeiden und sicherzustellen, dass sich das System während der Sommerzeitumstellung wie erwartet verhält, ist es wichtig, die folgenden Best Practices zu befolgen:

Informieren Sie alle Bediener und Benutzer über die bevorstehende Sommerzeitumstellung und erklären Sie die Auswirkungen auf das aufgezeichnete Filmmaterial, insbesondere die übersprungene Stunde während der Sommerzeit und die doppelte Stunde während der Winterzeit.

Stellen Sie sicher, dass alle Systemkomponenten, einschließlich Server, Kameras und zugehörige Geräte, mit einer genauen Zeitquelle synchronisiert sind, um eine Zeitverschiebung während der Umstellung zu verhindern.

Bereiten Sie die Bediener bei Filmmaterial mit Zeitstempeln auf eine mögliche Verwechslung dieser Zeitstempel während und nach der Umstellung vor.

Überprüfen Sie nach der Sommerzeitumstellung das Filmmaterial während des Übergangszeitraums. Stellen Sie sicher, dass die Aufnahmen vor und nach der Zeitumstellung intakt und zugänglich sind.

Im Falle einer Zeitumstellung sollten Sie sich bewusst sein, dass es zwei Sätze von Aufnahmen für dieselbe Stunde gibt. Stellen Sie sicher, dass die Bediener wissen, wie sie zwischen den beiden Aufzeichnungszeiträumen unterscheiden können.

Bei Systemen, die aufgrund von Bewegung oder Alarmen ausgelöst werden, überprüfen Sie alle Ereignisse, die während der Zeitumstellung aufgetreten sind, um sicherzustellen, dass sie ordnungsgemäß aufgezeichnet wurden.




Pagination
Previous page
Verwendung mehrerer Alarmmonitore
Next page
Systemüberwachung