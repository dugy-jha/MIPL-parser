# PelcoIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/pelcoipcapture-asennus-ja-kaytto

PelcoIPCapture - Asennus ja käyttö

Ajuri käyttää RTSP/RTP/UDP/IP-protokollia MPEG-4- ja H.264-videon vastaanottoon.
HTTP-protokollaa käytetään parametrien asettamiseen/hakuun, JPEG-videon vastaanottoon.
ja PTZ-toimintoihin.

Jos VMS:n ja kameroiden välissä on palomuuri, seuraavat RTSP/UDP/HTTP- ja
portit on avattava:

HTTP: oletusportti on 80 Sarix-kameroille ja 49152 muille kuin Sarix-kameroille,

RTSP: portti 554,

UDP: Tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3556-4556.

TCP: 3549 on GENA DigitalInputs -ilmoitusten oletusportti.

Katso myös PelcoIPCapture.xml, DigitalIOListener-osio, porttiarvo.

Esimerkiksi: jos VMS:ssä on neljä Pelco-kameraa, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se ohitetaan.

Sarixin, Enduran ja vesrionin uusimman sarjan ohjain 1.8.0.0.0 käyttää GENA-ilmoitusarkkitehtuuria. Ajuri määrittää automaattisesti Windowsin palomuurin sallimaan saapuvat yhteydet DigitalIOListener-porttiin. Katso myös addFirewallRule-vaihtoehto.

”DigitalIOListener"-osion ‘address’- ja ‘port’-vaihtoehtoja voidaan käyttää ulkoisen IP-osoitteen ja portin määrittämiseen, jos portti välitetään ulkoisesta verkosta samaan TCP-porttiin.

Rajoitukset

Muiden kuin Sarix-kameroiden JPEG-koodekin laadun ja resoluution määrittäminen ei ole tuettu. Kaikki JPEG-kuvat vastaanotetaan 4CIF-muodossa. SystemManager-kameran asetukset jätetään tässä tapauksessa huomiotta.

Pelco Sarix -kameroita voidaan käyttää SOAP-pyyntöjen kautta ilman käyttäjän todennusta oletusarvoisesti. Kuka tahansa valtuuttamaton käyttäjä voi siis tilata ja konfiguroida Pelco Sarix -kameran. Tällaisen käyttäytymisen välttämiseksi aseta ”Public User Access Level” -asetukseksi ”Disabled” Web-käyttöliittymän Users-välilehdellä.

Firmware-versiota ei voi hakea Pelco IP -kameroista. Tämä on Pelco API:n ominaisuus.

Pelco-kamerat soveltavat videovirran asetuksia noin 30 sekunnin kuluessa. CCRiA- ja CCFiA-ominaisuuksia ei siis voida toteuttaa Pelco IP -kameroissa.

Sarix MPEG-4 -kooderi ei tue yli 704x576-resoluutiota. Ajuri asettaa resoluution automaattisesti 704x576:een, jos käyttäjä yrittää käyttää suurempaa resoluutiota.

Ohjain ei voi vastaanottaa useita tuloja ja/tai lähtöjä IP110-kameralle ajoittain. Voit korjata tämän ongelman poistamalla kameran kameraluettelosta ja lisäämällä sen sitten uudelleen.

JPEG-pakkauksen todellinen kuvanopeus voi olla pienempi kuin vaadittu kuvanopeus, koska HTTP:n kautta tapahtuvassa kuvien kaappauksessa on viiveitä.

SARIX-kameroiden IO-toiminto ei toimi tällä hetkellä oikein. Tulojen tiloja ei voida hakea. Lähtökomponentti ei toimi kunnolla, koska tulojen tiloja ei tunneta.

