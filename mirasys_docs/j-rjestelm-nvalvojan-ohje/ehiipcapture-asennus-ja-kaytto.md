# EHIIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/ehiipcapture-asennus-ja-kaytto

EHIIPCapture - Asennus ja käyttö

Ajuri käyttää RTSP/RTP/HTTP/HTTPS/UDP/IP-protokollia videon vastaanottoon kaikissa pakkaustiloissa. HTTP/HTTPS-protokollia käytetään myös parametrien asettamiseen/hakuun ja videon etävirtaan. Jos DVMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP/HTTP/HTTPS-portit on avattava:

HTTP: oletusportti on 80,

HTTPS: oletusportti on 443,

RTSP: portti 554,

UDP: tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3556-4556.

Jos DVMS:ssä on esimerkiksi neljä kameraa, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se jätetään käyttämättä.

EHIIPCapture.xml-tiedostoa voidaan käyttää 360 asteen näkymän (kanavan) valitsemiseen - määritä seuraavassa XML-kohdassa käytettävät kanavanumerot:

<Channel360>1</Channel360>
<Channel360>2</Channel360>


Kun kanavanumerot on asetettu 360 asteen kameralle, kamera on poistettava ja lisättävä uudelleen, jotta kanavien oikeat ominaisuudet voidaan havaita.

Multicast-suoratoisto vaatii myös kaksi peräkkäistä porttia ääni- tai videovirtaa kohden, mutta porttien numerot riippuvat laiteasetuksista tai XML-konfiguraatiosta.

Laite voidaan esimerkiksi määrittää lähettämään kaikki virrat vain yhteen porttiin. Jos portti 40000 on määritetty tähän asetukseen, portit 40000-40001 on avattava.

Rajoitukset

Vain yhtä monilähetysvirtaa tuetaan. Äänikanavalle ja videokanavalle käytetään yhtä monilähetys-IP-osoitetta, mutta monilähetys-ääniportin on oltava saman virran osalta vähintään 2 kertaa suurempi kuin videoportin, ja monilähetys-videoportin on oltava toisen virran (esimerkiksi Live) osalta vähintään 6 kertaa suurempi kuin edellisen virran (esimerkiksi Tallennus) videoportti.

Äänikanava käyttää samaa monilähetys-IP-osoitetta kuin videovirran vastaanotin. Jos eri monilähetysosoitteet on määritetty, tämä voi aiheuttaa ristiriidan videokanavan (dynaamisen käyttöliittymän konfiguraatiosta) ja audiokanavan (ladattu XML-tiedostosta) soveltamassa monilähetysmäärityksessä.

Verkkokytkimessä on otettava käyttöön IGMP Snooping monilähetysviestintää varten.

HTTP/HTTPS-siirtoa varten toteutetaan seuraava logiikka: Dynaaminen RTPoverHTTP-kenttä lisätään, jos käytetään HTTP- tai HTTPS-viestintää. Laite tukee RTPoverHTTPS-ominaisuutta.

TLS-varmenteen osalta voidaan todeta, että kun RTSP-yhteys muodostetaan HTTPS:n (TLS) kautta, kamera jakaa julkisen varmenteensa Handshake-menettelyn aikana. Asiakkaiden ei siis tarvitse tallentaa tai pitää hallussaan kameran julkista sertifikaattia.

Multiple streaming -tilaa tuetaan oikein vain DVMS 6.1:stä alkaen.

Tallennuksen ja suoratoiston pakkausmuodon pitäisi olla sama useassa suoratoistotilassa.

Kamerat käynnistyvät uudelleen pakkausmuodon muuttamisen jälkeen, joten videon palauttaminen kestää noin 30 sekuntia pakkausmuodon muuttamisen jälkeen.

Etävirralla on sama resoluutio kuin Tallennusvirralla laitteissa, joissa on kaksi streamia kanavaa kohti (”Main” ja ”Sub”), joten resoluutioasetusta ei käytetä tällaisessa streamissa, joka on HTTP JPEG -kaappaus.

Laitteissa, joissa on 3 virtaa kanavaa kohti, tätä rajoitusta ei ole.

Jotkin Hikvisionin laiteohjelmistoversiot palauttavat luettelon resoluutioista, joita kamera ei tue. Näitä resoluutioita voidaan käyttää DVMS:ssä, mutta kameran kuvissa on artefakteja.

Hikvision-kamerat tukevat vain 6 RTSP-istuntoa samanaikaisesti. Tämä on Hikvisionin laiteohjelmiston rajoitus.

Liiketunnistus on määritettävä laitteessa manuaalisesti ennen käyttöä DVMS:ssä. MD-toiminto ei välttämättä toimi oikein vanhoissa laiteohjelmistoversioissa. Käytä uusinta laiteohjelmistoversiota käyttääksesi kaikkia ohjaimen ominaisuuksia.

Tulotilojen vastaanottaminen on otettava käyttöön XML-konfigurointitiedostossa ja määritettävä laitteen verkkokäyttöliittymässä (esim. ota tulotilojen lähettäminen käyttöön kohdassa ”Ilmoita valvontakeskukselle”).

Hikvsion-laitteiden kolmatta virtaa käytetään suorana lähetyksenä ja toista kaukosäätimenä.

Videohäviön tunnistus on määritettävä laitteessa manuaalisesti ennen kuin sitä käytetään DVMS:ssä. Se voidaan myös poistaa käytöstä tai ottaa käyttöön asetustiedostossa.

Pagination
Previous page
DahuaIPCapture - Asennus ja käyttö
Next page
EIPCapture - Asennus ja käyttö