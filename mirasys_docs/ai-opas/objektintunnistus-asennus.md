# Objektintunnistus Asennus | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/objektintunnistus-asennus

Objektintunnistus Asennus

OR-paketteja varten sinun on asennettava ORService- ja ODSService-paketit.

Vaatimukset

Järjestelmänvalvojan oikeudet

VMS-palvelimen objektintunnistuslisenssi

Objektintunnistuspalvelussa on samankaltaisuushaun nopeuttamiseksi samankaltaisuushaun välimuisti, joka voidaan kytkeä päälle tai pois päältä.

Huomautus: Välimuistin käyttö lisää muistin kulutusta.

Voit ottaa samankaltaisuushaun välimuistin käyttöön tai poistaa sen käytöstä palvelun asennuksen yhteydessä.

Asennus

Lataa uusin versio Extranetistä.

Pura tämä esimerkki C:\temp-kansioon.

Aloita asennus kaksoisnapsauttamalla asennustiedostoa.

Jatka napsauttamalla Asenna.

Jatka napsauttamalla Next (Seuraava).

Muuta asennuspaikkaa tarvittaessa, jos et muuta, jatka valitsemalla Next.

Muuta tarvittaessa palvelun HTTP-portti, pääpalvelimen osoite ja portti sekä tapahtumajonon osoite ja portti.

HTTP-portti on oletusarvoisesti 8092

Pääpalvelin (master) käyttää oletusarvoisesti porttia 8082.

Tapahtumajono käyttää oletusarvoisesti porttia 5672. Tapahtumajono asennetaan ODSService-paketin mukana.

Jatka valitsemalla Seuraava.

Valitse vähintään yksi laitteista, joita käytetään TAI:ssa:

CPU

Intel GPU

NVIDIAN NÄYTÖNOHJAIN

Jatka ja odota napsauttamalla Asenna.

Asennus kestää jonkin aikaa, kunnes se on valmis.

Mallien luominen voi kestää jopa 30 minuuttia. Tämä riippuu siitä, kuinka tehokas näytönohjain on käytössä.

Jatka valitsemalla Valmis.

Sulje asennus napsauttamalla Sulje.

Nyt Object Recognition Service on asennettu palvelimelle ja valmis käytettäväksi.

Pagination
Previous page
Objektintunnistus Johdanto
Next page
Mirasys Listojen Hallinta