# Hälytykset | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/halytykset

Hälytykset
Hälytysasetukset

Hälytysten hallintatyökalut mahdollistavat palvelinkohtaisten hälytysten luomisen erilaisiin liipaisuihin perustuen liikkeeseen, äänitasoon tai tiettyyn tekstidatatriggeriin.

Lisäksi laukaisimet voivat sisältää räätälöityjä kolmannen osapuolen liipaimia.

Hälytyksiä voidaan luoda, muokata ja poistaa VMS-videonhallintapalvelimet -välilehden Hälytykset -valikon kautta.




Uuden hälytyksen lisääminen
Yleinen

Valitse Uusi hälytys vasemmasta alakulmasta

Määritä hälytyksen nimi Nimi-kenttään

Kirjoita uuden hälytyksen Yleinen kuvaus ja Ylläpitäjän kuvaus vastaaviin kenttiin Nimi-kentän alla.

Valitse hälytyksen prioriteetti Korkea, Normaali tai Matala Prioriteettia käytetään määrittämään järjestys, jossa hälytykset suoritetaan, jos samanaikaisesti on useita hälytyksiä.

Valitse Hälytys on aktiivinen, kunnes se kuitataan luodaksesi hälytyksen jatkuvaksi; jos vaihtoehto valitaan, hälytys jatkuu, kunnes käyttäjä kuittaa sen Spotter-sovelluksen kautta.

Hälytyksen korostusvärin avulla järjestelmänvalvojat voivat määrittää mukautetun värin jokaiselle hälytykselle erikseen.

Valitse Käytä hälytystä profiileissa -valikosta profiilit, joissa hälytystä käytetään.   Huom: Hälytyksiä voidaan myös lisätä profiileihin Profiilit-välilehden kautta.

Laukaisin

8. Avaa Laukaisin-välilehti Laukaisin-välilehteä käytetään määrittämään laukaisimet, jotka käynnistävät hälytystapahtuman.

9. Valitse laukaisimen tyyppi avattavasta Tyyppi-valikosta.

Kamera

Ääni

Metadata

Teksikanava

Digitaalitulo

10. Valitse laite, joka laukaisee hälytyksen avattavan Tyyppi-valikon alla olevasta laiteluettelosta.

11. Valitse laukaiseva ehto näytön oikealla puolella olevasta ehtoluettelosta.

Kamerapohjaisissa laukaisuissa voit valita liiketunnistuksessa käytettävän maskin hälytyksen laukaisemiseksi.

Äänipohjaisissa laukaisuissa voit asettaa hälytyksen laukeamaan korkean tai matalan äänitason perusteella.

Tekstidataan (esim. VCA, metatieto jne.) perustuville liipaisuille voit asettaa hälytyksen laukeamaan tekstidatamerkkijonon perusteella.
 Lisäksi voit asettaa valinnaisen hälytyksen päättymislaukaisun merkitsemällä Määritä lopputulo ja valitsemalla merkkijonon. hälytyksen lopettamiseksi.

Digitaalituloon perustuvissa liipaisuissa hälytys laukeaa tulon napaisuuden muutoksen perusteella.

Toiminnot

12. Avaa Toiminnot-välilehti Toiminnot-välilehteä käytetään määrittämään toiminnot, jotka hälytys suorittaa, kun se on aktiivinen.

13. Valitse toimintotyyppi avattavasta Tyyppi-valikosta. Toimintotyyppi määrittelee hälytyksen perustoiminnot.

Toimintotyypit ja asetukset

Alla oleva luettelo sisältää oletustoimintotyypit ja niiden parametrit. Jotkut yllä luetelluista toimintotyypeistä eivät välttämättä ole käytettävissä kaikissa järjestelmissä.

Huom: Oletustoimintojen lisäksi järjestelmä voi sisältää kolmannen osapuolen moduulien kautta asennettuja hälytystoimintoja.

Videotallennus

