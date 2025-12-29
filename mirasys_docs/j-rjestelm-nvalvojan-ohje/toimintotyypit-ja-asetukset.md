# Toimintotyypit ja asetukset | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/toimintotyypit-ja-asetukset

Toimintotyypit ja asetukset

Alla oleva luettelo sisältää oletustoimintotyypit ja niiden parametrit. Jotkut yllä luetelluista toimintotyypeistä eivät välttämättä ole käytettävissä kaikissa järjestelmissä.

Oletustoimintojen lisäksi järjestelmä voi sisältää kolmannen osapuolen moduulien kautta asennettuja hälytystoimintoja.

Videotallennus

Videotallennus on kameroiden oletustoiminto. Kun tämän toimintotyypin sisältävä hälytys laukeaa, kameran oletusasetusten sijaan käytetään hälytystyypin määrittämiä tallennusasetuksia.

Jos Spotter:ssä hälytyksen ponnahdusikkunat on otettu käyttöön käyttäjäprofiilissa, Videotallennus -toiminnolla käytetyt laitteet näkyvät hälytyksen ponnahdusikkunassa, kun hälytys laukeaa.

Toiminto sisältää seuraavat kentät ja parametrit:

Viitekuva

Tämä staattinen kenttä sisältää kameran vertailukuvan (kuva) (A).

Käytä kamera-asetuksia

Hälytystallennus suoritetaan kamerakohtaisella resoluutiolla ja tallennusnopeudella valitsemalla tämä valintaruutu (B).

Resoluutio

Käytä liukusäädintä muuttaaksesi IP-kameran resoluutiota hälytyksen tallennuksen aikana. Liukusäädin on aktiivinen vain IP-kameroissa (C).

Kuvatahti

Käytä liukusäädintä muuttaaksesi kameran kuvatahtia hälytyksen tallennuksen aikana. Liukusäädin ei ole aktiivinen, jos Käytä kamera-asetuksia -valintaruutu on merkitty (D).

Esitallennus

Valitse tämä valintaruutu ottaaksesi tapahtumaa edeltävän tallennuksen käyttöön. Tapahtumaa edeltävän tallennuksen kesto voidaan asettaa Tapahtumaa edeltävä tallennusaika -liukusäätimellä (E).

Tapahtuman jälkeinen tallennus

Valitse tämä valintaruutu ottaaksesi tapahtuman jälkeisen tallennuksen käyttöön. Tapahtumaa edeltävän tallennuksen kesto voidaan asettaa Tapahtuman jälkeinen tallennusaika -liukusäätimellä (F).

Esi-ja jälkitallennuksen kesto

Näitä liukusäätimiä voidaan käyttää asettamaan toiminnon tallennusaika ennen ja jälkeen tapahtumaa. Liukusäätimet ovat aktiivisia vain, jos tapahtumaa edeltävä ja/tai tapahtuman jälkeinen tallennus on aktivoitu (G).

Kaikki laitteet (kamerat ja mikrofonit) on liitetty hälyttimeen, ja niiden tapahtumaa edeltävä ja jälkinauhoitus on aktivoitu jakaakseen saman tallennusajan ennen ja jälkeen tapahtuman.

Audiotallennus

Äänen tallennus on mikrofonien oletustoiminto. Kun tämän toimintotyypin sisältävä hälytys laukeaa, hälytystyypin määrittämiä tallennusasetuksia käytetään mikrofonin oletusasetusten sijaan.

Jos Spotter:ssä hälytyksen ponnahdusikkunat on otettu käyttöön käyttäjäprofiilissa, Audio-tallennus-toiminnolla käytetyt laitteet näkyvät hälytyksen ponnahdusikkunassa, kun hälytys laukeaa.

Toiminto sisältää seuraavat kentät ja parametrit:

Esitallennus

Valitse tämä valintaruutu ottaaksesi tapahtumaa edeltävän tallennuksen käyttöön. Tapahtumaa edeltävän tallennuksen kesto voidaan asettaa Tapahtumaa edeltävä tallennusaika -liukusäätimellä (A).

Jälkitallennus

Valitse tämä valintaruutu ottaaksesi tapahtuman jälkeisen tallennuksen käyttöön. Tapahtumaa edeltävän tallennuksen kesto voidaan asettaa Tapahtuman jälkeinen tallennusaika -liukusäätimellä (B).

Esi- ja jälkitallennuksen kesto

Näitä liukusäätimiä voidaan käyttää asettamaan toiminnon tallennusaika ennen ja jälkeen tapahtumaa. Liukusäätimet ovat aktiivisia vain, jos tapahtumaa edeltävä ja/tai tapahtuman jälkeinen tallennus on aktivoitu (C).

Kaikki hälyttimeen yhdistetyt laitteet (kamerat ja mikrofonit) ovat aktivoineet tapahtumaa edeltävän ja jälkeisen tallennuksen, jotta ne jakavat saman tapahtumaa edeltävän ja jälkeisen tallennusajan.

Digitaaliset lähdöt

Digitaalinen lähtö on digitaalisten I/O-laitteiden oletustoiminto. Kun tämän toimintotyypin sisältävä hälytys laukeaa, I/O-laite aktivoituu.

Vaikka toimintotyypin Esi- ja jälkitallennuksen kesto -liukusäätimet näytetään, ne eivät vaikuta toiminnon toimivuuteen.

PTZ-kameran esiasento

PTZ-kameran esiasento toimintoa käytetään ohjaamaan PTZ-kamera haluttuun esiasentoon Kun tämän toimintatyypin sisältävä hälytys laukeaa, PTZ-kamera siirtyy automaattisesti valittuun esiasetettuun asentoon.

