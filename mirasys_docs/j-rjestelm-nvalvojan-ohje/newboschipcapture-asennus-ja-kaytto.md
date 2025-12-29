# NewBoschIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/newboschipcapture-asennus-ja-kaytto

NewBoschIPCapture - Asennus ja käyttö

Jos VMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP- tai HTTPS-portit on avattava:

HTTP: oletusportti on 80,

HTTPS: oletusportti on 443,

RTSP: oletusportti on 554,

UDP: video-/äänivirtaa kohden tarvitaan kaksi peräkkäistä porttia porttialueella 3556-4556.

Jos DVMS:ssä on esimerkiksi neljä IP-kameraa, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se jätetään käyttämättä.

MPEG-4-videovirran vastaanottoajuri käyttää Bosch RCP+ SDK -kirjastoa. Se avaa satunnaisia UDP-portteja videodatan vastaanottoa varten. Ajuri voidaan määrittää XML-konfigurointitiedoston avulla seuraavien parametrien asettamiseksi Bosch IP -laitteille:

PTZ protocol (PelcoD, OSRD, BiCom)

Kalansilmävideokanava (vain yhtä voi käyttää)

Jpeg-stream (tallennus, live tai etäyhteys, oletuksena etäyhteys)

Edge-tallennustoimintojen tuki

Aikasynkronointi (käytössä / pois käytöstä)

Ohjaustila (aktiivinen/passiivinen)

Liikenne

Avainkehyksen väli

Videohäviön tarkistus (käytössä / pois käytöstä)

Rajoitukset

Kaikille Bosch-laitteille on määritettävä käyttäjä ja salasana. Muussa tapauksessa ajurit eivät tunnista kameraa (salasana ei saa olla tyhjä).

Järjestelmänhallinta voi päivittää ajurin versioon 1.3.0.0 vanhemmista versioista, joissa on tilattuja Bosch-kameroita VMS 7.0 -versiosta alkaen. Vanhemmissa VMS-versioissa kamerat on poistettava DVMS:stä ja lisättävä uudelleen ajuripäivitysten jälkeen.

Jos kamera on lisätty ilman äänikanavia, niiden ottamiseksi käyttöön kamera on myös poistettava ja lisättävä uudelleen DVMS:ään.

Ajuri ei poista tai muuta vanhaa BoschIPCapture-ajuria, mutta se käyttää rcpp.dll-tiedostoa kuten vanha ajuri.

Ajurin asentamiseksi ei siis pitäisi olla kytkettyjä Bosch-kameroita. Muuten ajurin asennus epäonnistuu.

Video-Jet-palvelinsarjaan MPEG-4-koodekkia varten liitettyjen NTSC-kameroiden enimmäisresoluutio on 352x240 (CIF). D1-resoluutio ei toimi, joten CIF-resoluutio näytetään D1:n sijasta.

Yhteen Video Jet -palvelimeen liitettyjen NTSC- ja PAL-kameroiden yhdistelmä on kielletty.

MJPEG-videokanavan todellinen kuvanopeus voi olla pienempi kuin asetuksissa määritetyt arvot.

VMS:n laatuasetus käyttää kameran tai videopalvelimen bittinopeusarvoa. Todellinen kuvanlaatu voi siis olla sama eri arvoilla (jos kehys voi läpäistä määritetyt bittinopeudet).

Boschin PTZ-kamerat käyttävät OSRD-protokollaa kameran ohjaamiseen. Tämä protokolla ei salli iiris-/tarkennusnopeuden muuttamista. Iirisointi ja tarkennus voidaan siis suorittaa ennalta määritetyllä nopeusarvolla. Nopeusarvot voidaan asettaa Web-käyttöliittymän kautta. VG4 AutoDome -kameran asetukset löytyvät täältä: Asetukset > Lisätila > Kamera > Objektiivi > Asetusryhmä 1.

OSRD-protokolla ei salli prepositioiden poistamista. Myöskään VG4-kamera ei salli olemassa olevan preposition uudelleenkirjoittamista ilman vahvistusta. Kamera näyttää ”Overwrite current scene?” -kysymyksen OSD-valikossa [Yes]- ja [No]-painikkeilla.

Tarkennuksen/riisin vaihtamista käytetään valinnan vahvistamiseen. Ohjain lähettää Iris-komennon esiasennon tallentamisen jälkeen, jotta käyttäjän ei tarvitse vahvistaa käsin esiasennon uudelleenkirjoitusta. Tässä algoritmissa on yksi ongelma: jos prepositio-paikka on tyhjä (ei vielä tallennettu), näet Iris-muutostekstin.

