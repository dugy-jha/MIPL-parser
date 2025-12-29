# NewActiIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/newactiipcapture-asennus-ja-kaytto

NewActiIPCapture - Asennus ja käyttö

Kaikissa pakkaustiloissa ohjain käyttää videon vastaanottoon RTSP/RTP/UDP/IP-protokollia. HTTP-protokollaa käytetään parametrien asettamiseen/hakuun.

Jos DVMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP-portit on avattava:

HTTP: oletusportti on 80,

RTSP: portti 7070,

UDP: tarvitaan kaksi peräkkäistä porttia videovirtaa kohden porttialueella 3556-5556.

NewActiIPCapture.xml-tiedostoa käytetään konfigurointiin:

Kuljettajan käyttäytyminen:

Unicast

Multicast:Primary

Multicast:Listener

Kameran virtaustila ja kiinnitystyyppi (kalansilmäkamerat) hyväksyvät kameran de-warpingin.

Virtaustilojen mahdolliset arvot: SINGLE, DUAL, EPTZ, MD_PRESET, FISHEYE_VIEW

Asennustyyppien mahdolliset arvot: WALL, CEILING

ACTi-videopalvelimien ensimmäinen PTZ-kanavan tunnus:
Yleinen ja IP-laitekohtainen konfigurointi on käytettävissä
Esim:
<Device address="192.168.1.75" port="80">
<FirstPTZChannelID>2</FirstPTZChannelID>
</Device>
Laitteen 192.168.1.75:80 ensimmäinen PTZ-kanavatunnus on 2, seuraava (monikanavainen laite) on 3 jne.

Rajoitukset

ACTi TCM-5311 voi lakata lähettämästä oikeaa virtaa, kun taustavaloa vaihdetaan äkillisesti.

ACTi MPEG4 -kamerat tarvitsevat viiveen parametrien asettamisen ja stream-virran käynnistämisen välillä (noin 3 sekuntia).

ACTi CAM-6510 ei toimi oikein 1 fps:n nopeudella, joten tämä arvo ei ole käytettävissä tässä kamerassa. ACTi CAM-6510 -kamera ei tue laadun muuttamista, joten kaikkien arvojen laatu on sama.

ACTi-kameroissa on eri kuvanopeudet eri pakkausmuodoille. Asetukset muunnetaan automaattisesti lähimpään oikeaan arvoon.

ACTi E96-, B54-, B55- ja B56-kamerat eivät tue de-warping-toimintoa kamerassa, joten XML-asetuksella ei ole vaikutusta näihin malleihin.

ACD-videopalvelimet toimivat vain, kun kuhunkin kanavaan on liitetty yksi PTZ-kamera, jonka kameratunnus on 1. Esimerkiksi ACD2100 toimii vain yhdellä kameralla ja ACD2200 neljällä kameralla. ACD:n monikanavaisissa laitteissa on eri RS485-portit PTZ-kameraliitäntöjä varten, ja kaikkien kameratunnusten on oltava yhtä suuria kuin 1.

ACTi-kameroiden todellinen kuvataajuus voi poiketa asetuksista. Se riippuu kameran asetuksista (objektiivin kompensointi ja suljinnopeus) ja valaistustasosta.

Videokamerat eivät tue I/O-toimintoa. Ne toimivat PAL-järjestelmässä, mutta tehdasasetuksena on NTSC. Tehdasasetusten soveltamisen jälkeen kamera ei toimi.

SED2100 toimii ACTi-kirjastojen kanssa. SED2100:n on tallennettava uudelleenkäynnistys jokaisen parametrimuutoksen jälkeen (kestää 30-60 sekuntia).

Esiasetusten nimet tallennetaan XML-tiedostoon (ei kameran esiasetusten hallintaa).

KCM:ssä K2-kalansilmäkameraa voidaan käyttää kahdessa videovirtatilassa: SINGLE ja EPTZ. Stream-tila tunnistetaan kameran tilatessa DVMS:ää, jolloin ohjain pitää tämän tilan. Stream-tilan vaihtamiseksi kamera on poistettava DVMS:stä, stream-tila on vaihdettava kameran web-käyttöliittymän kautta, ja sen jälkeen kamera voidaan tilata. Ajuri asettaa sen automaattisesti kaikille muille KCM- ja TCM-sarjoille SINGLE-videovirtatilaan.

ACTi-ajuri käyttää vakio-bittinopeusasetuksia, jotka skaalataan vastaavasta VMS-laatuarvosta:

CAM-arvot: 256K, 384K, 500K, 750K, 1M, 1.5M, 2M, 2.5M, 3M

ACM-arvot: 28K, 56K, 128K, 256K, 384K, 500K, 750K, 1M, 1.2M, 1.5M, 2M, 2.5M, 3M, UNLIMITED

TCM/KCM-arvot: 28K, 56K, 128K, 256K, 384K, 500K, 750K, 1M, 1.2M, 1.5M, 2M, 2.5M, 3M, 3.5M, 4M, 4.5M, 5M, 5.5M, 6M, UNLIMITED

VMS-laatu 50 % skaalautuu siis 1 Mbit/s bittinopeuden arvoon. Oikea DVMS-laatu on asetettava vastaamaan vaadittua verkon kaistanleveyttä.

