# NewPanasonicIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/newpanasonicipcapture-asennus-ja-kaytto

NewPanasonicIPCapture - Asennus ja käyttö

Kaikissa pakkaustiloissa ohjain käyttää RTSP/RTP/UDP-protokollia videon vastaanottoon, HTTP/HTTPS-protokollia parametrien asettamiseen/palauttamiseen ja PTZ-toimintoihin.

H.264/MPEG4-pakkaustilassa ohjain käyttää RTSP/RTP/UDP/IP-protokollia videon vastaanottoon. HTTP-protokollaa käytetään parametrien asettamiseen/hakuun ja MJPEG-virran jatkuvaan vastaanottoon.

Jos DVMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP-portit on avattava:

HTTP: oletusportti on 80,

RTSP: oletusportti on 554,

UDP: tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3556-4556.

NewPanasonicIPCapture.xml-tiedostoa käytetään konfigurointiin:

Ajurin käyttäytyminen:

Unicast

Multicast:Primary

Multicast:Listener

Lähetysprioriteetti:

Bitrate

Framerate

Paras ponnistus

Kehittynyt VBR

VBR

Vähimmäisbittinopeus (vain Best effort -tilassa)




Pagination
Previous page
NewMobotixIPCapture - Asennus ja käyttö
Next page
NewSamsungIPCapture - Asennus ja käyttö