# Kesäaika (DST) | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-k-ytt-ohje/V9.9/kesaaika-dst

Kesäaika (DST)

Tässä oppaassa kerrotaan, miten kesäajan siirtymisestä johtuvia mahdollisia ongelmia käsitellään videonhallintaohjelmistoa (VMS) käytettäessä. Siinä annetaan myös ohjeita tallennetun materiaalin hakemisesta kesäajan siirtymisen aikana, erityisesti ensimmäisen tunnin aikana ajanmuutoksen jälkeen.

Esittely

Kesäaikaan kuuluu kellojen siirtäminen yhdellä tunnilla eteenpäin keväällä (”kevät eteenpäin”) ja yhdellä tunnilla taaksepäin syksyllä (”syksy taaksepäin”). Muutoksen ajankohta vaihtelee maittain ja alueittain, mutta yleinen periaate on sama kaikkialla maailmassa.

:light_bulb_on:

VMS-järjestelmämme tallentaa kuvamateriaalia käyttäen UTC-aikaa (Coordinated Universal Time).

Kesäajan muutokset eivät vaikuta UTC-aikaan. Näin varmistetaan, ettei tallennettua materiaalia menetetä tai kopioida.

DST:n vaikutus videovalvontajärjestelmiin

Kesäajan siirtyminen voi aiheuttaa sekaannusta kuvamateriaalia tarkasteltaessa, koska järjestelmän paikallinen aika muuttuu, vaikka UTC pysyy samana.

Vaikka videomateriaalia ei menetetä tai kopioida UTC-aikana, paikallisen ajan muutos voi vaikuttaa siihen, miten se esitetään käyttäjille:

Ohitettu tunti voi saada käyttäjät luulemaan, että kuvamateriaalia puuttuu.

Toistuva tunti voi aiheuttaa sekaannusta, koska se luo kaksi sarjaa kuvamateriaalia, joilla on sama paikallinen aikaleima.

Kevät eteenpäin

Kevään kesäajan siirtymisen aikana kelloja siirretään yhdellä tunnilla eteenpäin, jolloin tietty tunti jää väliin. Koska järjestelmämme toimii UTC-ajan mukaan, tätä tuntia ei kirjata, koska sitä ei käytännössä ole olemassa paikallisessa ajassa.

:light_bulb_on:

Kevään kesäajan siirtymisen aikana ohitetun tunnin aikana ei tallenneta videota (kyseinen tunti riippuu paikallisesta aikavyöhykkeestä).

Käyttäjät saattavat havaita, että videomateriaalia puuttuu, mutta ohitettua tuntia ei yksinkertaisesti ole olemassa järjestelmän paikallisessa ajassa.

Materiaalin nouto kevään etenemisen aikana

Kun kyseessä on kevät eteenpäin, ymmärrä, että ohitettua tuntia ei ole järjestelmässä. Viimeinen käytettävissä oleva aineisto ennen ajanmuutosta on juuri ennen kuin aika vaihtuu kesäaikaan, ja seuraava käytettävissä oleva aineisto on tuntia myöhemmin. Ohitettua tuntia varten ei ole haettavissa kuvamateriaalia.

:light_bulb_on:
Kevät eteenpäin

Tuntia, joka on ohitettu, ei ole kuvattu. Tämä tunti vaihtelee sen aikavyöhykkeen mukaan, jossa järjestelmä sijaitsee.

Tallenteiden hakeminen: Viimeinen käytettävissä oleva kuvamateriaali ennen ajanmuutosta on juuri ennen ohitettua tuntia, ja seuraava käytettävissä oleva kuvamateriaali jatkuu ohitetun tunnin jälkeen.

Fall Back

Syksyllä kelloja siirretään tunnilla taaksepäin, jolloin toistetaan tietty tunti. Koska järjestelmämme toimii UTC-järjestelmässä, tämä tarkoittaa, että toistetun tunnin osalta tallennetaan kaksi erillistä kuvasarjaa.

Kun käytetään Spotter-sovelluksen ajanvalintaa toistetun tunnin kohdalla, kaikki aikapyynnöt muunnetaan toiselle tunnille. Tämä tarkoittaa sitä, että Spotterin aikajanaa käytettäessä toisto toistaa materiaalit ja tekee haun toiselta tunnilta.