Katso Spotter -käyttöoppaasta lisätietoja PTZ-kameran esiasetusten asettamisesta.

On huomattava, että tämä toiminto siirtää PTZ-kameran esiasetettuun asentoon, mutta se ei johda PTZ-kameran videosyötteen näyttämiseen asiakassovelluksen hälytysnäkymässä, ellei muita hälytystoimintoja, kuten Videotallennus,ole tehty. valittu PTZ-kameralle.

Toiminto sisältää seuraavat kentät ja parametrit:

Esiasento

Käytä pudotusvalikkoa valitaksesi esiasetettu asento, johon PTZ-kamera siirtyy hälytyksen aikana.

Vaikka toimintotyypin Esi- ja jälkitallennuksen kesto -liukusäätimet näytetään, ne eivät vaikuta toiminnon toimivuuteen.

PTZ-kamerakierto

PTZ-kamerakierros -toimintoa voidaan käyttää asettamaan PTZ-kamera aloittamaan esiohjelmoidun PTZ-kamerakierroksen. Kun tämän toimintotyypin sisältävä hälytys laukeaa, valittu PTZ-kamerakierros alkaa. Katso Spotter käyttöohjeesta lisätietoja PTZ-kamerakierrosten asettamisesta.

On huomattava, että tämä toiminto aloittaa PTZ-kamerakierroksen, mutta se ei johda PTZ-kameran videosyötteen näyttämiseen asiakassovelluksen hälytysnäkymässä, ellei muita hälytystoimintoja, kuten Videotallennus, ole valittu PTZ kameralle.

Toiminto sisältää seuraavat kentät ja parametrit:

Ohjelma

Valitse avattavasta valikosta PTZ-kamerakierros hälytyksen laukaisemisesta alkaen.

Vaikka toimintotyypin Esi- ja jälkitallennuksen kesto -liukusäätimet näytetään, ne eivät vaikuta toiminnon toimivuuteen.

Aseta liikkeentunnistusmaski

Aseta liiketunnistusmaski -toiminto voi muuttaa tietyn kameran hälytyksen aikana käyttämää liiketunnistusmaskia. Kun hälytys tapahtuu, määritetyn kameran liiketunnistusmaski muutetaan hälytyskohtaiseksi maskiksi. Hälytyksen päätyttyä järjestelmä palauttaa oletusmaskin.

Toiminto sisältää seuraavat kentät ja parametrit:

Maski

Valitse pudotusvalikosta liiketunnistusmaski, jota käytetään hälytyksen aikana.

Vaikka toimintotyypin Esi- ja jälkitallennuksen kesto -liukusäätimet näytetään, ne eivät vaikuta toiminnon toimivuuteen.

Sähköpostin lähetys

Sähköpostin lähetys -toimintoa voidaan käyttää sähköpostin lähettämiseen mihin tahansa sähköpostiosoitteeseen tai ryhmään, joka on määritetty Järjestelmä-välilehden Sähköpostiasetuksissa.

Voit valita, kenen vastaanottajan tai ryhmän tulee vastaanottaa hälytys.

Voit myös sisällyttää hälytyssähköpostiin yhden tai useamman skaalaamattoman tai pienennetyn kuvan. Poista valinta Lähetä lyhyessä muodossa -vaihtoehdosta ja valitse Liitä kuvia -vaihtoehto.

Tämän jälkeen voit valita kameran, kuvan skaalauskoon, halutun kuvien määrän ja aikajänteen, jolta kuvat noudetaan.

Kuvien määrä tässä kokoonpanossa on suurin toimitettava määrä. Kuvia saattaa saapua vähemmän

Kuvien liittäminen hälytyssähköpostiin saattaa johtaa suureen tietoliikenteeseen, joten on suositeltavaa testata konfigurointiasetuksia parhaan mahdollisen asetuksen löytämiseksi.

Jos kohtaat ongelmia, ettei kuvia saada toimitettua oletusasetuksella, on suositeltavaa valita useampi kuin yksi kuva "kuvien enimmäismäärä" -asetuksiin ja säätää liukusäätimiä hieman, jotta kuvien noutoaika on pidempi.

Toiminto sisältää seuraavat kentät ja parametrit:

Muoto

Määrittää viestin muodon lyhyeksi tai tavalliseksi.

Lyhytviesti sisältää enintään 160 merkkiä, eikä se voi sisältää ylimääräistä viestitekstiä tai kuvaliitteitä (katso alla).

Viesti

Tämä kenttä sisältää viestin, joka lähetetään vastaanottajille hälytyksen sattuessa. Viestikenttä on aktiivinen vain, jos sähköpostin muoto on asetettu niin pitkäksi.

Toisin kuin muut hälytystoiminnot, Lähetä sähköposti -toiminto voidaan valita vain kerran kullekin hälytykselle. Kun toiminto on valittu, se katoaa käytettävissä olevien toimintojen luettelosta.

Viestin otsikossa on hälytyksen nimi.

Poista hälytykset käytöstä

Poista hälytykset käytöstätoimintoa voidaan käyttää yhden hälytyksen perusteella estohälytyksiä lähettämiseen. Konfigurointi voidaan tehdä niin, että kaikki hälytykset ovat pois käytöstä, matalan ja keskitason hälytykset tai matalat hälytykset.

Tämän vaihtoehdon avulla tietyt hälytykset pysyvät aktiivisina, kun taas toiset vaimentuvat.

Hälytykset ovat pois käytöstä vain, kun ne poistava hälytys on aktiivinen.

Pagination
Previous page
Lisää - Poista hälytyksiä
Next page
ONVIF Profile M