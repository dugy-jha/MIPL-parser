# NewMobotixIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/newmobotixipcapture-asennus-ja-kaytto

NewMobotixIPCapture - Asennus ja käyttö

Kaikissa pakkaustiloissa ohjain käyttää HTTP-protokollaa videon vastaanottoon ja parametrien asettamiseen/palauttamiseen.

Jos DVMS:n ja kameroiden välillä on palomuuri, seuraavat portit on avattava: HTTP: oletusportti on 80.

Rajoitukset

Todellinen FPS on rajoitettu resoluutioasetuksilla (kameran ominaisuus): suuremmilla resoluutioilla on alhaisemmat todelliset fps-arvot. Esimerkiksi 800x600-resoluutiolla maksimi FPS on 9 MJPEG-koodekilla.

Äänitiedot voidaan vastaanottaa osana MxPEG-kehystä HTTP API -dokumentaation mukaisesti. Äänivirta ei siis ole käytettävissä MJPEG-virrassa.

Stream-tila muutettiin ”fast”-tilasta manuaaliseksi - tätä asetusta voidaan muuttaa web-käyttöliittymässä.




Pagination
Previous page
NewIQEyeIPCapture - Asennus ja käyttö
Next page
NewPanasonicIPCapture - Asennus ja käyttö