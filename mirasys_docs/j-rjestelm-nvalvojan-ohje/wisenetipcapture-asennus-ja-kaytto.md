# WisenetIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/wisenetipcapture-asennus-ja-kaytto

WisenetIPCapture - Asennus ja käyttö

Kaikissa pakkaustiloissa ohjain käyttää RTSP/HTTP/HTTPS(TLS)/RTP/UDP/IP-protokollia videon vastaanottamiseen. Myös HTTP/HTTPS-protokollaa käytetään parametrien asettamiseen/hakuun.

Jos VMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP/HTTPS-portit on avattava:

HTTP: oletusportti on 80,

HTTPS: oletusportti on 443,

RTSP: oletusportti on 554,

UDP: kaksi peräkkäistä porttia (alkaen parillisesta arvosta) per unicast-ääni- tai videovirta porttialueella 3556-4556.

HTTPS:n (TLS) kautta tapahtuvaa viestintää varten on valittava RTSP over HTTP -kuljetus, joka on nimetty seuraavasti HTTP:lle ja HTTPS:lle.

Jos esimerkiksi VMS:ssä on neljä IP-kameraa, portit 3556, 3557, 3558, 3559, 3560 ja 3561, 3562 ja 3563 käytetään. Jos jokin portti ei ole vapaa, porttipari jätetään väliin.

Monilähetyssuoratoisto vaatii myös kaksi peräkkäistä porttia ääni- tai videovirtaa kohden, mutta porttien numerot riippuvat laitteen asetuksista tai XML-konfiguraatiosta.

Laite voidaan esimerkiksi määrittää lähettämään kaikki virrat vain yhteen porttiin. Portit 40000-40001 on avattava, jos 40000-portti on määritetty tätä asetusta varten.

Rajoitukset

Rekisterikilven tunnistus määritetään suoraan kameraan asennetussa VaxALPR-lisäosassa käyttöohjeen ”VaxALPR On-Camera Software” mukaisesti. Ohjelmiston asennus ja kameran konfigurointi. Hanwha Manual”. LPR:n tarkkuutta ei ole mahdollista säätää XML:n avulla.

On suositeltavaa käyttää kameroita, joissa on Whisenet 5 ja Wisenet 7 -prosessorit, Vaxtor ALPR -liitännäisen (VaxALPR) kanssa.

TLS-varmenteen osalta voidaan todeta, että kun RTSP-yhteys muodostetaan HTTPS:n (TLS) välityksellä, kamera jakaa julkisen varmenteensa Handshake-menettelyn aikana, joten asiakkaan ei tarvitse tallentaa tai pitää hallussaan kameran julkista varmentetta.

Älä aseta tyhjää käyttäjänimeä valtuutusta varten. Jos käyttäjänimi on tyhjä, HTTP-pyyntöihin ei lisätä valtuutuksen sisältöotsakkeita.

Kamera saattaa palauttaa epätarkkoja resoluutio-ominaisuuksia, jos ”Käytävänäkymä”-vaihtoehto on asetettu 90 tai 270 asteeseen (kuten 800x448-vaihtoehto todellisen 448x800-resoluution sijasta). Stream vastaanotetaan tässä tapauksessa oikealla (pyöritetyllä) resoluutiolla.

Yksityisyysmaskeja sovelletaan SUNAPI-määritysten mukaisen enimmäisresoluutiokoon perusteella. Tämän seurauksena ne eivät välttämättä vastaa näytettäviä kohtia, jos käytetään rajattua kuvaa tai kuvaa, jonka kuvasuhde on erilainen. Tämä on normaalia. Käytä enimmäisresoluutiota System Manager/Spotter Admin -sovelluksissa yksityisyysmaskien muokkaamiseen.

SNB-9000-kameran (laiteohjelmistoversio 1.02_160215) yksityisyysmaskit saattavat ilmestyä ja kadota useita kertoja, kun ohjain soveltaa konfiguraatiota. Tämä on kameraan liittyvä ongelma, josta ilmoitettiin Hanwha Techwinin tukipalvelulle, mutta tällä hetkellä he eivät kuitenkaan aio julkaista uutta laiteohjelmistoversiota.

