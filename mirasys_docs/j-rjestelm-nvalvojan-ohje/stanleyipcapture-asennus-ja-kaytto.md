# StanleyIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/stanleyipcapture-asennus-ja-kaytto

StanleyIPCapture - Asennus ja käyttö

Kaikissa pakkaustiloissa ohjain käyttää RTSP/RTP/UDP/IP-protokollia videon vastaanottamiseen. HTTP-protokollaa käytetään parametrien asettamiseen/hakuun.

Jos VMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP-portit on avattava:

HTTP: oletusportti on 80,

RTSP: portti 554,

UDP: tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3556-4556.

Esimerkiksi: jos VMS:ssä on neljä kameraa, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se jätetään käyttämättä.

Rajoitukset

Ohjain havaitsee vain tällä hetkellä käytössä olevan profiilin ominaisuudet. Jos käyttäjä on muuttanut profiilia kameran verkkokäyttöliittymässä, kameran ominaisuudet on päivitettävä VMS:ssä (automaattinen haku on käynnistettävä uudelleen System Managerissa tai kamera on lisättävä uudelleen).

VMS:ssä ei ole mahdollista asettaa eri resoluutioiden määrää eri pakkausmuodoille, joten järjestelmänhallinnassa näytetään kaikki tuetut resoluutiot. Jos jokin resoluutio ei ole tuettu pakkausmuodossa, käytetään lähintä kelvollista resoluutiota.

Eri resoluutiot tukevat eri enimmäisruutunopeutta, joten ohjain käyttää lähintä voimassa olevaa ruutunopeuden arvoa. Jos esimerkiksi 1080p-resoluution maksimikuvataajuus on 15 kuvaa/s ja käyttäjä käyttää 30 kuvaa/s System Managerin asetuksissa, ohjain asettaa kameralle 15 kuvaa/s.

H.264-videovirrassa ei ole laatuasetusta, joten virran laadun hallitsemiseksi käytetään CBR-tilaa (constant bitrate mode). 1 % laatu System Managerissa tarkoittaa minimibittinopeuden arvoa ja 100 % laatu tarkoittaa maksimibittinopeuden arvoa.

Moninkertaisessa suoratoistossa kullakin suoratoistolla on vain yksi koodekki ja yksi resoluutio. Esimerkiksi kameran ensimmäisessä profiilissa on seuraavat yhdistelmät:

      -> H.264 :1920 x 1080

      -> H.264 :720 x 480

      -> JPEG :720 x 480

      -> JPEG :352 x 240

Ensimmäisessä striimissä on H.264-koodekki ja 1920x1080-resoluutio, toisessa striimissä on H.264-koodekki ja 720x480-resoluutio, kolmannessa striimissä on JPEG-koodekki ja 720x480-resoluutio. Ja neljättä yhdistelmää (JPEG-koodekki ja 352 x 240 resoluutio) käytetään jälleen ensimmäisessä striimissä. Moninkertainen suoratoisto voidaan poistaa käytöstä ohjaimen XML-tiedostossa.

Yksityisyysalueet voivat olla suuremmat kuin System Managerissa näkyvät, koska Stanley-kamerat käyttävät kiinteitä lohkoja maskin asettamiseen (20 lohkoa vaakasuunnassa ja 12 lohkoa pystysuunnassa).

Pagination
Previous page
SIPIPCapture - Asennus ja käyttö
Next page
VivotekIPCapture - Asennus ja käyttö