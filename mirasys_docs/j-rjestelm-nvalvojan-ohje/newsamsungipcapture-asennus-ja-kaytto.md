# NewSamsungIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/newsamsungipcapture-asennus-ja-kaytto

NewSamsungIPCapture - Asennus ja käyttö

Kaikissa pakkaustiloissa ohjain käyttää videon vastaanottoon RTSP/RTP/UDP/IP-protokollia. HTTP/HTTPS-protokollia käytetään parametrien asettamiseen/hakuun.

Jos VMS:n ja kameroiden välillä on palomuuri, seuraavat portit on avattava:

HTTP: oletusportti on 80,

HTTPS: oletusportti on 443,

RTSP: portti 554,

UDP: tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3556-4556.

Esimerkiksi: jos VMS:ssä on neljä Samsungin IP-kameraa, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se jätetään käyttämättä.

NewSamsungIPCapture.xml-tiedostoa käytetään:

Kuljettajan käyttäytymisen määrittäminen:

Unicast

Multicast:Primary

Multicast:Listener

Videokanavien asetukset:

Video channel protocol (RTP over UDP, RTP over RTSP)

Bitrate mode (CBR/VBR)

Rajoitukset

Samsung-kameroiden ominaisuuksia ei voida hakea aikaisemmista laiteohjelmistoversioista. Näiden kameroiden kaikki kameran ominaisuudet (lukuun ottamatta kameran mallinimeä) on koodattu ohjaimeen. Kaikki kamerat on siis päivitettävä uusimpaan laiteohjelmistoversioon.

Samsungin kamerat eivät tue tulojen konfigurointia CGI-komennoilla. Tulo on oletusarvoisesti konfiguroitu ”pois käytöstä”. Aseta tulon konfigurointi ”NO” (eli ”Normal Open”) web-käyttöliittymässä ennen kameran lisäämistä VMS:ään.

Samsung-kameran kuvataajuus voi poiketa asetuksista (+/- 3 kuvaa/s).

Ajuri tallentaa esiasetusten nimet XML-tiedostoon (Unicode-nimet tuetaan).

Samsungin PTZ-laitteet eivät tue nopeusparametria ”Siirry esiasetukseen” -komentoa varten. Siirry esiasetukseen -nopeus on siis aina sama.

Samsung-kamerat soveltavat kutakin yksityisyysvyöhykkeen konfiguraatiota erillisellä pyynnöllä (lisää/poista). Vyöhykkeen sijainnin muuttamiseksi on poistettava edellinen konfiguraatio ja lisättävä uusi sijainti eri pyynnöillä. Kamera käsittelee jokaisen lisäys-/poistopyynnön 0,6-0,8 sekunnin aikana. Näin ollen 10 yksityisyysvyöhykkeen sijainnin päivittäminen voi kestää 16 sekuntia.

Lopetettujen kameroiden aikavyöhykkeet saatetaan asettaa väärin aikasynkronoinnin aikana.

Käyttäjän on määritettävä IP-laite manuaalisesti seuraavasti, jos käyttäjä haluaa käyttää Edge-tallennusominaisuutta:

Ei ole mitään mahdollisuutta tietää, onko jokin tiedosto kirjoitushetkellä. Älä siis aseta Post-Alarm duration -vaihtoehtoa pitkiksi aikarajoituksiksi, sillä se voi johtaa siihen, että ajuri ohittaa tämän aikavälin.

On suositeltavaa kytkeä pois päältä ”Record 1 fps forcibly” -vaihtoehto. Tämä vaihtoehto voi kuitenkin olla poissa käytöstä joissakin tallennetun profiilin asetuksissa (katso lisätietoja kameran käyttöoppaasta). Tässä tapauksessa voit käyttää erillistä videoprofiilia videon tallentamiseen HD- ja Full-HD-kameroille.

On suositeltavaa käyttää automaattista SD-puhdistusta, jotta videotallennuksille jää tarvittava tila.

