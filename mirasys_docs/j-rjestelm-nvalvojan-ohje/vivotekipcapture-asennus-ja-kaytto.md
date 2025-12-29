# VivotekIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/vivotekipcapture-asennus-ja-kaytto

VivotekIPCapture - Asennus ja käyttö

Kaikissa pakkaustiloissa ohjain käyttää RTSP/RTP/UDP/IP-protokollia videon vastaanottamiseen. HTTP-protokollaa käytetään parametrien asettamiseen/hakuun.

Jos VMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP-portit on avattava:

HTTP: oletusportti on 80,

RTSP: portti 554,

UDP: tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3556-4556.

Esimerkiksi: jos VMS:ssä on neljä Vivotek IP-kameraa, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se jätetään käyttämättä.

Rajoitukset

Joskus kamera siirtyy ”vain HTTP” -tilaan verkkokapasiteettien havaintomekanismin (kameran sisäinen mekanismi) mukaan. Palauttaakseen kameran ”RTP”-tilaan se on käynnistettävä uudelleen.

Kamera ohittaa kanava-asetukset, kun se siirtyy tilasta ”quality priority” tilaan ”frame rate priority” tilaan. Videotila voidaan asettaa ohjaimen XML-tiedostossa.

Korkean resoluution oletuskatselumaskissa ei näy koko kuva. Se voidaan määrittää Web-käyttöliittymän avulla.

Suurten resoluutioiden enimmäiskuvanopeus on ilmoitettua alhaisempi.

Testatussa SD7323-kamerassa iiriksen muuttamista koskevat komennot eivät toimi.

AAC-äänen purku on tuettu VMS 7.4.4:stä tai uudemmasta versiosta alkaen.

Sony H-sarjan laitteet (kuten SNC-HM662-kamera) käyttävät Vivotek OEM SDK:ta toisin kuin muut Sony G6 -kamerat. Näihin laitteisiin tulisi käyttää Vivotekin natiiviohjainta Sonyn natiivin ohjaimen sijaan.

Windows XP:tä ei tueta ajuriversiosta 1.6.1.0 lähtien.

CCRiA- ja CCFiA-ominaisuudet käytettävissä vain laitteissa, jotka ovat 8xxx-sarjan tai uudemman sarjan laitteita.

Kun resoluutiota muutetaan hälytyksellä, käyttäjä voi nähdä yhden virheellisen kuvan. Tämä on laitteen ongelma - kamera lähettää yhden virheellisen kehyksen - eikä ohjain voi ohittaa sitä, koska kaikki otsikot näyttävät olevan kunnossa.

Pagination
Previous page
StanleyIPCapture - Asennus ja käyttö
Next page
WisenetIPCapture - Asennus ja käyttö