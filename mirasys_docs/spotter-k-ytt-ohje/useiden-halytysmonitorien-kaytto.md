# Useiden hälytysmonitorien käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-k-ytt-ohje/V9.9/useiden-halytysmonitorien-kaytto

Useiden hälytysmonitorien käyttö

Samalla Hälytys-ponnahdusikkuna-asetuksella kuin yllä, on mahdollista määrittää järjestelmä käyttämään useita hälytysvalvojia siten, että jokaisessa näytössä näkyy vain yksi hälytys (tai useita, jos halutaan). Järjestelmä voidaan määrittää esimerkiksi neljä erillistä hälytysmonitoria. Sitten hälytysmonitori numero 1 näyttää vanhimman hälytyksen, monitori 2 näyttää toiseksi vanhimman hälytyksen ja 3 näyttää kolmanneksi vanhimman hälytyksen. Näyttö 4 voidaan esimerkiksi määrittää näyttämään muut hälytykset.

Konfigurointi tehdään määrittämällä mikä hälytys Alarm-ponnahdusikkunassa tulee näkyä. Hälytysmonitori 1:n konfiguroimiseksi tulee valita ensimmäinen aktiivinen hälytys suodatuksesta.

Toiselle ja kolmannelle tulee avata uusi hälytysten ponnahdusikkuna ja sen jälkeen säätää suodatusta vastaavasti. Neljännelle ja lisähälytykselle asetusta tulee muuttaa seuraavasti:

Kun nämä neljän hälytyksen ponnahdusikkunat ovat auki ja määritettyinä, asettelu on nyt tallennettava. Jos aktiivisia hälytyksiä ei ole, hälytysmonitorit näyttävät selvitysnumeron, joka tietää, mikä monitori. Kun vain yksi hälytys on aktiivinen, se näkyy ensimmäinen näyttö.

Jos kaksi hälytystä on aktiivisia, vanhin näkyy ensimmäisessä näytössä ja uudempi hälytys avautuu toisessa näytössä.

Kolmas hälytys on kolmannessa näytössä.

Kun vanhin hälytys päättyy, se suljetaan ensimmäisestä näytöstä (1).
Monitorit päivittyvät automaattisesti niin, että näytössä 2 aiemmin ollut hälytys on nyt näytössä 1 ja niin edelleen.

Jos hälytysasetukset on määritelty niin, että hälytyskomponentit pidetään auki pidempään kuin hälytyksen kesto, hälytysten siirto tapahtuu vain, kun hälytyskomponentit ovat kiinni.
Tässä tapauksessa näytön yksi hälytysväri muuttuu aktiivisen hälytyksen väristä päättyneen hälytyksen väriksi.
Hälytyksen ponnahdusikkunan suodatinasetus tallennetaan asetteluihin ja tallennettuihin välilehtiin.
AVM:ää käytettäessä on suositeltavaa luoda kamera-välilehti, avata hälytysponnahdusikkuna kameravälilehdelle, määrittää suodatin ja tallentaa se sopivalla nimellä.
Välilehti voidaan sitten avata AVM:lle AVM-käyttökonsolin avulla.
On myös mahdollista määrittää useat hälytysmonitorit näyttämään Hälytysponnahdusikkuna ja Profiilikartta vierekkäin määrittämällä profiilikartta käyttämään samanlaisia suodatusasetuksia kuin hälytysponnahdusikkuna.

Pagination
Previous page
Hälytyksen nimen näyttäminen hälytysponnahdusikkunassa
Next page
Kesäaika (DST)