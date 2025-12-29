# Object Recognition (OR) Asetukset | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/object-recognition-or-asetukset

Object Recognition (OR) Asetukset

Järjestelmänvalvojan asetukset, joiden avulla käyttäjät voivat käyttää kohteiden tunnistusta Spotterin älykkäässä haussa.

Kohteen tunnistuksen asetukset

Objektintunnistusasetukset löytyvät System Managerista VMS Server -välilehdeltä > Kamerat.

Siirry Kamera-asetukset-ikkunassa OR-asetukset-välilehdelle.

Jos käyttäjälisenssi ei tue objektintunnistusominaisuutta, OR-asetukset-välilehti on piilotettu.

Valitse kamera, suoratoisto ja ota käyttöön TAI

Valitse kamera pudotusvalikosta kohdassa OR

Jos Stream on useampi kuin yksi, voit valita stream. Jos on vain yksi stream, on oletusstream kuten yllä olevassa kuvassa, ja pudotusvalikko on poistettu käytöstä.

Voit valita palvelun vasta, kun olet ottanut palvelun käyttöön napsauttamalla Enable OR for selected camera (Ota TAI käyttöön valitulle kameralle) -ruutua.

Jos Enable OR for selected camera (Ota TAI käyttöön valitulle kameralle) -ruutua ei ole rastitettu, Service (Palvelu) -pudotusvalikko ei ole käytössä.

Lisenssin tekstiruutu näyttää käytettyjen lisenssien määrän ja lisenssien enimmäismäärän.

Jos kamera ei tue TAI-palvelua tai palvelua ei ole käytössä, palvelua ei voi ottaa käyttöön lainkaan.

Keltainen kuvake ilmaisee tämän, ja jos käyttäjä vie hiiren sen päälle, näkyviin tulee työkaluvihje, jossa on teksti There's no active OR service for this camera.

Havaintoalue / kohteen vähimmäiskoko

Tunnistusalueella oleva kuva ladataan heti, kun nykyinen kamera on valittu Camera Combobox -valintaruudussa.

Kohteen vähimmäiskokoa voidaan säätää kahdella tavalla:

Säädä prosenttiosuus kohdassa Min. objektin korkeus (%).

Säädä se kehyksessä, jossa on ilmoitettu neliö kohdasta Minimi objektikoko. Neliöllä on sama väri kuin kehyksen oikealla puolella olevassa valitsijassa.

Minimikoko ei voi olla alle 10 %.

Tunnistusparametrit

Max objects - kuvasta tunnistettavien kohteiden enimmäismäärä. Arvon tulisi olla 1 ja 100 välillä.

Minimi luottamus (%) - tunnistimen luottamustaso. Jos havaitun kohteen luotettavuus on alle tämän raja-arvon, kohde jätetään huomiotta. Kelvolliset arvot ovat välillä 25 % - 95 %.

Havaintoväli (ms) - millisekuntien määrä, joka kuvaa, kuinka usein kohteen havaitseminen tehdään: jos se on esimerkiksi 250 ms, kohteen havaitseminen tehdään neljä kertaa sekunnissa (vaikka videovirran kehysnopeus olisi paljon suurempi, esimerkiksi 30 kuvaa sekunnissa).

Laite - käytetään päättelyyn. Käytettävissä olevat laitteet riippuvat varsinaisen palvelun laitteistosta.

Sisällytä pikkukuvan valintaruutu - sisällyttää tunnistuksen lähdekuvan pikkukuvan palautettuihin tietoihin tai ei.

Thumbnail height (px) - pikkukuvan korkeus pikseleinä. Ainoastaan käytössä, jos Sisällytä pikkukuva -ruutu on valittuna. Arvon tulisi olla 32 ja 128 pikselin välillä.

Sisällytä objektien kuvat valintaruutu - sisällytätkö objektien kuvat palautettuihin tietoihin vai et.

Enable images HW decoding -valintaruutu - mahdollistaa syötettyjen kuvien dekoodaamisen sopivimmalla laskenta-alustalla (CUDA, DXVA tai DirectX).

Kohteen tietovaraston asetukset

Jos haluat valita tietokantaan tallennettavien tapahtumien enimmäismäärän ja sen, kuinka kauan tapahtumia säilytetään, valitse System Managerin Järjestelmäasetukset > Object Data Store Settings.




Pagination
Previous page
Face Recognition (FR) Asetukset
Next page
VCA-asetukset