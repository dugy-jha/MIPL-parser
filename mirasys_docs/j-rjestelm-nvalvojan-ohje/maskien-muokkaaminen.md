# Liiketunnistuksen konfigurointi | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/maskien-muokkaaminen

Liiketunnistuksen konfigurointi

Pääset liiketunnistuksen määrityksiin System Managerissa valitsemalla VMS-palvelimen asetukset > Kameran asetukset > Liiketunnistus.

Valitse kamera avattavasta Kamera-valikosta.

Valitse Mask-asetukset-kohdasta maskin asetukset, jonka haluat määrittää.
Voit muuttaa maskin nimeä. Valitse Change Mask Name (Muuta maskin nimi) ja kirjoita maskille uusi nimi.
Huomaa, että maskin oletusasetuksia ei voi muuttaa.

Piirrä maski kuvan päälle valitaksesi, mille alueelle liiketunnistussyöttö lasketaan. Käytä näkymän oikealla puolella olevia piirtotyökaluja ja maalaa piirtotyökaluilla punaisella alueet, joilla haluat järjestelmän havaitsevan liikkeen, ja poista punainen alueilta, joilla haluat jättää liikkeen huomiotta.

Piirto

Työkalu

	

Nimi

	

Kuvaus







	

Kynä

	

Käytä asettaaksesi liiketunnistusalueen. Valitse kynän koko napsauttamalla jotakin työkalun kokopainikkeista (suuri, keskikokoinen, pieni).







	

Pyyhekumi

	

Käytä poistaaksesi valitut alueet, joita et halua sisällyttää. Valitse pyyhekumikoko napsauttamalla jotakin työkalun kokopainikkeista (suuri, keskikokoinen, pieni).







	

Lasso

	

Käytä alueiden valitsemiseen suorilla viivoilla. Jos kynätyökalu on valittu, tämän työkalun käyttäminen lisää valituille alueille. Jos pyyhekumityökalu on valittuna, tämä työkalu poistaa valitun alueen Napsauta kuvaa, josta haluat aloittaa valinnan. Napsauta uudelleen kohtaa, johon haluat ankkuroida viivan ja muuttaa suuntaa. Viimeistele valinta napsauttamalla aloituspistettä. Valittu alue maalataan punaiseksi tai punainen väri poistetaan.







	

Täytä / tyhjennä

	

Jos kynätyökalu on valittuna, tämän painikkeen napsauttaminen valitsee kuvan kokonaisalueen. Jos pyyhekumityökalu on valittuna, tämän painikkeen napsauttaminen poistaa kaikki valinnat.







	

Käännä vastakkaiseksi

	

Kääntää valitut ja valitsemattomat alueet. Joskus on helpompaa valita alue, jota et halua peittää, ja kääntää valinta sitten käänteiseksi.







	

Työkalun koko

	

Napsauta jotakin painikkeista valitaksesi kynän tai pyyhekumin koon (suuri, keskikoko, pieni).

Aseta tunnistusherkkyys liukusäätimellä.

Aseta liikkeen vähimmäismäärä liukusäätimellä.

Valitse liikkeentunnistusmenetelmä. Voit valita vertailevan, mukautuvan tai hermeneuttisen liikkeentunnistuksen. Tarkempi kuvaus näistä vaihtoehdoista on edellisellä sivulla.

Valitse joko käyttääksesi liikkeentunnistuksen kuvataajuuden oletusarvoa tai liukusäätimellä.

Valitse liikkeentunnistusalusta, joko vain VMS-palvelin tai VMS-palvelin ja kameralaitteisto.

Kun konfiguraatio on viimeistelty, liikkeentunnistusnaamarit on otettava käyttöön ajastimen avulla. Pääset liikkeentunnistusmääritykseen System Managerissa valitsemalla VMS-palvelimen asetukset > Kamera-asetukset > Aikataulutus. Katso seuraavasta asiakirjasta ohjeet aikatauluttajan käyttöön.

Laskuri

Voit testata liiketunnistusta laskurilla. Kun otat laskurin käyttöön, kamerasta lähetetään videokuvaa ja liiketunnistus lasketaan. Liiketunnistuksen tulos näkyy kuvan päällä. Laskurin arvot kasvavat aina, kun liikettä havaitaan asetusten mukaan.

Laskurin käyttäminen:

Ota laskuri käyttöön

Tarkista liikearvot

Kamerakuvasta näkyy, mikä alue kamerakuvassa aiheuttaa liiketunnistustallennuksen

Tallennusta edeltävä ja sen jälkeinen aika

Jos haluat nauhoitettua materiaalia ennen ja jälkeen liikkeen, käytä liikkeen esi- ja jälkitallennusta.

Kumpikin maski voidaan määrittää erikseen.

Arvot ovat välillä 0s - 60 minuuttia.

Voit kopioida valitut arvot kaikkiin kameroihin painikkeella Kopioi esi- ja jälkitallennusaika kaikille kameroille.

Pagination
Previous page
Liikkeentunnistus
Next page
Ajastin