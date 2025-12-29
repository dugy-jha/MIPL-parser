# NewIQEyeIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/newiqeyeipcapture-asennus-ja-kaytto

NewIQEyeIPCapture - Asennus ja käyttö

Ajuri käyttää RTSP/RTP/UDP/IP-protokollia H.264-pakattujen video- ja äänivirtojen vastaanottamiseen. HTTP-protokollaa käytetään parametrien asettamiseen/hakuun ja MJPEG-virran jatkuvaan vastaanottoon.

Jos DVMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP-portit on avattava:

HTTP: oletusportti on 80,

RTSP: oletusportti on 554,

UDP: tarvitaan kaksi peräkkäistä porttia audio/videovirtaa kohden porttialueella 3554-4556.

Rajoitukset

IQEye-kameroissa on yksi resoluutio ja useita rajattuja resoluutioita. Rajattuja resoluutioita ei käytetä ohjaimessa. Ajuri käyttää vain down sample -prosessia kuvan koon muuttamiseen (koko / 2, koko / 4 ja koko / 8). Alasnäytteenotto on käytössä kameroissa, jotka tukevat sitä (kamerat IQ73xx, IQ04xx, IQD4xx ja IQ54xx eivät tue sitä).

IQ712-kamerassa on MJPEG:n maksimikuvausnopeuden rajoitus - 15 kuvaa sekunnissa.

IQEye-kameroilla (paitsi IQ73xx) on vain yksi resoluutio H264:lle ñ 640x480. Muita voidaan käyttää vain MJPEG:lle.

H.264-koodekki tukee vain 5,10,15,30 kuvanopeuden arvoja kaikille kameroille. Muita arvoja käytetään vain MJPEG:ssä, ja ne skaalataan edellä mainittuihin arvoihin, jos H.264-koodekki on aktiivinen.

IQA25S-kameran MJPEG-koodekille 2560x1920- ja 1280x960-resoluutiot tukevat maksimitaajuusarvoa 7, 640x480- ja 320x240-resoluutioille vain maksimitaajuusarvoa 10 fps.

IQA25S-kameran JPEG-koodekin resoluution max /2 pitäisi toimia 10 fps, mutta se toimii sellaisenaan - max fps on 7, jos määritetty korkeampi - se asettaa 5 tai 4 fps, tämä on firmware ongelma.

Ajuri tukee vain G.711-äänivirran vastaanottoa. AAC-koodekkia ei tueta tällä hetkellä.

Pagination
Previous page
NewBoschIPCapture - Asennus ja käyttö
Next page
NewMobotixIPCapture - Asennus ja käyttö