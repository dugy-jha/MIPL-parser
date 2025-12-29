# VCA - Väri suodatin | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-vari-suodatin

VCA - Väri suodatin

Colour (Väri)-suodatin käyttää Colour Signature -algoritmia ja mahdollistaa kohteiden suodattamisen sen perusteella, sisältääkö kohde tietyn värikomponentin.

Värisignatuurialgoritmi vastaa havaitun kohteen jokaisen pikselin ryhmittelystä johonkin 10:stä värisäiliöstä.

Värisuodattimen avulla voit valita yhden tai useamman näistä väripesistä, ja se käynnistyy, jos kohde koostuu yhdestä tai useammasta näistä valituista väreistä.

Alla olevassa kuvassa on esimerkki seuratusta kohteesta, jonka värisignaatiomerkinnät on otettu käyttöön.
Tässä kohteeseen liitetty värivalikoima edustaa neljää tärkeintä väriä, jotka muodostavat yli 5 prosenttia kohteesta.

Tässä tapauksessa seurataan henkilöä, jolla on hyvin näkyvä suojavaatetus. Tässä värisuodatin on asetettu toimimaan keltaisella värillä, jolloin henkilö havaitaan mutta varjo jätetään huomiotta.

Väriluokitussuodatin yhdistetään yleensä johonkin muuhun sääntöön (tai muihin sääntöihin), jotta ei-toivotut kohteet eivät laukaise hälytystä, ja tätä havainnollistaa alla oleva esimerkkisääntökaavio.

Edellinen kuva havainnollistaa, kuinka ajoneuvoluokalla Vehicle (Ajoneuvo) määritetty objektiluokitussuodatin sisältää vain ajoneuvo-objekteja.

Alueella oleva henkilö suodatetaan pois, koska Person-luokkaa ei ole valittu suodatinluettelossa.

Kanavalla on oltava Värisignatuuri käytössä, jotta värisuodatin toimii.

Use table header to sort columns

Property

	

Description

	

Default Value




Name (Nimi)

	

A user-specified name for this rule

	

"Object Filter #"




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active




Input (Sisääntulo)

	

Sisääntulo sääntö

	

None




Colours (värit)

	

Hälytyksen laukaisemiseen sallitut värit

	

All Unchecked

Tyypillinen loogisen säännön yhdistelmä

Alla olevassa loogisessa säännössä tarkistetaan, että läsnäolosäännön laukaiseva kohde Junarivi, joka on liitetty alueeseen, sisältää myös vihreän värin yhtenä neljästä prosentuaalisesti tärkeimmästä väristä.

Ainoastaan Värisuodatin on asetettu arvoon Voi laukaista toimintoja, mikä tarkoittaa, että vain tämä loogisen säännön osa on käytettävissä toimintojen lähteenä.

Lisäksi kaikilla nopeussuodattimen tuottamilla toiminnoilla on tapahtumatyyppi Läsnäolo.




Pagination
Previous page
VCA - Objekti suodatin
Next page
VCA - Uudelleentriggeröintisuodatin