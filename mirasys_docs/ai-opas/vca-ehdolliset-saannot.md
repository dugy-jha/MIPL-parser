# VCA - Ehdolliset säännöt | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-ehdolliset-saannot

VCA - Ehdolliset säännöt

Ehdollinen syöttö, kuten suodatin, on sellainen, joka ei voi käynnistää toimintoa yksinään.
Se edellyttää toisen perustulon, ehdollisen säännön tai suodattimen syöttöä ollakseen mielekäs.
Esimerkki tästä on AND-sääntö. AND-sääntö vaatii toimiakseen kahden syötteen vertailun.

Luettelo kaikista ehdollisista säännöistä:

And

Continuously

Counter

Or

Previous

And

Looginen operaattori, joka yhdistää kaksi sääntöä ja laukaisee tapahtumia vain, jos molemmat syötteet ovat totta.

Property

	

Description

	

Default Value




Name (Nimi)

	

A user-specified name for this rule

	

"And #"




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä

	

Active




Input A (Sisääntulo A)

	

Ensimmäinen tulo

	

None




Input B (Sisääntulo B)

	

Toinen tulo

	

None




Per Target (Per kohde)

	

Laukaise yksi tapahtuma per seurattava kohde

	

Active

Jos tarkastellaan kohtausta, jossa on kaksi läsnäolosääntöä, jotka on yhdistetty kahteen erilliseen alueeseen, jotka on yhdistetty AND-säännöllä, alla olevassa taulukossa selitetään Per Target -ominaisuuden käyttäytyminen.
Huomaa, että kohde viittaa tässä seurattuun kohteeseen, jonka VCA-seurantamoottori havaitsee.

State

	

Per Target

	

Outcome




Object A in Input A, Object B in input B

	

On

	

Kullekin kohteelle luotiin kaksi tapahtumaa, yksi




Object A in Input A, Object B in input B

	

Off

	

Vain yksi syntynyt tapahtuma

Lisäksi on tärkeää huomata, että jos sääntö laukeaa, kun Per Target on kytketty pois päältä, se ei laukea uudelleen ennen kuin se "nollataan", eli kunnes AND-ehto ei ole enää tosi.

Continuously

Looginen operaattori laukaisee tapahtumia, kun sen syöttö on tapahtunut yhtäjaksoisesti käyttäjän määrittämän ajan.




Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittelemä nimi tälle säännölle

	

"Continuously #"




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä

	

Active




Input (Sisääntulo)

	

Sisääntulo sääntö

	

None




Per Target (Per kohde)

	

Laukaise yksi tapahtuma per seurattava kohde

	

Active




Aikaväli

	

Aika millisekunteina

	

1000 ms

Kun tarkastellaan kohtausta, jossa on yksi alue, tähän alueeseen liittyvä läsnäolosääntö ja tähän läsnäolosääntöön liitetty Continuously-sääntö, kun Per kohde -ominaisuus on käytössä, sääntö luo tapahtuman jokaisesta seuratusta kohteesta, joka on jatkuvasti läsnä alueella.

Kun ominaisuus on pois päältä, sääntö tuottaa vain yhden tapahtuman, vaikka alueella olisi useita seurattavia kohteita.
Lisäksi kun Per Target -ominaisuus on pois päältä, sääntö tuottaa tapahtumia vain, kun tila muuttuu - eli säännön ehto muuttuu totesta epätodeksi tai päinvastoin.

Kun Per kohde on pois päältä, tila muuttuu, kun:

Minkä tahansa määrän esineitä tulee kyseiselle alueelle ja pysyy siellä

Kaikki esineet poistuvat kyseiseltä alueelta

Or

Looginen operaattori, joka yhdistää kaksi sääntöä ja laukaisee tapahtumia, jos jompikumpi syötteistä on tosi.

Property

	

Description

	

Default Value




Name (Nimi)

	

A user-specified name for this rule

	

"Or #"




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä

	

Active




Input A (sisääntulo A)

	

Ensimmäinen sisääntulo

	

None




Input B (sisääntulo B)

	

Toinen sisääntulo

	

None




Per Target (per kohde)

	

Laukaise yksi tapahtuma per seurattava kohde

	

Active

 If we consider a scene with two presence rules, connected to two separate zones, connected by an OR rule, the table below explains the behaviour of the Per Target property.

State

	

Per Target

	

Outcome




Object A in Input A, No object in input B

	

On

	

Kullekin kohteelle luotiin kaksi tapahtumaa, yksi




No object in Input A, Object B in input B

	

On

	

Vain yksi tapahtuma luotiin (kohteelle B).




Object A in Input A, No object in input B

	

On

	

Vain yksi tapahtuma luodaan (kohteelle A)




Object A in Input A, No object in input B

	

Off

	

Vain yksi syntynyt tapahtuma




No object in Input A, Object B in input B

	

Off

	

Vain yksi syntynyt tapahtuma




Object A in Input A, No object in input B

	

Off

	

Vain yksi syntynyt tapahtuma

Previous

Looginen operaattori laukaisee syötetapahtumat, jotka olivat aktiivisia jossain vaiheessa menneen aikaikkunan aikana.
Tämä ikkuna määritellään nykyisen ajan ja nykyistä aikaa edeltävän ajanjakson välille (määritetään interval-parametrin arvolla).

Property

	

Description

	

Default Value




Name (Nimi)

	

A user-specified name for this rule

	

"Previous #"




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä

	

Active




Input (Sisääntulo)

	

Sisääntulo sääntö

	

None




Per Target (Per kohde)

	

Laukaise yksi tapahtuma per seurattava kohde

	

Active




Aikaväli

	

Aika millisekuntteina

	

1000 ms

Pagination
Previous page
VCA - Laskentalinja
Next page
VCA - Laskurit