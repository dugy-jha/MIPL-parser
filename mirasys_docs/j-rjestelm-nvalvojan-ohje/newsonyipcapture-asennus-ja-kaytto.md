# NewSonyIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/newsonyipcapture-asennus-ja-kaytto

NewSonyIPCapture - Asennus ja käyttö

Ohjain käyttää seuraavia protokollia videon vastaanottamiseen:

HTTP/HTTPS-protokollaa käytetään MJPEG-videon ja liiketunnistusvirran vastaanottamiseen;

RTP/UDP/IP-protokollia käytetään MPEG-4- ja H.264-videovirran ja äänivirran vastaanottamiseen;

RTSP-protokollaa käytetään RTP-virran ohjaamiseen G5 (5. sukupolvi) ja uudemmissa laitteissa;

HTTP-protokollaa käytetään äänivirran lähettämiseen kameraan.

HTTP/HTTPS-protokollaa käytetään myös parametrien asettamiseen/hakuun.

Jos VMS:n ja kameroiden välillä on palomuuri, seuraavien RTSP/UDP/HTTP/HTTPS-porttien on oltava seuraavat avattava:

HTTP: oletusportti on 80,

HTTPS: oletusportti on 443,

RTSP: oletusportti on 554,

UDP: tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3556-4556.

Esimerkiksi: jos 4 SONY IP-kameraa on määritetty vastaanottamaan MPEG-4- tai H.264-videota VMS-järjestelmässä, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se ohitetaan.

Ajuri voidaan konfiguroida XML-konfiguraatiotiedoston avulla SONY G5-G7 IP -laitteiden ääniparametrien asettamiseksi.

Rajoitukset

SNC-DM160-, SNC-DM110- ja SNC-CM120-kameramallit tukevat Light Funnel -toimintoa:

Ohjain asettaa Light Funnel -toiminnon aina ”auto”-tilaan. Kun se aktivoituu heikossa valaistuksessa, se lisää kuvan herkkyyttä, mutta 1280x960-resoluutiolla se siirtyy automaattisesti pienempään, 640x480-resoluutioon.

Valosuppilon aktivointi-/deaktivointiviive on noin 40 sekuntia.

Valosuppilo ei toimi, kun jokin seuraavista on asetettu:

Kuvan koko on jokin seuraavista:

JPEG - 960x720: MPEG4 - OFF

JPEG - 768x576: MPEG4 - OFF

JPEG-kuvan rajaus on päällä

SolidPTZ on päällä

Iris auki on päällä.

Huomaa, että kun Light Funnel on pois päältä, enimmäiskuvanopeus on 15 kuvaa sekunnissa. Lisätietoja on kameran käyttöoppaassa.

Suurilla kuvatarkkuuksilla kuvataajuus voi olla pyydettyä alhaisempi.

Analogisen videolähdön ominaisuuksia koskevat huomautukset

Ohjain poistaa analogisen videolähdön ominaisuuden käytöstä SONY G4 IP-kameroissa (4. sukupolvi). Tämän ominaisuuden ottaminen käyttöön rajoittaa tuettuja koodekkeja ja resoluutioita (esimerkiksi SCN-CS20-kamera tukee vain 640x480-resoluutiota).

Ohjain ei muuta analogisen videolähdön asetusta G5/G6 SONY IP -kameroille. Huomaa, että kameran suorituskykyyn voi vaikuttaa, jos tämä ominaisuus on asetettu ”Päällä” -asentoon.

Liiketunnistusominaisuuden huomautukset

Määritä liiketunnistusalueet manuaalisesti web-käyttöliittymän kautta ennen liiketunnistusajuritoiminnon käyttöä.

SONY-kamerat eivät välttämättä lähetä oikeaa liiketapahtumavirtaa, kun liiketunnistussivu avataan kameran verkkokäyttöliittymässä. Tämä tarkoittaa, että MD-toiminto ei toimi tässä tapauksessa oikein.

Muut rajoitukset

