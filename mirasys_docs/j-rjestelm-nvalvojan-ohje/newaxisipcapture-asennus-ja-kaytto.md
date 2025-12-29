# NewAxisIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/newaxisipcapture-asennus-ja-kaytto

NewAxisIPCapture - Asennus ja käyttö

Ohjain käyttää RTSP/HTTP/HTTPS/RTP/UDP/IP-protokollia monilähetysvirtojen ja H.264/MPEG-4-pakattujen unicast-virtojen vastaanottamiseen. HTTP-protokollaa käytetään myös parametrien asettamiseen/hakuun sekä äänivirran ja JPEG-videovirran vastaanottoon unicast-tilassa.

Jos DVMS:n ja kameroiden välissä on palomuuri, seuraavien RTSP/UDP/HTTP/HTTPS-porttien on oltava seuraavat avattava:

HTTP: Oletusportti on 80,

HTTPS: Oletusportti on 443,

RTSP: Oletusportti on 554,

UDP: Jokaista videovirtaa kohden tarvitaan kaksi peräkkäistä porttia porttialueella 3556-4556. Jos Multicast-tila on käytössä, on avattava kaksi peräkkäistä porttia audio-/videovirtaa kohden laitteen kokoonpanon mukaisesti.

Jos DVMS:ssä on esimerkiksi neljä IP-kameraa, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se jätetään käyttämättä. Portit 1024-1025 ja 1028-1029 on myös avattava alueen 3556-4556 lisäksi, jos laitetta käytetään Multicast-tilassa ja se on määritetty käyttämään 1024 porttia äänivirtaa varten ja 1028 porttia videovirtaa varten.

Ajuri voidaan määrittää XML-kokoonpanotiedoston avulla ottamaan käyttöön seuraavat toiminnot, jos Axis IP -laite tukee näitä toimintoja:

Multicast audio/video kaappaus

Axis Views

Jos käytät Axis LPR:ää ja sinulla on useita verkkosovittimia, sinun on asetettava oikea IP-osoite (osoitteet) konfigurointitiedostoon..

Rajoitukset

HTTPS (TLS) -tukea varten sinun on luotava ja asennettava CA-varmenne PC:n varmennepalveluun ja luotava varmenne kullekin kameralle Axisin oppaan avulla (”HowTo. AXIS Device Manager. HTTPS-varmenteen hallinta”).

AXIS-ajuri ei tue ”PTZ Control Queue” -vaihtoehtoa. Jos tämä vaihtoehto on käytössä, AXIS-laite havaitaan muuksi kuin PTZ-laitteeksi.

Yksityisyysvyöhykkeitä voidaan siirtää muutamalla pikselillä DVMS:ssä sovelletusta suorakulmiosta. Siirto riippuu kuvan kierto- ja peiliasetuksista (normaalia kuvaa siirretään oikealle). Tämä on kameran laiteohjelmiston ominaisuus.

Jos ”Kuvasuhteen korjaus” -vaihtoehto on käytössä Axis-laitteessa, todellinen kuvan resoluutio voi poiketa VMS:n resoluutiosta. Todellinen resoluutio on esimerkiksi 768x576, jos asetus on 704x576, tai 192x144, jos asetus on 176x144. Poista tämä vaihtoehto käytöstä, jos järjestelmäsi ei vaadi kuvasuhteen korjausta.

Jos verkkoyhteys katkeaa, P33-sarjan Axis-kamerat lähettävät muutaman sekunnin ajan videokuvaa eivätkä lähetä mitään 5-10 sekuntiin yhteyden palautumisen jälkeen. Tämä käyttäytyminen johtuu kameran DHCP-toteutuksesta. Käytä staattista IP-osoitetta välttääksesi tämän käyttäytymisen.

IP-laite on määritettävä manuaalisesti seuraavalla tavalla, jos haluat käyttää Edge-tallennusominaisuutta:

Kamerasta ei ole mahdollista vastaanottaa UTC-aikaa (Coordinated Universal Time), joten aikavyöhykkeeksi on asetettava ”GMT+0:00”. Myös kesäaikavaihtoehto on kytkettävä pois päältä.

Kameratapahtumat on määritettävä videotallennusta varten käyttäjän mieltymysten mukaisesti. Tapahtuman keston tulisi olla vähintään 3 sekuntia.

On suositeltavaa käyttää automaattista SD-puhdistusta, jotta videotallenteille jää riittävästi tilaa.

Kameran tallennustilassa olevissa videotallenteissa voi olla jopa 10-15 sekunnin pituisia aukkoja. Tämä on kameran ominaisuus, joten älä käytä videotallennuksen enimmäisasetuksia tällaisten aukkojen välttämiseksi.

Axis-monikatselukamerat (esim. M3007) voidaan määrittää vastaanottamaan videokuvaa tietystä videovirrasta XML-kokoonpanotiedoston avulla. Eri näkymillä on erilaiset ominaisuudet, joten kamera on tilattava uudelleen VMS:ään, jotta muuttuneet StreamConfiguration-asetukset voidaan ottaa käyttöön.