Videotallennus on kameroiden oletustoiminto. Kun tämän toimintotyypin sisältävä hälytys laukeaa, kameran oletusasetusten sijaan käytetään hälytystyypin määrittämiä tallennusasetuksia.

Jos Spotter:ssä hälytyksen ponnahdusikkunat on otettu käyttöön käyttäjäprofiilissa, Videotallennus -toiminnolla käytetyt laitteet näkyvät hälytyksen ponnahdusikkunassa, kun hälytys laukeaa.

Toiminto sisältää seuraavat kentät ja parametrit:

A) Viitekuva. Tämä staattinen kenttä sisältää kameran vertailukuvan (kuva).

B)Käytä kamera-asetuksia. Hälytystallennus suoritetaan kamerakohtaisella resoluutiolla ja tallennusnopeudella valitsemalla tämä valintaruutu.

C) Resoluutio. Käytä liukusäädintä muuttaaksesi IP-kameran resoluutiota hälytyksen tallennuksen aikana. Liukusäädin on aktiivinen vain IP-kameroissa.

D)Kuvatahti. Käytä liukusäädintä muuttaaksesi kameran kuvatahtia hälytyksen tallennuksen aikana. Liukusäädin ei ole aktiivinen, jos Käytä kamera-asetuksia -valintaruutu on merkitty.

E) Esitallennus. Valitse tämä valintaruutu ottaaksesi tapahtumaa edeltävän tallennuksen käyttöön. Tapahtumaa edeltävän tallennuksen kesto voidaan asettaa Tapahtumaa edeltävä tallennusaika -liukusäätimellä.

F) Tapahtuman jälkeinen tallennus. Valitse tämä valintaruutu ottaaksesi tapahtuman jälkeisen tallennuksen käyttöön. Tapahtumaa edeltävän tallennuksen kesto voidaan asettaa Tapahtuman jälkeinen tallennusaika -liukusäätimellä.

G) Esi-ja jälkitallennuksen kesto. Näitä liukusäätimiä voidaan käyttää asettamaan toiminnon tallennusaika ennen ja jälkeen tapahtumaa. Liukusäätimet ovat aktiivisia vain, jos tapahtumaa edeltävä ja/tai tapahtuman jälkeinen tallennus on aktivoitu.

Huomautus Kaikki laitteet (kamerat ja mikrofonit) on liitetty hälyttimeen, ja niiden tapahtumaa edeltävä ja jälkinauhoitus on aktivoitu jakaakseen saman tallennusajan ennen ja jälkeen tapahtuman.

Audiotallennus

Äänen tallennus on mikrofonien oletustoiminto. Kun tämän toimintotyypin sisältävä hälytys laukeaa, hälytystyypin määrittämiä tallennusasetuksia käytetään mikrofonin oletusasetusten sijaan.

Jos Spotter:ssä hälytyksen ponnahdusikkunat on otettu käyttöön käyttäjäprofiilissa, Audio-tallennus-toiminnolla käytetyt laitteet näkyvät hälytyksen ponnahdusikkunassa, kun hälytys laukeaa.

Toiminto sisältää seuraavat kentät ja parametrit:

A)Esitallennus. Valitse tämä valintaruutu ottaaksesi tapahtumaa edeltävän tallennuksen käyttöön. Tapahtumaa edeltävän tallennuksen kesto voidaan asettaa Tapahtumaa edeltävä tallennusaika -liukusäätimellä.

B)Jälkitallennus Valitse tämä valintaruutu ottaaksesi tapahtuman jälkeisen tallennuksen käyttöön. Tapahtumaa edeltävän tallennuksen kesto voidaan asettaa Tapahtuman jälkeinen tallennusaika -liukusäätimellä.

C) Esi- ja jälkitallennuksen kesto. Näitä liukusäätimiä voidaan käyttää asettamaan toiminnon tallennusaika ennen ja jälkeen tapahtumaa. Liukusäätimet ovat aktiivisia vain, jos tapahtumaa edeltävä ja/tai tapahtuman jälkeinen tallennus on aktivoitu.