Boschin videopalvelimet välittävät PTZ-komentoja sarjaportin kautta kytkettyihin kameroihin. Kameran tunnusta ei voi määrittää palvelimen vakioasetusten kautta. Liitetyt kamerat on siis määritettävä oikein (kameran laitteistoasetukset) PTZ-ohjauksen mahdollistamiseksi:

PTZ-protokollan pitäisi olla Pelco-D

PTZ-kameran tunnisteen on oltava sama kuin videokanavan numero. Esimerkiksi toiseen videotuloon kytketyn kameran kameratunnisteen on oltava 2.

Muiden sarjaportin asetusten on oltava samat kuin palvelimen asetusten (baudinopeus, pariteettibitti, stopbitit jne.).

Boschin videopalvelimissa ei ole sisäistä PTZ-toimintoa. Se välittää vain komentoja niiden sarjaportteihin liitettyjen kameroiden kanssa. Ajuri ei siis pysty tunnistamaan sarjaporttikameraan liitettyä toimintoa ja sitä, onko se PTZ.

Kaikki palvelimen videokanavat näkyvät PTZ-kanavina tämän ominaisuuden ansiosta.

NBC255:n ja NVC255:n resoluutiot ovat VGA ja QVGA. DVMS näyttää sen sijaan D1- ja CIF-tarkkuudet. (Näitä malleja ei voi havaita laitteen ominaisuuksista).

Moninkertainen suoratoisto tapahtuu koodereiden ominaisuuksien mukaan.

Kullakin videokanavalla on kaksi kooderia, joissa on tuettujen resoluutioiden määrä, joten kaikki resoluutiot eivät ole käytettävissä tallentavissa ja suorissa lähetyksissä.

Joitakin resoluutioita tuetaan vain ensimmäisen ja toisen enkooderin erityisillä yhdistelmillä, joten Live-virran resoluutio voi poiketa asetuksista, jos sitä ei voi asettaa nykyisen Tallennuksen resoluution kanssa.

Etävirta on MJPEG; siinä on kaikki käytettävissä olevat resoluutiot.

Streaming-rajoitus

Jos haluat muuttaa H.264-resoluutiota ja kuvanopeutta toissijaiselle streamille, sinun on poistettava ”Kopioi Stream 1” -tila käytöstä Web-käyttöliittymässä (Asetukset -> Lisäasetukset -> Kamera -> Encoder Streams -> Stream 2 -> Ominaisuus EI ole ”Kopioi Stream 1” -tilassa ”Stream 2” -tilassa);

Useita resoluutioita ei ole mahdollista käyttää (kullakin videokanavalla on kaksi kooderia, joilla on eri tuetut resoluutiot);

Kaukovirta on MJPEG, jossa on kaikki käytettävissä olevat resoluutiot.

MJPEG usean suoratoiston tilassa ei toimi vanhoissa sarjoissa, joissa on laiteohjelmisto 4.x.

PTZ-kameroiden liikkeentunnistus on määritettävä kameran Web-sivulla jokaisen kameran liikkeen jälkeen (Bosch-rajoitus).

PTZ-kameroiden yksityisyysvyöhykkeitä ei tueta.

Kamerat, joissa on COM-portti, näkyvät DVMS:ssä PTZ-kameroina. Ne voidaan liittää PTZ-alustaan ja PTZ toimii.

Ajuri synkronoi PC:n ajan kameran kanssa käyttäen UTC-aikaa (GMT+00:00) Edge-Storage-toimintoa varten. Edge-Storage ei toimi oikein, jos aika vaihdetaan toiseen.

Edge-Storage-toiminto toimii vain kameran ja VMS:n välisissä verkkokatkostilanteissa.

  Jos VMS käynnistettiin uudelleen tai ohjain suljettiin - VMS ei vastaanota tallennettua videokuvaa kamerasta.

Kameran tallennus on myös määritettävä, jotta VMS:n Edge-Storage-toimintoa voidaan käyttää.

Multicast-kaappauksen rajoitukset

Ajuri-instanssi voidaan määrittää käytettäväksi aktiivisena tai passiivisena. Aktiivinen instanssi pystyy muuttamaan IP-laitteen asetuksia ja käyttämään lisätoimintoja. Passiiviset instanssit pystyvät vastaanottamaan videovirtoja ja äänivirtoja multicastin kautta ja käyttämään digitaalisia I/O-toimintoja.

Passiivinen ei muuta seuraavia kameran asetuksia:

Codec

Quality

Resolution

Framerate

    Kamera on lisättävä aktiiviseen tallentimeen ennen kuin sitä käytetään passiivisessa kokoonpanossa.

Käyttäjän on varmistettava, että vain yksi tallennin muuttaa kameran asetuksia. Muiden tallentimien, jotka käyttävät tätä kameraa, tulisi olla passiivisessa tilassa.

