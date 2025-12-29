# Kaksivaiheinen tunnistautuminen | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/kaksivaiheinen-tunnistautuminen

Kaksivaiheinen tunnistautuminen

Kaksivaiheinen tunnistautuminen on toiminto, joka parantaa käyttäjän tunnistamista vaatimalla käyttäjätunnusta ja salasanaa sekä koodia ulkoisesta fyysisestä laitteesta.

Tämä tekee käytännössä mahdottomaksi mm. tietyt käyttäjäryhmät (esim. järjestelmänvalvojat) käyttämään jaettuja tunnistetietoja.

(Jaettujen tunnistetietojen käyttö tekisi lähes mahdottomaksi esimerkiksi seurata tiettyjä käyttäjän toimintoja tarkastuslokeista myöhemmin.)

Määrittäminen:

Järjestelmänvalvoja ottaa käyttöön 2-vaiheisen todennuksen tietylle käyttäjäryhmälle.

Kun ryhmän käyttäjä yrittää kirjautua sisään ensimmäistä kertaa, käyttäjää pyydetään käyttämään tai asentamaan mobiililaitteeseensa kaksivaiheinen todennusohjelma (esim. Authy, Google authenticator, MS Authenticator (saatavilla ilmaiseksi)).

VMS ja todennus-sovellus synkronoidaan sitten VMS-ohjelmiston kanssa.

Tämä tapahtuu siirtämällä VMS:n luoma "salainen avain" todennusohjelmistoon QR-koodin kautta tai kirjoittamalla se suoraan ohjelmistoon.

Esimerkki:

Tämän jälkeen todennusohjelma luo automaattisesti uudet kertaluonteiset salasanat.

(Salasanat vaihtuvat ajoittain ja synkronoidaan, koska VMS-kelloilla ja todennussovelluksella on sama aika.

Huomaa, että tämä ei vaadi suoraa tietoliikenneyhteyttä ohjelmiston välillä.)

Kirjautuminen:

Käyttäjä antaa VMS:lle tavalliset tunnistetiedot (käyttäjätunnus, salasana)

VMS pyytää todennuskoodia todennussovelluksesta jokaiselle kirjautumiselle.

Käyttäjä antaa kertaluonteisen salasanan todennussovelluksesta. Käyttäjä kirjoittaa ne VMS-sovellukseen.

Ylläpito:

Jos käyttäjä unohtaa 2-vaiheisen salaisen avaimensa, järjestelmänvalvoja voi nollata avaimen järjestelmänhallinnasta.

2-vaiheisen salaisen avaimen nollauksen jälkeen käyttäjän on päivitettävä yksityinen avain seuraavan kerran kirjautuessaan sisään. (Katso kohta 2).

Pagination
Previous page
Toiston nopeuden rooli
Next page
Asiakaskohtaisen käyttäjäryhmän luominen