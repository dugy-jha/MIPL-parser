# LGEIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/lgeipcapture-asennus-ja-kaytto

LGEIPCapture - Asennus ja käyttö

Ajuri käyttää RTSP/RTP/UDP/IP-protokollia videovirtojen ja syöttötilojen vastaanottamiseen kaikissa pakkaustiloissa. HTTP-protokollaa käytetään parametrien asettamiseen/hakuun.

Jos DVMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP-portit on avattava:

HTTP: oletusportit ovat 80 ja 81,

RTSP: portti 554,

UDP: Tarvitaan kaksi peräkkäistä porttia per videovirta ja kaksi peräkkäistä porttia per metatietovirta (syöttötilat) porttialueella 3556-4556.

Jos DVMS:ssä on esimerkiksi kaksi LG Electronicsin IP-kameraa, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se ohitetaan.

Rajoitukset

Muutamat LG Electronicsin laitteet eivät salli laitteen mallin vastaanottamista. Näiden kameroiden mallinimi näkyy muodossa ”LG Electronics IP-kamera”.

LDW2010F-N-kamera lähettää QCIF-virran 160x112-resoluutiolla 176x112-resoluution sijaan. Tämä on kameran ominaisuus.

LG Electronics -laitteiden digitaalisissa lähdöissä on yksi erityispiirre: niissä on kestovaihtoehto, eikä niitä voi sulkea pitkäksi aikaa. Laite avaa lähdön automaattisesti, kun kestoaika on päättynyt.

SOAP API ei tue komentoja tarkennus- ja iiristilojen vaihtamiseksi automaattisen ja manuaalisen arvon välillä. Jos käyttäjä siis haluaa käyttää iiriksen/tarkennuksen säätöä DVMS:ssä, hänen on muutettava tämä arvo Web-käyttöliittymän kautta manuaaliseksi.




Pagination
Previous page
IPCameraCapture - Asennus ja käyttö
Next page
NewActiIPCapture - Asennus ja käyttö