Yksityisyysvyöhykkeet-toimintoa voidaan käyttää, jos tallennuskanava käyttää ”Overview”-kalansilmänäkymää.

Muut näkymät eivät tue yksityisyyden suojaustoimintoa, koska nämä näkymät ovat ”Overview”-näkymän osia.

Multicast-kaappauksen rajoitukset

Axis IP -laitteet tukevat monilähetyskaappausta Stream Profiles -ominaisuuden avulla (laitteet, joissa on laiteohjelmistoversio 5.0 tai uudempi), ja ne voidaan määrittää XML-tiedoston avulla. Vanhemmat laitteet käyttävät aina unicast-suoratoistoa.

Stream Profiles -tuki voidaan tarkistaa Web-käyttöliittymän kautta: ”Video & Audio >> Stream Profiles” -osion pitäisi olla käytettävissä. Käyttäjä voi käyttää mitä tahansa olemassa olevaa profiilia multicast-suoratoistokonfigurointiin tai antaa järjestelmän luoda uuden profiilin. Katso lisätietoja XML-konfiguraatiotiedoston kohdasta ”MulticastProfiles”.

Älä käytä samaa stream-profiilia eri streameille - se voi aiheuttaa ristiriitoja videoasetusten sovelluksen aikana.

Multicast-kaappaus voidaan ottaa käyttöön XML-kokoonpanotiedoston kautta käyttämällä StreamingMode-vaihtoehtoa. Tämä vaihtoehto luetaan streamia käynnistettäessä, joten laitteen asetusten päivittäminen riittää, jotta muutettu StreamingMode-vaihtoehto otetaan käyttöön. Huomaa, että DVMS:ssä on optimointi kanavan uudelleenkäynnistystä varten versiosta 7.4.1 lähtien, joten tässä tapauksessa on muutettava yhtä kunkin kameran videovaihtoehdoista, jotta stream voidaan käynnistää uudelleen.

Ajuri-instanssi voidaan määrittää käytettäväksi ensisijaisena tai kuuntelijana. Ensisijainen instanssi pystyy muuttamaan IP-laitteen asetuksia ja käyttämään lisätoimintoja. Kuuntelijainstanssit pystyvät vastaanottamaan video- ja äänivirtoja multicastin avulla ja mahdollistavat digitaalisten I/O-toimintojen käytön.

Kuuntelijatallennin ei muuta mitään kameran puolella olevia asetuksia. Jos esimerkiksi kamerassa ei ole määritettyä profiilia, sitä ei luoda, eikä ohjain voi vastaanottaa videokuvaa. Kamera on lisättävä ensisijaiseen tallentimeen ennen kuin sitä käytetään kuuntelijakokoonpanossa.

Lisävirrat (Live ja Remote) ovat aktiivisia, jos ne on avattu vain asiakkaissa. Jotta voit käyttää päivitettyjä Multiple Streaming -asetuksia, sinun on käynnistettävä (tai pidettävä auki) nämä streamit ensisijaisessa tallentimessa sen jälkeen, kun stream-asetukset on muutettu DVMS:ssä. Muussa tapauksessa kamera ei voi käyttää uusimpia stream-asetuksia.

Hälytysominaisuuksien (CFiA/CRiA) Motion Detection and Change -vaihtoehtoa ei voi käyttää monilähetystilassa edellä mainittujen aikakatkaisuongelmien vuoksi.

Käyttäjien on varmistettava, että vain yksi tallennin muuttaa Axis IP -laitteiden asetuksia. Muiden tallentimien, jotka käyttävät tätä kameraa, on oltava kuuntelutilassa.

Axis-kamerat eivät välttämättä tue useampaa kuin yhtä monilähetysvirtaa, jos kamera on määritetty käyttämään tiettyä porttia monilähetystä varten (nollasta poikkeava ”Videoportti”-asetus ryhmässä ”Järjestelmäasetukset >> Verkko >> RTP”). Kamera palauttaa RTSP 461 ”Unsupported transport” -virheen virran käynnistysyritykselle, jos yksi monilähetysvirta on jo käynnistetty. Määritä automaattinen portin valinta (aseta ”Videoportti”-asetukseksi 0) välttääksesi tämän käyttäytymisen.

On suositeltavaa määrittää sen verkkosovittimen IP-osoite, jonka kautta kamera on liitetty, jotta multicast-suoratoisto voidaan vastaanottaa oikein, jos käytettävissä on useampi kuin yksi verkkosovitin.

Kukin Unicode-merkki tallennetaan symbolikoodina (esimerkiksi %u0227), ja sitä varten tarvitaan 6 tavua. Unicode-preposition nimen pituus voi siis olla vain 11 symbolia 64:n sijasta.

