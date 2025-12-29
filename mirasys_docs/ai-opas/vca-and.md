# VCA - And | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-and

VCA - And

Looginen operaattori, joka yhdistää kaksi sääntöä ja laukaisee tapahtumia vain, jos molemmat syötteet ovat totta.

Graafinen näkymä
Lomakkeen näkymä
Konfigurointi
Use table header to sort columns

Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittelemä nimi tälle säännölle

	

“And #”




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active




Input A (Sisääntulo A)

	

Ensimmäinen sisääntulo

	

None




Input B (Sisääntulo B)

	

Toinen sisääntulo

	

None




Per Target (Per kohde)

	

Laukaise yksi tapahtuma per seurattava kohde

	

Active

Jos tarkastellaan kohtausta, jossa on kaksi läsnäolosääntöä, jotka on yhdistetty kahteen erilliseen alueeseen, jotka on yhdistetty AND-säännöllä, alla olevassa taulukossa selitetään Per Target -ominaisuuden käyttäytyminen. Huomaa, että kohde viittaa tässä seurattuun kohteeseen, jonka VCA-seurantamoottori havaitsee.

Use table header to sort columns

State

	

Per Target

	

Outcome




Object A in Input A, Object B in input B

	

On

	

Kaksi tapahtumaa, yksi kullekin kohteelle




Object A in Input A, Object B in input B

	

Off

	

Vain yksi syntynyt tapahtuma




Pagination
Previous page
VCA - Ehdolliset sääntötyypit
Next page
VCA - Continuously