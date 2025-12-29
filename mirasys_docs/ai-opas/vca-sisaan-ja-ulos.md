# VCA - Sisään ja ulos | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-opas/V9.9/vca-sisaan-ja-ulos

VCA - Sisään ja ulos

Enter (Sisään)-sääntö havaitsee, kun kohteet tulevat alueelle.
Toisin sanoen, kun kohteet siirtyvät alueen ulkopuolelta vyöhykkeen sisäpuolelle.
Sitä vastoin Exit (poistumissääntö) havaitsee, kun objekti poistuu vyöhykkeestä: kun se ylittää alueen rajan sisäpuolelta ulkopuolelle.

Huomautus: Enter ja Exit säännöt eroavat ilmestymis- ja katoamissäännöistä seuraavasti:

Enter-sääntö havaitsee jo seuratut kohteet, jotka ylittävät alueen rajan ulkopuolelta sisäpuolelle, kun taas appear-sääntö havaitsee kohteet, joita aletaan seurata alueen sisällä (esim. kun ne ilmestyvät kohtaukseen oven läpi).

Exit-sääntö havaitsee jo seuratut kohteet, jotka ylittävät alueen rajan sisäpuolelta ulkopuolelle, ja katoamissääntö havaitsee kohteet, joita ei enää seurata alueen sisällä (esim. poistuvat kohtauksesta oven kautta).




Konfiguraatio Enter

Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittelemä nimi tälle säännölle

	

"Enter #"




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active




Zone (Alue)

	

Alue, johon tämä sääntö liittyy

	

None

Konfiguraatio Exit

Property

	

Description

	

Default Value




Name (Nimi)

	

Käyttäjän määrittelemä nimi tälle säännölle

	

"Exit #"




Can Trigger Actions (Voi laukaista toimintoja)

	

Määrittää, voiko tämän säännön tuottamat tapahtumat käynnistyä.

	

Active




Zone (Alue)

	

Alue, johon tämä sääntö liittyy

	

None




Pagination
Previous page
VCA - Ilmestyvät ja katoavat
Next page
VCA - Suunta