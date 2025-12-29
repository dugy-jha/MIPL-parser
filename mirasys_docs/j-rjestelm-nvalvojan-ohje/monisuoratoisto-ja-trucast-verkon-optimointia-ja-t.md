# Monisuoratoisto ja TruCast verkon optimointia ja tallennusta varten | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/monisuoratoisto-ja-trucast-verkon-optimointia-ja-t

Monisuoratoisto ja TruCast verkon optimointia ja tallennusta varten

Koska TruCastille on mahdollista käyttää myös muuta kuin tallennusstreamia, tämä tulee ottaa huomioon verkon kapasiteettia suunniteltaessa.

Käyttäjät voivat esimerkiksi katsoa live-kuvia TruCastilla suuremmalla kuvanopeudella (esimerkiksi 25 fps) ja tallentaa aina pienemmällä kuvanopeudella (esimerkiksi kahdeksan kuvaa sekunnissa).

Tämä vähentää huomattavasti tallennus- ja verkkovaatimuksia.

TruCastin vaikutus kuvan viiveeseen

Koska TruCast-striimi ei kulje VMS-palvelimelle ja takaisin, viive kamerasta asiakkaalle on hieman pienempi, mutta ero palvelimelta saatuun streamiin ei ole suuri, vain muutama millisekunti.

Kahden streamin tilan eroa on vaikea havaita tosielämässä.

Ominaisuudet, joita ei tueta TruCast Streaming 2:ssa

TruCast ei tue PTZ-ohjausta tai ääntä

Lisäksi TruCast tukee tällä hetkellä vain live-kuvia. Toisto (tallennettujen kuvien) vastaanotetaan tällä hetkellä aina palvelimelta.

Lisenssit

TruCast edellyttää, että VMS-lisenssillä on TruCast-ominaisuus ja TruCast-asiakasohjaintunnisteet.

Nämä TruCast-ajurilisenssit ja TruCast-ominaisuus ovat aina käytössä Mirasys V9 -tuoteversiossa.

Useita Spotter-sovelluksia

Koska jokainen TruCast-katselija avaa yksittäisen uuden streamin kamerasta asiakkaalle, käyttäjien tulee kokeilla kuinka monta streamia voidaan luotettavasti avata käyttämistään kameroista. Käytännössä 3-5 streamia toimii yleensä ok.

Asiakasohjelman ajurin asentaminen

Ennen TruCastin käyttöä tarvittavat asiakasohjaimet on asennettava System Manager -sovelluksen kanssa, jos niitä ei ole asennettu alkuperäisen järjestelmäasennuksen yhteydessä.

Asiakasohjainpaketit ovat saatavilla Mirasysin koko asennuspaketissa. Ne on nimetty ".sdi"-tiedostotunnisteella.

Nämä ohjaimet asennetaan System Manager -sovelluksen ensimmäiselle sivulle "Asenna asiakasohjelman ajuri".

Uudet ajurit voidaan lisätä painamalla "Asenna uusi asiakasohjain" -painiketta ja valitsemalla SDI-paketit.

Tämän jälkeen valitse OK

Ajurien asennuksen jälkeen ne on vielä ladattava katselu Spotter-sovellukselle. Tämä tehdään, kun Spotter käynnistetään uudelleen työpöydältä.

Kun Spotter on ladannut uudet ajurit, järjestelmä on valmis TruCast-käyttöön.

Huomaa, että vain ne kamerat, joiden asiakasohjelmiston ajuri on asennettu, näkyvät TruCast-käytössä.

Monisuoratoiston määrittäminen

TruCast voi käyttää mitä tahansa suoratoistoa kamerasta, tallennuslaatua, katselulaatua tai suoratoiston laatua.

Multi-streaming on käytössä ja konfiguroitu tyypillisesti System Managerissa – kameroissa.

Spotter-asiakasasetuksissa – streaming – multi-streaming käyttäjä voi valita, kumpaa striimeistä käytetään katseluun. Samaa asetusta käytetään vakio- ja TruCast-katselussa.

TruCast oletusasetukset

Oletusasetukset kaikille kameroille, joita ei ole käytetty TruCastissa aiemmin, voidaan määrittää kohdassa Spotter-asetukset – streaming – TruCast-oletusarvo.

Mahdolliset arvot ovat

Striimaa aina videonhallintapalvelimelta

Striimaa VMS-palvelimelta, jos siihen on yhteys, ja muuten striimaa kameralta

Striimaa aina kameralta




Pagination
Previous page
Verkon optimointi
Next page
TruCastin käyttö