# Master-palvelin | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/master-palvelin

Master-palvelin

Verkkojärjestelmässä yksi palvelimista on asetettava pääpalvelimeksi.
Master-palvelin on valvontajärjestelmän keskuspalvelin.
Kaikki muut VMS-palvelimet muodostavat yhteyden siihen, ja kaikki asiakassovellukset kommunikoivat pääpalvelimen kautta.
Jos järjestelmä sisältää vain yhden palvelimen, silloin tämä palvelin on pääpalvelin.
Jos palvelimia on useampi kuin yksi, pääpalvelin voidaan asettaa vapaasti.
On suositeltavaa, että pääpalvelin on omistettu palvelin pelkästään tätä tarkoitusta varten laajemmassa järjestelmässä .

HUOMIO: Pääpalvelimissa on oltava SQL Server Express 2019 tai muu Microsoft SQL Server asennettu.

Pääpalvelin tekee nämä asiat:

Se varmistaa kaikkien järjestelmään kirjautumista yrittävien ohjelmien ja käyttäjien henkilöllisyyden (todennus).

Se tallentaa kaikki järjestelmän kokoonpanotiedot.

Se tallentaa kaikki käyttäjätiedot.

Se valvoo järjestelmää.

Se synkronoi kaikkien palvelimien kellot.

Se tuottaa raportteja.

Se tallentaa ohjelmistovahdin tapahtumat

Se tallentaa hälytykset

Se tallentaa kirjausketjut.

Pagination
Previous page
VMS-palvelimet
Next page
Asiakasohjelmistot