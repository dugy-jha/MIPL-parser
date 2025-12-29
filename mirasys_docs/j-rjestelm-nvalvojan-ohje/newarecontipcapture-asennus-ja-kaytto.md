# NewArecontIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/newarecontipcapture-asennus-ja-kaytto

NewArecontIPCapture - Asennus ja käyttö

H.264-pakkaustilaohjain käyttää RTSP/RTP/UDP/IP-protokollia videon vastaanottoon yleisillä kuvanopeuksilla. HTTP-protokollaa käytetään parametrien asettamiseen/hakuun, MJPEG/H.264-virran vastaanottoon kameran hitaiden kuvataajuuksien tapauksessa ja jatkuvaan MJPEG-vastaanottoon.

Jos DVMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP-portit on avattava:

HTTP: oletusportti on 80,

RTSP: oletusportti on 554,

UDP: tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3554-4556.

Ajuri voidaan määrittää XML-määritystiedoston avulla seuraavien parametrien asettamiseksi:

Sisävalaistuksen kompensointiarvo

Kanavakohtaiset parametrit:

MaxFrameRate - maksimikuvanopeus täydellä resoluutiolla

MaxFrameRateHalf - maksimikuvanopeus puolikasta resoluutiota varten

RTP over RTSP -kuljetusprotokolla

RTP-lohkon koko (jos tietty reititin sitä vaatii).

BitrateMode (CBR, VBR tai Auto - jälkimmäinen kertoo ohjaimelle, että se ohittaa laadunmuutoksen kameran aikana).

BitrateMin (CBR:n minimibittinopeus)

BirateMax (CBR:n suurin bittinopeus)

KeyFrameIntervalMs (Kehyksen sisäinen väli ms, 0 - kaikki intras)

IndoorLightFrequency - valon taajuus

Rajoitukset

Suurin kuvataajuusarvo lasketaan Arecontin ”salaisen” kaavan avulla. Todellinen kuvataajuus voi olla määritettyä pienempi - se riippuu verkko-olosuhteista.

Jotkin kuvien resoluutiot voivat poiketa asetuksista, esimerkiksi 1600x1200 on 1600x1184. Tämä johtuu siitä, että Arecont-kameran resoluution on oltava jaollinen 32:lla täydessä tilassa ja 64:llä puolikkaassa tilassa.

Arecontin maksimiresoluutio asetetaan kamerassa. VMS käyttää sitä ja puolta siitä. Jos haluat muuttaa enimmäisresoluutiota, sinun on muutettava se kamerassa ja lisättävä kamera VMS:ään.

Arecontin kameroissa on vain kaksi täyttä kuvan resoluutiota - sensorin enimmäisresoluutio ja puolet siitä. Muut resoluutiot rajataan maksimiresoluutiosta, eikä niitä käytetä ohjaimessa.

AV8185:ssä ja AV8180:ssä ei ole IO:ta (niiden asiakirjoissa olevat tiedot ovat virheellisiä).

AV3135:ssä on kaksi anturia: päivä- ja yöanturi. Molemmat toimivat tietyillä resoluutioilla. VMS näyttää resoluutiot päivätilaa varten; todellinen kuvan resoluutio voi poiketa asetuksista.

Arecontin kamerat voivat muuttaa kuvan resoluutiota dynaamisesti. Todellinen kuvan resoluutio voi poiketa asetuksista.

DVMS tukee enintään 30 kuvaa/s, joten kaikilla Arecontin kameroilla on tämä rajoitus (vaikka ne tukisivat yli 30 kuvaa/s).

Arecontin 4ch-kameroilla voi olla ongelmia, kun käytetään H.264 + MJPEG -tekniikkaa. On parempi käyttää yhtä pakkausmuotoa kaikille kanaville.




Pagination
Previous page
NewActiIPCapture - Asennus ja käyttö
Next page
NewAxisIPCapture - Asennus ja käyttö