# Automatische Router-Konfiguration | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/automatische-router-konfiguration

Automatische Router-Konfiguration

Wenn ein VMS-Server startet, versucht er, UPnP-Geräte aus dem Netzwerk zu erkennen.
Der Router muss UPnP (Universal Plug and Play) unterstützen, was auf dem Gerät aktiviert sein muss.
Der Server verfügt über eine kontinuierliche UPnP-Geräteerkennung, wenn er ausgeführt wird Wenn Netzwerkänderungen vorgenommen werden, erkennt der Server automatisch neue Router und führt eine Portweiterleitung zu ihnen durch.
Es werden nur UPnP-Geräte mit externen (WAN-)Adressen erkannt.
Wenn der Benutzer die Portweiterleitung automatisch entfernen möchte, kann er dies über den Systemmanager tun .
Danach erinnert sich der Server daran, dass die Einstellungen entfernt wurden, und leitet die Portweiterleitung nicht an diesen Router weiter.
Die Software erlaubt es nicht, die Portweiterleitungszuordnung zu löschen, wenn der Server mit einer externen Adresse zum System hinzugefügt wird.
Das Löschen der Portweiterleitungszuordnung würde dies tun Trennen Sie das System, und es wäre keine weitere Konfiguration möglich.
Wenn die Weiterleitungs-Port-Einstellungen geändert werden und die Verbindung zum Server nach einer Weile nicht wiederhergestellt wird, kann es erforderlich sein, den neu zu starten router.
Server benötigen vier Ports für die Server-zu-Server-Kommunikation. Der erste Server, der Portweiterleitung durchführt, beansprucht die Ports 5008, 5009, 5010  und 5011.
Der zweite Server beansprucht die Ports 15012-5015, der dritte Server die Ports 5016-5019. Und so weiter. (Vorausgesetzt, alle Ports sind verfügbar).
Der erste Port wird für die SMServer-Kommunikation verwendet (5008, 5012, 5016…)
Der zweite Port wird für die DVRServer-Prozesskommunikation verwendet (5009, 5013, 5017…)
Bei einer Verbindung zu einem Master-Server ist der Port normalerweise 5008. Beim Hinzufügen neuer Server zum Master ist der Port normalerweise 5009. Wenn mehr als ein Server vor Ort ist, dann sind die Ports 5009 + 4, 5009 + 8 usw.

Pagination
Previous page
Port-Weiterleitung
Next page
Einzelner Server hinter Router