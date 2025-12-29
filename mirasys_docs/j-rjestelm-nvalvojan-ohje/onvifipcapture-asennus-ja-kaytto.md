# OnvifIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/onvifipcapture-asennus-ja-kaytto

OnvifIPCapture - Asennus ja käyttö

Kaikissa pakkaustiloissa ohjain käyttää RTSP/RTP/UDP/IP-protokollia videon vastaanottamiseen. HTTP-protokollaa käytetään parametrien asettamiseen/hakuun.

Jos VMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP-portit on avattava:

HTTP: oletusportti on 80,

RTSP: oletusportti on 554,

UDP: tarvitaan kaksi peräkkäistä porttia per unicast-ääni- tai videovirta porttialueella 3556-4556.

Jos esimerkiksi VMS:ssä on neljä IP-kameraa, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se jätetään käyttämättä.

Multicast-suoratoisto vaatii myös kaksi peräkkäistä porttia ääni- tai videovirtaa kohden, mutta porttien määrä riippuu laitteen asetuksista tai XML-konfiguraatiosta. Laite voidaan esimerkiksi määrittää lähettämään kaikki virrat vain yhteen porttiin. Portit 40000-40001 on avattava, jos 40000-portti on määritetty tähän asetukseen.

Rajoitukset

PTZ Area Zoom -komento yhdistetään oletusarvoisesti PTZ Center -komennon kanssa, jos se on tuettu.

PTZ Center -komennon tarkkuus on vähäinen, koska tarkkuus riippuu suuresti kameramekanismista, pysty- ja vaakasuuntaisista kuvakulmista sekä nykyisen objektiivin optisista poikkeamista (esim. vääristymistä). Tällä hetkellä ei ole paikkaa näiden asetusten syöttämiselle ja tallentamiselle.

Ajuri tarvitsee mediaprofiilin vastaanottaakseen esiasetuksia IP-laitteesta. Ne voidaan siis ladata sen jälkeen, kun videovirta on tilattu.

Ajuri käyttää aikaleimoja laitteen todennukseen ONVIF-määritysten mukaisesti. ONVIF-yhteensopivan laitteen kellonaika ja sen tietokoneen kellonaika, johonVMS Recorder on asennettu, on siis synkronoitava ennen tämän laitteen käyttöä.

Ajuri ei tue Unicode-esimerkkejä.

Usean suoratoisto-ominaisuuden rajoitukset voivat riippua käytetystä laitteesta (esimerkiksi encoder1:n resoluutio ei voi olla suurempi kuin encoder2:n resoluutio). Lue laitteen käyttöohjeesta nämä rajoitukset.

Monikanavaiset laitteet voivat tukea eri ominaisuuksia eri kanaville. Esimerkiksi ensimmäinen kanava tukee H.264- ja MPEG-4-virtaa 1920x1080-resoluutiolla ja toinen kanava tukee vain H.264-koodausta mutta suuremmalla 4096x2160-resoluutiolla. VMS-arkkitehtuuri ei salli erilaisten ominaisuuksien välittämistä eri kanaville, joten kaikkien kanavien ominaisuudet yhdistetään (eli MPEG-4-koodaus ja 4096x2160-resoluutio ovat käytettävissä molemmissa kanavissa yllä olevassa esimerkissä).

Ajuri valitsee sopivan vaihtoehdon automaattisesti, jos käyttäjä yrittää käyttää vaihtoehdon arvoa, jota nykyinen videokanava ei tue.

Joissakin tapauksissa käyttäjä voi kohdata ”Ei signaalia” -ongelman, koska ONVIF-yhteensopivaan laitteeseen on sovellettu väärää konfiguraatiota (”ter:Action > ter:ConfigurationConflict”-viesti ilmestyy lokitiedostoon). Tässä tapauksessa käyttäjän on korjattava VMS:n asetukset laitteen ominaisuuksien mukaisesti, jos Multiple streaming on käytössä. Jos Multiple streaming -vaihtoehtoa ei käytetä, ota käyttöön vähimmäisasetukset lisävirroille Web-käyttöliittymän kautta tai poista ne kokonaan käytöstä.

ONVIF-yhteensopivat laitteet eivät ehkä pysty vaihtamaan suoratoistotilaa ”single stream”-tilasta ”triple stream”-tilaan soveltamatta asetuksia toista streamia varten. Toisin sanoen etävirtausta ei ehkä aseteta oikein, jos suoraa lähetystä ei käynnistetä sen jälkeen, kun monivirtaustoiminto on otettu käyttöön.

