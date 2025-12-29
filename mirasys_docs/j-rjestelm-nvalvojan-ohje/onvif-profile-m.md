# ONVIF Profile M | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/onvif-profile-m

ONVIF Profile M

Ohjelmistomme tukee nyt ONVIF-profiilia M, joten se voi reagoida kamera analytiikan tuottaman hälytyksen laukaisuun. Tämän merkittävän päivityksen ansiosta VMS-järjestelmämme voi reagoida tehokkaasti kameroiden hälytyslaukaisuihin, mikä lisää mahdollisuuksia parantaa kohteiden turvallisuutta tai hyödyntää videoanalytiikkaa muihin tarpeisiin.

Saumattoman integroinnin ja vaatimustenmukaisuuden varmistamiseksi olemme testanneet tämän uuden ominaisuuden Axis, Bosch ja Hanwha kameramerkkien kanssa. 

ONVIF hälytyslaukaisin

Kun olet lisännyt laitteen, joka tukee ONVIF Profiilia M, sinun ei tarvitse tehdä mitään erityisiä toimenpiteitä ottaaksesi nämä laukaisimet käyttöön tai poistaaksesi ne käytöstä. Ne lisätään automaattisesti kameran metatietojen laukaisimiin. System Managerin hälytyskonfiguroinnissa tämä näkyy laukaisin välilehdellä ja listattuna ONVIF nimellä. Näitä käyttäen voit luoda uusia hälytyksiä.

ONVIF hälytyslaukaisimen tekeminen

Laitteen hälytykset/laukaisimet on määritettävä laitteen web-käyttöliittymän avulla, koska System Managerissa ei ole käyttöliittymää niiden määrittämiseen. Tämä konfigurointi on tehtävä ennen laitteen lisäämistä VMS:ään tai laitteen ominaisuudet on päivitettävä System Managerissa, jotta laitteen muutokset tulevat näkyviin.

Käynnistä System Manager.

Lisää laite jossa on ONVIF Profili M tuki.

Siirry Videohallintapalvelimet välilehteen.

Valitse Hälytykset.

Valitse uusi hälytys.

Avautuu Yleinen välilehti, josta voit antaa hälytykselle nimi ja valita mitkä profiilit käyttää hälytystä.

Siirry Laukaisin välilehti.

Valitse tyypiksi Metadata.

Valitse ONVIF metadatan tyyppi jota haluat käyttää hälytyksen laukaisuun.

Siirry Toiminnot välilehteen ja valitse haluamasi toiminto hälytykselle.

Siirry Kalenteri välilehteen ja valitse mitkä päivät/tunnit ovat käytössä hälytykselle. Oletuksena hälytys on 24h käytössä joka päivälle.

Valitse lopuksi OK alalaidasta.

Pagination
Previous page
Toimintotyypit ja asetukset
Next page
Hälytykset Kalenteri