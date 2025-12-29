# Face Recognition (FR) Asetukset | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/face-recognition-fr-asetukset

Face Recognition (FR) Asetukset

RTSP Server Streaming ominaisuus pitää olla mukana lisenssissä.

Face Recognition Asetukset

Kasvontunnistusasetukset löytyvät System Managerista VMS Server -välilehdeltä > Kamerat.

Siirry Kamera-asetukset-ikkunassa FR-asetukset-välilehdelle.

Jos lisenssi ei sisällä Smart FR ominaisuutta, FR asetukset välilehti ei ole käytettävissä. 

Valitse kamera, stream ja ota FR käyttöön

Valitse kamera FR:n avattavasta valikosta.

Jos Stream on useampi kuin yksi, voit valita stream. Jos on vain yksi stream, käytössä on oletusstream kuten yllä olevassa kuvassa, ja pudotusvalikko on poistettu käytöstä.

Voit valita palvelun vasta, kun olet ottanut palvelun käyttöön napsauttamalla Enable FR for selected camera (Ota FR käyttöön valitulle kameralle) -ruutua.

Jos Enable FR for selected camera (Ota FR käyttöön valitulle kameralle) -ruutua ei ole rastitettu, Service (Palvelu) -pudotusvalikko ei ole käytössä.

Lisenssin tekstiruutu näyttää käytettyjen lisenssien määrän ja lisenssien enimmäismäärän.

Kasvontunnistusasetukset

Kun kamera, sen virta ja FR-tunnistuspalvelu on valittu, kasvontunnistusasetuksia voidaan säätää.




Kasvojentunnistuksen asetukset

Kun kamera, kameran striimi ja FR-palvelu on valittu, FR-asetuksia voi muokata. Kasvojentunnistuksen asetukset löytyvät Tunnistusparametrit kohdasta FR-asetukset välilehdeltä Kamera-asetukset ikkunassa.

Kasvojentunnistuksen asetukset ovat FR-palvelua varten.

Tunnistusalue - määrittää sen alueen minkä sisältä kasvoja tunnistetaan.

Maksimi kasvojen määrä – maksimimäärä sille kuinka monta kasvoa kuvasta tunnistetaan. Arvon tulisi olla väliltä 1 - 5.

Minimi luotettavuus – minimiarvo tunnistuksen luotettavuudelle. Jos luotettavuus jää alle tämän raja-arvon, niin tunnistus hylätään. Sallitut arvot ovat väliltä 25% - 95%.

Minimi kasvokuvan korkeus – kasvojen minimikorkeus % kuvan korkeudesta. Sallitut arvot ovat väliltä 5% - 50%. Oletusarvo on 10%.

Minimi kasvojen samankaltaisuus – jos samankaltaisuus on sama tai suurempi kuin tämä raja-arvo, niin se tulkitaan niin että kysessä on sama henkilö. Arvon tulisi olla väliltä 50% - 95%.

Saman kasvon tunnistusväli – kuinka monta sekuntia pitää kulua ennen kuin lähetetään uusi tapahtuma saman kasvon tunnistuksesta.

Laite – mitä laitetta käytetään tunnistuksissa. Käytettävissä olevat laitteet riippuvat siitä mitä laitteita on FR-palvelimella.

Pikkukuvan korkeus – pikkukuvan korkeus pikseleinä. Arvon tulisi olla väliltä 32 -128.

Sisällytä pikkukuva – otetaanko tunnistustapahtumaan mukaan pikkukuva siitä kuvasta mistä tunnistus tehtiin.

Sisällytä kasvokuva – otetaanko tunnistustapahtumaan mukaan kuvat kasvoista.

Ota kuvien laitepurku käyttöön – käytä näytönohjainta kuvien dekoodaamiseen (CUDA, DXVA or DirectX).

Tallenna asetukset

Klikkaa Kamera-asetukset ikkunan alaosassa olevaa OK-nappulaa.

Klikkaa Peruuta-nappulaa jos haluta sulkea ikkunan tallettamatta muutoksia.

Poistettaessa kameran striimiä, jos striimi on käytössä FR-palvelussa, tulee FR-palvelulle valita “None”.

Muut asetuksien päivitykset

FR-palvelimien asetuksia päivitetään myös kun järjestelmän asetukset muuttuvat:

VMS-palvelimen poisto: jos VMS-palvelin poistetaan, kaikki siihen liittyvät kamerat otetaan pois käytöstä FR-palvelimilta.

Kamera poisto: jos kamera poistetaan, niin se otetaan pois käytöstä FR-palvelimilta. Sama kamera-striimi ei voi olla käytössä useammalla FR-palvelimella, mutta FR-palvelimella voi olla monta kamera-striimiä.

Kuvan resoluution ja kompression muutokset: uudet asetukset otetaan käyttöön FR-palvelimella kun asetukset talletaan.

RTSP asetukset: jos salasana, käyttäjätunnus, RTSP portin numero, yms. parametrit muuttuvat, uudet asetukset otetaan käyttöön FR-palvelimella kun asetukset talletaan..

Kuvan resoluution muutos laitteistoasetuksissa: jos resoluutiota muutetaan, uudet asetukset otetaan käyttöön FR-palvelimella kun asetukset talletaan.

Kameran vaihto laitteistoasetuksissa: jos kamera muuttuu toiseksi laitteeksi (vaihdetaan IP-osoite tms.), uudet asetukset otetaan käyttöön FR-palvelimella kun asetukset talletaan.

Pagination
Previous page
License Plate Recognition (LPR) Asetukset
Next page
Object Recognition (OR) Asetukset