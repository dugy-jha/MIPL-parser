# Kameroiden lisääminen CSV-tiedoston avulla | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/kameroiden-lisaaminen-csv-tiedoston-avulla

Kameroiden lisääminen CSV-tiedoston avulla

Kameraroiden asetukset voidaan viedä CSV-tiedostoon ja tuoda CSV-tiedostosta VMS-palvelimelle. Näin järjestelmänvalvojat voivat tehdä joukkomuutoksia kameran asetuksiin ja tuoda sitten muutetut asetukset VMS-järjestelmään. VMS:ään on myös mahdollista lisätä uusia kameroita tällä toiminnolla.

CSV-tiedoston tuonti ja vienti

System Manager laitteistoasetuksissa on seuraavat painikkeet kameran asetusten viemiseen tiedostoon ja kameran asetusten tuomiseen tiedostosta CSV-muodossa.




CSV tiedoston formaatti

Jokaisen kameran CSV-tiedostomuoto käyttää seuraavia otsikon nimiä.

Name - Kamerakanavan nimi.

Number - Kamerakanavan numero VMS-palvelimella.

Description - Kamerakanavan kuvaus.

AdmDescription - Kamerakanavan järjestelmävalvojan kuvaus.

Address - Kameralaitteen osoite.

Port - Kameralaitteen portti.

UserName - Kameralaitteen käyttäjänimi.

Password - Kameralaitteen salasana.

Driver - Ajurin nimi / native (haetaan kaikilla natiiveilla ajureilla) / onvif (käytetään vain ONVIF ajuria. Toiminto käyttää ensimmäistä ajuria, jonka nimessä on annettu ajurin nimi. Esimerkiksi, axis → NewAxisIPCapture.

Channel - Laitteen kanavanumero, jos laite tukee useampaa kuin yhtä kanavaa. Yhden kanavan laitteilla tämä voidaan jättää tyhjäksi.

IsInUse - Onko kamerakanava käytössä.

IsAudioInUse - Onko laitteen audio käytössä, jos laite tukee audiokanavia.

IsIOInUse - Onko laitteen I/O kanavat käytössä. Asetusta käytetään vain, kun asetuksia viedään CSV-tiedostoon. Tuonnissa I/O kanavat otetaan käyttöön, jos laite tukee niitä.

Is360 - Onko laite 360 kamera.

Framerate - Tallennusstriimin kuvatahti pyöristettynä lähimpään tuettuun arvoon. Muiden striimien otsikot: Framerate1, Framerate2, Framerate3.

Resolution - Tallennusstriimin kuvatahti formaatissa leveys x korkeus (esim 1920x1080) pyöristettynä lähimpään tuettuun arvoon. Muiden striimien otsikot: Resolution1, Resolution2, Resolution3.

Codec - Tallennusstriimin käyttämä kompressiotapa pyöristettunä lähimpään arvoon: JPEG, MPEG, H264, WMC9, PARSE, H265, MXPEG. Muiden striimien otsikot: Codec1, Codec2, Codec3.

Quality - Tallennusstriimin käyttämä kompressiolaatu pyöristettunä lähimpään arvoon arvoalueella 1-100. Muiden striimien otsikot: Quality1, Quality2, Quality3.

Bitrate - Tallennusstriimin käyttämä bit rate arvo pyöristettynä lähimään tuettuun arvoon. Muiden striimien otsikot: Bitrate1, Bitrate2, Bitrate3.

Vienti

Käyttäjä voi valita kansion, johon kameran asetusten CSV-tiedosto viedään, ja antaa tiedoston nimen. Käyttäjä voi myös määrittää erottimen, jota käytetään CSV-tiedostossa.

Kun vienti onnistuu, vilkkuva vihreä kuvake näytetään. Virhetilanteessa näkyy vilkkuva punainen kuvake.

Tuonti

Kun käyttäjä napsauttaa tuontipainiketta, näkyviin tulee Valitse tiedosto -valintaikkuna, jossa voit valita tuotavan CSV-tiedoston. Kun tiedosto on valittu, kameran lisäysnäkymä näytetään, jos CSV-tiedoston jäsennys ja vahvistus on suoritettu onnistuneesti.

Seuraavia vahvistussääntöjä käytetään tuodun CSV-tiedoston jäsentämiseen.

CSV-tiedoston sarakkeen erotin on pilkku (,) tai puolipiste (;).

Otsikkojen nimien järjestys (eli sarakejärjestys) on vapaa.

Käyttämättömät otsikkonimet (eli sarakkeet) voidaan jättää pois.

Vain Address-otsikon nimi on pakollinen. Jos se puuttuu, CSV-tiedoston tietoja ei hyväksytä.

Jos joitain ominaisuuksien nimiä ja tietoja ei ole olemassa, käytetään sisäistä oletusarvoa.

Vahvistusvirheitä ja varoituksia varten luodaan ponnahdusikkuna, ja lisätietoja tulostetaan System Managerin lokiin.

CSV-tiedoston kautta tuodut kamerat voidaan asettaa passiiviseen tilaan osana tuontiprosessia. Järjestelmänvalvojat voivat määrittää tämän asetuksen CSV-tiedostossa.

Usean suoratoiston tilaa (käytössä tai pois käytöstä) voidaan käyttää, kun kamera tukee sitä, sekä bittinopeustilaa bittinopeuden osalta.

Äänikanavia ei saa lisätä automaattisesti, jos sitä ei ole lisätty CSV-tiedostojen tuonnin yhteydessä.

Huomaa, että tuotaessa monikanavaisia laitteita, joilla on asetettu kanavanumero sarakkeessa "Numero", kullekin laitteelle on määritettävä kanavanumero manuaalisesti. Tallentimen kanavanumero (sarakkeesta Number) on myös määritettävä laitteen kanavanumerolle (sarake Channel). Tämä voidaan ratkaista jättämällä Number- ja Channel-sarakkeet pois.

CSV-tiedoston tarkistuksen ja jäsentämisen jälkeen tilasarake ilmoittaa, onko kamera jo lisätty järjestelmään (On järjestelmässä) vai onko se uusi kamera (Ei lisätty).

Lisää- ja Muokkaa-valintaruudut tulevat näkyviin, jos tuodussa CSV-tiedostossa on sekä muutoksia olemassa oleviin kameroihin että uusia kamerakokoonpanoja.

Näillä vaihtoehdoilla voidaan valita, lisätäänkö ja/tai muokataanko CSV-tiedoston kameroita. Suorita-painike on käytössä, kun kameroita on lisättävä tai muokattava. Napsauttamalla Suorita-painiketta CSV-tiedoston asetukset otetaan käyttöön (muokataan ja/tai lisätään) nykyisiin asetuksiin.

Asetusten voimaantulon jälkeen kunkin kameran tila päivitetään, valintaikkuna voidaan sulkea asetusten voimaantulon jälkeen napsauttamalla ok-painiketta tai peruutuspainikkeesta ennen asetusten käyttöönottoa.

Muokatut kamera-asetukset ja/tai lisätyt kamerat otetaan käyttöön VMS-palvelimessa, kun laitteistoasetukset on tallennettu.

Pagination
Previous page
Laitteistoasetukset
Next page
VMS-videonhallintapalvelimien lisäys ja poisto