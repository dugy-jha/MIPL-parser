# Serverdiagnose | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/serverdiagnose

Serverdiagnose

Die VMS-Server-Diagnose zeigt Informationen über den Server und die CPU- und Netzwerkauslastung an.

Diagnose

Die Registerkarte Diagnose zeigt diese Informationen:

Informationen zum Server:

Softwareversion

Modell

Anzahl der Kameras, Audiokanäle, Digitaleingänge, Digitalausgänge und Videoausgänge

Der Name des Computers und die Zeitzone

Informationen zum Betriebssystem

Prozessorinformationen

Installierte Treiber, z. B. Capture-Treiber, Videoausgabetreiber, Digitalausgabetreiber und PTZ-Treiber

Protokolldateien

Die Registerkarte Protokolldateien zeigt eine Liste der Protokolldateien an.

So zeigen Sie den Inhalt einer Protokolldatei an:

Wählen Sie die Datei aus der Dropdown-Liste aus. Der Inhalt wird im Inhalt der ausgewählten Protokolldatei angezeigt

Leistung

Auf der Registerkarte Leistung können Sie diese überwachen:

CPU auslastung.

Nutzung des physischen Speichers.

Nutzung des virtuellen Speichers.

Netzwerktraffic.

Benutzter Speicherplatz.

Lagerung

Auf der Registerkarte Speicher können Sie Datenträger- und Dateieigenschaften überwachen. Sie können beispielsweise den freien Speicherplatz überprüfen oder gespeicherte Daten nach Kamera und Audiokanal überwachen.

Allgemein Gesamtaufnahmekapazität. Zeigt die gesamte Speicherkapazität an, die für die Aufnahmen reserviert ist.

Belegter Speicherplatz Die Menge an Speicherplatz, die die Aufzeichnungen belegt haben.

Freier Speicherplatz. Für Aufzeichnungen ist freier Speicherplatz verfügbar.
 % belegt. Der Prozentsatz der belegten Festplattenkapazität.

Durchschnittliche Speichergeschwindigkeit. Wird berechnet, indem die seit dem letzten Start des Servers gespeicherte Datenmenge durch die Betriebszeit dividiert wird.

VMS-Server-Betriebszeit Zeigt die Betriebszeit des Servers seit dem letzten Start an.

Der Zähler zeigt die Differenz zwischen der aktuellen Uhrzeit und der Startzeit in Tagen, Stunden und Minuten an.

Festplatten

Gesamtaufzeichnungskapazität. Zeigt die Speicherkapazität an, die für die Aufnahmen auf dem ausgewählten Datenträger reserviert ist.

Verwendeter Speicherplatz. Benutzter Speicherplatz auf der ausgewählten Festplatte.

Freier Speicherplatz. Auf dem ausgewählten Datenträger ist freier Speicherplatz für Aufzeichnungen verfügbar.

% verwendet. Der Prozentsatz des belegten Speicherplatzes der für die Aufzeichnungen reservierten Gesamtkapazität.

Gesamtaufzeichnungs-Cache. Zeigt die Gesamtkapazität des Caches an, der für die temporäre Speicherung von Daten verwendet wird, bevor sie dauerhaft auf eine Festplatte geschrieben werden.
Aufgrund des Caches können Video und Audio sofort aufgezeichnet werden, wenn der Server gestartet wird. Der Cache wird auch für die Aufzeichnung vor dem Ereignis verwendet.

Das System berechnet automatisch, wie viel Cache-Speicherplatz es haben muss, und weist den Speicherplatz entsprechend zu.

Verwendeter Aufzeichnungs-Cache. Temporärer Speicherplatz, der derzeit verwendet wird.

Freier Aufzeichnungscache. Temporärer Speicherplatz, der derzeit frei ist.

Kameras

Älteste Zeit. Datum und Uhrzeit des ältesten Bildes im Store.

Neueste Zeit.

Datum und Uhrzeit des neuesten Bildes im Store.

Gesamtnr. Bilder. Die Gesamtzahl der Bilder im Store.

Durchschnittliche Bildgröße. Die durchschnittliche Bildgröße.

Verwendeter Speicherplatz. Dieser Wert zeigt, wie viel Speicherplatz die Bilder und Metadatendateien dieser Kamera beanspruchen.

% verwendet. Dieser Wert zeigt an, wie viel Prozent des Speicherplatzes diese Kamera von der für die Aufzeichnungen reservierten Gesamtkapazität belegt hat.

Audiokanäle

Älteste Zeit. Das Datum und die Uhrzeit des ältesten Audio-Samples im Speicher.

Neueste Zeit. Das Datum und die Uhrzeit der neuesten Probe im Geschäft.
Eine Gesamtzahl von Proben. Die Gesamtzahl der Audio-Samples im Store.
Durchschnittliche Sample-Größe. Die durchschnittliche Audio-Sample-Größe.
Verwendeter Speicherplatz. Dieser Wert zeigt an, wie viel Speicherplatz die Audio-Samples und Metadatendateien des Audiokanals beanspruchen.
% verwendet. Dieser Wert zeigt an, wie viel Prozent des Speicherplatzes der Audiokanal von der für die Aufzeichnungen reservierten Gesamtkapazität belegt hat.

Textkanäle

Älteste Zeit. Das Datum und die Uhrzeit des ältesten Textdatenbeispiels im Speicher.

Neueste Zeit. Das Datum und die Uhrzeit der neuesten Probe im Geschäft.

Eine Gesamtzahl von Proben. Die Gesamtzahl der Textdatenbeispiele im Speicher.

Durchschnittliche Stichprobengröße. Die durchschnittliche Stichprobengröße von Textdaten.

Verwendeter Speicherplatz. Dieser Wert zeigt, wie viel Speicherplatz die Textdatenbeispiele und Metadatendateien aus dem Textkanal beanspruchen. 

% verwendet. Dieser Wert zeigt an, wie viel Prozent des Speicherplatzes der Textkanal von der für die Aufnahmen reservierten Gesamtkapazität belegt hat.




Pagination
Previous page
SM-Server-Diagnose
Next page
Audit-Protokoll