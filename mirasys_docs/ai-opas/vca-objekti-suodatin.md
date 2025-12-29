# VCA - Objekti suodatin | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-objekti-suodatin

VCA - Objekti suodatin

Object classification (Objektiluokitus)-suodattimella voidaan suodattaa pois objektit, jotka käynnistävät säännön, jos niitä ei luokitella tiettyyn luokkaan (esim. henkilö, ajoneuvo).

Objektiluokitussuodatin on yhdistettävä johonkin toiseen sääntöön tai muihin sääntöihin, jotta voidaan estää ei-toivottuja objekteja laukaisemasta hälytystä, ja tätä havainnollistaa alla oleva esimerkkisääntökaavio.

Edellinen kuva havainnollistaa, kuinka ajoneuvoluokan kanssa määritetty objektiluokitussuodatin sisältää vain ajoneuvo-objekteja.

Alueella oleva henkilö suodatetaan pois, koska Person-luokkaa ei ole valittu suodatinluettelossa.

Kanava on kalibroitava, jotta objektiluokitussuodatin on käytettävissä.

Use table header to sort columns

Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittelemä nimi tälle säännölle

	

"Object Filter #"




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä

	

Active




Input (Sisääntulo)

	

Sisääntulo sääntö

	

None




Classes (Luokat)

	

Hälytyksen laukaisemiseen sallitut objektiluokat

	

None

Tyypillinen loogisen säännön yhdistelmä

Alla olevassa loogisessa esimerkkisäännössä tarkistetaan, onko alueeseen Keskus liitetyn läsnäolosäännön laukaiseva kohde luokiteltu myös Ajoneuvoksi, joka on määritetty kohdesuodattimen Ajoneuvosuodattimessa.

Ainoastaan Objekti-suodattimen arvoksi on asetettu Can Trigger Actions, mikä tarkoittaa, että vain tämä loogisen säännön osa on käytettävissä toimien lähteenä.

Lisäksi kaikilla nopeussuodattimen tuottamilla toiminnoilla on tapahtumatyyppi Läsnäolo.




Pagination
Previous page
VCA - Nopeussuodatin
Next page
VCA - Väri suodatin