PTZ-laitteiden yksityisyysmaskeja ei tueta, koska Mirasys VMS:ssä ei ole mahdollisuutta määrittää maskin sijaintia pallokoordinaattien avulla.

Useat kamerat, kuten PNM-9030V, tukevat yksityisyyden suojausta vain yleiskatsauskanavalle. Muut kanavat näyttävät osan yleiskatsauskanavasta, eikä niillä ole mahdollisuutta asettaa omia naamioita.

Koska VMS:ssä ei ole mahdollisuutta määrittää ominaisuuksia kullekin videokanavalle erikseen, kaikilla kamerakanavilla on sama (enimmäis)määrä käytettävissä olevia naamioita. Tässä tapauksessa maskit toimivat kuitenkin vain yleiskatsauskanavalle. Muiden kanavien yksityisyysmaskiasetukset jätetään huomiotta.

Wisenet PNM-9030V -näyte tukee yksityisyyden suojausominaisuutta vain ”Overview”-kanavalle.

Muiden kanavien kuva ei tue yksityisyyden suojausta. Näin ollen kaikki ”Overview”-kanavan kuvassa maskien peittämät kohteet näkyvät helposti muissa kanavissa.

Tämä on Hanwhan konsepti, ja se mainitaan kameran teknisissä tiedoissa.

SNB-9000-kamera (laiteohjelmiston versio 1.02_160215) ei pysty vaihtamaan koodekkia SUNAPI-kutsulla.

Tämä on kameraan liittyvä ongelma, ja siitä ilmoitettiin Hanwha Techwinin tukipalvelulle, mutta heillä ei ole tällä hetkellä suunnitelmaa uuden laiteohjelmistoversion julkaisemisesta.

Vaihda koodekki manuaalisesti Web-käyttöliittymän kautta, jos videoasetusten soveltamisessa ilmenee ongelmia.

SNB-9000-kamera vaihtaa resoluutiota hälytyksen mukaan (CCRiA-toiminto) 8 sekunnin aikana. Tämä käyttäytyminen johtuu useista viiveistä kamerapuolella, kun virta lähetetään uudelleen, eikä sitä voida parantaa ohjaimen puolella. Kuvanopeuden muuttaminen hälytyksen yhteydessä (CCFiA) kestää 2 sekuntia, koska kamera käyttäytyy samalla tavalla.

Muista siis nämä rajoitukset, jos CCRiA/CCFiA-toimintoja on tarkoitus käyttää tämän kameran kanssa asennuksessasi.

Ajuri ei salli PTZ-toimintojen käyttöä kameroissa, joissa on ”Cropped image” -ominaisuudet (kuten SNB-9000- tai SNV-8080-kamerat).

Kamerat, joissa on moottoroitu tarkennus-/zoom-objektiivi, eivät tue jatkuvaa zoomausta/tarkennusta kuten PTZ-kamerat. Zoomauksen/tarkennuksen muutosta käytetään vaiheittaisena säätönä Web-käyttöliittymässä. Tämän seurauksena zoomin/tarkennuksen muutos on diskreetti. Ohjain lähettää toistettavia askelkomentoja myös silloin, kun zoomaus-/tarkennusnäppäintä painetaan jatkuvan liikkeen jäljittelemiseksi.

Hanwha box -kamerat (joiden mallissa on B-merkki, kuten XNB-xxxx tai QNB-xxxx) tukevat ulkoista PTZ-ominaisuutta, jonka avulla kameraa voidaan käyttää PT-alustan kanssa. Valitettavasti HTTP API -kutsujen avulla ei voida havaita, onko kamera liitetty PT-alustaan vai ei, joten ulkoisen PTZ-ominaisuuden tukevat laatikkokamerat havaitaan PTZ:nä. Tämä on HTTP API / kameralaitteiston rajoitus.

Hanwhan laitteissa on seuraavat rajoitukset esiasetettujen asemien nimien osalta:

