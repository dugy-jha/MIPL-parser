# VCA - Hylätty ja poistettu esine | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-hylatty-ja-poistettu-esine

VCA - Hylätty ja poistettu esine

Hylätyn ja poistetun esineen sääntö käynnistyy, kun esine on joko jätetty määritellylle alueelle, esimerkiksi kun henkilö jättää laukun junalaiturille, tai kun esine on poistettu määritellyltä alueelta.
Hylättyjä esineitä koskevalla säännöllä on kesto-ominaisuus, joka määrittelee ajan, jonka esine on oltava hylätty tai poistettu, jotta sääntö käynnistyy.

Alla on esimerkkiskenaario, jossa pussi jätetään määritellylle alueelle, jolloin sääntö aktivoituu.

Alla on samanlainen esimerkkiskenaario, jossa pussi poistetaan määritellyltä alueelta, jolloin sääntö aktivoituu.

Huomautus: Hylätyn ja poistetun kohteen havaitsemiseen käytetty algoritmi on sama kummassakin tapauksessa, joten se ei voi erottaa toisistaan hylättyjä tai poistettuja kohteita.
Tämä johtuu siitä, että algoritmi analysoi vain sitä, miten pikselilohkot muuttuvat suhteessa taustamalliin, joka rakennetaan ajan myötä.




Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittelemä nimi tälle säännölle

	

"Abandoned #"




Zone (Alue)

	

Alue, johon tämä sääntö liittyy

	

None




Duration (Kesto)

	

Aika, jonka objektin on täytynyt olla hylätty tai poistettu ennen kuin sääntö käynnistyy

	

0




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä

	

Active

Pagination
Previous page
VCA - Aggressiivinen käyttäytyminen
Next page
VCA - Ilmestyvät ja katoavat