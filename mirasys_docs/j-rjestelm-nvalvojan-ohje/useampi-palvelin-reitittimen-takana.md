# Useampi palvelin reitittimen takana | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/useampi-palvelin-reitittimen-takana

Useampi palvelin reitittimen takana

Scenario 2: Useampi kuin yksi palvelin yhden reitittimen takana (WAN-osoite)

Jos käyttäjä määrittää laajemman järjestelmän, jossa on useita palvelimia samassa paikassa, hän voi lisätä palvelimet System Manager -sovellukseen ulkoisilla tai sisäisillä IP-osoitteilla.
Kun uutta VMS-palvelinta lisätään, jos palvelin on tehnyt automaattisen portin edelleenlähetyksen, ohjelmisto kertoo, että käyttäjä voi valita sisäisen IP-osoitteen tai ulkoisen IP-osoitteen välillä.
Jos palvelinta käytetään WAN-verkosta, tulee valita ulkoinen IP-osoite.
Tarkka portit, joihin palvelin on siirtänyt portin, voivat löydetään käynnistämällä Järjestelmänhallinta paikalliselta palvelimelta.
Kun palvelin lisätään pääpalvelimeen, joka ei ole paikallisessa verkossa(ei voi käyttää paikallista IP-osoitetta), käyttäjän on tiedettävä ulkoinen IP-osoite ja tiedettävä ensimmäinen portti, johon portin uudelleenohjaus tehtiin.
Jos lisätty palvelin yksittäinen palvelin, portti on todennäköisesti 5009.
Jos samassa paikassa on useita palvelimia, ne todennäköisesti saavat portit, jotka alkavat numeroilla 5009, 5013, 5017, 5021…

Pagination
Previous page
Yksi palvelin reitittimen takana
Next page
Useampi kuin yksi palvelin useilla sivustoilla