# OR Service-Installation | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/or-service-installation

OR Service-Installation

Für OR müssen Sie die Pakete ORService und ODSService installieren.

Anforderungen

Administratorrechte

Object Recognition-Lizenz auf dem VMS-Server

Der Objekterkennungsdienst verfügt über einen Cache für die Ähnlichkeitssuche, um die Ähnlichkeitssuche zu beschleunigen, der ein- oder ausgeschaltet werden kann.

Hinweis: Die Verwendung des Caches erhöht den Speicherverbrauch.

Sie können den Ähnlichkeitssuch-Cache bei der Installation des Dienstes aktivieren oder deaktivieren.

Installation

Laden Sie die neueste Version aus dem Extranet herunter.

Entpacken Sie dieses Beispiel in den Ordner C:\temp.

Starten Sie die Installation durch Doppelklick auf die Installationsdatei.

Klicken Sie auf Installieren, um fortzufahren.

Klicken Sie auf Weiter, um fortzufahren.

Ändern Sie bei Bedarf den Installationsort, wenn nicht, klicken Sie auf Weiter, um fortzufahren.

Ändern Sie den HTTP-Port des Dienstes, die Adresse und den Port des Hauptservers (Master) sowie die Adresse und den Port der Ereigniswarteschlange, falls erforderlich.

Der HTTP-Port ist standardmäßig 8092

Der Hauptserver (Master) verwendet standardmäßig Port 8082

Die Ereignis-Warteschlange verwendet standardmäßig Port 5672. Die Ereignis-Warteschlange wird mit dem ODSService-Paket installiert.

Klicken Sie auf Weiter, um fortzufahren.

Wählen Sie mindestens eines der Geräte aus, die für den OR verwendet werden sollen:

CPU

Intel-GPU

NVIDIA-GPU

Klicken Sie auf Installieren, um fortzufahren, und warten Sie.

Die Installation wird einige Zeit in Anspruch nehmen, bis sie abgeschlossen ist.

Die Erstellung von Modellen kann bis zu 30 Minuten dauern. Dies hängt davon ab, wie leistungsfähig die Grafikkarte ist, die verwendet wird.

Klicken Sie auf Fertig stellen, um fortzufahren.

Klicken Sie auf Schließen, um die Installation zu beenden.

Der Objekterkennungsdienst ist nun auf dem Server installiert und einsatzbereit.

Pagination
Previous page
Objekterkennung Einführung