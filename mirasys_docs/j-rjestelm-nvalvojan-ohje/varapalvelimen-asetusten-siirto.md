# Varapalvelimen asetusten siirto | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/varapalvelimen-asetusten-siirto

Varapalvelimen asetusten siirto
Varapalvelimen asetusten siirto

Tuettu V9.5.0:sta lähtien

V9.5.0:ssa palautus voidaan tehdä joko automaattisesti tai manuaalisesti, eikä asetusten varmuuskopiointia tarvitse käyttää vikasietotilan palauttamiseen.
Varapalvelimen asetusten siirto käyttää samoja toimintoja kuin varapalvelin, mutta käänteisessä järjestyksessä siirtämällä palvelintoiminnot varapalvelimelta takaisin korjatulle palvelimelle. Manuaalinen varapalvelimen siirto voidaan tehdä varapalvelimen lokista. Automaattinen palautus käynnistää palautuksen, kun automaattinen palautus on käytössä ja yhteys epäonnistuneeseen tallentimeen palautetaan onnistuneesti.

Varapalvelimen asetusten siirron prosessi

Kun varapalvelimen asetusten siirto käynnistetään(manuaalisesti tai automaattisesti)

Tarkista, että varapalvelinlokin merkintä on kelvollinen ja että lokin varapalvelintila on oikea

Tarkista, että varapalvelin toimii edelleen normaalina tallentimena

Tarkista, että viallinen palvelin on edelleen rikki

Tarkista, että varapalvelin on käytössä lisenssissä

Tarkista, että viallisella tallentimelle ei ole käynnissä palautusprosessia

Päivitä varapalvelinloki, joka alkaa

Hanki varapalvelimen asetukset, määritystiedostot, maskit ja aikataulut tallentimen asetusten välimuistista

Aseta viallisen tallentimen asetukset

Merkitse varapalvelin toimimaan uudelleen varapalvelimena ja merkitse epäonnistunut tallennin ok-tilaan

Päivitä varapalvelinloki, joka on suoritettu

Lähetä järjestelmämuutosilmoitus asiakkaille

Manuaalinen varapalvelimen asetusten siirto

Varapalvelimen toimintojen siirto voidaan käynnistää manuaalisesti Varapalvelimen manuaalinen toimintojen  siirto on mahdollista, jos

Varapalvelimen käyttöönotto on tehty onnistuneesti

Varapalvelimen siirto ei ole kesken tai siirtoa ei ole jo tehty

Käyttäjän rooli mahdollistaa varapalvelimen toimintojen manuaalisen siirron

Automaattinen varapalvelimen asetusten siirto

Automaattinen palautus voidaan ottaa käyttöön tallentimen yleisistä asetuksista, kun varapalvelin on käytössä tallentimessa. Automaattista varapalvelinprosessia ei tapahdu, jos huoltotila on päällä.
Automaattinen palautus käynnistyy, kun SMServer muodostaa yhteyden epäonnistuneeseen tallentimeen.
Varapalvelimen toimintojen siirron-toiminto hakee sitten kaikki varapalvelinlokimerkinnät epäonnistuneen tallentimen varapalvelinlokitietokannasta, jos vikasietoprosessi on suoritettu onnistuneesti ja palautusprosessia ei ole suoritettu onnistuneesti eikä palautusprosessi ole käynnissä.
Jos yksi tai useampi lokimerkintä löytyy, palautusprosessi (kuvattu yllä) käsitellään.
Jos automaattisen palautusvaatimuksen täyttäviä varapalvelinlokimerkintöjä on useampi kuin yksi, uusinta lokimerkintää käytetään palautusprosessissa. Kun palautusprosessi on suoritettu onnistuneesti, palautukseen käytetty lokimerkintä päivitetään, jotta palautus on suoritettu onnistuneesti. Muiden lokimerkintöjen kohdalla palautus ja materiaalin kopiointi on merkitty onnistuneiksi.


Materiaalin kopiointi varapalvelimen asetusten siirron yhteydessä

Materiaalikopiointi tehdään varapalvelimesta päätallentimeen, tämä tehtävä lisätään tallentimen käsittelyyn DVRFailoverServicen avulla.

DVRFailoverServicellä on seuraavat menetelmät:

StartDataCopy - lisää uusi materiaalin kopiointitehtävä tallentimen käsittelyjonoon

UpdateClientInfo - päivitä tallentimen asiakastiedot, jos tallentimen ja SMS-palvelimen välinen yhteys katkesi kommunikoimaan virhetallennuksen kanssa oikein

UpdateFailoverTaskStates - päivitä materiaalin kopion tila, jos yhteys tallentimen ja SMS-palvelimen välillä katkesi

Palvelin tallentaa materiaalin kopiointitehtävän tietokantaan ja käsittelee ne yksitellen. Jos jokin tehtävä epäonnistuu, tallennin tallentaa viimeiset tehtäväajat ja ilmoita ja jatka muiden tehtävien kanssa

Mitä kopioidaan materiaalin kopioinnin aikana tietyn ajanjakson ajaksi (varapalvelin siirron alkaminen ja palautuksen lopetus):

Äänitiedot kaikille konfiguroiduille äänikanaville

Videotiedot kaikille määritettyille videokanaville

Tekstitiedot kaikille määritetyille tekstikanaville

Metadata kaikille määritettyille video- ja tekstidatakanaville

ANPR-tiedot kaikille määritetyille videokanaville

Hälytykset kaikille määritetyille hälytystunnuksille

Tallennin käsittelee jokaisen yllä olevan kanavan yksitellen ja tallentaa viimeksi vastaanotetun kanavan ajan. Jos palvelimien välinen yhteys katkeaa tai tapahtuu virhe, palvelin tallentaa materiaalikopiointitehtävän viimeisen tilan ja jatkaa viimeisestä käsittelemättömästä kanavasta (ja viimeisestä käsitellystä kanavasta).

Palvelin käyttää äänen, videon, tekstin ja metatietojen toistotoimintoja sekä ANPR- ja Alarms-hakupalveluita saadakseen tarvittavat tiedot tietyltä ajanjaksolta.
Myöskään Geniune-kanavien tietoturvarajoitusten vuoksi emme voi käyttää tallenninta ZpaServerinä ja ZpaClientinä samanaikaisesti, 
joten takaisinkutsut eivät toimi palvelimesta palvelimeen.

Varapalvelinsiirtojen loki

Valitse Avaa varapalvelinsiirtojen loki-painiketta Videonhallintapalvelimet-välilehdeltä

2. Vikatilanne loki näyttää Aktiiviset varapalvelimet ja Suoritetut varapalvelimen asetusten siirrot

Aloita asetusten siirto valitulta varapalvelimelta

3. Liitä korjattu VMS-palvelin verkkoon samalla IP-osoitteella

4. Valitse palvelin listalta

5. Valitse Aloita asetusten siirto valitulta varapalvelimelta

Kun asetukset on siirretty onnistuneesti, niin ilmoitus varapalvelimen siirto OK näytetään aloitusajalla, loppuajalla sekä kestolla

Materiaalin kopiointi valitulle palvelimelle

Valitse palvelin listalta

Valitse luettelosta ensimmäinen materiaalikopio, jota ei ole vielä viimeistelty

Valitse Aloita materiaalin kopiointi valitulle palvelimelle




Pagination
Previous page
Failover-järjestelmän rakentaminen
Next page
Mirasys VMS käyttöönoton pikaohje