Samsungin 7000-sarjan kameroissa on ongelma videodatan tallentamisessa tapahtumittain. Kamera ei tallenna mitään, vaikka tallentamiseen määritetyt tapahtumat ovat saaneet signaalin. Kamera aloittaa videon kirjoittamisen uudelleenkäynnistyksen jälkeen tai joskus kameran asetusten palauttamisen jälkeen tehdasasetuksiin. Tämä on kameran ongelma.

Vanhat Samsungin kameramallit, kuten SNP-570 ja SND-460, jotka käyttävät STW SDK:ta (STW-kamerat seuraavissa huomautuksissa) ja joiden laiteohjelmistoversio on ennen 1.3.5:tä, eivät tue kameran ominaisuuksien hakemista. Nämä kamerat tunnistetaan ”Samsung IP-kameraksi” ja ne toimivat vain PAL-videotilassa.

Samsungin STW-kamerat eivät tue komentoa ”switch output off”. Kamera kytkee lähdöt automaattisesti pois päältä Web-käyttöliittymän lähtöasetusten mukaisesti.

Samsungin STW-kamerat lähettävät MPEG-4-striimiä 12,5 FPS:n nopeudella 10 ja 15 FPS-asetuksilla.

Samsung STW -kamerat pienentävät MPEG-4-koodekin videolaatuarvoa automaattisesti liikkeen aikana. Tämä on kameran ominaisuus (Samsung Techwin Supportin tietojen mukaan).

Kuvataajuus vaihtelee MPEG-4-pakkaustilassa Samsung STW -kameroissa. Tämä johtuu RTP-pakettien vastaanottamisesta väärällä järjestysnumerolla. Tämä on kameran ongelma.

Samsung STW -kameroiden videovirrassa on FPS-vaihtelua, jos kameran valotusasetukset ovat virheelliset. Voit korjata asetukset käyttämällä Web-käyttöliittymän Live View -sivun ”Camera Setup” -painiketta.

Samsungin STW-kamerat siirtyvät käytöstä poistettuun tilaan (palauttaa HTTP-vastauksen tilakoodilla 500 kaikille pyynnöille) sen jälkeen, kun yhteys oli katkennut lyhyeksi ajaksi ja sitten palautunut. Ongelma toistuu 30 prosentin todennäköisyydellä vain MJPEG-koodekilla.

FPS-asetuksia sovelletaan virheellisesti MJPEG-videovirtaan. Tämä kameran ongelma koskee Samsungin STW-kameroita, joissa on laiteohjelmiston versio 1.3.5 tai aikaisempi. MJPEG-videovirran todellinen FPS saattaa siis olla vaadittua alhaisempi.

MJPEG-videovirta pysähtyy pitkän työskentelyajan jälkeen (esimerkiksi yön yli kestävien testien aikana). Tämä johtuu siitä, että kamera palauttaa HTTP-vastauksiin tilakoodin 500 kaikille pyynnöille. Tässä tapauksessa kamera on käynnistettävä uudelleen manuaalisesti. Tämä ongelma koskee Samsung STW -kameroita.

SNP-1000A-kamera lähettää MJPEG-virran 8-9 FPS:n nopeudella 10 FPS- ja D1-resoluutioasetuksilla. Tämä on firmware-ongelma.

SNP-1000A-kamera lakkaa käsittelemästä HTTP-pyyntöjä verkkoyhteyden katkeamisen ja palauttamisen jälkeen (esimerkiksi sen jälkeen, kun ”Ei signaalia” on ollut 2 minuutin ajan). Tämä johtuu siitä, että kamera palauttaa HTTP-vastauksiin tilakoodin 403 kaikille pyynnöille. Tässä tapauksessa kamera on käynnistettävä uudelleen manuaalisesti.

SNP-1000A- ja SNC-550-kamerat eivät tue MPEG-4 RTP-palveluja. Vain MJPEG-videovirta on käytettävissä näissä kameroissa.

SNP-1000A-kamera kääntyy 0 asteen ja 350 asteen välillä. Aste-arvot välillä 351-359 eivät ole käytettävissä - tämä on kameran ominaisuus.