Sen verkkosovittimen IP-osoite, jonka kautta kamera on liitetty, on määritettävä, jotta multicast-suoratoisto voidaan vastaanottaa oikein, jos käytettävissä on useampi kuin yksi verkkosovitin. Windowsissa oletusasetukseksi merkittyä verkkosovitinta käytetään, jos mitään vaihtoehtoa ei ole määritetty. Äänikanavan verkkosovitin (jos tietokoneessa on useita verkkosovittimia) on määritettävä XML-tiedostossa, dynaamista käyttöliittymää sovelletaan vain videokanavaan.

Aikasynkronointi on poistettu käytöstä passiivisen ja reunavaraston osalta, eikä se ehkä toimi oikein.

Käytön tulisi taata aikasynkronointi PC:lle, jossa on aktiivitilan tallennin, ja PC:lle, jossa on passiivitilan tallennin.

Vanhoissa Bosch-sarjoissa, joissa on laiteohjelmisto 4.x, on seuraava rajoitus:

HTTPS-tila ei toimi

MJPEG multicast-tilassa ei toimi (vain JPEG-pyynnöt HTTP:n kautta).

Firmware 6.22:n yksityisyysvyöhykkeitä ei tueta.

Vanhat Bosch-sarjat (kuten Gen4) tekevät joskus ”automaattisen rajauksen”. Tämän prosessin aikana kamerasta tuleva virta ei ole sujuva.

Passiivisessa tilassa vanhat MPEG4-tuella varustetut kamerat on asetettava oikeaan pakkausmuotoon, tai näyttöön tulee ”Ei signaalia”.

Reunatallennuksen tallennus on asetettava kameran Web-käyttöliittymässä 1. reunatallennusvirraksi.

Bosch IP -laitteet eivät välttämättä palauta tietoja laitteen tallennustilaan tallennetuista ääniväleistä RCP+-pyyntöjen kautta (numerolla = 90 + kanavan ID). Tämän seurauksena Audio Edge -toiminto ei toimi oikein. Ongelmasta ilmoitettiin Boschin teknikoille (20/Nov/2019), mutta ratkaisua ei vielä ole.

Kaikki Bosch-kamerat eivät pysty havaitsemaan liikettä, joten kameran verkkosivulta on tarkistettava, tukeeko se liiketunnistusta vai ei.

Kameran käyttäminen suojatussa tilassa

Asenna varmenne kameraan ja tietokoneeseen, jossa on tallennin

Aseta RTP over HTTP -suoratoistotila kameran asetuksissa System Managerissa;

Aseta oikeat kameran tunnistetiedot (äänen lähettämistä varten kameraan, jos sitä ei tarvita - mitä tahansa tunnistetietoja voidaan käyttää, todennus tehdään varmenteen avulla); ääni kameraan ei ole suojattu, joten se tarvitsee oikeat tunnistetiedot toimiakseen.

H.264- ja H.265-tuella varustettu Bosch-kamera on asetettava vaaditulle koodekille ennen DVMS:ään lisäämistä, koska joillakin kameroilla on erilainen luettelo tuetuista resoluutioista / kuvataajuuksista kullekin koodekille.

Kameran tuetut resoluutiot riippuvat tällä hetkellä asetetusta koodekista (H.264 / H.265). Joten kamera lisätään tällä hetkellä valitulla koodekilla, DVMS ei muuta sitä kameran lisäämisen aikana.

Videokatkostarkistusta käytetään vain koodereissa, joissa on analogisia kameroita, jotta voidaan havaita, toimiiko kamera vai ei. Sitä ei tule käyttää muissa Bosch-laitteissa.

Jos äänikoodekki on vaihdettu, SD-kortti on alustettava, koska ohjain yrittää vastaanottaa ääntä nykyisillä asetuksilla. Jos kameraan on asetettu AAC, mutta tallennus on tehty G711:llä, reunaäänitietoja ei vastaanoteta oikein.

Jos käytetään useita suoratoistoja, kaikilla kanavilla on oltava sama koodekki (H.264 tai H.265), Bosch-kamerat eivät voi suoratoistaa molempia samaan aikaan.

Bosch-laitteet eivät käsittele RTSP PAUSE -komentoa oikein (jatkavat lähetystä sen jälkeen).

Käytämme siis RTSP TEARDOWN -käskyä pysäyttääksemme virran, jos liikettä ei tapahdu (kun kamerapohjainen MD on käytössä).




Pagination
Previous page
NewAxisIPCapture - Asennus ja käyttö
Next page
NewIQEyeIPCapture - Asennus ja käyttö