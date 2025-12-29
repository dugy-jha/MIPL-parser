# IIS Manual installation via Command Prompt | Mirasys Help Center

Source: https://documentation.mirasys.com/frequently-asked-questions/faq/iis-manual-installation-via-command-prompt

IIS Manual installation via Command Prompt

On default Spotter Web installer install/activate IIS and needed features but some cases there is need to do this manually.

Open Command Prompt using Administrator account/user rights.

Run this command and wait.

C:\Windows\system32\DISM.EXE /online /enable-feature /all /FeatureName:IIS-WebServerRole /FeatureName:IIS-WebServer /FeatureName:IIS-CommonHttpFeatures /FeatureName:IIS-StaticContent /FeatureName:IIS-DefaultDocument /FeatureName:IIS-DirectoryBrowsing /FeatureName:IIS-HttpErrors /FeatureName:IIS-HttpRedirect /FeatureName:IIS-ApplicationDevelopment /FeatureName:IIS-ASPNET45 /FeatureName:IIS-NetFxExtensibility45 /FeatureName:IIS-NetFxExtensibility /FeatureName:IIS-ISAPIExtensions /FeatureName:IIS-ASP /FeatureName:IIS-ISAPIFilter /FeatureName:IIS-HealthAndDiagnostics /FeatureName:IIS-HttpLogging /FeatureName:IIS-LoggingLibraries /FeatureName:IIS-RequestMonitor /FeatureName:IIS-HttpTracing /FeatureName:IIS-CustomLogging /FeatureName:IIS-Security /FeatureName:IIS-WindowsAuthentication /FeatureName:IIS-RequestFiltering /FeatureName:IIS-IPSecurity /FeatureName:IIS-Performance /FeatureName:IIS-HttpCompressionStatic /FeatureName:IIS-WebServerManagementTools /FeatureName:IIS-ManagementConsole /FeatureName:IIS-ManagementScriptingTools /FeatureName:IIS-ManagementService /FeatureName:IIS-WebSockets /FeatureName:IIS-CGI /FeatureName:IIS-ServerSideIncludes /FeatureName:IIS-BasicAuthentication /FeatureName:IIS-DigestAuthentication /FeatureName:IIS-WindowsAuthentication /FeatureName:IIS-ClientCertificateMappingAuthentication /FeatureName:IIS-IISCertificateMappingAuthentication /FeatureName:WAS-WindowsActivationService /FeatureName:WAS-ProcessModel /FeatureName:WAS-ConfigurationAPI /FeatureName:WCF-Pipe-Activation45 /FeatureName:WCF-TCP-Activation45 /FeatureName:WCF-TCP-PortSharing45 /FeatureName:WCF-HTTP-Activation


This command install/activate IIS and needed features that you can install Spotter Web to server.

Installation fails

Check that there is Net. Framework 3.5 installed on server.

If installation still fails you can find more information from DISM.log file

Default location C:\WINDOWS\Logs\DISM\dism.log

Limitations

When using Spotter Web on normal Windows operating system like Windows 10 or 11, Microsoft has limited connection to 10 simultaneously connections. Windows Server side there is not limitations for this.

Pagination
Previous page
If Spotter Web installations fails
Next page
Spotter Web layout saving fails