ACTi-videopalvelimissa ei ole sisäistä PTZ-protokollaa; ne lähettävät PTZ-komennot uudelleen kameran COM-porttiin läpinäkyvässä tilassa. Tällä hetkellä vain PelcoD-protokolla on toteutettu. Jos ACTi-videopalvelimeen liitetty analoginen kamera ei toimi PelcoD:n kanssa, ohjainta ei voi käyttää kameran ohjaamiseen.

ACTi fish-eye -mallit eivät tue kaikkia virtaustiloja. Esimerkiksi ACTi I51 tukee vain DUAL (Panorama), FISH_EYE ja EPTZ stream -tiloja. Muilla asetuksilla ei ole vaikutusta ja niitä käytetään stream-tilassa, joka on asetettu kamerassa.

Stream-tila ja asennustyyppi on asetettava ennen kameran lisäämistä DVMS:ään. Näiden arvojen muuttamiseksi käyttäjän on poistettava kamera DVMS:stä, tehtävä muutokset asetustiedostoon ja lisättävä kamera uudelleen DVMS:ään.

Kalansilmäkameran moninkertaista suoratoistoa tuetaan vain näissä suoratoistotiloissa:

DUAL - 2 streamia

MD_PRESET - 2 virtaa WALL-asennustyypissä, 3 osoitteessa CEILING

Digitaalinen PTZ toimii kalansilmäkamerassa vain EPTZ stream -tilassa.

Jos resoluutiota tai stream-tilaa on muutettu, kalansilmäkameran esiasetuksista tulee virheellisiä, ne on poistettava DVMS:stä ja määritettävä uudelleen.

MPEG4 on pois päältä DUAL stream -tilassa, koska se on käytettävissä vain 1. streamissa.

6VGA- ja 4VGA-suoratoistotiloja ei tueta.

NewActiIPCapture.xml-tiedoston Stream-tila-asetukset koskevat vain kalansilmäkameroita. Muiden kameroiden stream-tila-asetukset saadaan kamerasta, kun se lisätään DVMS:ään. Jos kamerassa on DUAL stream mode -asetus - moninkertainen suoratoisto on aktiivinen, jos SINGLE - ei.

DUAL stream -tilassa stream 1:n kuvataajuuden on oltava suurempi tai yhtä suuri kuin stream 2:n. Muussa tapauksessa stream 1:n kuvataajuus on rajoitettu stream 2:n kuvataajuuteen. Esimerkiksi stream 1:n ja stream 2:n kuvataajuusasetukset ovat 30 ja 25. Virran 1 todellinen kuvataajuus on 25

KCM/TCM-kamerat eivät voi ottaa käyttöön yksityisyysmaskeja toisessa virrassa. Yksityisyysmaskit otetaan siis käyttöön vain yksivirtaisissa tiloissa (kamerassa on oltava yksivirtainen tila ennen sen lisäämistä DVMS:ään). KCM/TCM-kameroissa on yleinen ongelma, joka liittyy yksityisyysmaskeihin ja resoluutioihin, joiden resoluutio on vähintään 1920x1080 - yksityisyysmaski voidaan asettaa vain näytön vasempaan osaan (ACTi-rajoitus).

ACTi ACM -kameroissa on ongelma yksityisyysmaskiasetusten kanssa. Yksityisyysmaskin sijainti on oikea vain enimmäisresoluutiolla; pienemmillä resoluutioilla yksityisyysmaskin sijainti voi poiketa asetuksista.

ACTi ACM -sarjan kamerat voivat palauttaa liiketunnistusominaisuuden, mutta kameran verkkosivulla ei ole määritettävissä MD-arvoa. Näissä malleissa ei voida käyttää ”Tallennin ja kameralaitteisto” MD:tä.

Multicast ei ole käytössä ACTi CAM -malleissa. Kaikki nämä mallit toimivat vain Unicastilla. Näitä kameroita ei voi käyttää useissa DVMS-instansseissa!

Unicast mode: Ajuri muuttaa kameran asetukset DVMS-asetusten mukaisesti ja vastaanottaa ääni- ja videotiedot kamerasta unicast-yhteyden avulla.

Multicast:Primary: Ajuri muuttaa kameran asetuksia DVMS-asetusten mukaisesti ja vastaanottaa ääni- ja videotiedot kamerasta multicast-yhteyden avulla.

Multicast:Listener: ajuri ei muuta kameran asetuksia, vaan vastaanottaa vain ääni- ja videodataa kamerasta multicast-yhteyden avulla.

Jos kameraa käytetään useissa DVMS-instansseissa, yhdelle DVMS:lle on määritettävä Multicast:Primary ja muille Multicast:Listener.

Useita Multicast:Primary -konfiguraatioita tai Multicast:Primary- ja Unicast-konfiguraatioita ei sallita; muissa tapauksissa kameran pitäisi olla ylikuormitettu jatkuvilla samanaikaisilla asetusmuutoksilla.

Reunatallennusta tuetaan vain DEBI-sarjassa laiteohjelmistosta 6.07.23 ja uudemmista versioista alkaen.

Kamera on synkronoitu UTC (GMT +00) -aikaan, jotta vältytään paikalliseen aikaan liittyviltä ongelmilta.

RTP over RTSP -tila ei toimi seuraavissa kamerasarjoissa. Nämä kamerat eivät tue tätä tilaa tai niitä ei ole täysin testattu:

VIDO AMU-xxx

ACTI KCM-xxx

ACTI ACM-xxx







Pagination
Previous page
LGEIPCapture - Asennus ja käyttö
Next page
NewArecontIPCapture - Asennus ja käyttö