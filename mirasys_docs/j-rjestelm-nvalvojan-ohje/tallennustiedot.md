# Tallennustiedot | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/tallennustiedot

Tallennustiedot

Tallennusasetuksissa voit asettaa tallennetun videon, äänen ja tekstidatan sekä hälytystietojen tallennusajan.

Lisäksi, kun olet lisännyt kiintolevyn palvelimeen, voit asettaa sen lisätietotallennustilaksi tallennusasetusten kautta.

Tallennusasetuksia käytetään myös automaattisen arkistoinnin konfigurointiin, jolloin palvelinkohtaisista video-, ääni- ja tekstitiedoista voidaan tehdä varmuuskopioita päivittäin tai viikoittain.

Video-, ääni-, tekstidataa ja hälytystallenteita säilytetään, kunnes niille määritetty Maksimi-päivämäärä on ylitetty tai kunnes varattu tallennustila on loppunut.

Tallennuskapasiteetin lisääminen

Jos tarvitaan lisää tallennustilaa, voit lisätä uusia kiintolevyjä tai yhdistää verkkoaseman tietojen tallennusta varten (eli NAS-tuki).

Verkkotallennuslevyjä voi olla useita ja paikallisia levyjä voidaan käyttää samanaikaisesti.

Huom: Kun lisäät tallennusasemia vanhaan Mirasys-tiedostojärjestelmään (VMS-palvelimen versio 7.5.x tai aikaisempi), kaikkien tallennusasemien kapasiteettia suositellaan olevan sama, minkä tahansa yksittäisen levyn tulee olla kooltaan alle 10 Tt ja kokonaismäärä VMS-järjestelmää kohden. palvelimen tulee olla kooltaan alle 25 TB.

Useiden tallennuslevyjen käytöllä on se etu, että materiaalin kirjoitus voidaan jakaa kaikille asemille, jolloin yksittäisen materiaaliaseman häviäminen ei todennäköisesti pyyhi suuria osia tallennetusta materiaalista.

Kiintolevyn lisääminen:

Asenna uusi kiintolevy ja ota se käyttöön käyttöjärjestelmässä

Aineistoasetuksista valitse Lisää levy Lisää levy valintaikkuna tulee näkyviin.Vähintään vapaata tilaa uudessa levylaatikossa osoittaa, kuinka paljon vapaata tilaa uudella levyllä on oltava.

Valitse levy luettelosta ja napsauta OK.

Verkkoaseman yhdistäminen:

Valitse kohdassa  Tallennusasetukset   Verkkoasema  -valintaruutu.

Avaa verkkoaseman määritysnäyttö tarvittaessa napsauttamalla Määritä verkkoasema

Kirjoita verkkoaseman käyttäjänimi ja salasana Käyttäjänimi- ja Salasana-kenttiin.

Kirjoita verkkoaseman sijainti Verkkoaseman polku -kenttään.

Valitse OK

Käytä Varattu tila -liukusäädintä asettaaksesi verkkoasemalle varatun tilan tiedon tallennusta varten.

Useiden verkkoasemien yhdistäminen:

Asenna ja määritä verkkotallennus toimimaan paikallisesti yhdistettynä asemana (käytä esimerkiksi iSCSI-käynnistystä tai vastaavaa).

Aineistoasetuksista valitse Lisää levy Lisää levy -valintaikkuna tulee näkyviin.

Tallennustilaa ei voi määrittää iSCSI-levyille.

Valitse OK Toista muille levyille.

Videon, äänen ja tekstin tallennusasetukset
Vähimmäisaika

Jos haluat priorisoida tallennuksia yhdestä tai useammasta video-, ääni- tai tekstidatakanavasta, varmista, että vähimmäisarvot ovat riittävän alhaiset muille kanaville.

Aseta sitten korkeampi arvo korkean prioriteetin kanavalle tai kanaville.

Jos valitset Automaattinen, järjestelmä poistaa tallenteet kanavilta, jotka käyttävät eniten tallennustilaa.

Maksimi

Järjestelmä tutkii tallenteet päivittäin ja poistaa enimmäispäiviä vanhemmat tallenteet.

Jos valitset Automaattinen, tallenteet poistetaan vain, kun vapaata tilaa ei ole riittävästi.