SNC-DM160-, SNC-DM110- ja SNC-CM120-kamerat tukevat 1280x960-, 960x720- ja 768x576-resoluutioita, ja niitä käytetään vain JPEG-pakkauksen kanssa, mutta nämä resoluutiot näkyvät myös MPEG-4:n kanssa System Managerin kamera-asetuksissa. Jos jokin näistä resoluutioista on valittu MPEG-4:n kanssa, todellinen resoluutio on aina 640x480.

SNC-CS20-, SNC-DS60- ja SNC-DS10-kamerat tukevat 768x576-resoluutiota vain JPEG-pakkauksen kanssa, mutta tämä resoluutio näkyy System Managerissa myös MPEG-4:n kanssa.

Kaikkien G3-kameroiden P-mallien (3. sukupolvi) enimmäiskuvanopeus on 8 kuvaa sekunnissa (N-mallit 10 kuvaa sekunnissa) H.264-pakkauksella, mutta System Managerin kameran asetuksissa näkyy maksimissaan 25 kuvaa sekunnissa. Koska jotkin kameramallit voivat tuottaa jopa 12 kuvaa sekunnissa, ohjain käyttää tätä arvoa enimmäiskuvanopeutena.

JPEG-pakkauksella System Manager näyttää G2-kameroiden (2. sukupolvi) kuvataajuudeksi 1-25, mutta kamerat tukevat vain 5, 6, 8, 10, 15, 20 (ja 30 NTSC-tilassa) kuvaa sekunnissa.

Esiasetustoiminnot ja yksityisyysvyöhykkeet eivät toimi oikein VMS 5.9.8:ssa. Tämä ongelma johtuu joidenkin ohjelmien rajapintojen yhteensopimattomuudesta.

Joissakin tilanteissa SONY-kamerat alkavat lähettää MJPEG-koodekille videokuvaa vaadittua suuremmalla kuvataajuudella. Esimerkiksi zoomauksen jälkeen SONY SNC-Z20P -kamera lähettää MJPEG-videovirtaa 24-25 kuvaa sekunnissa, vaikka kuvataajuus on asetettu 20:een järjestelmänhallinnassa. Tämä on kameran laiteohjelmiston ominaisuus.

SONY SNC-Z20 -kamera lähettää MJPEG-videovirran pienemmällä kuvataajuudella kuin on tarpeen, kun enimmäistarkkuus- ja laatuasetukset on asetettu. Esimerkiksi maksimikuvanopeus 736x544-resoluutiolla ja 100 % laatuasetuksella ei voi olla suurempi kuin 3. Tämä on kameran ominaisuus.

SONY SNC-Z20 -kamera tukee zoomaus- ja tarkennustoimintoja, mutta se ei tue lainkaan panorointi- ja kallistustoimintoja. VMS näyttää kuitenkin joka tapauksessa Pan/Tilt-ohjauksen Device-ikkunassa (vaikka kamera ei tue Pan/Tilt-toimintoa ja ohjain on poistanut sen käytöstä). Tämä on VMS:n ongelma.

SONY SNC-Z20 -kamera ei tue esiasetustoimintoa. Mutta ”Lisää esiasento” -painike on aina käytössä sitä varten VMS 5.4.4:ssä. Tämä on VMS-ongelma.

SONY SNC-CH210 tukee 2048x1536-resoluutiota vain MJPEG-videokoodekille (kuvasuhdeasetus on asetettava 16:9-arvoon). Muiden koodekkien enimmäisresoluutio on 1600x1200.

Muutamissa G5-kameroissa (5. sukupolvi) on rajoitus yksityisyydensuojan suorakulmion kokoon. Suorakulmion koko ei voi olla suurempi kuin 1/16 kameran kuvasta:

640x480 pikseliä SNC-CH220/DH220-kameroissa (suhteessa maksimiresoluutioon 1920x1080).

200x140 pikseliä SNC-EM520/EM521-kameroissa (suhteessa enimmäisresoluutioon 800x600).

Todelliset yksityisyyden suoja-alueet voivat siis olla alhaisemmat kuin mitä käyttäjät ovat käyttäneet tämän kameran ominaisuuden vuoksi.

