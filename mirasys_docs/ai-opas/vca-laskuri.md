# VCA- Laskuri | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-laskuri

VCA- Laskuri

Counters (laskurit) voidaan määrittää laskemaan, kuinka monta kertaa sääntö käynnistyy. Esimerkiksi linjan ylittäneiden henkilöiden määrä. Laskurisääntö on suunniteltu hyödynnettäväksi kahdella tavalla:

Lisäys / vähennys: jolloin laskuri kasvaa liitetyn säännön (sääntöjen) mukaan (+1 jokaisesta säännön laukaisusta) ja vähenee toisen liitetyn säännön (sääntöjen) mukaan (-1 jokaisesta säännön laukaisusta).

Occupancy: jolloin laskuri kuvastaa niiden kohteiden lukumäärää, jotka tällä hetkellä laukaisevat liitetyn säännön (liitetyt säännöt).

Laskurin kolmeen tuloon voidaan liittää useampi kuin yksi sääntö. Tämä mahdollistaa esimerkiksi sen, että kahden läsnäolosäännön miehitys näkyy yhdessä laskurissa tai että useampi kuin yksi sisään-/uloskäyntiportti näkyy yhdessä laskurissa. Seuraavassa on esimerkki sääntökaaviosta, joka havainnollistaa tätä.

Yleisesti ottaen yhtä laskuria ei pitäisi käyttää sekä miehitykseen että lisäykseen/poistoon.

Laskurin kynnysarvo-operaattorin avulla käyttäjä voi rajoittaa, milloin laskuri tuottaa tapahtuman. Valitun käyttäytymisen ja määritetyn kynnysarvon perusteella laskuri voidaan määrittää lähettämään tapahtumia vain tietyissä tilanteissa. Kynnysarvo-operaattoreita ovat mm:

Greater than or equal to (Suurempi tai yhtä suuri kuin)

Less than or equal to (Pienempi tai yhtä suuri kuin)

Greater than (Suurempi kuin)

Less than (Vähemmän kuin)

Equal to (Yhtä suuri kuin)

Not Equal to (Ei vastaava kuin)

None ( Ei mikään)

Paikannuslaskurit

Kun laskuri lisätään, se näkyy videovirrassa alla olevan kuvan mukaisesti. Laskuri voidaan sijoittaa uudelleen tarttumalla laskurin nimen alla olevaan kahvaan ja siirtämällä laskuri haluttuun paikkaan.

Kun napsautat hiiren oikealla painikkeella (tai napautat ja pidät hiiren painettuna tabletilla) ruudukkoa, näyttöön tulee kontekstivalikko.

Graafinen näkymä
Lomakkeen näkymä
Konfigurointi
Use table header to sort columns

Property

	

Description

	

Default Value




Name (Nimi)

	

A user-specified name for this rule

	

“Counter #”




Increment (Lisäys)

	

The rule which, when triggered, will add one to the counter

	

None




Decrement (Vähennys)

	

The rule which, when triggered, will subtract one from the counter

	

None




Occupancy (Käyttömäärä)

	

Asettaa laskurin säännön aktiivisten laukaisimien nykyiselle lukumäärälle.

	

None




Reset (Nollaa)

	

Nollaa laskennan arvoksi 0, kun määritetty(t) sääntö(t) käynnistyy(vät).

	

None




Threshold Operator (Kynnysoperaattori)

	

Määrittää, milloin laskuri laukaisee tapahtumia kynnysarvon perusteella.

	

None




Threshold Value (Kynnysarvo)

	

Arvo, jota Threshold-operaattori käyttää käyttäytymisen määrittelyyn.

	

0




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active




Reset Counter (Nollaa laskuri)

	

Painike, jolla laskurin arvo voidaan nollata arvoon 0.

	

None

Jos esimerkiksi läsnäolosääntö on asetettu miehityskohteeksi ja kaksi kohdetta laukaisee tällä hetkellä kyseisen läsnäolosäännön, laskuri näyttää arvoa 2.

Tyypillinen loogisen säännön yhdistelmä

Alla oleva laskuri-esimerkki kasvattaa laskuria kahden syöttösäännön perusteella, jotka on liitetty vyöhykkeisiin Centre (keskelle) ja Top (ylös), mikä tarkoittaa, että kun jompikumpi näistä syöttösäännöistä laukeaa, laskuria kasvatetaan + 1:llä. Laskuri pienenee myös poistumissäännön Exit perusteella, joka vähentää laskurista 1 aina, kun objekti poistuu vyöhykkeeltä Centre. Kynnysoperaattori ja kynnysarvo rajoittavat laskurin tuottamaan tapahtumia vain, kun laskuri on yli 20.

Ainoastaan laskurisäännön Counter (Laskuri) arvoksi on asetettu Can Trigger Actions (Voi laukaista toimintoja), mikä tarkoittaa, että vain tämä loogisen säännön osa on käytettävissä toimintojen lähteenä. Tällöin tätä sääntöä lähteenä käyttävä toiminto käynnistyy aina, kun laskuri muuttuu.




Pagination
Previous page
VCA - Continuously
Next page
VCA - Not