# Ohjelmistovahtiloki | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/ohjelmistovahtiloki

Ohjelmistovahtiloki

Järjestelmä näyttää oletusarvoisesti kaikkien palvelimien ohjelmistovahdin lokit.
Voit kuitenkin valita yhden tai useita palvelimia vasemmalla olevasta luettelosta.
Voit lajitella lokit napsauttamalla sarakeotsikoita.
Jos haluat päivittää luettelon sulkematta ikkunaa, napsauta Päivitä-painiketta.

Ohjelmistovahdin lisätoiminnallisuudet

Watchdog-toiminto sisältää kolme uutta protokollaa: TCP, SMS (vaatii ulkoisen SMS-moduulin) ja muokattava sähköpostilomake.

Jokaisella uudella protokollalla on oma ajuri:

C:\Program Files\DVMS\DVR\WDEventProviders\

WDEventProviderSMS.xml

WDEventProviderSMTP.xml

WDEventProviderTCP.xml

Tällä hetkellä näitä tiedostoja on muokattava manuaalisesti. Jokainen XML-tiedosto sisältää määritysvaihtoehtojen dokumentaation.
Uudet määritysvaihtoehdot sisältävät suodatettuja ja ehdollisia varoituksia (eli "lähetä varoitus X vain kerran 60 minuutissa" tai "lähetä varoitus X vain, jos ehto Y ei täyty kahdessa minuutissa") , ja muokattava varoitusviestimuoto.
Kun tiedostot on muokattu, Watchdog on käynnistettävä uudelleen, jotta muutokset tulevat voimaan.

Huom: Tätä ominaisuutta suositellaan vain kokeneille käyttäjille. XML-tiedostot ovat erittäin alttiita kirjoitusvirheille ja väärin kirjoitetuille merkkijonoille ja avaimille.
Pienikin virhe voi aiheuttaa kohtalokkaita virheitä. Mirasys ei ota vastuuta XML-virheistä, jotka aiheutuvat tiedostojen muokkaamisesta.

Pagination
Previous page
Ohjelmistovahtiasetukset
Next page
Ohjelmistovahti eventit