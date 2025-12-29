# NewSiquraIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/newsiquraipcapture-asennus-ja-kaytto

NewSiquraIPCapture - Asennus ja käyttö

Kaikissa pakkaustiloissa ohjain käyttää videon vastaanottoon RTSP/RTP/UDP/IP-protokollia. HTTP-protokollaa käytetään parametrien asettamiseen/hakuun ja PTZ-toimintoihin.

Jos VMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP-portit on avattava:

HTTP: oletusportti on 80,

RTSP: oletusportti on portti 554,

UDP: tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3556-4556.

Esimerkiksi: jos DVMS:ssä on neljä Siqura-koodekkia, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se jätetään käyttämättä.

Rajoitukset

H.264-dekooderi saattaa joskus epäonnistua vastaanotetun kuvakehyksen dekoodaamisessa ja aiheuttaa virheen DVR-lokitiedostoon.

Joskus analoginen dome-kamera ei käsittele PTZ-komentoja. Esimerkiksi kupukamera ei joskus pysähdy ohjauksen lopettamisen jälkeen tai ei liiku äkillisen suunnanmuutoksen jälkeen. Lisäksi toinen HTTP-komento, jossa on samat parametrit, jätetään huomiotta, kunnes vastaanotetaan HTTP-komento, jossa on eri parametri. Kyseessä on todennäköisesti Siqura-videopalvelimen ominaisuus.

Siqura MD2x/HD2x -kameroiden MJPEG-video pysähtyy hetkeksi suoran lähetyksen aikana. Näyttää siltä, että yksi ruutu jää väliin. Sama tapahtuu myös Web-käyttöliittymässä. Tämä on kameran ongelma.

Siqura MD2x -kamerat, joissa on vanha laitteistokanta, eivät tue Output-toimintoa. Ajuri ei pysty havaitsemaan laitteistotietoja, joten DVMS:ssä näkyy joka tapauksessa ulostulo.

Siqura-laitteet eivät tue jatkuvaa iiriksen vaihtamista - tämä on laiteohjelmiston ominaisuus.

Kaikki esiasetetut komennot, jotka on kuvattu MD2x/MD6x/HD2x/HD6x-protokollassa (tiedostonimi ”NKF - Protocol Hotkey 20090805”) komentoina kameran erikoistoimintojen käyttämiseksi, poistetaan käytöstä PTZ-moduulissa. Siqura PTZ-kameroiden tuettu esiasetusmäärä on siis alle 256.

Siqura PTZ-kameroiden MJPEG-kooderi toimii alhaisemmalla prioriteetilla kuin muut kooderit (MPEG-4 ja H.264). Todelliset ruutunopeusarvot voivat siis olla pienempiä kuin MJPEG HTTP -kanavalle vaaditaan, erityisesti heikossa valaistuksessa.

Ohjain tallentaa prepositioiden nimet XML-tiedostoon. Unicode-esimerkkien nimiä tuetaan ajuriversiosta 1.9.2.0 lähtien.




Pagination
Previous page
NewSamsungIPCapture - Asennus ja käyttö
Next page
NewSonyIPCapture - Asennus ja käyttö