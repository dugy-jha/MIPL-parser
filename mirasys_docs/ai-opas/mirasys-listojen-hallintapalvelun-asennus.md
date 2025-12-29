# Mirasys Listojen hallintapalvelun asennus | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/mirasys-listojen-hallintapalvelun-asennus

Mirasys Listojen hallintapalvelun asennus
Vaatimukset

Ylläpitäjän oikeudet

Listojen hallintapalvelu -ominaisuus sisältyy versioon 9.6.0.

Asennus

Lataa viimeisin version Extranetista

Pura paketti esimerkiksi C:\temp -kansioon

Käynnistä asennus tuplaklikkaamalla asennuspakettia

Klikkaa Install aloittaaksesi asennus

Vaihda PostgreSQL-tietokannan salasana

Odota, että PostgreSQL on asennettu

Sinun on ehkä hyväksyttävä asennuksen aikana palomuuriin tehtävät muutokset.

Klikkaa Next jatkaaksesi

Vaihda tarvittaessa asennuspolku, jos tälle ei ole tarvetta klikkaa Next jatkaaksesi

Vaihda portit ja osoitteet tarvittaessa

Jos asennat listojen hallinta palvelun toiselle koneelle, sinun tulee muuttaa Master address -osoite vastaamaan VMS Master -palvelimen osoitetta.

Event queue -osoite on sama osoite, johon listojen hallinta palvelu on asentuu. Pidä tämä oletuksena.

Klikkaa Next jatkaaksesi

Klikkaa Install ja odota

Asennus vie jonkin aikaa kunnes se on valmis

Sinun on ehkä hyväksyttävä asennuksen aikana palomuuriin tehtävät muutokset.

Asennusohjelma asentaa RabbitMQ Serverin, joka käsittelee listojen hallintapalvelun, kasvojentunnistuspalvelun ja rekisterilaattojen tunnistus palvelun tapahtumia.

Vakio portti 5672 TCP.

Klikkaa Finish lopettaaksesi asennus

Klikkaa Close sulkeaksesi asennus

Nyt listojen hallintapalvelu on asennettu palvelimelle ja valmis käytettäväksi.

Listojen hallintapalvelu lähettää tiedot VMS Master -palvelimelle ja voit määrittää palvelun System Managerin kautta.

Pagination
Previous page
Mirasys Listojen Hallinta Esittely
Next page
Mirasys Kasvojen Tunnistus