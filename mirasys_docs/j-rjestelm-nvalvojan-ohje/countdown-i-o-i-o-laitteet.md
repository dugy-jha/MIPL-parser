# Countdown I/O (I/O-laitteet) | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/countdown-i-o-i-o-laitteet

Countdown I/O (I/O-laitteet)

Countdown I/O:lla on mahdollista luoda toimintoja sen perusteella, tapahtuvatko jotkin tapahtumat tietyn ajan kuluessa vai eivät.

Kun järjestelmähallinnassa luodaan uusi Countdown I/O, se luo automaattisesti 4 tuloa ja 4 lähtöä.

Countdown I/O:ssa on kaksi perustilaa. Kaksi ensimmäistä tulo/lähtöparia ovat tyyppiä 1 ja kaksi viimeistä paria tyyppiä 2.

Lisenssi ohjaa loogista IO:ta ja lähtölaskentaa. Jos lisenssiä ei ole, uuden IO:n luominen epäonnistuu.

Tapahtuman kesto ylitetty -tila (tyyppi 1)

Ensinnäkin on mahdollista laukaista hälytys, jos jokin tapahtuma kestää suunniteltua kauemmin.

Oletetaan esimerkiksi, että aika on 10 sekuntia. Jos lähtö yksi laukeaa ja pysyy aktiivisena alle määritetyn ajan, hälytystä ei tule.

Jos lähtö laukeaa ja pysyy aktiivisena määritellyn ajan pidempään, tapahtuu hälytys.

Kun luot uutta Countdown I/O:ta, kaksi ensimmäistä tulo-lähtö-paria ovat tämän tyyppisiä.

Odotettu laukaisutila (tyyppi 2)

Toiseksi, on mahdollista laukaista hälytys, jos odotettua pulssia ei vastaanoteta määritetyn ajan sisällä.

Esimerkiksi aika on 10 sekuntia, ja odotamme normaalin toiminnan saavan pulsseja lähdöstä 3 2-3 sekunnin välein.

Kun pulssi puuttuu yli 10 sekuntia, tulotila muutetaan aktiiviseksi. Se pysyy aktiivisena, kunnes vastaanotetaan seuraava lähtölaukaisu.

Uutta Countdown I/O:ta luotaessa viimeinen tulo-lähtöpari on tätä tyyppiä.

Pagination
Previous page
Logical I/O (I/O-laitteet)
Next page
Scheduled IO (I/O-laitteet)