Huom: Jos vähimmäisarvot ovat liian korkeat joillekin kanaville, mutta samaan aikaan niitä ei ole asetettu muille kanaville, järjestelmä poistaa tallennukset kanavilta, joille ei ole asetettu vähimmäisarvoa.

Hälytysten säilytysaika
Vähimmäisaika

Järjestelmä poistaa hälytykset, jotka ovat vähimmäisarvoa vanhempia.

Jos valitset Automaattinen, järjestelmä poistaa hälytystallenteet kanavilta, jotka käyttävät eniten tallennustilaa.

Maksimi

Järjestelmä tutkii hälytystallenteet päivittäin ja poistaa ne enimmäispäiviä vanhemmat.

Jos valitset Automaattinen, tallenteet poistetaan vain, kun vapaata tilaa ei ole riittävästi.

Lokimerkinnät

Tämä arvo määrittää, kuinka monta hälytystapahtumaa enintään säilytetään hälytyslokissa.

Järjestelmä tarkastaa lokimerkintöjen lukumäärän tunneittain ja poistaa vanhimmat kirjaukset, jos ne ylittyvät.

% maksimi

Tämä arvo määrittää, kuinka paljon tallennustilaa hälytystallenteet saavat käyttää kaikesta tallennustilasta.

Niin kauan kuin tallennustilaa ei käytetä, hälytystallenteet voivat käyttää tätä arvoa enemmän tilaa.

Järjestelmä poistaa ensin vanhimmat hälytystallenteet ennen muiden video- tai äänitallenteiden poistamista, jos kaikki tallennustila on käytetty.

Automaattinen video-, ääni- ja tekstitietojen poistaminen

Kun määritetty enimmäistallennusaika on ylitetty, tallennetut video-, ääni-, teksti- ja hälytystiedot poistetaan automaattisesti – tietojen enimmäistallennusaika, jonka järjestelmä tarkistaa päivittäin.

Koska tallennetun tietovirran koko voi vaihdella merkittävästi videokuvan liikkeen, äänitasojen muutosten tai tekstidatatapahtumien määrän vuoksi, tallennustilan tarvetta voi olla vaikea ennustaa tarkasti.

Siten järjestelmä saattaa joskus katsoa tarpeelliseksi varmistaa vapaan tallennustilan poistamalla automaattisesti vanhan materiaalin enimmäisvarastointiajasta riippumatta.

Jos tiedot on poistettava vapaan tallennustilan varmistamiseksi, poistoprosessi etenee seuraavan kaavan mukaan:

Yksinkertaisesti sanottuna tämä säilytysprosessi menee näin, kun VMS tarvitsee lisää tallennustilaa:

Tarkista hälytyskiintiö, jos hälytysmateriaalitiedostoja on enemmän kuin asetettu kiintiössä (% kaikista tiedoista), poistetaan vanhin hälytystiedosto ja käytämme sen uudelleen

Tarkista hälytystietojen minimiasetukset - jos hälytyskanavilla on tietoja, jotka ylittävät minimihälytysasetukset - otamme niistä vanhimman tiedoston, poistamme sen ja käytämme uudelleen

Tarkista kaikkien materiaalikanavien (video, ääni, data) vähimmäisasetukset - jos joillain kanavilla on dataa, joka ylittää vähimmäisasetukset - otamme niistä vanhimman tiedoston, poistamme sen ja käytämme uudelleen

Tarkista vanhin tiedosto kanavista automaattisilla min asetuksilla, jos niitä on, jos on - otamme niistä vanhimman tiedoston, poistamme sen ja käytämme uudelleen

Jos edelleen, mitään ei löydy – otamme vain vanhimman tiedoston kaikista kanavista (materiaali ja hälytys), puhdistamme sen ja käytämme uudelleen

Lisäksi meillä on taustatehtävä, joka poistaa materiaalitiedostot max asetusten mukaan.

Käynnistysjakso on asetettu minimiin kaikilta kanavilta (materiaali ja hälytys).

Huom: Jotta levytilan puutteesta johtuva automaattisen poiston tarve olisi mahdollisimman pieni, on hyvä seurata levyn käyttöä säännöllisesti ja muuttaa enimmäistallennusaikaa ja varattua levytilaa.

On suositeltavaa käyttää manuaalisia tai automaattisia arkistointityökaluja varmistaaksesi, että mitään oleellisia tietoja ei poisteta tallennustilaongelmissa.

