# Video-Einstellungen | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-benutzerhandbuch/V9.9/video-einstellungen

Video-Einstellungen
Videoeinstellungen

Die Videoeinstellungen ermöglichen die Einstellung benutzerdefinierter Dekodierung und das Ändern von Rendering-Technologien, um die Leistung je nach Hardware zu verbessern.

Videodekodierung

Verwenden Sie benutzerdefinierte Decodierungseinstellungen ermöglicht Ihnen die Auswahl einer bestimmten Decodierungseinstellung und die Entscheidung, wie viel Prozent der Streams mit der GPU decodiert werden.

H.264 codec

IPP:  nutzt die CPU

CoreAVC:  Kann CPU oder Nvidia CUDA verwenden

Nvidia:  erfordert Nvidia-GPU

Intel:  verwendet CPU; Wenn der Prozessorchip über eine integrierte Intel Graphics-GPU verfügt, kann er auch GPU verwenden

H.265 codec

Nvidia:  basiert erfordert Nvidia GPU

Intel:  verwendet CPU; Wenn der Prozessorchip über eine integrierte Intel Graphics-GPU verfügt, kann er auch GPU verwenden. Der Slider beeinflusst, wie viele Kameras CPU / GPU verwenden.

Wie viele Streams werden mit der Display-Hardware dekodiert 

Definiert, wie viel Prozent der Kameras CPU/GPU verwenden.
Wenn die Dekodierungsmethode Nvidia ausgewählt und der Schieberegler auf z. 50 %, die Hälfte der Kameras wird mit Nvidia dekodiert und die andere Hälfte wird CoreAVC verwenden, wenn es sich um H.264 handelt, und eine Intel-CPU, wenn es sich um H.265 handelt

Video-Rendering

Ermöglicht das Ändern des Videorenderings in WPF (Standard) oder DirectX

Aktivieren Sie die reibungslose Videoskalierung

Es verwendet einen anderen Bildzeichnungsmechanismus und hat einen Glättungseffekt auf das Video, insbesondere wenn die Bildrate hoch ist (über 20 fps).
Die Einstellung für die glatte Videoskalierung sollte jedoch nicht verwendet werden, wenn der Benutzer mehrere Spotter-Fenster geöffnet hat.
Die glatte Videoskalierung verbessert das Erscheinungsbild des Videobilds, aber diese Einstellung erhöht die Computerlast leicht.




Pagination
Previous page
Streaming-Einstellungen
Next page
Anzeige