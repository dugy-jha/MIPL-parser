# VCA - Laskurit | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-laskurit

VCA - Laskurit

Counters (laskurit) näkyvät vain VCA-kokoonpanossa. Jos haluat käyttää laskureita Spotterissa, katso Spotterin käsikirjaa.
Laskurit voidaan konfiguroida laskemaan, kuinka monta kertaa jokin sääntö laukeaa, esimerkiksi kuinka monta ihmistä ylittää jonon.

Laskentasääntö on suunniteltu käytettäväksi kahdella tavalla:

Increment / Decrement (Lisää/Vähennä): Laskuria kasvatetaan liitetyn säännön (sääntöjen) avulla (+1 jokaisesta säännön laukaisusta) ja vähennetään toisen liitetyn säännön (sääntöjen) avulla (-1 jokaisesta säännön laukaisusta).

Occupancy: Laskuri kertoo niiden kohteiden lukumäärän, jotka laukaisevat tällä hetkellä liitetyn säännön (liitetyt säännöt).

Laskurin kolmeen tuloon voidaan liittää useampi kuin yksi sääntö.
Tämä mahdollistaa esimerkiksi sen, että kahden läsnäolosäännön miehitys voidaan heijastaa yhteen laskuriin tai useampi kuin yksi sisään-/uloskäyntiportti voidaan heijastaa yhteen laskuriin, ja tätä havainnollistaa alla oleva esimerkkisääntökaavio.
Yleisesti ottaen yhtä laskuria ei pitäisi käyttää sekä miehitykseen että lisäykseen/poistoon.

Huomautus: laskurin luomat tapahtumat eivät käynnistä syväoppimissuodatinta, vaikka se olisi käytössä kanavalla.

Laskurien asettelu

Kun se lisätään, laskuriobjekti visualisoidaan videovirrassa alla olevan kuvan mukaisesti.
Laskuria voidaan siirtää ottamalla kiinni laskurin nimen alla olevasta kahvasta ja siirtämällä laskuri haluttuun paikkaan.




Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittelemä nimi tälle säännölle

	

"Counter #"




Increment (Lisäys)

	

Sääntö, joka laukaistessaan lisää laskuriin yhden.

	

None




Decrement (Vähennys)

	

Sääntö, joka lauetessaan vähentää laskurista yhden.

	

None




Occupancy (Käyttöaste)

	

Asettaa laskurin säännön aktiivisten laukaisimien nykyiseen lukumäärään*.

	

None




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active




Reset Counter (Nollaa laskuri)

	

Painike, jolla laskurin arvo voidaan nollata arvoon 0.

	

None

Jos esimerkiksi läsnäolosääntö on asetettu Occupancy ja kaksi kohdetta laukaisee tällä hetkellä kyseisen läsnäolosäännön, laskuri näyttää arvoa '2'.

Pagination
Previous page
VCA - Ehdolliset säännöt
Next page
VCA - Objekti jälki