# DahuaIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/dahuaipcapture-asennus-ja-kaytto

DahuaIPCapture - Asennus ja käyttö

Ajuri käyttää RTSP/RTP/UDP/IP-protokollia videon vastaanottoon kaikissa pakkaustiloissa.

HTTP-protokollaa käytetään parametrien asettamiseen/hakuun. Jos DVMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP-portit on avattava:

HTTP: oletusportti on 80,

RTSP: portti 554,

UDP: tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3556-4556.

Jos DVMS:ssä on esimerkiksi neljä Dahua IP-kameraa, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se jätetään käyttämättä.

Rajoitukset

Useilla suoratoisto-ominaisuuksilla voi olla rajoituksia, jotka riippuvat käytetystä laitteesta (esimerkiksi Extra-virran resoluutio ei voi olla suurempi kuin päävirran videon resoluutio). Tutustu laitteen käyttöohjeisiin saadaksesi tietoa näistä rajoituksista.

CCRiA (Can Change Resolution in Alarm) -ominaisuutta ei tueta, koska uuden resoluution käyttöönotto kestää kauemmin kuin signaalin menetyksen aikakatkaisu.

Kamerat, joissa on kaksi toisistaan riippuvaista tunnistinta, esimerkiksi DH-SDT4E425-8P-GB-APV1, eivät ole täysin tuettuja.
VMS-järjestelmämme ei tue saman laitteen eri kanavien eri resoluutioita. Kaikilla kanavilla on sama resoluutioluettelo, mutta vain tuettuja resoluutioita voidaan käyttää.
Sama koskee resoluution muuttamista hälytystoiminnossa.

Jos Dahua/Stanley-laitteet eivät muuta resoluutiota tai kuvanopeutta oikein, päivitä se uuteen laiteohjelmistoon. Ajuri tulostaa seuraavan viestin DVRLog.txt-tiedostoon:

”Videokanavia ei voi määrittää laitteelle <ip>:80, tuloskoodi: 12002 (Pyynnön aikakatkaisu).” ” Laite ei ehkä hyväksy uusia videoasetuksia ilman oikeaa Bitrate-parametria. Kamera lähettää väärän bittinopeusalueen, ja ohjain laskee laadun mukaan Bitrate-arvon, jota ei voida hyväksyä, ja yrittää soveltaa sitä sekä CBR- että VBR-tiloissa. Bitrate-alue on mahdollista ohittaa käyttämällä seuraavaa DahuaIPCapture.xml-tiedostossa olevaa vaihtoehtoa <BitrateMap enabled=”yes” Ajurilla on sisäinen bitrate-kartta useimmille resoluutioille 1920x1080:een asti vain H.264-koodekille. On mahdollista lisätä lisää bittinopeuksia korkeammille resoluutioille ja JPEG-koodekille, kuten ajurin XML:ssä olevissa esimerkeissä näytetään.

Dahua-laite voidaan lisätä pienemmällä maksimikuvanopeudella kuin mitä jotkin resoluutiot tukevat. Päivitä laiteohjelmisto. Jos se ei ole käytettävissä, poista Dahua-laite DVMS:stä, aseta tarvittavat videoasetukset Web-käyttöliittymän avulla ja lisää se uudelleen.

Jos Dahua-laite palauttaa useita ”400” tai ”500” HTTP-virheitä, päivitä laite uuteen laiteohjelmistoon. Jos laiteohjelmistopäivitystä ei ole saatavilla, DahuaIPCapture.xml-tiedostossa on useita parametreja:

<UseEventManager>false</UseEventManager> EventManeger-kyselypyyntöjen poistaminen käytöstä

<InputCheckTimeout>1000</InputCheckTimeout> Voit säätää digitaalisten tulojen pyyntöjen väliä vain, jos <UseEventManager>false</UseEventManager>-vaihtoehto on poistettu käytöstä.

<Control digitalInputs="false" motionDetection="false" /> Kameralaitteiston digitaalisten tulojen ja liiketunnistuksen poistaminen käytöstä

Äänitoimintojen rajoitukset:

Ohjain käyttää äänitoimintoja sellaisenaan säätämättä ääniparametreja (kuten lähtövahvistusta). Määritä nämä parametrit Web-käyttöliittymän kautta.

Ajuri tukee G.711- ja G.726-äänikoodauksia. AAC-koodausta ei tueta.

Joissakin laiteohjelmistoversioissa Two-Way-ääni ei ehkä toimi verkkoyhteyden katkaisemisen jälkeen. Poista laite DVMS:stä, käynnistä se uudelleen ja lisää se uudelleen. Jos haluat poistaa tämän ominaisuuden käytöstä tietyn laitteen osalta, aseta seuraava vaihtoehto: <TwoWayAudio>NO</TwoWayAudio>