Huom: Kaikki hälyttimeen yhdistetyt laitteet (kamerat ja mikrofonit) ovat aktivoineet tapahtumaa edeltävän ja jälkeisen tallennuksen, jotta ne jakavat saman tapahtumaa edeltävän ja jälkeisen tallennusajan.

Digitaaliset lähdöt

Digitaalinen lähtö on digitaalisten I/O-laitteiden oletustoiminto. Kun tämän toimintotyypin sisältävä hälytys laukeaa, I/O-laite aktivoituu.

Huom: Vaikka toimintotyypin Esi- ja jälkitallennuksen kesto -liukusäätimet näytetään, ne eivät vaikuta toiminnon toimivuuteen.

PTZ-kameran esiasento

PTZ-kameran esiasento toimintoa käytetään ohjaamaan PTZ-kamera haluttuun esiasentoon Kun tämän toimintatyypin sisältävä hälytys laukeaa, PTZ-kamera siirtyy automaattisesti valittuun esiasetettuun asentoon. Katso Spotter -käyttöoppaasta lisätietoja PTZ-kameran esiasetusten asettamisesta.

On huomattava, että tämä toiminto siirtää PTZ-kameran esiasetettuun asentoon, mutta se ei johda PTZ-kameran videosyötteen näyttämiseen asiakassovelluksen hälytysnäkymässä, ellei muita hälytystoimintoja, kuten Videotallennus,ole tehty. valittu PTZ-kameralle.

Toiminto sisältää seuraavat kentät ja parametrit:

Esiasento Käytä pudotusvalikkoa valitaksesi esiasetettu asento, johon PTZ-kamera siirtyy hälytyksen aikana.

Huom: Vaikka toimintotyypin Esi- ja jälkitallennuksen kesto -liukusäätimet näytetään, ne eivät vaikuta toiminnon toimivuuteen.

PTZ-kamerakierto

PTZ-kamerakierros -toimintoa voidaan käyttää asettamaan PTZ-kamera aloittamaan esiohjelmoidun PTZ-kamerakierroksen. Kun tämän toimintotyypin sisältävä hälytys laukeaa, valittu PTZ-kamerakierros alkaa. Katso Spotter käyttöohjeesta lisätietoja PTZ-kamerakierrosten asettamisesta.

On huomattava, että tämä toiminto aloittaa PTZ-kamerakierroksen, mutta se ei johda PTZ-kameran videosyötteen näyttämiseen asiakassovelluksen hälytysnäkymässä, ellei muita hälytystoimintoja, kuten Videotallennus, ole valittu PTZ kameralle.

Toiminto sisältää seuraavat kentät ja parametrit:

Ohjelma. Valitse avattavasta valikosta PTZ-kamerakierros hälytyksen laukaisemisesta alkaen.

Huom: Vaikka toimintotyypin Esi- ja jälkitallennuksen kesto -liukusäätimet näytetään, ne eivät vaikuta toiminnon toimivuuteen.

Aseta liikkeentunnistusmaski

Aseta liiketunnistusmaski -toiminto voi muuttaa tietyn kameran hälytyksen aikana käyttämää liiketunnistusmaskia. Kun hälytys tapahtuu, määritetyn kameran liiketunnistusmaski muutetaan hälytyskohtaiseksi maskiksi. Hälytyksen päätyttyä järjestelmä palauttaa oletusmaskin.

Toiminto sisältää seuraavat kentät ja parametrit:

Maski Valitse pudotusvalikosta liiketunnistusmaski, jota käytetään hälytyksen aikana.

Huom: Vaikka toimintotyypin Esi- ja jälkitallennuksen kesto -liukusäätimet näytetään, ne eivät vaikuta toiminnon toimivuuteen.

Sähköpostin lähetys