Ohjain käyttää eri virtojen asetuksia peräkkäin, ei samanaikaisesti. Lisävirtojen käynnistäminen voi siis kestää kauemmin kuin pelkän tallennusvirran käynnistäminen.

Ajuri käyttää PTZ-palvelun versiota 2.0 ONVIF-määritysten mukaisesti. Vanhat laitteet saattavat kuitenkin käyttää PTZ-palvelun aiempaa 1.0-versiota, joten ohjain ei havaitse PTZ-ominaisuuksia oikein. Määritä tässä tapauksessa oikea PTZ-palvelun versio XML-konfiguraatiotiedoston avulla.

Ajuri käyttää Pull-Point-mekanismia digitaalisten tulojen tilojen vastaanottamiseen ja liiketunnistusvirran seuraamiseen. Jos ONVIF-yhteensopiva laite tukee tätä mekanismia, sen on asetettava WSPullPointSupport-ominaisuus tds:GetCapabilitiesResponse-kohdassa ONVIF Core -eritelmän kohdan 9.9 mukaisesti. Digitaalisia tuloja ja VMD-toimintoja ei havaita, jos tämä ominaisuus on asetettu tukemattomaksi.

Äänitoimintojen rajoitukset

Ohjain käyttää äänitoimintoja ”sellaisenaan” ilman ääniparametrien (kuten ulostulovahvistuksen) säätöä. Valmistajakohtaisilla parametreilla, kuten ”input/output interval” tai ”output duration”, ei ole asianmukaisia vaihtoehtoja ONVIF-määrityksissä. Määritä nämä parametrit Web-käyttöliittymän kautta manuaalisesti ennen kameran käyttöä.

Multicast-kaappauksen rajoitukset

Multicast-kaappaus voidaan ottaa käyttöön XML-konfiguraatiotiedoston avulla StreamingMode-valinnalla. Tämä vaihtoehto luetaan streamia käynnistettäessä, joten laitteen asetusten päivittäminen riittää ottamaan muutetun StreamingMode-vaihtoehdon käyttöön.

Huomaa, että VMS:ssä on optimointi kanavien uudelleenkäynnistystä varten versiosta 7.4.1 lähtien, joten tässä tapauksessa on muutettava yhtä videovaihtoehtoa kunkin kameravirran osalta niiden uudelleenkäynnistämiseksi. Myös ääniasetukset on päivitettävä, jotta vaihtoehto otetaan käyttöön.

Ajuri-instanssi voidaan määrittää käytettäväksi ensisijaisena tai kuuntelijana. Ensisijainen instanssi pystyy muuttamaan IP-laitteen asetuksia ja käyttämään lisätoimintoja. Kuuntelijainstanssit pystyvät vastaanottamaan videovirtoja ja äänivirtoja monilähetyksenä ja käyttämään digitaalisia I/O- ja VMD-toimintoja.

Ohjain valitsee videolähteiden, videokoodereiden ja mediaprofiilien yhdistelmän toimintojen tunnistuksen aikana. Sama koodaus on valittava sekä ensisijaiseen että kuuntelijakappaleeseen, jotta ne voivat valita saman mediaprofiilin. Muussa tapauksessa kuuntelija-ajurin instanssi yrittää tilata toisen profiilin ja vastaanottaa toisen multicast-virran tai ei vastaanota lainkaan tietoja.

Listener-tallennin ei muuta mitään konfiguraatiota ONVIF-yhteensopivan laitteen puolella. Jos esimerkiksi kamerassa ei ole käytettävissä mediaprofiilia, sitä ei luoda eikä ohjain pysty vastaanottamaan video- tai äänivirtaa. ONVIF-laite on lisättävä ensisijaiseen tallentimeen ennen kuin sitä käytetään kuuntelijakokoonpanossa.

Lisävirrat (Live ja Remote) ovat aktiivisia, jos ne on avattu vain asiakkaille. Jotta päivitetyt Multiple Streaming -asetukset voidaan ottaa käyttöön, nämä streamit on käynnistettävä (tai pidettävä auki) ensisijaisessa tallentimessa sen jälkeen, kun stream-asetuksia on muutettu VMS:ssä. Muuten uusimpia stream-asetuksia ei sovelleta kameraan.

Käyttäjän on varmistettava, että vain yksi tallennin muuttaa ONVIF-yhteensopivien IP-laitteiden asetuksia. Muiden näitä laitteita käyttävien tallentimien pitäisi olla kuuntelijatilassa.

