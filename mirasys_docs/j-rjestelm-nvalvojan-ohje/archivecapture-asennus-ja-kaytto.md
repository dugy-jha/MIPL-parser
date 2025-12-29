# ArchiveCapture - Asennus ja käyttö | Mirasys Help Center

Source: https://documentation.mirasys.com/j-rjestelm-nvalvojan-ohje/V9.9/archivecapture-asennus-ja-kaytto

ArchiveCapture - Asennus ja käyttö

Arkiston polku asetetaan osoitekenttään (automaattinen hakuikkuna).

Ohjaimen määritys tehdään seuraavasti ArchiveCapture.xml:

Silmukkatoiminnallisuus

Alkuperäisten (kaapattujen) kehysten aika

Kuvataajuus (konfiguroitavissa tai oletusarvo)

Tallennetun arkiston kaappauksen aikarajat

Videokanavien ottaminen käyttöön/pois käytöstä

”Kanavat”- ja ‘raja’-osiot voidaan poistaa kokonaan käytöstä (attribuutti enabled=”0").

Ilman ArchiveCapture.xml-tiedostoa käytetään oletusarvoja.

XML-tiedoston asetuksia sovelletaan vain arkistohakuprosessin aikana.

PAUSE, CONTINUE ja NEXT_FRAME on toteutettu yli CIPVideoCapture::SetExtendedProperty(const char* const aProperty, void* aValue, unsigned long aChannelId) jossa:
aPropertykomento, voi olla ”PAUSE”, ”CONTINUE” ja ”NEXT_FRAME”.
aValue- tulevia tarpeita varten, olisi oltava NULL
aChannelId- kanavatunnus




Pagination
Previous page
Ajurin asennus ja käyttö
Next page
CanonIPCapture - Asennus ja käyttö