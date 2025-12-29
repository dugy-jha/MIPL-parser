# PSIAIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/psiaipcapture-asennus-ja-kaytto

PSIAIPCapture - Asennus ja käyttö

Kaikissa pakkaustiloissa ohjain käyttää RTSP/RTP/UDP/IP-protokollia videon vastaanottamiseen. HTTP-protokollaa käytetään parametrien asettamiseen/hakuun.

Jos VMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP-portit on avattava:

HTTP: oletusportti on 80,

RTSP: portti 554,

UDP: tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3556-4556.

Esimerkiksi: jos VMS:ssä on neljä kameraa, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se ohitetaan.

Rajoitukset

Vain ensisijainen videokanava on tuettu (jos kamerassa on useita kanavia).

Pagination
Previous page
PelcoIPCapture - Asennus ja käyttö
Next page
RTSPIPCapture - Asennus ja käyttö