Sen verkkosovittimen IP-osoite, jonka kautta kamera on liitetty, on määritettävä, jotta multicast-suoratoisto voidaan vastaanottaa oikein, jos käytettävissä on useampi kuin yksi verkkosovitin. Windowsissa oletukseksi merkittyä verkkosovitinta käytetään, jos mitään vaihtoehtoa ei ole määritetty.

Ajuri saattaa kirjoittaa viestin virheellisestä multicast-konfiguraatiosta (kuten: ter:InvalidArgVal > ter:InvalidMulticastSettings). Tämä viesti tarkoittaa, että multicast-konfiguraatiossa on jotain vikaa eikä video- tai äänivirtaa voida käynnistää.

Määritä Multicast-osio XML-konfiguraatiotiedostossa ongelman ratkaisemiseksi tai säädä arvoja, jos tämä osio on jo olemassa.

Useat ONVIF-yhteensopivat IP-laitteet (esimerkiksi Axis) mahdollistavat videovirran säilyttämisen, kun asiakas muuttaa videoparametrejaan. Tämän seurauksena tällainen laite pitää aktiivisen videovirran Multicast:Listener -instanssille, jossa on aiemmat asetukset, ja käynnistää toisen videovirran Multicast:Primary -instanssille, jossa on päivitetyt asetukset.

Videoasetusten valvonta on otettava käyttöön kuuntelijan puolella käyttämällä VideoSettingsMonitoringInterval -parametria. Lisätietoja on konfigurointitiedoston kommenteissa.

Videon liikkeentunnistustoiminnon rajoitukset

Laitteen on tuettava 'tns1:VideoSource/MotionAlarm'-aihealuetta, jotta se tukee liikkeentunnistustoimintoa. Mukautettuja aihekokonaisuuksia, kuten 'tns1:VideoAnalytics/tnssamsung:MotionDetection', voidaan myös tukea, mutta ne toimivat vain yksikanavaisissa laitteissa, koska näissä aihekokonaisuuksissa ei ole videolähteen tai kanavan tunnisteita lähdetietoina tapahtumailmoituksissa.

VMS:ssä ei ole käytettävissä IP-laitteeseen liittyviä liikkeentunnistusasetuksia. Liiketunnistusasetukset (alueet, herkkyys, kohteen koko jne.) on siis määritettävä IP-laitteeseen manuaalisesti ennen tämän toiminnon käyttämistä VMS:ssä.

Liiketunnistusta voidaan käyttää Multicast-suoratoiston kanssa. ”Tallennin ja kameralaitteisto” -vaihtoehto on otettava käyttöön sekä ensisijaisessa että kuuntelevassa tallentimessa, jotta videovirtauksen pysäytys/jatkaminen onnistuisi oikein.

Videovaihtoehtojen soveltamisen ajankohtaa ei ole mahdollista havaita ilman kameran kokoonpanon muuttamista. Ajuri lisää CFiA/CRiA-ominaisuuksien tuen kaikille laitteille, mutta se ei voi taata, että kamera vaihtaa vaihtoehtoja hälytyksen perusteella riittävän nopeasti.

  Kokeile CFiA/CRiA-toimintoa testiasennuksessa, ennen kuin otat ne käyttöön turvajärjestelmien kanssa.

Muut huomautukset

Ajuri käyttää oletusarvoisesti ”RTP over RTSP” -kuljetusta videon/audion suoratoistoon ajuriversiosta 1.5.0.0 lähtien.

ONVIF-yhteensopivan laitteen palauttamat digitaaliset tulot lajitellaan tunnuksen nimen mukaan, jotta voidaan varmistaa, että laite ei järjestä niitä uudelleen alkutilapyynnön yhteydessä. Tämän seurauksena todelliset tulonumerot voivat poiketa VMS-arvoista (kuten ”1”, ”2”, ..., ”10” -luettelo lajitellaan muotoon ”1”, ”10”, ”2”, ..., ”9”).

Vaihtoehtojen muuttaminen hälytyksen aikana (CRiA/CFA) -toimintoa voidaan käyttää vain ”aktiivisessa” ohjaustilassa. Passiivisessa tilassa ohjain ei muuta mitään IP-kameran vaihtoehtoa, joten virta jatkuu ilman resoluution tai kuvataajuuden muuttumista.

Windows XP:tä ei tueta ajuriversiosta 1.5.0.0 lähtien.

Pagination
Previous page
NewSonyIPCapture - Asennus ja käyttö
Next page
PelcoIPCapture - Asennus ja käyttö