SONY G5 -kamerat lähettävät HD-videovirtaa jopa 15 Mbps:n nopeudella. HD-resoluution tilaaminen

korkealaatuisen videon H.264/MPEG-4-koodekille tai HD-resoluutioisen videon MJPEG-koodekille useammasta kuin yhdestä kamerasta voi aiheuttaa viiveitä videovirrassa. Esimerkiksi todellinen kuvataajuus hyppää 2..13:n välein 15 fps-asetuksella.

SONY G5/G6 -kamerat käynnistävät oman videokooderin uudelleen videoasetusten muuttamisen jälkeen. Tämä toiminto kestää 3-8 sekuntia, joten CCRiA- ja CCFiA-toimintoja (vaihtoehtojen muuttaminen hälytyksen perusteella) ei voi käyttää näiden kameroiden kanssa.

SONY SNC-VB630 -kamera käynnistää H.264-virran liikkeellä 10-20 kuvaa sekunnissa sen sijaan, että se soveltaisi 50 kuvaa sekunnissa, kun 1 % laatu on valittu. Käytä 2 %:n laatuarvoa välttääksesi tämän käyttäytymisen.

SONY G6 -kamerat käyttävät laatuasetuksia (muuttuva bittinopeus) H.264-virran laadun asettamiseen. Aiemmat kamerasukupolvet käyttivät CBR (Constant bit-rate) -vaihtoehtoa MPEG-4- ja H.264-koodauksille.

Moninkertainen suoratoisto-ominaisuus on käytettävissä SONY G5- ja G6-laitteissa ja VMS-versiossa 6.1.1 ja uudemmissa. Vanhemmat SONY-laitteet eivät tue tätä ominaisuutta.

SONY G5/G6 -kamerat soveltavat videoasetuksia usean sekunnin ajan ja saattavat lopettaa suoratoiston tämän toimenpiteen aikana. Minkä tahansa striimin käynnistäminen voi siis aiheuttaa muiden aktiivisten striimien uudelleen tilaamisen.

SONY G5 -kameroilla on seuraavat rajoitukset Multiple streaming -ominaisuuden osalta

SNC-RS44/RS46/RS84/RS86-kamerat tukevat enintään kolmea virtausta. Muut G5-laitteet tukevat vain 2 streamia (tallennus ja live).

Toisen striimin resoluutio ei voi olla suurempi kuin 640x480, paitsi jos se on sama kuin ensimmäisen striimin resoluutio.

Kolmannen stream-kuvan resoluution on oltava sama kuin ensimmäisen tai toisen stream-kuvan nykyinen resoluutio.

G5-kamerat eivät ehkä käynnistä videovirtaa, jos MJPEG on valittuna Live stream -tilassa maksimiresoluutiolla. Tämä ongelma johtuu kameran odottamattomasta käyttäytymisestä (RTSP PLAY -pyyntö palauttaa virhekoodin 451). Vaihda koodausta tai pienennä resoluutioasetuksia, jos tämä ongelma ilmenee.

Ajuri valitsee sopivan resoluution automaattisesti asetusten soveltamisen aikana, jos kamera ei tue nykyistä resoluutiota. Virran resoluutio voi siis poiketa VMS:ssä käytetyistä asetuksista. Tutustu kameran Web-käyttöliittymään saadaksesi tietoa videoasetusten rajoituksista.

SONY G5/G6 -kameroissa voi olla ongelmia G.726-äänivirran koodauksessa/dekoodauksessa (kohinaa, ei ääntä jne.). Käytä G.711-koodekkia, jos G.726-koodekissa on ongelmia.

Äänilähtö (lähetys kameraan) ei välttämättä palaudu signaalin menetyksen jälkeen SONY G6 -kameroissa.

Kamera saattaa palauttaa HTTP-virhekoodin 503. Palauttaaksesi äänilähtötoiminnot käynnistä kamera uudelleen Web-käyttöliittymän kautta, ”System” - ”Initialize” - ”Reboot”.

