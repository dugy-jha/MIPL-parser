# VCA - Takaa-ajo | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-takaa-ajo

VCA - Takaa-ajo

Tailgating (takaa-ajo) -sääntö havaitsee kohteet, jotka ylittävät vyöhykkeen tai viivan nopeasti peräkkäin.
Tässä esimerkissä kohde 1 on ylittämässä havaintolinjan. Toinen kohde (kohde 2) seuraa tiiviisti perässä.
Perässäajon havaitsemiskynnys on asetettu 5 sekunniksi.
Tämä tarkoittaa sitä, että kaikki kohteet, jotka ylittävät linjan 5 sekunnin kuluessa siitä, kun jokin kohde on jo ylittänyt linjan, laukaisevat kohteen perässäajosäännön.

Kohde 2 ylittää viivan 5 sekunnin kuluessa kohteesta 1. Tämä laukaisee perässäajosuodattimen ja aiheuttaa tapahtuman.

Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittämä nimi säännölle

	

"Tailgating #"




Zone (Alue)

	

Alue, johon tämä sääntö liittyy

	

None




Duration (Kesto)

	

Enimmäisaika, joka kuluu ensimmäisen ja toisen kohteen vyöhykkeelle saapumisen välillä säännön käynnistämiseksi.

	

0




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, Voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active

 

Pagination
Previous page
VCA - Läsnäolo
Next page
VCA - Pysähtynyt