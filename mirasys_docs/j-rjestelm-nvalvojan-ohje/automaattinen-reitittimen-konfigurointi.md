# Automaattinen reitittimen konfigurointi | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/automaattinen-reitittimen-konfigurointi

Automaattinen reitittimen konfigurointi

Kun VMS-palvelin käynnistyy, se yrittää löytää UPnP-laitteita verkosta.
Reitittimen on tuettava UPnP:tä (Universal Plug and Play), jonka on oltava käytössä laitteessa.
Palvelimella on jatkuva UPnP-laitteen etsintä käynnissä, joten jos verkkoon tehdään muutoksia, palvelin havaitsee automaattisesti uudet reitittimet ja välittää niille portin.
Vain UPnP-laitteet, joilla on ulkoinen (WAN) osoite, tunnistetaan.
Jos käyttäjä haluaa poistaa portin uudelleenohjauksen automaattisesti, hän voi tehdä sen järjestelmänhallinnasta. .
Tämän jälkeen palvelin muistaa, että asetukset on poistettu, eikä porttivälitystä tälle reitittimelle.
Ohjelmisto ei salli portin edelleenohjauskartoituksen poistamista, jos palvelin on lisätty järjestelmään ulkoisella osoitteella.
Portin edelleenlähetyksen poistaminen irroittaa järjestelmän, eikä muita määrityksiä ole mahdollista tehdä.
Jos edelleenlähetysportin asetuksia muutetaan ja yhteys palvelimeen ei ole palannut hetken kuluttua, saattaa olla tarpeen käynnistää uudelleen reititin.
Palvelimet tarvitsevat neljä porttia palvelimen välistä viestintää varten. Ensimmäinen palvelin, joka suorittaa portin edelleenohjauksen, vaatii portteja 5008, 5009, 5010  ja 5011.
Toinen palvelin vaatii portteja 5012-5015, kolmas palvelin portteja 5016-5019. Ja niin edelleen (Olettaen, että kaikki portit ovat käytettävissä).
Ensimmäistä porttia käytetään SMS-palvelinviestintään (5008, 5012, 5016…)
Toista porttia käytetään DVRServer-prosessiviestintään (5009, 5013, 5017…)
Käytettäessä yhteyttä pääpalvelimeen, portti on tyypillisesti 5008. Kun lisäät uusia palvelimia isäntäkoneeseen, portti on yleensä 5009. Jos paikalla on useampi kuin yksi palvelin, portit ovat 5009 +4, 5009 + 8 jne.

Pagination
Previous page
Portinohjaus
Next page
Yksi palvelin reitittimen takana