Sähköpostin lähetys -toimintoa voidaan käyttää sähköpostin lähettämiseen mihin tahansa sähköpostiosoitteeseen tai ryhmään, joka on määritetty Järjestelmä-välilehden Sähköpostiasetuksissa.

Voit valita, kenen vastaanottajan tai ryhmän tulee vastaanottaa hälytys.

Voit myös sisällyttää hälytyssähköpostiin yhden tai useamman skaalaamattoman tai pienennetyn kuvan. Poista valinta Lähetä lyhyessä muodossa -vaihtoehdosta ja valitse Liitä kuvia -vaihtoehto.

Tämän jälkeen voit valita kameran, kuvan skaalauskoon, halutun kuvien määrän ja aikajänteen, jolta kuvat noudetaan.

Huom:

Kuvien määrä tässä kokoonpanossa on suurin toimitettava määrä. Kuvia saattaa saapua vähemmän

Kuvien liittäminen hälytyssähköpostiin saattaa johtaa suureen tietoliikenteeseen, joten on suositeltavaa testata konfigurointiasetuksia parhaan mahdollisen asetuksen löytämiseksi.

Jos kohtaat ongelmia, ettei kuvia saada toimitettua oletusasetuksella, on suositeltavaa valita useampi kuin yksi kuva "kuvien enimmäismäärä" -asetuksiin ja säätää liukusäätimiä hieman, jotta kuvien noutoaika on pidempi.

Toiminto sisältää seuraavat kentät ja parametrit:

Muoto  – Määrittää viestin muodon lyhyeksi tai tavalliseksi.

Lyhytviesti sisältää enintään 160 merkkiä, eikä se voi sisältää ylimääräistä viestitekstiä tai kuvaliitteitä (katso alla).

Viesti  – Tämä kenttä sisältää viestin, joka lähetetään vastaanottajille hälytyksen sattuessa. Viestikenttä on aktiivinen vain, jos sähköpostin muoto on asetettu niin pitkäksi.

Huom:

Toisin kuin muut hälytystoiminnot, Lähetä sähköposti -toiminto voidaan valita vain kerran kullekin hälytykselle. Kun toiminto on valittu, se katoaa käytettävissä olevien toimintojen luettelosta.

Viestin otsikossa on hälytyksen nimi.

Poista hälytykset käytöstä

Poista hälytykset käytöstätoimintoa voidaan käyttää yhden hälytyksen perusteella estohälytyksiä lähettämiseen. Konfigurointi voidaan tehdä niin, että kaikki hälytykset ovat pois käytöstä, matalan ja keskitason hälytykset tai matalat hälytykset.

Tämän vaihtoehdon avulla tietyt hälytykset pysyvät aktiivisina, kun taas toiset vaimentuvat.

Hälytykset ovat pois käytöstä vain, kun ne poistava hälytys on aktiivinen.

ONVIF profile M

Ohjelmistomme tukee nyt ONVIF-profiilia M, joten se voi reagoida kamera analytiikan tuottaman hälytyksen laukaisuun. Tämän merkittävän päivityksen ansiosta VMS-järjestelmämme voi reagoida tehokkaasti kameroiden hälytyslaukaisuihin, mikä lisää mahdollisuuksia parantaa kohteiden turvallisuutta tai hyödyntää videoanalytiikkaa muihin tarpeisiin.

Saumattoman integroinnin ja vaatimustenmukaisuuden varmistamiseksi olemme testanneet tämän uuden ominaisuuden Axis, Bosch ja Hanwha kameramerkkien kanssa. 

ONVIF hälytyslaukaisin

Kun olet lisännyt laitteen, joka tukee ONVIF Profiilia M, sinun ei tarvitse tehdä mitään erityisiä toimenpiteitä ottaaksesi nämä laukaisimet käyttöön tai poistaaksesi ne käytöstä. Ne lisätään automaattisesti kameran metatietojen laukaisimiin. System Managerin hälytyskonfiguroinnissa tämä näkyy laukaisin välilehdellä ja listattuna ONVIF nimellä. Näitä käyttäen voit luoda uusia hälytyksiä.