Multicast-kaappauksen rajoitukset:

Multicast-kaappaus voidaan ottaa käyttöön XML-määritystiedoston kautta käyttämällä RTPMode-vaihtoehtoa. Tämä vaihtoehto luetaan virran käynnistyksen yhteydessä, joten laitteen asetusten päivitys riittää aktivoimaan muuttuneen RTPMode-vaihtoehdon.

Käyttäjän on varmistettava, että vain yksi tallennin muuttaa IP-laitteiden asetuksia. Muut tallentimet, jotka käyttävät tätä kameraa, eivät saa muuttaa asetuksia.
Poista kamera-asetusten muutokset käytöstä seuraavan vaihtoehdon avulla <ChangeSettings>false</ChangeSettings>
Tässä tilassa ohjain ei muuta seuraavia kameran asetuksia:
= Quality
= Resolution
= Framerate

<ChangeSettings>true</ChangeSettings>
Ajuri muuttaa kameran asetukset DVMS-asetusten mukaisesti ja vastaanottaa ääni- ja videotiedot kamerasta multicast-yhteyden avulla. Määritä tämä tila vain ensisijaiselle tallentimelle.

Toissijaisen tallentimen seuraavat asetukset määritetään samoin kuin ensisijaisen tallentimen asetukset:
= Multiple streaming option
= Video Codec for all streams

Salattuun suoratoistoon liittyy tunnettuja ongelmia ja rajoituksia:

Dahua IP Capture -ajuri tukee salattujen videovirtojen vastaanottamista IP-laitteista. Salatun videovirran käsittely perustuu 3. osapuolen Dahua-kirjastoihin (Dahuan NetSDK ja PlaySDK).

Virran salaus on otettava käyttöön Web UI:n kautta ennen sen käyttämistä Mirasys VMS:ssä. Ota se käyttöön siirtymällä laitteen asetuksiin ja valitsemalla ”System”-ryhmä ja sen jälkeen ”Security”- tai ”Safety”-alaryhmä (nimi voi vaihdella eri laitteissa). Valitse asetusten valintaikkunasta välilehti ”Järjestelmäpalvelu” ja ota sitten käyttöön valintaruutu ”Audio and Video Transmission Encryption”.

Jos IP-laite tukee virran salausta, järjestelmä lisää ”AES-256 Encrypted” -kuljetuksen ja valitsee sen oletusarvoiseksi kuljetukseksi. Jos sinun ei tarvitse käyttää virran salausta ñ valitse mikä tahansa muu kuljetus, joka perustuu vaatimuksiisi.

Virran salauksessa käytetään AES-256-algoritmia Dahuan GDPR-määrittelyasiakirjan mukaisesti. Avainkehyssalausta käytetään. Toisin sanoen:
= Virran salausta voidaan käyttää H.265-, H.264- ja MPEG-4-koodauksissa;
= MJPEG-virtaa ei voi salata ja vastaanottaa SDK-kirjastojen kautta sellaisenaan.

MPEG-4-salausta tuetaan. Mirasysissa ei kuitenkaan ollut käytettävissä laitetta, jolla sitä olisi voitu testata. Niinpä toteutus tehtiin SDK:n dokumentaation perusteella, mutta sitä ei testattu.

Äänen salaus on saatavilla NetSDK:n kautta, mutta sitä ei ole toteutettu ohjaimessa.

Salaus ei ole tuettu multicast-suoratoistossa.

Multicast-tilassa tapahtuvaa videokuvausta varten on mahdollista määrittää osoitteet ja portit laitteessa ja ohjaimen XML-tiedostossa ja poistaa videoasetusten säätäminen käytöstä seuraavalla vaihtoehdolla <ChangeSettings>false</ChangeSettings>.

Zoomaus ei ehkä toimi oikein Stanley IPC-STAN-6100IRV -kamerassa. Kyseessä on kameran laiteohjelmistoon liittyvä ongelma.'

Ajuri ei tue Unicodea PTZ-esiasetusten (preposition) nimissä.

Älä yritä etsiä kameraa <All drivers> vaihtoehto ja <default> valtakirja tai väärä salasana - se voi lukita käyttäjätilin. Lisää laite käyttämällä yhtä 'DahuaIPCapture' -ajuria.

Tämä ohjain ei tue Windows XP:tä.

Pagination
Previous page
CanonIPCapture - Asennus ja käyttö
Next page
EHIIPCapture - Asennus ja käyttö