Vain aakkosnumeeriset symbolit (A-Z, a-z, 0-9) ovat sallittuja;

Esiasetusnimen pituus on rajoitettu 12 symboliin. 

Tämän seurauksena ajuri versiosta 1.0.2.0 lähtien tallentaa esiasetusten sijainnin *.preset XML-tiedostoihin. Jos tiedosto ei sisällä esiasetettuja sijainteja, ohjain yrittää ladata todelliset tiedot esiasetetuista sijainneista Wisenet IP -laitteesta.

XML-tallennuksen käyttö mahdollistaa myös Unicode-symbolien käytön esiasetettujen asemien nimissä.

GOV Length -arvo asetetaan automaattisesti puoleen nykyisestä kuvataajuudesta (eli 2 avainkuvaa sekunnissa) tallennusprofiilin osalta, eikä sitä voi säätää Web-käyttöliittymän tai HTTP API -komentojen kautta. Valitse toinen profiili ”Record”-profiiliksi, jos tämä rajoitus ei sovi kokoonpanoosi.

Monianturisella Wisenet IP -laitteella voi olla eri kanavien resoluutio-ominaisuudet. Esimerkiksi PNM-9030V-näyte tukee 6096x2540- ja 2688x1120-resoluutiota ensimmäiselle kanavalle, jopa 2592x1944-resoluutiota neljälle seuraavalle kanavalle ja jopa 1920x1080-resoluutiota kuudennelle ja seitsemännelle kanavalle.

Valitettavasti VMS:ssä ei ole mahdollisuutta määrittää eri kanaville eri resoluutiojoukkoja - tämä on ohjelmistoarkkitehtuurin rajoitus. Toisin sanoen kaikki resoluutiot (6096x2540, 2688x1120 ja 2592x1944) ovat käytettävissä kaikilla kanavilla.

Jos kanava ei tue valittua resoluutiota, sen sijaan käytetään lähintä suurempaa tai suurinta resoluutiota. Esimerkissä 2592x1944 valinnan tapauksessa 2688x1120 käytetään 1. kanavalle ja 1920x1080 7. kanavalle.

Äänikanava käyttää samaa videoprofiilia, jota käytetään videovirran vastaanottamiseen.

Se voi aiheuttaa ristiriidan videokanavalla (dynaamisen käyttöliittymän konfiguraatiosta) ja äänikanavalla (ladattu XML-tiedostosta) käytetyssä multicast-konfiguraatiossa.

Äänikanava siis muuttaa monilähetysmääritystä vain siinä tapauksessa, että videokanava ei ole vielä muuttanut sitä. Muussa tapauksessa olemassa olevaa monilähetyskonfiguraatiota käytetään äänivirran monilähetykseen.

Laitteen videoprofiilia käytetään äänen vastaanottamiseen ja lähettämiseen. Mikä tahansa videoprofiilin asetuksen muutos, joka aiheuttaa RTSP-istunnon uudelleen käynnistymisen, voi aiheuttaa myös äänivirran uudelleen tilaamisen.

VMS:llä ei ole mahdollisuutta määrittää ääniasetuksia System Managerissa, joten nämä asetukset on määritettävä XML-kokoonpanotiedoston avulla.

Oletusarvoisesti määritetään vain äänenkooderi (<Encoding>-vaihtoehto): AAC äänituloa varten ja G.711 äänilähtöä varten. Muut ääniasetukset (mukaan lukien äänenvoimakkuus/vahvistus) määritetään käyttämään kameran Web-käyttöliittymässä tällä hetkellä valittuja arvoja.

Wisenet-kameroilla voi olla kuvanopeusrajoitus, joka riippuu samanaikaisesti suoratoistettavien profiilien määrästä:

Uusi Q-sarja voi tukea 1920x1080-striimiä yhteensä 45 kuvaa sekunnissa. Esimerkiksi QND-6082R-kamera tukee jopa 30 kuvaa sekunnissa H.264-virtaa maksimiresoluutiolla 1920x1080. Jos kamera lähettää suoratoistoa yhdestä profiilista, se tuottaa 30 kuvaa sekunnissa. Jos kuitenkin suoratoistoa tehdään kahdesta eri profiilista samoilla H.264 1080p @ 30 fps -suoratoistoasetuksilla, kamera suoratoistaa kumpaakin vain 22 kuvaa sekunnissa.

