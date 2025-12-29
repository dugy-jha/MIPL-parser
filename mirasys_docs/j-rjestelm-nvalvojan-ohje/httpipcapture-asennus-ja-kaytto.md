# HTTPIPCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/httpipcapture-asennus-ja-kaytto

HTTPIPCapture - Asennus ja käyttö

Ohjain käyttää HTTP-protokollaa IP-laitteiden videovirtojen vastaanottamiseen.

Ajuri odottaa, että laitteeseen lisätään HTTP-URI ja se sijoitetaan ”IP-osoite”-kenttään.

Tarvittava portti voidaan määrittää erikseen ”Port”-kentässä tai HTTP URI:ssä. HTTP URI -portilla on korkeampi prioriteetti; jos se on asetettu, DVMS-porttikenttä jätetään huomiotta.

Virran URI-vaatimukset: HTTP URI on määritettävä täydessä muodossa, esim. http://192.168.1.70:8080/video.

Stream URI voidaan tarkistaa kolmannen osapuolen soittimilla, kuten VLC:llä.

Rajoitukset

Jos kamera vaatii Basic HTTP -valtuutuksen, oikea käyttäjänimi ja salasana on asetettava, muuten videokuvaa ei tule.




Pagination
Previous page
GatewayIPCapture - Asennus ja käyttö
Next page
IPCameraCapture - Asennus ja käyttö