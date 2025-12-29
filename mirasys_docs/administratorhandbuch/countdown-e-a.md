# Countdown-E/A | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/countdown-e-a

Countdown-E/A

Mit Countdown I/O ist es möglich, Aktionen basierend darauf zu erstellen, ob einige Ereignisse in einem definierten Zeitraum eintreten oder nicht.

Wenn im System Manager ein neuer Countdown-E/A erstellt wird, erstellt dieser automatisch 4 Eingänge und 4 Ausgänge.

Countdown I/O hat zwei grundlegende Modi. Die ersten beiden Ein-/Ausgangspaare sind vom Typ 1, die letzten beiden Paare vom Typ 2.

Eine Lizenz steuert logische E/A und Countdown-E/A. Wenn die Lizenz nicht vorhanden ist, schlägt das Erstellen neuer E/A fehl.

Ereignisdauer überschritten Modus (Typ 1)

Erstens ist es möglich, einen Alarm auszulösen, wenn ein Ereignis länger dauert als die geplante Dauer.

Nehmen wir zum Beispiel an, die Zeit beträgt 10 Sekunden. Wird Ausgang eins ausgelöst und bleibt kürzer als die definierte Dauer aktiv, erfolgt kein Alarm.

Wird der Ausgang ausgelöst und bleibt länger als die definierte Dauer aktiv, erfolgt ein Alarm.

Beim Erstellen eines neuen Countdown-E/A sind die ersten beiden Eingangs-Ausgangspaare von diesem Typ.

Erwarteter Triggermodus (Typ 2)

Zweitens ist es möglich, einen Alarm auszulösen, wenn ein erwarteter Impuls nicht innerhalb der definierten Zeit empfangen wird.

Zum Beispiel beträgt die Zeit 10 Sekunden, und wir erwarten, dass der normale Betrieb alle 2-3 Sekunden Impulse von Ausgang 3 erhält.

Wenn der Impuls länger als 10 Sekunden fehlt, wird der Eingangszustand auf aktiv geändert. Es bleibt aktiv, bis der nächste Ausgangstrigger empfangen wird.

Beim Erstellen eines neuen Countdown-E/A ist das letzte Eingangs-Ausgangs-Paar von diesem Typ.

Pagination
Previous page
Logische E/A
Next page
Geplante E/A