SNP-1000A-kamera ei tue jatkuvia liikekomentoja. Ajuri toteuttaa jatkuvan liikkeen mekanismin emuloinnin. Tämä mekanismi vähentää seuraavat ongelmat:

Kameran liikuttelu on huomaamatonta.

MJPEG-stream pysähtyy joskus muutamaksi sekunniksi kameran liikkuessa suurimmalla nopeudella. Todennäköisesti kameran laiteohjelmisto ei pysty käsittelemään videovirtaa ja monia liikkumiskomentoja samanaikaisesti.

Kamera liikkuu virheellisesti ala-asennossa, kun yritetään siirtää alaspäin. Kamera kääntää pystysuuntaisen mittakaavan ja liikkuu ylöspäin, jos komento ”move down” vastaanotetaan ja kamera kulkee ala-asennon läpi. Seuraava ”siirry alas” -käsky ei kuitenkaan käännä mittakaavaa ja kamera siirtyy jälleen ala-asentoon.Preposition storing does not work for SNP-1000A camera with current firmware version. Firmware update is required.

7002-sarjan kameroissa on rajoitus aktiivisten profiilien lukumäärälle. Aktiivisten videovirtojen määrä on rajoitettu kahteen, jos kukin niistä käyttää 1024x768 tai suurempaa resoluutiota. Monivirtausominaisuus ei siis välttämättä toimi oikein näissä kameroissa.

Ajuri tukee vain G.711-äänenkoodausta. G.711-koodaus on siis valittava manuaalisesti Web-käyttöliittymän kautta, jos kamera tukee useampaa kuin yhtä äänikoodausta.

VMS ei tue PTZ-kameroiden yksityisyysvyöhykkeitä. Yksityisyysvyöhyketuki havaitaan, jos kamera ei tue panorointi-/kallistusliikettä.

Samsungin laitteissa, joissa on WR3.0-ohjelmistoalustaversio, on ongelma SSL-toteutuksessa, joka ei salli POST-komentojen käyttöä. Tämän seurauksena yksityisyysvyöhykkeet-toimintoa ei voi käyttää, kun HTTPS-tuki on aktivoitu. Samsung lupasi korjata asian seuraavassa laiteohjelmistoversiossa.

Samsungin laitteet, joissa on WR3.0-ohjelmistoalustaversio, lähettävät videovirran alhaisella kuvataajuudella (esimerkiksi 2-3 sovelletun 20:n sijasta), jos äänivirta on tilattu ennen videovirtaa. Tämä käyttäytyminen johtuu kameran RTSP-moduulin toteutuksesta. Tallenna kameran asetukset uudelleen ilman muutoksia, jotta kamera palaa normaaliin suoratoistotilaan.

Jos käytetään vakio-bittinopeusasetuksia (CBR) Samsung-laitteissa, joissa on profiilituki, VMS-laatu muunnetaan bittinopeusasetuksiksi prosentteina käyttäen seuraavia rajoja:

2Mbps - 15Mbps resoluution leveyden ollessa 1600px tai suurempi;

1024Kbps - 10Mbps resoluution leveydelle 1024px - 1600px;

512Kbps - 5Mbps, kun resoluution leveys on 640px - 1024px;

64Kbps - 2Mbps, kun resoluution leveys on alle 640px.

Oikea VMS-laatu olisi asetettava vastaamaan vaadittua verkon kaistanleveyttä. Muut kamerat käyttävät vakiolaatuasetuksia, eivät bittinopeutta.

Bittinopeus voidaan rajoittaa 6 Mbps:iin, jos videoprofiili on määritetty tallennustilassa sisäiselle flash-kortille (Edge Storage). Ajuri ei muuta GOP-koon arvoa videoprofiileille, jotka on määritetty tallennustilaan. Välttääksesi tämän rajoituksen määritä erillinen profiili sisäistä tallennusmateriaalia varten kameran Web-käyttöliittymän avulla (kohdassa ”Videoprofiili”).

VBR:n käyttäminen äänen ja usean suoratoiston kanssa edellyttää, että kamerassa on firmaware 2.x tai uudempi versio. Vanhalla laiteohjelmistolla video ei toimi monivirtausta varten.