Vinkki: Voit asettaa Ohjelmistovahti-tapahtuman ilmoittamaan, jos tallennustila on vähissä.

Arkisto

Voit asettaa järjestelmän arkistoimaan automaattisesti video-, ääni- ja tekstidataa päivittäin tai viikoittain.

Arkistotiedostot voidaan luoda automaattisesti palvelimen kiintolevyille tai verkkoasemalle.

Arkistotiedostot voidaan avata millä tahansa Spotter-asiakasohjelmalla.

Huom: Arkistotiedostot voivat olla suuria, ja siten ne voivat täyttää tallennustilan nopeasti. Arkistotiedostot tulee säännöllisesti kopioida ja poistaa palvelimen kiintolevyiltä tai verkkoasemilta, joille ne tallennetaan automaattisesti.

Automaattisen arkistoinnin määrittäminen:

Napsauta Datatiedostojen säilytysaika -ruudussa laitteita, jotka haluat sisällyttää automatisoivaan arkistointiprosessiin.  
VINKKI:Valitse viereiset laitteet tai kansiot, pidä SHIFT-näppäintä painettuna ja napsauta sitten ensimmäistä ja viimeistä laitetta, jonka haluat valita.

Jos haluat lisätä laitteen valintaan tai poistaa sen valinnasta, pidä CTRL-näppäintä painettuna ja napsauta sitten laitetta, jonka haluat lisätä tai poistaa.
Huomaa: Laiteryhmän (kansion) valitseminen valitsee myös sen sisällön.

Valitse Arkisto-valintaruutu

Valitse Muokkaa arkistointiasetuksia

Aseta arkiston salasana napsauttamalla Vaihda arkiston salasana

Valitse, luodaanko arkisto päivittäin vai viikoittain valitsemalla  Joka päivä tai Kerran viikossa

Jos määrität arkistoinnin tapahtuvaksi päivittäin, valitse avattavasta Arkistointiaika-valikosta aika, jolloin arkistotiedostot luodaan.

Jos määrität arkistoinnin tapahtuvaksi joka viikko, valitse avattavista Arkistointiviikonpäivä- ja Arkistointiaika-valikoista päivämäärä ja aika, jolloin arkistotiedostot luodaan.

Valitse Arkistoitu ajanjakso -liukusäädintä asettaaksesi arkistotiedostoissa käytettävän ajanjakson.

Valitse, luodaanko arkistot paikalliselle asemalle (palvelimelle) vai verkkoasemalle valitsemalla VMS-palvelinhakemisto tai Verkkohakemisto.

Napsauta  Vaihda hakemistoa  tai  Vaihda verkkoasemaa  -painiketta asettaaksesi hakemiston arkiston tallentamista varten.

Valitse OK

Käytä käyttöjärjestelmän välimuistia

VMS 8. x:ssä ja uudemmissa on mahdollisuus ottaa käyttöjärjestelmän välimuisti käyttöön fyysistä levyä käytettäessä.

VMS V9.4:ssä ja uudemmissa on mahdollisuus asettaa käyttöjärjestelmän välimuistin enimmäiskoko.

Mikä tahansa ohjelmisto voi käyttää levyä suorakäyttötilassa, kun käyttöjärjestelmä ei käytä välimuistia ja käyttää käyttöjärjestelmän välimuistia.

Viimeinen auttaa käsittelemään epävakaa kuormitusta kiintolevylle ja tallentamaan eniten käytetyt tiedon osat.

Windows Server- ja Windows-työpöytäversioilla on erilaiset prioriteetit sovelluksille - Windows Servicen taustapalvelut ja työpöytäversioiden prioriteetit käyttöliittymäsovelluksille.

Lisäksi Windows Server käyttää enemmän järjestelmäresursseja välimuistiin esim. HDD-käyttö ja voi käyttää jopa 90% RAM-muistista tähän.

Välttääksesi tilanteet, joissa koko RAM-muisti on tiedostojärjestelmän välimuistin käytössä, DVMS 9.4 ja uudemmat on mahdollista rajoittaa käyttöjärjestelmän välimuistin enimmäiskokoa.

Käyttöjärjestelmän välimuistin enimmäisasetukset ovat voimassa PC:n uudelleenkäynnistykseen asti, joten ne asetetaan aina tallennin käynnistyessä.




Pagination
Previous page
ONVIF-profiilin M mukautetut hälytyslaukaisimet
Next page
Tekstikanavat