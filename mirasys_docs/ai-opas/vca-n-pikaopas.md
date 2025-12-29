# VCA:n Pikaopas | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-n-pikaopas

VCA:n Pikaopas

Tämä käyttöopas käsittelee jokaista aihetta yksityiskohtaisesti. Jotta pääset nopeasti alkuun, oleellisimmat aiheet on lueteltu alla.

Seuraavat vaiheet on suoritettava jokaiselle palvelimelle:

Päätä, mitkä VCA-toiminnot vastaavat tarpeitasi. Ohjeita saatavilla otamalla yhteys Mirasys-edustajaan tai tutustumalla Mirasysin VCA-koulutukseen.

Hanki ja asenna Mirasys VMS -järjestelmä ja siihen liittyvä ohjelmistolisenssiavain, jossa muut tarvittavat ominaisuudet on otettu käyttöön.

Lisää ja määritä videokameroiden asetukset, joita aiot käyttää VCA:ta varten, ja ota VCA-toiminto käyttöön kameran asetuksissa.

Ota hermeneuttinen liikkeentunnistustila käyttöön jokaisessa VCA:ssa käytettävässä kamerassa.

Vie VCA-core HW GUID ja hanki Mirasysilta VCA-aktivointilisenssikoodi ja aktivoi Mirasys VCA näillä lisensseillä.

Kalibroi kukin kamera VCA-asetuksissa, jos objektiluokitusta tarvitaan.

Määritä havaitsemisalue ja säännöt kullekin kameralle.

Määritä tarvittaessa hälytykset VCA-tapahtumien perusteella.

Tarkista VCA:n toiminnallisuuden visualisointi Spotter for Windows -sovelluksen avulla.

VCA-lisenssin HWGUID-tunnuksen saamiseksi yksi kamera on otettava käyttöön System Managerin kamera-asetuksissa, jotta VCA-moottori käynnistyy. Kun VCA on käynnissä, VCA HWGUID-tunnus voidaan hakea System Managerin VMS-palvelimen lisenssi-dialogista.

VCA-moottori käynnistyy VMS-palvelimessa, kun vähintään yksi kamera on määritetty käyttämään VCA:ta System Managerin kamera-asetuksissa. Ensimmäisellä VCA-moottorin käynnistyksellä käännetään NVIDIA-kirjastot, jos Deep Learning on käytössä. Tämä voi viedä paljon aikaa, ja se riippuu käytetystä laitteistosta. Käännöksen aikana VCA ei toimi.

On erittäin suositeltavaa odottaa, kunnes NVIDIA-kirjastot on käännetty VCA:n käyttöönoton jälkeen, ennen kuin suoritat muita toimintoja VMS-palvelimella.

Pagination
Previous page
Tietoa Mirasys VCA:sta
Next page
Mirasys VCA:n edellytykset