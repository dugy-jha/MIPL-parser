# Asenna ajuri | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/asenna-ajuri

Asenna ajuri

IP-kameroiden, digitaalisten I/O-laitteiden tai tekstidatan käyttäminen VMS-järjestelmässä edellyttää, että kunkin laitteen ohjain on asennettu palvelimelle.
Ohjelmisto sisältää kaikki ohjaimet ja laajennukset, jotka ovat sisältyneet ohjelmiston aikaisempiin versioihin.
Kuitenkin , tarvittaessa uudet ohjaimet ja liitännäiset voidaan asentaa manuaalisesti.
Uuden ohjaimen asentamiseksi tarvitset laitekohtaisen ohjaimen asennuspaketin.
Ajurin asennuspaketti on pakattu (zip-pakattu) kansio, joka sisältää ohjaintiedostot.
Ajuria asennettaessa asennuspaketti, järjestelmä vertaa asennuspaketissa olevia tiedostoja palvelimilla oleviin tiedostoihin.
Yleensä se asentaa tiedostot vain, jos niitä ei ole palvelimilla tai jos asennuspaketin tiedostot ovat uudempia kuin palvelimilla olevat tiedostot. .
Voit kuitenkin pakottaa järjestelmän asentamaan minkä tahansa ohjainversion tarvittaessa.

Huom: Jos haluat päivittää jo olemassa olevan kameraohjaimen, poista kamera järjestelmästä ennen ajurin päivittämistä.Kameran poistamisen jälkeen asenna ajuritiedosto, jonka jälkeen voit asentaa kameran uudelleen.Uuden ohjaimen asennuksen jälkeen sinun on määritettävä ohjainta käyttävät laitteet.

Ajurin asentaminen:

Avaa Järjestelmä\Ohjelmalisäkkeet\Asenna ajuri

Valitse asema, jossa ohjainpaketti sijaitsee, etsi ja valitse ohjainpaketti (.zip-tiedosto). Asenna ajuri-näkymä avataan

3. Valitse videonhallintapalvelimet, joihin ajuri asennetaan

4. Jos haluat pakottaa järjestelmän asentamaan ohjainpaketin version, valitse  Asenna ajuri, vaikka VMS-palvelimella olisi sama tai uudempi versio ajurista.

5. Valitse Asenna Tila-sarakkeessa näkyy teksti Asenenttu, jos ohjaimen asennus onnistui. Jos ohjainta ei ole asennettu, sarakkeessa näkyy virheilmoitus.

6. Valitse OK

Huomio:

Jos sinun on päivitettävä ajurit muille laitteistoille kuin IP-kameroille, ota yhteyttä järjestelmän toimittajaan.

32-bittinen järjestelmä vaatii 32-bittisen ohjainpaketin ja 64-bittinen järjestelmä 64-bittisen ohjainpaketin.




Pagination
Previous page
Mirasys Camera -ajurit
Next page
Ajurin asennus ja käyttö