Uusi L-sarja voi tukea 1920x1080-striimiä yhteensä 30 kuvaa sekunnissa.

Mirasys VMS:ssä on ongelma G.726-äänivirran dekoodaamisessa useista näytteistä, kuten seuraavat näytteet

Wisenet XND-8080R. Ongelma korjataan seuraavissa ajurijulkaisuissa, käytä G.711- tai AAC-koodausta, jos G.726-äänen dekoodauksessa ilmenee ongelmia.

Ajuri tukee vain Edge-Storage-ominaisuuden uutta versiota, joka on käytettävissä VMS-versiosta 8.0 lähtien. Edge-Storage-ominaisuutta ei havaita aiemmissa VMS-versioissa.

Wisenet SNF-8010 -kamerassa on ongelma tallennettujen tietovälien etsinnässä: se havaitsee vain sellaiset tietovälit, joiden alku ja loppu ovat pyydetyn ajanjakson sisällä. Muut kameranäytteet havaitsevat myös välijaksoja (eli tallennuksen alkamisaika on ennen pyydettyä jaksoa ja päättymisaika on jakson sisällä tai sen jälkeen).

SNF-8010-kameran valmistus on jo lopetettu (vuodesta 2018 lähtien), joten ongelmaa ei korjata kameran puolella. Mirasysilla ei myöskään ole suunnitelmia lisätä ajuriin erillistä käsittelylogiikkaa yksittäiselle mallille.

Useat monianturilaitteet tukevat materiaalin tallentamista rajoitetulla määrällä kanavia.

Esimerkiksi PNM-9030V-näytteen avulla voidaan tallentaa videokuvaa vain ”Overview”-kanavalta.

Tässä tapauksessa ohjain käyttää Edge-Storage-ominaisuutta vain niiden kanavien osalta, joilla on ”Recording”-ominaisuus ”Recording”-ominaisuusryhmässä.

SUNAPI v2.x -määrittelyissä on seuraavat rajoitukset tallennustoimintojen käsittelyyn liittyville HTTP- ja RTSP-pyynnöille:

Millisekuntia ei ole saatavilla;

Aika on määritettävä paikallisessa muodossa (ei UTC-tukea) kaikissa pyynnöissä;

Laitteen palauttamat aikavälit ovat myös paikallista aikaa.

  Nämä rajoitukset voivat aiheuttaa seuraavia ongelmia:

Koska aikaresoluutio on yksi sekunti, siirtyminen tallennus- ja reunamateriaalien välillä ja päinvastoin voi aiheuttaa toistuvia fragmentteja, joiden kesto on enintään yhden sekunnin pituinen, tai tietoja voi jäädä puuttumaan enintään yhden sekunnin pituisia tietoja;

Paikallisen ajan ja UTC-ajan välinen muuntaminen voi aiheuttaa ongelmia aineiston valinnassa, kun siirrytään kesäaikaan tai kesäajasta (DST);

Aikavyöhykkeen vaihtaminen voi aiheuttaa väärän aikavälien valinnan intervallivastaanoton aikana.

Wisenet-laitteet tukevat vain yhtä RTSP-yhteyttä toistoa varten samanaikaisesti. Jos siis käytetään monikanavaista laitetta, kadonneet tiedot vastaanotetaan laitteen SD-kortilta sarjassa: kaikkien kanavien kaikki aikavälijaksot lähetetään yhteen jonoon, ja ne poistetaan jonosta vain, jos muita aikavälijaksoja ei tällä hetkellä käsitellä.

Ajuria voidaan käyttää Windows 7:n tai uudemman käyttöjärjestelmän kanssa. Vanhempia käyttöjärjestelmiä ei tueta.

Pagination
Previous page
VivotekIPCapture - Asennus ja käyttö
Next page
Asenna metadata-ajuri