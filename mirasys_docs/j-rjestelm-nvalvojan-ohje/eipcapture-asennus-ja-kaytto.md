# EIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/eipcapture-asennus-ja-kaytto

EIPCapture - Asennus ja käyttö

Ajuri käyttää RTSP/RTP/UDP/IP-protokollia videon vastaanottoon kaikissa pakkaustiloissa.

HTTP-protokollaa käytetään parametrien asettamiseen/hakuun.

Jos VMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP-portit on avattava:

HTTP: oletusportti on 80,

RTSP: portti 554,

UDP: tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3556-4556.

Esimerkiksi: jos DVMS:ssä on 4 El.MO- tai Dynacolor IP-kameraa, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se ohitetaan.

Rajoitukset

WinInet-kirjastoa käytetään HTTP-tietojen lähettämiseen/vastaanottamiseen DVMS:n ja e-Vision/Dynacolor-kameran välillä. Tämän kirjaston 8.0-versiossa on rajoitus: vain 2 HTTP-yhteyttä voidaan avata samanaikaisesti (katso seuraava artikkeli: http://support.microsoft.com/kb/183110).> Tämä ongelma tulee ajankohtaiseksi, kun Internet Explorer on päivitetty 8.0:aan tai uudempaan versioon.

Jos kameran Web-käyttöliittymä avataan samalla tietokoneella, jossa tätä ohjainta käytetään, muutamia HTTP-pyyntöjä ei ehkä lähetetä tämän rajoituksen vuoksi. Tällöin automaattinen haku ei ehkä löydä kameraa, tai jotkin toiminnot eivät ehkä toimi lainkaan.

”Video OCX protocol” -vaihtoehto on asetettava ‘RTP over UDP’ (tai ‘RTP over RTSP(TCP)’ joissakin tapauksissa), jotta RTP/RTSP-videovirta saadaan vastaanotettua oikein. Tätä vaihtoehtoa ei voi asettaa CGI-pyynnön kautta, joten aseta se manuaalisesti Web-käyttöliittymän kautta (Streaming-välilehti) ennen kameran käyttöä.

El.MO- ja Dynacolor-kameroilla (lukuun ottamatta Dynacolor HD WDR IP -kameroita) on erityiset resoluutioasetukset. Kamera saattaa tukea eri koodekkien eri resoluutioita. Esimerkiksi NH-sarjan kamerat tukevat seuraavia resoluutioita (enimmäiskuvanopeus on kuvattu suluissa):

MJPEG video codec - 1280x960(12.5 fps), 640x480(25 fps);

MPEG4 video codec - 640x480(25 fps), 320x240(12.5 fps), 352x288(12.5 fps), 176x144(12.5 fps).

Kun yrität asettaa tukematonta resoluutiota, käytetään sopivinta resoluutiota. Katso yksityiskohtaiset tiedot kameran tuetuista resoluutioista kameran asetuksista (Streaming -> Video Format -sivu, kohta ”Video Resolution”).

El.MO- ja Dynacolor-kamerat tukevat vain yhtä tai kahta kuvanopeutta (esimerkiksi 25 tai 12,5 NH-sarjan PAL-kameroissa). Muita kuvataajuuksia voidaan käyttää ”Frame Skip” -asetuksella. Yleensä kamera tukee sisäisesti 5, 10 ja 15 kuvan ohitusta. Jos kamera tukee 25 kuvaa/s tietyllä resoluutiolla, kamera lähettää virran, jossa on 5, 2,5 ja 1,67 kuvaa/s asianmukaisilla kuvan ohitusasetuksilla. Todellinen ruutunopeus voi siis olla suurempi kuin VMS:ssä käytetty, kun yrität asettaa tukematonta ruutunopeutta. Käytetään sopivinta arvoa.

NH-sarjan kameroiden videovirrassa on VGA-resoluutiolla epätasainen kuvataajuus korkeimmalla kuvataajuudella ja laatuasetuksilla (sekä MPEG-4- että MJPEG-koodekit). Todellinen kuvataajuus vaihtelee 18 ja 30 arvon välillä, mutta keskimääräinen kuvataajuusarvo on 1-2 kuvaa sekunnissa vaadittua pienempi. Tämä johtuu kamerasta.

Dynacolor- ja El.MO-kamerat soveltavat jokaista virtausasetuksia koskevaa pyyntöä noin 20 sekunnin kuluessa. Tämä on kameran ominaisuus.

IP PTZ -kameroissa on seuraavat ongelmat:

Kamera palauttaa aina HTTP-virhekoodin 503 jokaisesta IO-komennosta - tämä on laiteohjelmiston ongelma. IO-moduuli on tilapäisesti poistettu käytöstä IP PTZ -sarjan kameroissa.

Kamera kääntää ”tarkennus”-komennon toisinpäin: se suorittaa ”tarkenna lähelle”-toiminnon ”tarkenna kauas”-komennolle ja päinvastoin. Tämä on laiteohjelmiston ongelma.

Kamera ei palauta yhteyttä verkkokaapelin irrottamisen jälkeen. Kun yhteys on palautettu, kamera on käynnistettävä uudelleen manuaalisesti.

HD WDR IP -kameroissa on seuraavat ongelmat:

Kamera lähettää MPEG-4-kuvia vaadittua suuremmalla kuvataajuudella. Kamera voi esimerkiksi lähettää jopa 16 kuvaa sekunnissa maksimiresoluutiolla (1280x960) 12,5:n sijasta.

Kamera ei tue H.264-koodekin enimmäistarkkuuden (1280x960) Frame Skipping -toimintoa. Tämä on kameran ominaisuus. Tämän seurauksena H.264-koodekin enimmäistarkkuudelle on käytettävissä vain yksi kuvanopeus (maksimi, 25 tai 30 kuvaa/s).

V-sarjan kameroissa on ongelma H.264-koodekin kanssa. Kun H.264-koodekin 100 %:n laatua on sovellettu, kamera lähettää virheellisen videovirran (VLC-soitin ei toista sitä, ja VMS näyttää paljon ruutujen ohitusviestejä). Tätä ongelmaa esiintyy satunnaisesti.

5 megapikselin 360∞-kalansilmäkamerat tukevat vain kalansilmäkuvia. Tällä hetkellä ne eivät tue toisen katselualueen valitsemista.

Useita suoratoiston rajoituksia:

DVMS 6.1.1:stä alkaen Full-HD Quad Stream -kameroille on tarjolla useita suoratoisto-ominaisuuksia. Muita kameroita käytetään yhden striimin laitteina.

Tallennus ja suorat lähetykset tukevat vain H.264-koodausta. Kaukovirta tukee sekä MJPEG- että H.264-koodausta.

Eri virtojen resoluutiot riippuvat toisistaan. Resoluutioon sovelletaan seuraavaa sääntöä: Live-virran resoluutio ei voi olla suurempi kuin tallentavan virran resoluutio. Sama sääntö koskee etä- ja suoratoistovirtoja. Lisätietoja näistä resoluutiorajoituksista on laitteen käyttöoppaassa tai Web-käyttöliittymässä.







Pagination
Previous page
EHIIPCapture - Asennus ja käyttö
Next page
GatewayIPCapture - Asennus ja käyttö