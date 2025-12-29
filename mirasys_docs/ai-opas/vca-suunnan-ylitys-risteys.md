# VCA - Suunnan ylitys risteys | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-suunnan-ylitys-risteys

VCA - Suunnan ylitys risteys

Directional crossing (Suunnan ylitys risteys) -sääntö on suunniteltu vähentämään vääriä hälytyksiä, jotka ovat yleisiä yksinkertaisissa linjan ylitystapauksissa. Suuntaa-antava ylitys on suunniteltu käytettäväksi alueen eikä linjan kanssa, ja se lisää useita lisätarkistuksia kohteelle, kun se saapuu alueelle ja poistuu sieltä.

Jotta objekti laukaisisi Directional Crossing -säännön, sen on:

saapua alueelle kulkien suuntaan, joka kuuluu hyväksymiskulmaan.

sen on oltava luokiteltu johonkin määritettyyn objektiluokkaan.

poistua alueelta kulkien suuntaan, joka on hyväksymiskulman sisällä.

Määritä suunta ja hyväksymiskulma siirtämällä nuolinäppäimiä suunnanvalvontawidgetissä. Ensisijainen suunta osoitetaan suurella keskellä olevalla nuolella. Hyväksymiskulma on kahden pienemmän nuolen välinen kulma.

Seuraava kuva havainnollistaa, miten määritettyyn suuntaan liikkuva valkoinen auto käynnistää säännön, kun taas muut kohteet eivät.

Graafinen näkymä
Lomakkeen näkymä
Konfiguraatio
Use table header to sort columns

Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittämä nimi säännölle

	

“Directional #”




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, Voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active




Zone (Alue)

	

Alue, johon tämä sääntö liittyy

	

None




Angle (Kulma)

	

Ensisijainen suuntakulma, 0 - 359. 0 viittaa ylöspäin.

	

0




Acceptance (Hyväksyntä)

	

Sallittu poikkeama ensisijaisen suunnan kummallakin puolella, joka silti laukaisee säännön.

	

0




Classes (Luokat)

	

Hälytyksen laukaisemiseen sallitut objektiluokat

	

None

Pagination
Previous page
VCA - Suunta
Next page
VCA - Oleskelu