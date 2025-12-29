# HTTPIPCapture - Installation und Verwendung | Mirasys Help Center

Source: https://documentation.mirasys.com/administratorhandbuch/V9.9/httpipcapture-installation-und-verwendung

HTTPIPCapture - Installation und Verwendung

Der Treiber verwendet das HTTP-Protokoll, um Videoströme von IP-Geräten zu empfangen.

Der Treiber erwartet, dass die HTTP-URI zum Gerät hinzugefügt und in das Feld „IP-Adresse“ eingetragen wird.

Der erforderliche Port kann separat im Feld „Port“ oder in der HTTP-URI angegeben werden. Der HTTP-URI-Port hat eine höhere Priorität; wenn er angegeben ist, wird das DVMS-Portfeld ignoriert.

Die Stream-URI-Anforderungen: Die HTTP-URI sollte im vollständigen Format angegeben werden, z. B. http://192.168.1.70:8080/video.

Die Stream-URI kann über Player von Drittanbietern, wie VLC, überprüft werden.

Einschränkungen

Wenn die Kamera eine Basic-HTTP-Autorisierung erfordert, müssen der richtige Benutzername und das richtige Kennwort eingegeben werden. Andernfalls wird kein Video übertragen.




Pagination
Previous page
GatewayIPCapture - Installation und Verwendung
Next page
IPCameraCapture - Installation und Verwendung