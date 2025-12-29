# Audit trail loki | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/audit-trail-loki

Audit trail loki

Audit trail lokeja voidaan käyttää VMS järjestelmän käyttäjien aktiviteettien hakuun. Ne löytyvät System Manager sovelluksesta, Järjestelmä-välilehden Seuranta kohdasta.

Audit trail lokit

Audit trail dialogissa Administrator-käyttäjä voi hakea audit trail tapahtumia useilla hakuparametreilla.




Tulokset näytetään listalla ajan mukaan lajiteltuina. Audit trail tapahtumat voidaan lajitella muidenkin kenttien mukaan, klikkaamalla listan sarakkeen otsikkoa.

Hakuparametrit

Seuraavia parametreja voidaan käyttää audit trail tapahtumien hakuun.

Päivä - Valitse haun alkupäivä. Nappulat vasemmalla ja oikealla puolella valitsevat edellisen tai seuraavan päivän.

Aika - Valitse haun alkuaika. Nappulat vasemmalla ja oikealla puolella valitsevat edellisen ja seuraavan tunnin. Nappulat ylös ja alas vähentävät tai lisäävät aikaan 10 minuuttia.

Käyttäjä - Käyttäjä jonka tapahtumia haetaan. Kaikki = haetaan kaikkien käyttäjien tapahtumia.

Sovellus - Minkä sovelluksen tapahtumia haetaan. Kaikki = haetaan kaikkien sovellusten tapahtumia.

Max operaatioiden määrä - Maksimimäärä kuinka monta tapahtumaa haetaan alkuajasta eteenpäin.

Videonhallintapalvelimet - VMS-palvelin-pudotusvalikossa näkyvät kaikki mahdolliset valittavissa olevat VMS-palvelinten arvot.

Haun loppuaika - jos valittu, mahdollistaa haun loppuajan asettamisen samalla tavalla kuin alkuaika asetettiin. Jos ei valittu, loppuaikaa ei käytetä (= haku nykyhetkeen asti)

Audit trail tapahtumat - Mitä tapahtumaa haetaan: voidaan valita yksi tai useampi tapahtuma, kaikki tai ei yhtään tapahtumaa. Jos ei ole valittu yhtään tapahtumaa tai kaikki, niin haetaan kaikki tapahtumat. Näitä nappuloita voi käyttää tapahtumien valintaan:

Valikon laajennus

Valitse kaikki

Tyhjää valinnat




Hakutulokset

Löydetyt audit trail tapahtumat näytetään listalla. Jokaisesta audit trail tapahtumasta näytetään listalla:

Aika - tapahtuman aika.

Käyttäjä - Käyttäjä joka suoritti toimenpiteen.

Sovellus - Sovellus millä toimenpide tehtiin.

Tapahtuma - Tapahtuman nimi. Kun tapahtuma liittyy kameran tarkastukseen ja operaattorin on lisättävä kommentti ennen toistomateriaalin käyttöä, tapahtuma sisältää kommentin.

Tapahtuman tila - Onnistuiko toiminto vai ei.

Objekti - Objekti riippuu itse operaatiosta. Jos esimerkiksi avaat kameran, kameran nimi näytetään.

Videonhallintapalvelimet - Näyttää, millä VMS-palvelimella operaatio tapahtui.

Audit lokin vienti

Listalla olevat audit trail tapahtumat voidaan tallentaa PDF tiedostoon klikkaamalla listan alapuolella olevaa nappulaa. Dialogissa voidaan antaa tiedoston nimi, sijainti, ja kuvaus sisällöstä. Otsikko muodostetaan tallennusajasta ja sen käyttäjän nimestä kuka loi PDF-tiedoston. PDF tiedosto sisältää kaiken listalla näkyvän tiedon.

Pagination
Previous page
Palvelimen diagnostiikka
Next page
Lisenssit