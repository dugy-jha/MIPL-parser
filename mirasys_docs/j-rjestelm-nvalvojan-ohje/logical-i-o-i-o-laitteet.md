# Logical I/O (I/O-laitteet) | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/logical-i-o-i-o-laitteet

Logical I/O (I/O-laitteet)

Loogisella I/O:lla on mahdollista luoda toimintoja OR- ja AND-operaattoreiden perusteella.

I/O-ohjain emuloi ulkoista I/O:ta, joka on kytketty itseensä. Esimerkki:

Jos asiakas esimerkiksi haluaa varmistaa, että automaattinen rekisterikilven tunnistus (ANPR) -tapahtuma laukeaa, kun auto on kameran edessä, loogista I/O:ta voidaan käyttää luomaan "sääntö", joka johtaa vain toimintaan. kun VCA havaitsee auton JA samaan aikaan, tapahtuu ANPR-lukutapahtuma.

Toinen esimerkki voisi olla se, että sisäänkäynnin ”portti”, jossa on kaksi ovea, mahdollistaa toisen oven avaamisen vain, kun ensimmäinen on kiinni.

Loogista I/O:ta voidaan käyttää samasta liitännästä kuin muuta System Managerin digitaalista I/O:ta.

Lisenssi ohjaa loogista IO:ta ja lähtölaskentaa. Jos lisenssiä ei ole, uuden IO:n luominen epäonnistuu.

Kun uusi looginen I/O lisätään, dialogin ensimmäinen vaihtoehto on, kuinka monta lähtötilaa käytetään operandeina JA/TAI-päätöksenteossa.

Vähimmäismäärä on kaksi ja enimmäismäärä 32.

 

Kaikki loogiset I/O:t luovat automaattisesti neljä tuloa, joita voidaan käyttää.

 

Input

	

Type




1

	

OR




2

	

AND




3

	

HOLD AND




4

	

PULSE AND

Seuraavissa osissa kuvataan eri tuloja yksityiskohtaisemmin alla olevan esimerkin avulla:

Esimerkissä on 2 lähtöä, joita käytetään Nämä näkyvät IO-luettelossa lähtöinä 3 ja 4.

Automaattisesti luodut 4 tuloa näkyvät luettelossa tuloina 5, 6, 7 ja 8.

"OR" tulo

Ensimmäinen tulo, jonka Looginen I/O luo, on OR-signaali. Jos jokin lähdöistä on päällä, OR-tulo kytketään päälle.

Esimerkissämme tulo 5 on OR-signaali. Jos jompikumpi lähtö 3 TAI lähtö 4 kytketään päälle, tulo 5 kytkeytyy päälle.

Tulo pysyy päällä niin kauan kuin jokin lähdöistä on päällä. (Ellei pulssitilaa ole valittu, katso lisätietoja alta)

"AND" tulo

Toinen tulo on AND-signaali. Jos kaikki lähdöt ovat päällä samanaikaisesti, AND-tulo kytketään päälle. Esimerkissämme, jos molemmat lähdöt 3 ja 4 ovat päällä samanaikaisesti, tulo 6 kytkeytyy päälle.

Tulo pysyy päällä niin kauan kuin kaikki lähdöt ovat päällä. (Ellei pulssitilaa ole valittu, katso lisätietoja alta)

"HOLD AND"

HOLD AND-tulo aktivoituu, jos kaikki lähdöt ovat aktii

visia samanaikaisesti ja aika ensimmäisestä aktivoinnista viimeiseen aktivointiin on lyhyempi kuin HOLD AND odotusaika -liukusäätimessä määritetty aika.

Esimerkissämme, jos lähtö 3 kytketään päälle ja sitten lähtö 4 päälle 10 sekunnin sisällä, tulo 7 aktivoituu.

Tulo pysyy päällä niin kauan kuin kaikki lähdöt ovat päällä. (Ellei pulssitilaa ole valittu, katso alta lisätietoja

"PULSE AND"

PULSE AND -tulo aktivoituu, jos kaikki lähdöt  o

vat olleet aktiivisia tietyn ajan kuluessa.

Jos esimerkissämme lähtö 3 on ollut aktiivinen 10 sekunnin sisällä ja lähtö 4 tulee aktiiviseksi, tulo 8 kytkeytyy päälle.

Tulo 8 pysyy, kunnes määritetty aika on kulunut vanhimmasta aktivoivasta lähdöstä (ellei pulssitilaa ole valittu, katso lisätietoja alta).

Esimerkissämme, kun 10 sekuntia on kulunut lähdön 3 aktivoinnista, tulo 8 sammuu.

Pulssi-tila tuloille

Jokaiselle neljälle sisääntulolle on mahdollista määrittää pulssitila käytettäväksi.

ja

Pulssin kestoa voidaan myös säätää.

Jos pulssitila on käytössä, tulo sammuu asetetun pulssin keston jälkeen.

raavasti:

Se tarkoittaisi tällaista käytöstä:

Pagination
Previous page
LoopBack I/O (I/O-laitteet)
Next page
Countdown I/O (I/O-laitteet)