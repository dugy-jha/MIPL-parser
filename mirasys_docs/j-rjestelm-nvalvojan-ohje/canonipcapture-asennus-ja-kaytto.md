# CanonIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/canonipcapture-asennus-ja-kaytto

CanonIPCapture - Asennus ja käyttö

Kaikissa pakkaustiloissa ohjain käyttää RTSP/RTP/UDP/IP-protokollia videovirran ja syöttötilojen vastaanottamiseen.

HTTP-protokollaa käytetään parametrien asettamiseen/hakuun.

Jos VMS:n ja kameroiden välillä on palomuuri, seuraavat RTSP/UDP/HTTP-portit on avattava:

HTTP: oletusportit ovat 80,

RTSP: portti 554,

UDP: Tarvitaan kaksi peräkkäistä porttia videovirtaa kohti ja kaksi peräkkäistä porttia metatietovirtaa kohti (syöttötilat) porttialueella 3556-4556.

Esimerkiksi: jos DVMS:ssä on kaksi IP-kameraa, käytetään portteja 3556, 3557, 3558, 3559, 3560, 3561, 3562 ja 3563. Jos jokin portti ei ole vapaa, se jätetään käyttämättä.

CanonIPCapture.xml-tiedostoa käytetään ohjaimen käyttäytymisen määrittämiseen:

Unicast

Multicast:Primary

Multicast:Listener

PTZ-nopeuden rajoituksen parametrit:

PanSpeed (1 - 100%, rajoitusnopeus vaadittua prosenttiarvoa varten)

TiltSpeed (1 - 100%, rajoitusnopeus vaadittua prosenttiarvoa varten)

ZoomSpeed (1 - 100%, rajoitusnopeus vaadittua prosenttiarvoa varten)

PTZQueueSize (PTZ-jonon koko, voidaan optimoida hitaille kameroille.)

Rajoitukset

Vanhat Canon-kamerat, joissa on laiteohjelmisto 1.0.3 tai aikaisempi, voivat käynnistyä uudelleen jokaisen resoluutiomuutoksen yhteydessä. Tämä voi kestää 1-5 minuuttia.

VB-S-kameroissa on 2 H.264-virtaa, joita voidaan käyttää tallentamiseen ja suorana lähetyksenä VMS:ssä. Muissa sarjoissa on vain 1 H.264-kanava.

VB-S-kameroiden enimmäisruutunopeus on rajoitettu 15 ruutuun valituilla resoluutioilla. Jos jokin näistä yhdistelmistä on asetettu, fps muuttuu, vaikka DVMS-asetukset olisivat erilaiset:

1920x1080 - Kaikki koot

Kaikki koot - 1920x1080

1280x960 - 1280x960

1280x720 - 1280x720

VB-M-, VB-H- ja VB-S-sarjan kamerat Liikkuvan kohteen tunnistus eroaa tavanomaisesta liikkeentunnistuksesta. Tunnistuksessa luodaan staattinen ”taustakuva” ja verrataan havaintoalueella tapahtuvia muutoksia tähän kuvaan.
Kamera lähettää ”Tapahtuma ON”-tilailmoituksen, kun kohde tulee havaintoalueelle, ja lähettää ”Tapahtuma OFF”-tilailmoituksen, kun kohde poistuu havaintoalueelta ja kohtaus vaihtuu takaisin alkuperäiseen ”Taustakuvaan”."”
Jos tila ”Tapahtuma päällä” jatkuu yli 5 minuutin ajan, kamera pitää tätä uutena taustatilana, lähettää tilan ”Tapahtuma pois päältä” ja palaa hälytystunnistuksen valmiustilaan.

Unicast mode: Ajuri muuttaa kameran asetukset DVMS-asetusten mukaisesti ja vastaanottaa ääni- ja videotiedot kamerasta Unicast-yhteyden avulla.

Multicast:Primary: Ajuri muuttaa kameran asetuksia DVMS-asetusten mukaisesti ja vastaanottaa ääni- ja videotiedot kamerasta multicast-yhteyden avulla.

Multicast:Listener: Ajuri ei muuta kameran asetuksia, vaan vastaanottaa vain ääni- ja videotiedot kamerasta multicast-yhteyden avulla.

Jos kameraa käytetään useissa DVMS-instansseissa, yhdelle DVMS:lle on määritettävä Multicast:Primary ja muille Multicast:Listener.

Useita Multicast:Primary -konfiguraatioita tai Multicast:Primary ja Unicast -konfiguraatioita ei sallita; muissa tapauksissa kameran pitäisi olla ylikuormitettu jatkuvilla samanaikaisilla asetusmuutoksilla.

CCFIA ja CCRIA on poistettu käytöstä VB-M-sarjassa, koska tämän sarjan kamerat vaativat uudelleenkäynnistyksen asetusten muuttamisen jälkeen.

Pagination
Previous page
ArchiveCapture - Asennus ja käyttö
Next page
DahuaIPCapture - Asennus ja käyttö