Multicast ei ole käytössä Samsungin malleissa, joissa on vanha SDK (ei-profiilikamerat). Kaikki nämä mallit toimivat vain Unicastilla. Näitä kameroita ei voi käyttää useissa VMS-instansseissa!

Unicast-tila: Ajuri muuttaa kameran asetuksia VMS-asetusten mukaisesti ja vastaanottaa ääni- ja videotiedot kamerasta unicast-yhteyden avulla.

Multicast: Ensisijainen: Ajuri muuttaa kameran asetuksia VMS-asetusten mukaisesti ja vastaanottaa ääni- ja videodataa kamerasta multicast-yhteyttä käyttäen.

Multicast:Kuuntelija: Ohjain ei muuta seuraavia kameran asetuksia:

Laatu

Resoluutio

Framerate

Multicast:Listener -kohdassa seuraavat asetukset määritetään samalla tavalla kuin Multicast:Primary -kohdassa:

Multiple streaming -vaihtoehto

Videokoodekki kaikille lähetyksille

Jos kameraa on tarkoitus käyttää useissa VMS-instansseissa, yhden VMS:n asetukseksi on määritettävä Multicast:Primary ja muiden Multicast:Listener.

Useita Multicast:Primary -konfiguraatioita tai Multicast:Primary- ja Unicast-konfiguraatioita ei sallita, sillä muussa tapauksessa kamera olisi ylikuormitettu jatkuvilla samanaikaisilla asetusten muutoksilla.

Multicast-osoite ja -portti on asetettava kullekin profiilille kameran Web-käyttöliittymässä, tai multicast ei toimi. Kun moninkertainen suoratoisto on käytössä, ohjain luo MLIVE-profiilin - monilähetysosoite ja -portti on asetettava myös siihen.

Alueen zoomaus- ja keskitystoiminnot ovat käytettävissä Samsungin kameroissa, joissa on SUN API 2.0 -tuki.

Iiriksen vaihtaminen on hidasta kameran rajoituksen vuoksi). Yksi napsautus - yksi muutos.

Kun kameraa siirretään (tai zoomataan), automaattinen iiris ja automaattitarkennus otetaan käyttöön.

Audio in Edge -ominaisuuden tukeminen edellyttää VMS-version 7.4.3.71 tai uudempaa versiota.

Uusissa kamerasarjoissa (kuten QNO/QNV/QND-7010R-näytteissä) on rajoituksia 2 megapikselin ja sitä suurempien resoluutioiden käyttämiselle H.264-virroissa:

Yli 2 megapikselin resoluutiot ( 2592x1520 / 2560x1440 / 2304x1296) Maksimikuvanopeus jaetaan aktiivisten virtojen määrän kesken:

20 fps / 2 streamia = 10 fps per stream;

20 fps / 3 streamia = 6 fps per stream.

Yksi yli 2 megapikselin stream + 2 megapikselin stream:

15 kuvaa sekunnissa per stream kaksoissuoratoistokokoonpanoissa (esimerkki: 2592x1520 @ 20 kuvaa sekunnissa + 1920x1080 @ 20 kuvaa sekunnissa).

10 kuvaa sekunnissa per stream kolminkertaisessa streaming-kokoonpanossa (esimerkki: 2592x1520 @ 20 fps + 1920x1080 @ 20 fps + 1920x1080 @ 20 fps).

Vain 2MP (1920x1080) -videovirrat:

Ei rajoituksia 2 streamille (20 fps per stream).

15 kuvaa sekunnissa per stream 3 streamin osalta

Vaihtoehdon vaihtaminen hälytyksen (CCFiA/CCRiA) perusteella on käytettävissä laitteissa, jotka mahdollistavat vaihtoehdot nopeammin kuin 2 sekuntia. Ennen vuotta 2015 julkaistut laitteet eivät tue tätä toimintoa.

Windows XP:tä ei tueta ajuriversiosta 2.2.18.1 lähtien.




Pagination
Previous page
NewPanasonicIPCapture - Asennus ja käyttö
Next page
NewSiquraIPCapture - Asennus ja käyttö