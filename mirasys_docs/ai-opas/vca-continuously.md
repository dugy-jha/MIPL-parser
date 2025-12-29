# VCA - Continuously | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-continuously

VCA - Continuously

Continuously (Jatkuvasti) on looginen operaattori, joka laukaisee tapahtumia, kun sen syöttö on tapahtunut yhtäjaksoisesti käyttäjän määrittämän ajan.

Graafinen näkymä
Lomakkeen näkymä
Konfigurointi
Use table header to sort columns

Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittelemä nimi tälle säännölle

	

“Continuously #”




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active




Input (Sisääntulo)

	

Sisääntulo

	

None




Per Target (Per kohde)

	

Laukaise yksi tapahtuma per seurattava kohde

	

Active




Interval (Aikaväli)

	

Aika millisekunteina

	

1

Kun tarkastellaan kohtausta, jossa on alueeseen liitetty Läsnäolosääntö ja tähän Läsnäolosääntöön liitetty Jatkuvasti-sääntö, ja kun Per kohde -ominaisuus on käytössä, sääntö luo tapahtuman jokaiselle seuratulle kohteelle, joka on jatkuvasti läsnä alueella. Kun ominaisuus on pois päältä, sääntö tuottaa vain yhden tapahtuman, vaikka alueella olisi useita seurattuja kohteita. Lisäksi kun Per Target -ominaisuus on pois päältä, sääntö tuottaa tapahtumia vain silloin, kun tila muuttuu, eli säännön ehto muuttuu totesta epätodeksi tai päinvastoin. Kun Per kohde on pois päältä, tila muuttuu, kun:

Minkä tahansa määrän esineitä tulee kyseiselle alueelle ja pysyy siellä

Kaikki esineet poistuvat kyseiseltä alueelta

Pagination
Previous page
VCA - And
Next page
VCA- Laskuri