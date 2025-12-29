# License Plate Recognition (LPR) Asetukset | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/license-plate-recognition-lpr-asetukset

License Plate Recognition (LPR) Asetukset

Järjestelmänvalvojan asetukset, joiden avulla operaattorit voivat käyttää rekisterikilven tunnistusta Spotter Smart Searchissa ja Spotter Smart Recognitionissa.

RTSP Server Streaming ominaisuus pitää olla mukana lisenssissä.

License Plate Recognition asetukset

Rekisterikilven tunnistusasetukset löytyvät System Managerista VMS Server -välilehdeltä > Kamerat.

Siirry Kamera-asetukset-ikkunassa LPR-asetukset-välilehdelle.

Jos lisenssissä ei ole Smart LPR ominaisuutta, LPR asetuksia ei voi muokata.

Valitse kamera, stream ja ota LPR käyttöön

Valitse kamera LPR:n pudotusvalikosta.

Jos Stream on useampi kuin yksi, voit valita stream. Jos on vain yksi stream, käytössä on oletusstream kuten yllä olevassa kuvassa, ja pudotusvalikko on poistettu käytöstä.

Voit valita palvelun vasta, kun olet ottanut palvelun käyttöön napsauttamalla Enable LPR for selected camera (Ota LPR käyttöön valitulle kameralle) -ruutua.

Jos Enable LPR for selected camera (Ota LPR käyttöön valitulle kameralle) -ruutua ei ole rastitettu, Service (Palvelu) -pudotusvalikko ei ole käytössä.

Lisenssin tekstiruutu näyttää käytettyjen lisenssien määrän ja lisenssien enimmäismäärän.

Tunnistusparametrit

Kun kamera, kameran striimi ja LPR-palvelu on valittu, LPR-asetuksia voi muokata. Asetukset löytyvät Tunnistusparametrit kohdasta LPR-asetukset välilehdeltä Kamera-asetukset ikkunassa.

Asetukset ovat LPR-palvelua varten.

Tunnistusalue - määrittää sen alueen minkä sisältä rekisterikilpiiä tunnistetaan.

Saman rekisterinumeron tunnistuksen viive - kuinka monta sekuntia pitää kulua ennen kuin lähetetään uusi tapahtuma saman rekisterinumeron tunnistuksesta.

Maksimi rekisterilaattojen määrä - maksimimäärä sille kuinka monta rekisterikilpeä tunnistetaan.

Minimi merkkitunnistuksen luotettavuus - minimiarvo rekisterinumeron merkkien tunnistuksen luotettavuudelle, väliltä 25% - 95%.

Minimi rekisterilaattojen tunnistusluotettavuus - minimiarvo rekisterikilpien tunnistuksen luotettavuudelle, väliltä 25% - 95%.

Minimi rekisterilaatan korkeus - rekisterikilpien minimikorkeus % kuvan korkeudesta, väliltä 1% - 50%.

Tunnistusväli - millisekunttia, kuinka usein tunnistusta tehdään: jos se on esimerkiksi 250 ms, niin tunnistus tehdään 4 kertaa sekunnissa (vaikka videostriimin kuvatahti olisi paljon korkeampi, kuten 30 fps).

Laite - mitä laitetta käytetään tunnistuksissa. Käytettävissä olevat laitteet riippuvat siitä mitä laitteita on LPR-palvelimella.

Alue - minkä maanosan (Eurasia tai Americas) mallia käytetään tunnistuksissa.

Minimi maatunnistuksen luotettavuus - minimiarvo maatunnistuksen luotettavuudelle, väliltä 25% - 95%.

Aktivoi maatunnistus - maatunnistus käytössä / ei käytössä. Maatunnistuksen aktivointi voi parantaa rekisterinumeroiden tunnistuksen tarkkuutta.

Sisällytä rekisterilaattakuvat - otetaanko tunnistustapahtumiin mukaan kuvat rekisterikilvistä.

Ota kuvien laitepurku käyttöön - käytä näytönohjainta kuvien dekoodaamiseen (CUDA, DXVA or DirectX).

Tallenna asetukset

Klikkaa Kamera-asetukset ikkunan alaosassa olevaa OK-nappulaa.

Klikkaa Peruuta-nappulaa jos haluta sulkea ikkunan tallettamatta muutoksia.

Muut asetuksien päivitykset

LPR-palvelimien asetuksia päivitetään myös kun järjestelmän asetukset muuttuvat:

VMS-palvelimen poisto: jos VMS-palvelin poistetaan, kaikki siihen liittyvät kamerat otetaan pois käytöstä LPR-palvelimilta.

Kamera poisto: jos kamera poistetaan, niin se otetaan pois käytöstä LPR-palvelimilta. Sama kamera-striimi ei voi olla käytössä useammalla LPR-palvelimella, mutta LPR-palvelimella voi olla monta kamera-striimiä.

Kuvan resoluution ja kompression muutokset: uudet asetukset otetaan käyttöön LPR-palvelimella kun asetukset talletaan.

RTSP asetukset: jos salasana, käyttäjätunnus, RTSP portin numero, yms. parametrit muuttuvat, uudet asetukset otetaan käyttöön LPR-palvelimella kun asetukset talletaan..

Kuvan resoluution muutos laitteistoasetuksissa: jos resoluutiota muutetaan, uudet asetukset otetaan käyttöön LPR-palvelimella kun asetukset talletaan.

Kameran vaihto laitteistoasetuksissa: jos kamera muuttuu toiseksi laitteeksi (vaihdetaan IP-osoite tms.), uudet asetukset otetaan käyttöön LPR-palvelimella kun asetukset talletaan.

Pagination
Previous page
Kohteiden peittäminen
Next page
Face Recognition (FR) Asetukset