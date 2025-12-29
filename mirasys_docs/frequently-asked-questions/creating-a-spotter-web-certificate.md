# Spotter Web Certificate using Let´s Encrypt - v1.0 | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/creating-a-spotter-web-certificate

Spotter Web Certificate using Let´s Encrypt - v1.0

Let’s Encrypt is a free, automated, and open certificate authority (CA), run for the public’s benefit.
It is a service provided by the Internet Security Research Group (ISRG).

Requirement for Let's Encrypt certificate

Windows Server 2016 or newer

Domain/subdomain

Certificates are bound to the domain

Example sub.domain.com

Win-acme tool

Win-acme

Creating a Spotter Web certificate

Browse to Win-acme

Click Download

Download latest package

Copy and extract the package to that PC, where Spotter Web is installed

Click wacs.exe

Type N and press ENTER

Check that the tool is detecting the site and select the correct number and press ENTER

If the tool can’t find binging, please check that you have added the website address in the binding. See section Applying the certificate to the Spotter Web.

Check that the tool is showing the correct address and select the shown number and press ENTER

Answer Y to the question Continue with this selection and press ENTER

Answer Y to the question Open in the default application and press ENTER

Agree the the term by typing Y and press ENTER

After this, you can add an email where you get updates related to problems and abuse.

When this is done, the tool makes a certificate for this domain address. Now you can close the tool by typing Q and press ENTER.

Applying the certificate to the Spotter Web

To use the Let’s Encrypt certificate for Spotter Web, you need to change the hostname for the sub.domain.com address.

Open Internet Information Services Manager

Open SpotterWeb Site

Select Bindings

Click Edit

Type the correct Host name

Click Select to browser certificate created by Let´s encrypt

Click OK

When you reopen the site, you can see that it is encrypted, and you are ready to use the site securely.

Pagination
Previous page
Spotter Web Tips and Tricks
Next page
If Spotter Web installations fails