# Mehr als ein Server hinter dem Router | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/mehr-als-ein-server-hinter-dem-router

Mehr als ein Server hinter dem Router

Szenario 2: Mehrere Server hinter einem einzigen Router (WAN-Adresse)

Wenn der Benutzer ein umfangreicheres System mit mehreren Servern an einem einzigen Standort konfiguriert, kann er die Server mit den externen oder internen IP-Adressen zur System Manager-Anwendung hinzufügen. ein Hinweis zeigt, dass er zwischen einer internen IP-Adresse und einer externen IP-Adresse wählen kann. 
Wenn der Server aus dem WAN verwendet werden soll, dann sollte die externe IP-Adresse gewählt werden.
Die genauen Ports, auf die der Server eine Port-Weiterleitung vorgenommen hat gefunden werden, indem Sie den System Manager auf dem lokalen Server starten Die Portweiterleitung wurde durchgeführt an.
Wenn der hinzugefügte Server ein einzelner, eigenständiger Server ist, ist der Port höchstwahrscheinlich 5009.
Wenn sich mehrere Server auf derselben Site befinden, erhalten sie höchstwahrscheinlich die Ports beginnend mit 5009, 5013, 5017, 5021…

Pagination
Previous page
Einzelner Server hinter Router
Next page
Mehr als ein Server auf mehreren Sites