# VCA - Or | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-or

VCA - Or

Looginen operaattori, joka yhdistää kaksi sääntöä ja laukaisee tapahtumia, jos jompikumpi syötteistä on tosi.

Graafinen näkymä
Lomakkeen näkymä
Konfigurointi
Use table header to sort columns

Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittelemä nimi tälle säännölle

	

“Not #”




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

If we consider a scene with two Presence rules connected to two separate zones, connected by an OR rule, the table below explains the behaviour of the Per Target property.

Use table header to sort columns

State

	

Per Target

	

Outcome




Object A in Input A, No object in input B

	

On

	

Kaksi tapahtumaa, yksi kullekin kohteelle




No object in Input A, Object B in input B

	

On

	

Vain yksi syntynyt tapahtuma objekti B:lle




Object A in Input A, No object in input B

	

On

	

Vain yksi syntynyt tapahtuma objekti A:lle




Object A in Input A, No object in input B

	

Off

	

Vain yksi syntynyt tapahtuma




No object in Input A, Object B in input B

	

Off

	

Vain yksi syntynyt tapahtuma




Object A in Input A, No object in input B

	

Off

	

Vain yksi syntynyt tapahtuma

Lisäksi on tärkeää huomata, että jos sääntö laukeaa, kun Per Target on kytketty pois päältä, se ei laukea uudelleen ennen kuin se "nollataan", eli ennen kuin OR-ehto ei ole enää tosi.




Pagination
Previous page
VCA - Not
Next page
VCA - Previous