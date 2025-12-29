# IPCameraCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/ipcameracapture-asennus-ja-kaytto

IPCameraCapture - Asennus ja käyttö

Ajuri käyttää RTSP/RTP/UDP/IP-protokollia videon ja äänen vastaanottoon kaikissa pakkaustiloissa.

HTTP/HTTPS-protokollaa käytetään parametrien asettamiseen/hakuun ja PTZ-toimintoihin.

Jos DVMS:n ja UDP-IP-laitteiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP/HTTP/HTTPS-portit on avattava:

HTTP: oletusportti on 80,

HTTPS: oletusportti on 443 (jos se on käytössä kamerassa).

RTSP: portti 554,

UDP: tarvitaan kaksi peräkkäistä porttia audio/videovirtaa kohden porttialueella 3556-4556.

Rajoitukset

UDP-kamerat eivät joskus käsittele PTZ-pysäytyskomentoa. Tämän ongelman välttämiseksi ohjain lähettää neljä pysäytyskomentoa.

UDP/Amano/GANZ-kameroille ei ole iirisasetuksia. UDP/Amano/GANZ-kameroiden laiteohjelmisto mahdollistaa videostandardien vaihtamisen, mutta kamerat tukevat (yleensä) vain yhtä niistä.

2Mpx-kameroissa on ongelma MJPEG 100 % -laadun kanssa - se lopettaa suoratoiston. 2Mpx-kameroilla on eri resoluutiot MPEG4-koodekille (ei 2Mpx).

IPE1100 M -kameroissa on enimmäistarkkuusasetus (SETUP > Video & Audio > Video-In > Video Resolution -parametri). Tämä asetus määrittää käytettävissä olevien resoluutioiden luettelon - esim. 2 Mpx:n minimiresoluutio on VGA, eikä pienempiä resoluutioita ole käytettävissä.

Useiden suoratoisto- tai monilähetyssuoratoisto-ominaisuuksien ottaminen käyttöön voi heikentää laitteen suorituskykyä. Siksi molemmat videovirrat lähetetään nykyistä pienemmillä kuvataajuuksilla.

IPE-sarjan laitteet lähettävät kaikki streamit epävakaalla kuvanopeudella, jos vähintään yksi näistä streameista on määritetty MJPEG-koodausta varten. Kuvataajuus muuttuu vakaaksi, kun MJPEG-virta pysäytetään. Tämä on IPE-sarjan laitteiden ominaisuus.

IPN/IPX-laitteet voivat soveltaa videoasetuksia pitkään (70-90 sekuntia), jos moninkertainen suoratoisto on käytössä. Odota, että videovirta alkaa, ennen kuin muutat videoasetuksia uudelleen.

IPN/IPX-sarjan laitteissa on seuraava huomautus Web-käyttöliittymässä: ”Jos pystysuora resoluutio 1080P on valittu, muut videovirrat eivät voi tukea vaakasuoraa resoluutiota, joka on suurempi kuin 1088.”.” Kameran käyttäytyminen voi olla odottamatonta, jos käyttäjä yrittää soveltaa 1080p-resoluutiota molempiin videovirtoihin.

Multicast-kaappauksen rajoitukset:

Multicast-kaappaus voidaan ottaa käyttöön XML-konfiguraatiotiedoston avulla käyttämällä StreamingMode-vaihtoehtoa. Laitteen asetusten päivittäminen riittää muuttuneen StreamingMode-vaihtoehdon aktivoimiseksi.

Ajuri-instanssi voidaan määrittää ensisijaiseksi tai kuuntelijaksi. Ensisijainen instanssi voi muuttaa IP-laitteen asetuksia ja käyttää lisätoimintoja. Kuuntelijainstanssit voivat vastaanottaa video- ja äänivirtoja monilähetyksenä ja käyttää digitaalisia I/O-toimintoja.

Käyttäjän on varmistettava, että vain yksi tallennin muuttaa UDP IP -laitteiden asetuksia. Muiden tallentimien, jotka käyttävät tätä laitetta, pitäisi olla kuuntelutilassa.

Monilähetysvirta käyttää samoja asetuksia, kunnes se käynnistetään uudelleen, vaikka virran asetuksia muutettaisiin. Virran tilan muuttaminen (käynnistys tai pysäytys) kestää 6-10 sekuntia. Virran asetusten soveltaminen kestää siis 30-60 sekuntia.

Huomaa, että ohjain käyttää vain oletussovitinta multicast-suoratoistoon. Monilähetys ei siis välttämättä toimi oikein, jos tietokoneessa on useampi kuin yksi verkkokortti. Ota yhteyttä asiakastukeen, jos multicast-konfiguroinnissa ilmenee ongelmia.

Aikasynkronointitoimintojen rajoitukset:

Aikavyöhykkeen vaihtaminen ei vaikuta järjestelmän aikaan ennen uudelleenkäynnistystä. Oikean ajan käyttämiseksi ohjain voi siis käynnistää kameran uudelleen aikavyöhykeasetuksen muutoksen jälkeen.

Kesäaika-asetus (DST) on aina käytössä IPN/IPX-sarjan kameroissa. Tämä on kameran laiteohjelmiston rajoitus.

Edge Storage -toimintojen rajoitukset:

Edge Storage -toiminto on tuettu vain IPX/IPN-sarjan kameroissa laiteohjelmistoversiosta 1.8.0.4 alkaen.

Tallennus SD-kortille on määritettävä manuaalisesti kameran verkkokäyttöliittymässä ennen tämän toiminnon käyttämistä VMS:ssä.

IPN/IPX-kamerat mahdollistavat vain H.264-virran tallentamisen SD-kortille. Tallennukseen käytettävän profiilin koodauksen muuttaminen kytkee videomateriaalin tallentamisen SD-kortille pois päältä.

IPN/IPX-kamerat mahdollistavat tallennetun materiaalin haun vain tapahtumien perusteella. Tämä on kameran SDK:n rajoitus. Tämän rajoituksen vuoksi Jatkuva tallennus -asetuksilla tallennettua videokuvaa ei voida käsitellä.

Tapahtuman enimmäiskesto on 65 sekuntia (5 sekuntia ennen tallennusta ja 60 sekuntia tallennuksen jälkeen). Pidempien aikavälien tallennusta ei voi määrittää.







Pagination
Previous page
HTTPIPCapture - Asennus ja käyttö
Next page
LGEIPCapture - Asennus ja käyttö