ONVIF hälytyslaukaisimen tekeminen

Laitteen hälytykset/laukaisimet on määritettävä laitteen web-käyttöliittymän avulla, koska System Managerissa ei ole käyttöliittymää niiden määrittämiseen. Tämä konfigurointi on tehtävä ennen laitteen lisäämistä VMS:ään tai laitteen ominaisuudet on päivitettävä System Managerissa, jotta laitteen muutokset tulevat näkyviin.

Käynnistä System Manager.

Lisää laite jossa on ONVIF Profili M tuki.

Siirry Videohallintapalvelimet välilehteen.

Valitse Hälytykset.

Valitse uusi hälytys.

Avautuu Yleinen välilehti, josta voit antaa hälytykselle nimi ja valita mitkä profiilit käyttää hälytystä.

Siirry Laukaisin välilehti.

Valitse tyypiksi Metadata.

Valitse ONVIF metadatan tyyppi jota haluat käyttää hälytyksen laukaisuun.

Siirry Toiminnot välilehteen ja valitse haluamasi toiminto hälytykselle.

Siirry Kalenteri välilehteen ja valitse mitkä päivät/tunnit ovat käytössä hälytykselle. Oletuksena hälytys on 24h käytössä joka päivälle.

Valitse lopuksi OK alalaidasta.

Kalenteri

Määritä tämä, kun hälytys on aktiivinen

Valitse OK

Erityispäivät

Hälytyskohtaiset loma-aikataulut voivat luoda aikatauluja tietyille päivämäärille tai asettaa tietyn päivämäärän käyttämään toiselle viikonpäivälle suunniteltua hälytysaikataulua. Erityispäivät määritetään hälytyksen Kalenteri-välilehdeltä

Tietyn päivämäärän asettaminen toimimaan toisen viikonpäivän aikataulun kanssa:

Valitse viikonpäivä näytön vasemmassa reunassa olevasta aikataululuettelosta.

Valitse haluamasi vuosi ja kuukausi kalenterin yläpuolella olevista pudotusvalikoista.

Lisää aikataulu napsauttamalla päivämäärää kalenterissa.

Mukautetun aikataulun luominen:

Valitse Lisää

Kirjoita loma-aikataulun nimi Aikataulun nimi -kenttään.

Voit luoda aikataulun valitsemalla näytön vasemmalla puolella olevasta Päällä/Pois-luettelosta Pois ja merkitsemällä kellonajat, jolloin hälytys on sammutettu päiväksi.

Valitse OK

Valitse haluamasi vuosi ja kuukausi kalenterin yläpuolella olevista pudotusvalikoista.

Lisää aikataulu napsauttamalla päivämäärää kalenterissa.

Muokatun aikataulun muokkaaminen:

Valitse mukautettu aikataulu näytön vasemmassa reunassa olevasta aikataululuettelosta.

Valitse Muokkaa

Suorita muutokset

Valitse OK

Muokatun aikataulun poistaminen:

Valitse mukautettu aikataulu näytön vasemmassa reunassa olevasta aikataululuettelosta.

Valitse Poista

Alkuperäisen aikataulun palauttaminen:

Napsauta Palauta  näytön vasemmassa reunassa olevasta aikataululuettelosta.

Napsauta kalenterissa päivää, jonka haluat palauttaa.

Hälytyksen poistaminen
Hälytyksen poistaminen

Valitse VMS-videonhallintapalvelimet-välilehti

Avaa Hälytykset

Valitse poistettava hälytys napsauttamalla sen nimeä.

Valitse Poista hälytys vasemmasta alakulmasta

Hälytys poistetaan järjestelmästä.

Pagination
Previous page
UniversalOutputDriver (I/O-laitteet)
Next page
Hälytysasetukset