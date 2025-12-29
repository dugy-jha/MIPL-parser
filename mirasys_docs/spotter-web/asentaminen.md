# Asentaminen | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-web/V9.9/asentaminen

Asentaminen
Jos haluat käyttää Spotter Webiä, pääpalvelimen PITÄÄ olla V9.4 tai uudempi!
Käyttöjärjestelmän rajoituksia

Jos SpotterWeb on asennettu asiakaskäyttöjärjestelmään, samanaikaisesti voi olla enintään 10 yhteyttä: https://docs.microsoft.com/en-us/iis/troubleshoot/request-restrictions

Jokaista SpotterWeb-kirjautumista kohden muodostetaan 3 yhteyttä: HTTP, SignalR tapahtumia varten ja WebSocket suoratoistoa varten. Joten esimerkiksi Windows 10 Professionalissa vain 3 asiakasta voi kirjautua sisään samanaikaisesti.

Windows Server-käyttöjärjestelmässä ei ole vastaavia rajoituksia, joten on erittäin suositeltavaa asentaa SpotterWeb Windows Server -käyttöjärjestelmään.

Kun SpotterWeb asennetaan asiakaskäyttöjärjestelmään, asennusohjelma antaa varoituksen OS/IIS-rajoituksista.

Spotter Webin asentaminen

Aloita asennus napsauttamalla SpotterWeb-asennuspakettia

Valitse Install

3. Vahvista ilmoitus käyttöjärjestelmän rajoituksesta

4. Valitse Next

5. Käytä oletusasennuskansiota ja napsauta Next

6. Aseta master-palvelimen osoite (master-palvelimen tietokoneen nimi)

7. Käytä oletusarvoista -master-palvelimen porttia ja -master-palvelimen HTTP-porttia

8. Valitse Next

9. Aseta SpotterWeb-sivuston osoite (master-palvelimen tietokoneen tietokoneen nimi)

10. Käytä oletusarvoista SpotterWeb HTTPS -porttia(443)

11. Tarkista, että Set firewall exceptions on valittuna

12. Valitse Next

13. Valitse Install

14. Valitse Finish

15. Valitse OK ja viimeistele asennus




Pagination
Previous page
Verkkotopologia
Next page
Kirjautuminen - Spotter Web