Ensimmäisen tunnin aineistojen käyttämiseksi operaattorit voivat aloittaa toiston eteenpäin kesäajan siirtymistä edeltävältä tunnilta tai aloittaa toiston taaksepäin kesäajan siirtymisaikaa edeltävältä tunnilta.

Ohjeet materiaalin noutoa varten Fall Backin aikana

Fall Back -siirtymää varten kirjataan kaksi erillistä tuntia. Nämä kaksi erillistä tuntia voidaan erottaa toisistaan järjestelmän aikaleiman perusteella. Voit varmistaa, että oikea tunti on haettu, tarkastelemalla järjestelmän lokia tai vesileimaa, josta käy ilmi tallennuksen todellinen kellonaika.

Tarkista järjestelmälokeista ja tapahtumalokeista tarkat ajat, jolloin järjestelmä on säätänyt kelloaan.

Kun käytetään Spotter-sovelluksen ajanvalintaa toistetun tunnin kohdalla, kaikki aikapyynnöt muunnetaan toiselle tunnille. Tämä tarkoittaa sitä, että Spotterin aikajanaa käytettäessä toisto toistaa materiaalit ja tekee haun toiselta tunnilta.

Ensimmäisen tunnin aineistojen käyttämiseksi operaattorit voivat aloittaa toiston eteenpäin kesäajan siirtymistä edeltävältä tunnilta tai aloittaa toiston taaksepäin kesäajan siirtymisaikaa edeltävältä tunnilta.

:light_bulb_on:
Fall Back

Tietty tunti tallennetaan kahdesti, kerran ennen kellon taaksepäin siirtämistä ja kerran sen jälkeen.

Tallenteiden hakeminen: Kahden tallennetun tunnin erottaminen toisistaan. Tarkastele järjestelmälokia tai vesileimaa erottaaksesi toisistaan kaksi toistetun tunnin tallenteiden sarjaa.

Kun käytät Spotter-sovellusta toistamiseen, huomaa, että kaikki toistetun tunnin aikana tehdyt aikapyynnöt oletusarvoisesti kohdistuvat kyseisen tunnin toiseen esiintymään.

Voit hakea toistetun tunnin ensimmäisen esiintymän kuvamateriaalia seuraavasti:

Aloita toisto kesäajan säätöä edeltävältä tunnilta.

Käyttää taaksepäin toistoa alkaen kesäajan muutoksen jälkeisestä tunnista.

Parhaat käytännöt DST-siirtymien käsittelyyn Mirasys VMS:ssä

Jotta sekaannukset voidaan minimoida ja varmistaa, että järjestelmä käyttäytyy odotetulla tavalla DST-siirtymien aikana, on tärkeää noudattaa seuraavia parhaita käytäntöjä:

Ilmoita kaikille operaattoreille ja käyttäjille tulevasta kesäajan muutoksesta ja selitä sen vaikutus tallennettuun kuvamateriaaliin, erityisesti ohitettu tunti keväällä eteenpäin ja päällekkäinen tunti syksyllä taaksepäin.

Varmista, että kaikki järjestelmäkomponentit, mukaan lukien palvelimet, kamerat ja niihin liittyvät laitteet, on synkronoitu tarkan aikalähteen kanssa, jotta estetään ajan siirtyminen siirtymän aikana.

Kun kyseessä on aikaleimattu kuvamateriaali, valmistele operaattorit mahdolliseen sekaannukseen aikaleimoissa siirtymisen aikana ja sen jälkeen.

Tarkista kuvamateriaali kesäajan muutoksen jälkeen siirtymäkauden aikana. Varmista, että ennen ajanmuutosta ja sen jälkeen tehdyt tallenteet ovat ehjiä ja käytettävissä.

Jos aika siirtyy takaisin, muista, että samalta tunnilta on olemassa kaksi kuvasarjaa. Varmista, että operaattorit osaavat erottaa nämä kaksi tallennusjaksoa toisistaan.

Jos järjestelmät käynnistyvät liikkeen tai hälytysten perusteella, tarkista, että kaikki ajanmuutoksen aikana tapahtuneet tapahtumat on tallennettu asianmukaisesti.

Pagination
Previous page
Useiden hälytysmonitorien käyttö
Next page
Järjestelmän monitorointi