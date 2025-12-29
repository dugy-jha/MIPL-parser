# VCA - Nopeussuodatin | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-nopeussuodatin

VCA - Nopeussuodatin
Nopeussuodatin

Speed filter (Nopeussuodattimen) avulla voidaan tarkistaa, onko syötteen laukaisseen kohteen nopeus alemman ja ylemmän rajan määrittelemän nopeusalueen sisällä.

Kanavan on oltava kalibroitu, jotta nopeussuodatin on käytettävissä.

Yleensä tämä sääntö yhdistetään läsnäolosääntöön, ja tätä havainnollistaa alla oleva esimerkkisääntökaavio.

Seuraava kuva havainnollistaa, kuinka tällainen sääntöyhdistelmä laukeaa 52 km/h:n nopeudella liikkuvan auton kohdalla, mutta 12 km/h:n nopeudella liikkuva henkilö jää määritetyn alueen (25-100 km/h) ulkopuolelle eikä näin ollen laukaise sääntöä.

Use table header to sort columns

Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittämä nimi säännölle

	

"Speed #"




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active




Input (Sisääntulo)

	

Sisääntulo sääntö

	

None




Min Speed (Vähimmäisnopeus)

	

Vähimmäisnopeus (km/h), jolla kohteen on kuljettava, jotta sääntö toimisi.

	

0




Max Speed (Enimmäisnopeus)

	

Enimmäisnopeus (km/h), jolla kohde voi ajaa säännön laukaisemiseksi.

	

0

Tyypillinen loogisen säännön yhdistelmä

Alla olevassa loogisessa esimerkkisäännössä tarkistetaan, että kohde, joka laukaisee alueeseen Roundabout Area liitetyn läsnäolosäännön, kulkee myös nopeussäännön Speed Filter 25-100 km/h määrittämällä nopeudella 25-100 km/h.
Vain nopeussuodattimen arvoksi on määritetty Can Trigger Actions, mikä tarkoittaa, että vain tämä loogisen säännön osa on käytettävissä toimien lähteenä. Lisäksi kaikilla nopeussuodattimen tuottamilla toiminnoilla on tapahtumatyyppi Läsnäolo.




Pagination
Previous page
VCA - Suodattimet
Next page
VCA - Objekti suodatin