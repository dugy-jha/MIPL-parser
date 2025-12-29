# RTSPIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/rtspipcapture-asennus-ja-kaytto

RTSPIPCapture - Asennus ja käyttö

Ajuri käyttää RTSP/RTP/UDP/IP-protokollia videovirran vastaanottamiseen IP-laitteista.

Ohjain odottaa RTP- tai RTSP-URI:ta laitteen lisäämiseksi. Tämä URI olisi sijoitettava ”IP Address”-kenttään.

Tarvittava portti voidaan määrittää erikseen ”Port”-kentässä tai se voidaan sisällyttää RTSP/RTP URI:hen. RTSP URI -portilla on korkeampi prioriteetti, jos se on asetettu, VMS-porttikenttä jätetään huomiotta.

Virran URI-vaatimukset:

RTSP URI on ilmoitettava täydessä muodossa, esim. seuraavassa muodossa: rtsp://192.168.1.70:554/?h264x=0

Kameroille, jotka lähettävät useita videovirtoja (kuten ACTi), on myös määritettävä oikea raidan ID: rtsp://192.168.1.75:7070/track1

Myös RTP-suoratoistolaitteilla pitäisi olla oikea etuliite: rtp://62.97.61.37:15000/

RTP steam URI hyväksyy myös multicast-osoitteet: rtp://239.232.192.255:20000/

Huomaa, että stream URI voidaan tarkistaa kolmannen osapuolen soittimella, kuten VLC tai QuickTime.

Jos VMS:n ja kameroiden välillä on palomuuri, seuraavat portit on avattava:

RTSP: oletusportti on 554,

UDP: RTSP-tilassa tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3556-4556. Parametreissa määritetty portti on avattava RTP-suoratoistotilaa varten.

Esimerkiksi: jos VMS:ssä on kaksi IP-kameraa, portteja 3556, 3557, 3558 ja 3559 käytetään RTSP-istuntoihin. Jos jokin portti ei ole vapaa, se ohitetaan.

RTSP-suoratoisto voidaan määrittää myös RTSPIPCapture.xml-määritystiedoston avulla. Sen avulla voidaan muuttaa seuraavia asetuksia:

RTP-videokuljetus. Seuraavia tyyppejä tuetaan: RTPoverUDP ja RTPoverRTSP.
<RTPMode>RTPoverRTSP</RTPMode>

Keep-alive-viestien poistaminen käytöstä. Muutamat laitteet eivät ehkä tue keep-alive-käsittelyä, joten se voidaan poistaa käytöstä 0-vaihtoehdolla, jossa määritetään <KeepAlive>1</KeepAlive> Nämä arvot voidaan asettaa kullekin laitteelle erikseen.

Huulisynkronoinnin jäljitys voidaan ottaa käyttöön seuraavalla vaihtoehdolla: <LogLevel>4</LogLevel>

Rajoitukset

Jos kamera vaatii RTSP-valtuutuksen, oikea käyttäjänimi ja salasana on asetettava, muuten videokuvaa ei tule.

RTP-tilan huomautukset:

RTP-videostriimauksen IP-laitteiden pitäisi pystyä lähettämään SPS- ja PPS-otsakkeita virrassa. Ajuri ei pysty purkamaan H.264-virtaa oikein ilman näitä otsikoita.

Ajuri ei pysty käynnistämään RTP-virtausta itse - se käyttää vain laitteen jatkuvasti tuottamaa RTP-virtaa.

Äänen synkronointi RTCP:n avulla EI ehkä toimi seuraavissa tapauksissa:

jos laite lähettää RTCP-raportin datapaketin jälkeen;

RTP over RTSP -tilassa;

Jos RTCP-synkronointi on käytettävissä, voit löytää seuraavat viestit DVRLog.txt-tiedostosta:

    "Video frame time was synchronized by RTCP successfully"

MPEG2 TS -muodon huomautukset

Ajurin versio 1.2.0.0 tukee vain H.264- ja AAC-koodekkeja MPEG2 TS -formaattia varten.

Ei ole mahdollista vastaanottaa vain video- tai äänivirtaa, koska ne lähetetään yhdellä RTP-virralla.

Äänikanava havaitaan kaikissa laitteissa, jotka käyttävät MPEG2 TS -formaattia (MPEG II -kuljetusvirta).

Aseta seuraavaksi arvoksi ”false”, jos haluat poistaa äänen käytöstä valitusta laitteesta:

XML
        <AudioChannel>

          <Enabled>false</Enabled> 

        </AudioChannel>


Windows XP:tä ei tueta ajuriversiosta 1.0.1.5 lähtien.

Pagination
Previous page
PSIAIPCapture - Asennus ja käyttö
Next page
SIPIPCapture - Asennus ja käyttö