Axis P1428-E -kamera tukee vain kahta 4K-virtaa (3840x2160) samanaikaisesti. Vältä 4K-tarkkuuden käyttöä kaikissa streameissa monivirtaustoiminnossa ja minimoi niiden sääntöjen määrä, jotka käyttävät 4K-tarkkuutta SD-kortille tallentamiseen.

Ajuri mahdollistaa ohjaustilan vaihtamisen ”aktiivisen” ja ”passiivisen” välillä versiosta 2.5.5.0 lähtien. ”Passiivisessa” tilassa ohjain ei muuta mitään videoon liittyviä parametreja, joten tässä tilassa seuraavat toiminnot eivät toimi:

Yksityisyysvyöhykkeiden konfigurointi

Hälytysvaihtoehtojen muuttaminen (esim. CFiA/CRiA-toiminnot)

Jos kamera hyväksyy videoparametrit RTSP- tai HTTP-striimi-URI:n kautta, ohjain käynnistää striimin ilman niitä. Toisin sanoen käytetään Web-käyttöliittymän kautta käytettyjä stream-asetuksia.

Yksityisyysmaskien soveltaminen voi kestää kauan (jokaisen alueen luominen voi kestää jopa sekunnin), joten se voi hidastaa stream-käynnistystä. Videon tilaamisen nopeuttamiseksi ohjain soveltaa yksityisyysmaskeja videovirran käynnistyksen jälkeen.

Ajuriversioissa ennen 2.5.7.0 on ongelma usean tunnistimen laitteiden yksityisyysmaskien luomisessa. Ajuri käytti aina ensimmäisen kanavan mallia, joten yksityisyysvyöhykkeet saattoivat näkyä virheellisesti (esimerkiksi väärällä kanavalla).

Poista yksityisyysvyöhykkeet manuaalisesti Web-käyttöliittymän kautta tai palauta laite tehdasasetuksiin, jos havaitset tällaista käyttäytymistä. Tämän jälkeen ohjain luo yksityisyysmaskit käyttämällä oikeita malleja seuraavan videokanavan käynnistyksen yhteydessä.

Axis Zipstream -tekniikkaa (<http://www.axis.com/global/en/technologies/zipstream)> voidaan käyttää ohjaimen kanssa. Ohjaimessa ei ole tämän ominaisuuden konfigurointimahdollisuutta, joten se on otettava käyttöön manuaalisesti Web-käyttöliittymän kautta.

Huomaa, että:

Web-käyttöliittymän kautta tehdyt videoasetusten muutokset (mukaan lukien Axis Zipstream -asetukset) vaikuttavat muutosten jälkeen käynnistettyihin videovirtoihin. Videovirta on siis käynnistettävä uudelleen, jotta päivitetyt asetukset voidaan ottaa käyttöön.

VMS-ohjelmiston on vastaanotettava yksi intraframe sekunnissa videovirran jälkikäsittelyä varten (VCA, liikkeentunnistus jne.). Dynamic GOP -vaihtoehdon käyttö voi aiheuttaa ongelmia jälkikäsittelyssä, joten tämän vaihtoehdon käyttöä ei suositella.

Windows XP:tä ei tueta ajuriversiosta 2.5.0.0 lähtien.

Uudet Axis-kamerat (firmware 5.50 ja uudemmat) käyttävät uutta API:ta liikkeentunnistukseen, jota ohjain ei tällä hetkellä tue. VMD-ominaisuus ei ole käytössä näissä kameroissa, kunnes ajuriin lisätään uusi API-tuki.

Axis Licence plate recognition -sovellus käyttää HTTP POST -pyyntöjä ANPR-tietojen lähettämiseen. Ohjain käynnistää HTTP-palvelimen vastaanottamaan näitä HTTP POST -viestejä. Jos tietokoneessa on useampi kuin yksi verkkosovitin, kuljettajan XML-tiedoston AxisANPR/NetworkInterface-parametrin AxisANPR/NetworkInterface-parametriin on määritettävä sen verkkosovittimen oikea IP-osoite, jota käytetään yhteydenpitoon kameran kanssa. Muussa tapauksessa kamera ei lähetä ANPR-tietoja tietokoneeseen. Jos käytetään Failoveria, on asetettava molemmat osoitteet - pääpalvelin ja Failover.

Axis muutti date.cgi API:n time.cgi API:ksi kellonajan asettamiseksi / saamiseksi kamerasta / kameraan. Tämä uusi time.cgi API toimii kuitenkin hitaasti, joten ohjain saa ajan kamerasta hieman viiveellä. Lisäksi time.cgi:ssä ei edelleenkään ole milisekuntia, joten tämä aikasynkronointi ei ole tarkka. Ajuri yrittää laskea kameran ja PC:n välisen aikaeron tallentimen avulla, mutta tämä laskenta ei ole tarpeeksi tarkkaa. Tämä laskenta voidaan kytkeä pois päältä konfigurointitiedostossa, jos aika synkronoidaan VMS:n ulkopuolella.




Pagination
Previous page
NewArecontIPCapture - Asennus ja käyttö
Next page
NewBoschIPCapture - Asennus ja käyttö