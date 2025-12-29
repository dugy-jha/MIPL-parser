# Lokien tallennus | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/lokien-tallennus

Lokien tallennus

Jos järjestelmässä on ongelmia, voit viedä lokitiedostoja ja lähettää ne järjestelmän toimittajalle.
Voit tallentaa lokitiedostot kiintolevylle, levykkeelle tai muulle siirrettävälle tai ei-irrotettavalle laitteelle.

Lokitiedostot tallennetaan pakattuun (zip-tiedostoon).

Lokitiedostojen vienti käyttäen System Manager -ohjelmistoa

Avaa Järjestelmä\Varmuuskopiointi\Lokien tallennus

2. Valitse lokit. Jos palvelimessa on ollut ongelmia, valitse kyseisen palvelimen lokit. Valitse lisäksi System Management Server -palvelimen ja asiakasohjelman lokit. 

Huomaa, että asiakaslokit ovat koneelta, jolla käytät järjestelmänhallintasovellusta.

Nopeaa valintaa varten voit käyttää järjestelmälokien ja VMS-palvelimen lokipaneelien alle sijoitettuja Valitse Kaikki- ja Poista Valinnat -painikkeita. Valitse tai tyhjennä kaikki valinnat tietyille palveluryhmille (esim. rekisterikilven tunnistuspalvelu), jotka sisältävät tiettyjä palveluita, napsauttamalla palveluryhmän valintaruutua.

3. Paina OK-nappia.

4. Valitse tallennuslaite ja kansio, johon haluat tallentaa lokitiedostot. Luo uusi kansio napsauttamalla Uusi kansio -painiketta. 

5. Kirjoita ZIP-tiedoston nimi ja napsauta OK.

Näet viennin edistymisen Tallennuksen edistyminen -ikkunassa. Toiminnot suoritetaan järjestyksessä ylhäältä alas.

Lokien vienti voidaan peruuttaa napsauttamalla ikkunan alareunassa olevaa Peruuta-painiketta.

5. Napsauta OK sulkeaksesi ikkunan, kun vienti on valmis.

6. Järjestelmä vie tiedostot ZIP-tiedostoon. Lähetä ZIP-tiedosto järjestelmän toimittajalle. Palvelulokitiedostot tallennetaan ZIP-päätiedoston sisäiseen ZIP-arkistoon.

Lokien ZIP-arkiston tyypillinen sisältö on seuraava:

Jotkut palvelun aliarkistot voivat jäädä lisäämättä, jos palveluihin ei ole saatu yhteyttä.

Lokitiedostojen vienti käyttäen System Monitor -ohjelmistoa

Järjestelmälokeja on mahdollista kerätä System Monitor -sovelluksen kautta.

1. Avaa System Monitor ja napsauta Tallenna loki-painiketta:

2. Anna arkiston nimi ja anna polku tallennusta varten valintaikkunassa tallentaaksesi vientiarkiston.

3. Napsauta OK aloittaaksesi lokien keräämisen.

System Monitor kerää palvelinlokeja sekä asiakasohjelmien lokeja ja lokien ZIP-arkiston tyypillinen sisältö on sama kuin System Managerin ZIP-arkiston sisältö.

Jotkut palvelun aliarkistot voivat jäädä lisäämättä, jos palveluihin ei ole saatu yhteyttä.

Pagination
Previous page
Varmuuskopiointi
Next page
Asetusten varmuuskopiointi