SONY G7 -kameran rajoitukset

”Lähtötilat":

SONY G7 voi toimia useissa eri ”lähtötiloissa”. ”Lähtötila"-vaihtoehtoa voidaan muuttaa Web-käyttöliittymän kohdassa ‘Järjestelmä’ - ‘Asennus’.

Ennen tämän tilan muuttamista on suositeltavaa poistaa kamera VMS:stä. Lähtötilan muuttamisen jälkeen kamera on lisättävä uudelleen järjestelmään.

Moninkertainen suoratoisto on käytettävissä vain seuraavissa ”Lähtötiloissa”:

”4K Multi streaming”

”Älykäs rajaus (FullHD)”

”Älykäs rajaus (VGA)”

”HDMI"-lähtötilassa olevaa kameraa ei voida tunnistaa ja lisätä.

Saatavilla olevien videoresoluutioiden, videokoodekkien ja kuvataajuuksien luettelo on rajoitettu ja riippuu valitusta ”Lähtötilasta” ja ”Kuvasuhteesta”. Lisää kamera uudelleen VMS:ään, kun olet muuttanut tätä tilaa.

SONY G7 -kameroiden kuvataajuusarvot ovat liukulukuarvoja. Ajuri pyöristää arvon lähimpään kokonaislukuun.

H264Quality-vaihtoehtoa ei voida hyväksyä SONY G7 -laitesarjassa. Ajuri muuntaa ”Quality”-arvon H.264-koodekin bittinopeusarvoksi.

SONY G7 -kameroiden ”4K”-lähtötiloissa VMS-videokoodekki ei voi purkaa H.264-korkearesoluutioista virtaa oikein, jos kamerassa on käytössä ”B-kuva”-vaihtoehto. Ajuri poistaa sen oletusarvoisesti käytöstä.

Jos Edge Storage -tallennus on käytössä, H.264-koodekin bittinopeus on rajoitettu enintään 8 Mbps:iin.

SONY H-sarjan laitteet (kuten SNC-HM662-kamera) käyttävät eri SDK:ta kuin muut SONY G6 -kamerat, eikä niitä voi lisätä natiivilla SONY-ajurilla. Käytä sen sijaan Vivotek IP Capture -ajuria tälle laitesarjalle.

SONY SNC-EMX32R/52R -laitteet käyttävät eri SDK:ta kuin muut SONY G6/G7 -kamerat, eikä niitä voi lisätä natiivilla SONY-ajurilla. Käytä sen sijaan BOSCH-ajuria (NewBoschIPCapture) tälle laitesarjalle.

Ajan synkronointitoiminto käyttää seuraavia sääntöjä:

Aikasynkronointimenettely alustetaan jollakin seuraavista ehdoista:

Windows-järjestelmän aika muuttuu;

Windowsin aikavyöhykkeen muutos;

Edellisessä aikasynkronoinnissa tapahtuu jokin virhe;

Edellinen onnistunut synkronointi suoritettiin yli 30 minuuttia sitten.

Nämä olosuhteet tarkistetaan 5 minuutin välein

Uusi aika asetetaan IP-laitteelle, jos laitteen ja tallentimen aikojen välinen ero on vähintään 10 sekuntia.

SONY HTTP API mahdollistaa ajan käyttämisen GMT-muodossa, joten ajuri ei päivitä IP-laitteen aikavyöhykeasetuksia.

Vaihtoehtojen muuttaminen hälytystilanteessa (CRiA/CFA) -toimintoa voidaan käyttää vain ”aktiivisessa” ohjaustilassa. Passiivisessa tilassa ohjain ei muuta mitään IP-kameran vaihtoehtoa, joten virta jatkuu ilman, että resoluutio tai kuvataajuus muuttuu.

Windows XP:tä ei tueta ajuriversiosta 2.6.0.0 lähtien.




Pagination
Previous page
NewSiquraIPCapture - Asennus ja käyttö
Next page
OnvifIPCapture - Asennus ja käyttö