Luettelo tuetuista kuvataajuuksista voi vaihdella Sarix-kameroiden eri koodekkien välillä. Jos käyttäjä yrittää käyttää tukematonta kehysnopeusarvoa, käytetään seuraavaksi suurempaa kehysnopeusarvoa (esimerkiksi arvoa 7,5 tukemattoman arvon 6 sijasta). Jos käyttäjä yrittää käyttää suurempaa arvoa kuin tuettu enimmäisarvo, enimmäisarvoa käytetään automaattisesti. Katso luettelo tuetuista kehysnopeusarvoista kameran Web-käyttöliittymästä.

Nopeusparametri ei ole tuettu Pelco PTZ IP -kameroissa seuraavissa PTZ-toiminnoissa:

Tarkennus;

Zoomaaminen;

Iiriksen vaihtaminen;

Siirtyminen esiasetettuun sijaintiin. Kuljettaja siis käyttää näitä toimintoja sellaisenaan: kamera käsittelee ne kaikissa tapauksissa vakionopeudella.

Spectra HD -kamera lähettää H.264-videovirran vaadittua alhaisemmalla kuvataajuudella (esimerkiksi todellisella 1 fps sovelletun 4 fps:n sijasta), jos kuvataajuuden arvo on tasainen. Useimmat parittomat arvot (paitsi 1 ja 25) käsitellään oikein. Tämä on laiteohjelmistoon liittyvä ongelma.

Ajuri ei pysty jäsentämään kameran SOAP-vastausta, jos konfiguraationimissä käytetään epästandardeja symboleja (kuten umlauteja tai hieroglyfejä). Näiden symbolien käyttö voi aiheuttaa virheellistä ajurin käyttäytymistä, joten vältä näiden symbolien käyttöä, kun konfiguroit Sarix-kameraa Web-käyttöliittymän kautta.

Pelco 1080p -kamerat eivät ehkä lähetä H.264-koodattua videovirtaa 1080p-resoluutiolla pienillä kuvanopeuksilla (1-4). Tämä on Pelcon laiteohjelmiston tunnettu ongelma. Katso lisätietoja Pelco Knowledge Base -tietokannasta: <http://www.pelco.com/sites/global/en/sales-and-support/faq/faq_main.page?AID=12392>

Ratkaise ongelma VMS-ohjelmistossa käyttämällä alhaisinta laatua näille asetuksille.

Digitaalitulojen kyselyyn käytetty GetAlarmStates-kutsu on vanhentunut, eikä Pelcon tukitiimi suosittele sitä kaupalliseen käyttöön. Digitaalisten tulojen kysely 2 sekunnin välein voi aiheuttaa kameran roikkumisen 2-3 päivän työskentelyn jälkeen. Digitaalitulotoiminto on siis oletusarvoisesti poistettu käytöstä, mutta se voidaan ottaa käyttöön XML-konfigurointitiedoston avulla, jos sitä tarvitaan.

Kamera voidaan joutua lisäämään uudelleen konfiguraatiotiedoston muutoksen jälkeen.

Portti 3549 on sallittava saapuville yhteyksille Windowsin palomuurissa Sarix-, Endura- ja sitä uudempien sarjojen DigitalIO-toimintoa varten. Katso myös PelcoIPCapture.xml, DigitalIOListener-osio, porttiarvo.

Kameroiden vanhemmissa versioissa on ongelma, jos Digital Outputs -pyyntöjä lähetetään hyvin usein. Jos käyttäjä konfiguroi usein vaihtuvat lähdöt (useammin kuin yksi kytkentä minuutissa), kamera saattaa roikkua useiden päivien jälkeen. Välttääksesi tämän ongelman ota Digital Outputs -toiminto pois käytöstä ajurin konfigurointitiedoston avulla.

Pelco Optera-sarjan panoraama-IP-kameroissa (IMM12018-, IMM12027- ja IMM12036-mallit) on erityinen toteutus stream dewarpingille, jota ei ole vielä integroitu natiiviin ohjaimeen.

Käytä sen sijaan ONVIF IP Capture -ajuria tämän laitesarjan laitteille.




Pagination
Previous page
OnvifIPCapture - Asennus ja käyttö
Next page
PSIAIPCapture - Asennus ja käyttö