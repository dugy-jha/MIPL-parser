# Mirasys VCA Lisenssi Serveri | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/mirasys-vca-lisenssi-serveri

Mirasys VCA Lisenssi Serveri

Tämä lisenssipalvelin mahdollistaa VCA:n käytön virtuaalikoneissa tai jos haluat käsitellä lisensointia yhdessä paikassa kaikkien palvelimien osalta. Tätä varten sinun on asennettava Mirasys VCA License Server fyysiseen laitteistoon ja lisensoitava se.
Tämä palvelin voi sitten jakaa lisenssejä virtuaalikoneille.

Tätä ominaisuutta tuetaan versiossa 9.4 eteenpäin.

Älä asenna lisenssipalvelimelle muita palveluita. Tämä voi aiheuttaa ongelmia lisensointipuolella.

VCA-lisenssipalvelinta ei tarvitse asentaa, jos käytät lisenssipalvelimena esimerkiksi Masteria ja tämä on fyysinen palvelin. Tässä tapauksessa VMS sisältää VCA:n ja voit asentaa lisenssit System Manager - VCA Settings -ohjelman kautta. Yhdistä sitten jokainen palvelin tähän Master IP-osoitteeseen.

Portti

8080, TCP VCA-lisenssipalvelimen hallintaa varten.

15769, TCP VCA-lisenssiporttia varten

Asennus

Lataa uusin Mirasys VCA License Server -paketti Mirasys Extranetistä.

Pura ZIP-paketti haluttuun paikkaan ja aloita asennus kaksoisnapsauttamalla asennustiedostoa.

Jatka napsauttamalla Next (Seuraava)

Hyväksy End-User License Agreement (loppukäyttäjän lisenssisopimus) ja napsauta Next (Seuraava).

Seuraa ohjeita, kunnes asennus on valmis

Käyttö ja lisensointi

Mirasys VCA License Serveriin kirjaudutaan selaimella ja siirrytään sivustolle http://localhost:8080/.
Oletuskäyttäjätunnus on admin ja oletussalasana on admin

Pääsivulla pääset asetuksiin burger-valikon kautta.
Lisenssin lisääminen

Avaa Asetukset

Avaa lisenssit

Kopioi laitteistokoodi ja lähetä se Mirasysille saadaksesi lisenssitiedot.

Kun olet saanut aktivointikoodin Mirasysilta, liitä koodi Aktivointikoodi-kenttään ja napsauta Lisää uusi lisenssi-painiketta.

Kun olet lisännyt halutut lisenssit tai lisenssit järjestelmään, voit jatkaa Mirasys VMS:n puolella.

Mirasys VMS:n konfigurointi

System Manager, siirry palvelinosioon ja valitse VCA-asetukset.

Tämä avaa uuden ikkunan, josta löytyy samanlainen burgerivalikko kuin aiemmin.

Tämän valikon alta löydät Asetukset, joilla voit kertoa lisenssipalvelimen DNS/IP-osoitteen.

Sinun on täytettävä lisenssipalvelimen osoite, jonka jälkeen voit klikata yhdistä.

Jos yhteys on muodostettu onnistuneesti, tämä näyttää Mirasys VCA License Server -lisenssit. Tämän jälkeen voit siirtyä VCA-asetuksiin ja lähteisiin määrittääksesi halutun lisenssin halutulle kamerakanavalle.




Pagination
Previous page
Mirasys VCA Deep Learning
Next page
Pilvipalvelun Lisensöinti