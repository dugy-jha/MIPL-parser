# Alarm Triggering Web API | Mirasys Help Center

Source: https://documentation.mirasys.com/integrations/integrations/alarm-triggering-api

Alarm Triggering Web API

Available from VMS V9.9.0

Overview

This document provides a summary of the Alarm Triggering Web API, which is designed to manage external alarm triggers in the VMS system. The HTTP API is hosted in port 8083 by the VMS server. The API allows users to add, update, delete, and retrieve external alarm triggers, as well as manage their states. It provides a way to programmatically interact with the VMS system to enhance automation and integration with other systems. The configured external alarm triggers can be used in Mirasys VMS to configure alarms that are triggered by the external alarm triggers and can perform various functions as an alarm action, like starting a camera recording, sending an email, moving the PTZ camera to a preset, etc.

The Alarm Triggering API can be used to define two types of alarm triggers: generic and channel-based alarm triggers. The generic alarm triggers can be defined for device-level alerts like a device malfunction. The channel-base trigger can be defined for many channels at once by giving the channel range. The channel-based alarm triggers can be used for alerts that occur on each device channel.

Getting Started

To start using the Alarm Triggering Web API, you need the following:

Install Mirasys VMS V9.9 or a newer version, or upgrade the existing system to the latest Mirasys VMS version.

Add necessary devices to the VMS server, like cameras and I/O devices in the System Manager VMS settings. Please see the Mirasys VMS settings documentation on how to add devices to the VMS system.

Ensure you have access to a VMS system where the API is enabled. The Alarm Triggering API has to be enabled for a VMS server in the System Manager alarm trigger settings before the API can be accessed. Please see the instructions on how to manage the VMS server alarm trigger settings.

You need a valid VMS user account with permission to use the API and use the user credentials on each API request. VMS users can be managed in the System Manager users tab. Please see the Mirasys VMS settings documentation on how to manage users in the VMS system.

A valid license key must be included in all API requests. The API license key is provided by Mirasys when the integration work is started. Please see the generic Mirasys Integration process documentation.

Ensure network settings and firewall allow communication with the VMS server via the specified API endpoints in port 8083.

More information for each step can be found from https://documentation.mirasys.com/

Authentication and license

Authentication is crucial to securing the API’s data for developers and end users. The Alarm Triggering API uses the Digest authentication. All API methods require "Digest" HTTP authorization with a valid VMS username and password. In case of user authentication failure, an Unauthorized HTTP response is returned.

In addition to the user authentication, each API request must include a valid license key in the "License" HTTP header to ensure API access. In case of license check failure, a BadRequest HTTP response is returned.

Each API request should contain the following information:

Digest HTTP authorization header

Digest authentication is enabled by providing the user credentials to .Net HttpClient as follows

C#
[C# .Net 8]
var client = new HttpClient(new HttpClientHandler { Credentials = new NetworkCredential(username, password) }, true);


License HTTP header as the following Name, Value pair

Name: License

Value: The license key

C#
[C# .Net 8]
client.DefaultRequestHeaders.Add("License", licenseKey);


VMS service validates each request by checking in order the following

The user credentials are correct

The license key is included in the VMS server license

Endpoint Definition

API endpoints define where the API interacts with the VMS system. Below are the main endpoints for the Alarm Triggering API:

1. Get Triggers

Description: Retrieves a list of all configured external alarm triggers.

Method: GET

URI: /recorder/externalalarmtriggers

Parameters: -

Content: -

HTTP response:

200 Ok: Configured alarm triggers are returned in the response content.

400 Bad request: An error occurred while processing the request. The response message contains more information about the error.

401 Unauthorized: User authentication has failed.

403 Forbidden: Given license is missing or invalid.

500 Internal Server Error: An unexpected error has occurred on the server side. The response message contains more information about the error.

Response content: List of all configured alarm triggers in JSON format

Each trigger contains the following fields

id: Trigger ID

name: Name of the trigger

triggerType: 0 = generic trigger, 1 = channel trigger

channelStart: Channel trigger range start number. Not used for Generic type triggers and can be set to -1. For Channel triggers, the range is 0-32766.

channelEnd: Channel trigger range end number. Not used for Generic type triggers and can be set to -1. For Channel triggers, the range is 0-32766.

An example of an alarm trigger list with two triggers where one is a generic trigger and the second is a channel trigger

[JSON]
[{"id":"3eb4afae-3aba-4aae-931e-544c4eff242a","name":"Trigger 1","triggerType":0,"channelStart":-1,"channelEnd":-1},{"id":"bfa03a1f-9d4e-4e99-a931-9061e3f65134","name":"Trigger 2","triggerType":1,"channelStart":1,"channelEnd":10}]

2. Add Triggers

Description: This adds new external alarm triggers to the system.

Method: POST

URI: /recorder/externalalarmtriggers

Parameters: -

Content: List of new alarm triggers to be added in JSON format

Each trigger contains the following fields

id: Trigger ID

name: Name of the trigger

triggerType: 0 = generic trigger, 1 = channel trigger

channelStart: Channel trigger range start number. Not used for Generic type triggers and can be set to -1. For Channel triggers, the range is 0-32766.

channelEnd: Channel trigger range end number. Not used for Generic type triggers and can be set to -1. For Channel triggers, the range is 0-32766.

Example of a channel alarm trigger

[JSON]
[{"id":"bfa03a1f-9d4e-4e99-a931-9061e3f65134","name":"Trigger 2","triggerType":1,"channelStart":1,"channelEnd":10}]


HTTP response:

200 Ok: Alarm triggers adding request was processed successfully. Response content contains response information for each given alarm trigger.

400 Bad request: An error occurred while processing the request. The response message contains more information about the error.

401 Unauthorized: User authentication has failed.

403 Forbidden: Given license is missing or invalid.

500 Internal Server Error: An unexpected error has occurred on the server side. The response message contains more information about the error.

Response content: Operation information for each alarm trigger in JSON format.

operation: The performed operation

1 = Add

2 = Update

3 = Delete

hasErrors:

True = Operation was successful for all given alarm triggers

False = Operation failed on one or more alarm triggers

results:

List of key-value pairs for each alarm trigger containing

id = Alarm trigger id

result = Operation result where ‘OK’ is for success, error text for failure

Example

[JSON]
{"operation":1,"hasErrors":false,"results":[{"id":"25f5cdaa-2456-4333-add9-d922d45ad1ab","result":"OK"}]}

3. Update Triggers

Description: Updates existing external alarm triggers.

Method: PUT

URI: /recorder/externalalarmtriggers

Parameters: N/A

Parameters: -

Content: List of alarm triggers to be updated in JSON format

Each trigger contains the following fields

id: Trigger ID

name: Name of the trigger

triggerType: 0 = generic trigger, 1 = channel trigger

channelStart: Channel trigger range start number. Not used for Generic type triggers and can be set to -1. For Channel triggers, the range is 0-32766.

channelEnd: Channel trigger range end number. Not used for Generic type triggers and can be set to -1. For Channel triggers, the range is 0-32766.

Example of a channel alarm trigger

[JSON]
[{"id":"bfa03a1f-9d4e-4e99-a931-9061e3f65134","name":"Trigger 2","triggerType":1,"channelStart":1,"channelEnd":10}]


HTTP response:

200 Ok: The Alarm triggers updating request was processed successfully. Response content contains response information for each given alarm trigger.

400 Bad request: An error occurred while processing the request. The response message contains more information about the error.

401 Unauthorized: User authentication has failed.

403 Forbidden: Given license is missing or invalid.

500 Internal Server Error: An unexpected error has occurred on the server side. The response message contains more information about the error.

Response content: Operation information for each alarm trigger in JSON format.

operation: The performed operation

1 = Add

2 = Update

3 = Delete

hasErrors:

True = Operation was successful for all given alarm triggers

False = Operation failed on one or more alarm triggers

results:

List of key-value pairs for each alarm trigger containing

id = Alarm trigger id

result = Operation result where ‘OK’ is for success, error text for failure

Example

[JSON]
{"operation":2,"hasErrors":false,"results":[{"id":"25f5cdaa-2456-4333-add9-d922d45ad1ab","result":"OK"}]}

4. Remove Triggers

Description: Removes specified external alarm triggers from the system.

Method: DELETE

URI: /recorder/externalalarmtriggers

Parameters: N/A

Content: List of alarm trigger IDs to be deleted in JSON format

Example of an alarm trigger ID list

[JSON]
["bfa03a1f-9d4e-4e99-a931-9061e3f65134"]


HTTP response:

200 Ok: Alarm triggers removing request was processed successfully. Response content contains response information for each given alarm trigger.

400 Bad request: An error occurred while processing the request. The response message contains more information about the error.

401 Unauthorized: User authentication has failed.

403 Forbidden: Given license is missing or invalid.

500 Internal Server Error: An unexpected error has occurred on the server side. The response message contains more information about the error.

Response content: Operation information for each alarm trigger in JSON format.

operation: The performed operation

1 = Add

2 = Update

3 = Delete

hasErrors:

True = Operation was successful for all given alarm triggers

False = Operation failed on one or more alarm triggers

results:

List of key-value pairs for each alarm trigger containing

id = Alarm trigger id

result = Operation result where ‘OK’ is for success, error text for failure

Example

[JSON]
{"operation":3,"hasErrors":false,"results":[{"id":"25f5cdaa-2456-4333-add9-d922d45ad1ab","result":"OK"}]}

5. Send Trigger State

Description: Sends the state of a specified trigger to the VMS system.

Method: GET

URI: /recorder/externalalarmtriggers/<Trigger GUID>?channel=<Channel Number>&activation=<Activation Type>

Parameters:

Trigger GUID: The ID of an existing alarm trigger

channel: The number of the alarm trigger channel number. For Channel triggers, the range is 0-32766.

activation: Trigger activation type

0 = Active: The alarm trigger is activated, and the alarm that is configured using the trigger will continue until the trigger is inactivated

1 = Inactive: The alarm trigger is inactivated, and the alarm that is configured using the trigger will end

2 = One shot: The alarm trigger is put to active and then deactivated immediately

Content: N/A

HTTP response:

200 Ok: The alarm trigger state was changed successfully.

400 Bad request: An error occurred while processing the request. The response content contains more information about the error.

404 Not found: Either the trigger with the given ID was not found, or there is no alarm configured for the trigger. The response content contains more information about the error.

401 Unauthorized: User authentication has failed.

403 Forbidden: Given license is missing or invalid.

500 Internal Server Error: An unexpected error has occurred on the server side. The response message contains more information about the error.

Response content: Failed operation information in text format.

Status and Error Codes

The API uses standard HTTP status codes to indicate the success or failure of an API request. Here are some common status codes and their meanings:

200 OK: The request was successfully processed by the server. The response message for adding, updating, and deleting the alarm triggers will contain detailed information about the operation result for each given alarm trigger object.

Note: Even though the call returns the ok response, check the response content when adding, updating, or removing alarm triggers for any errors that have occurred for any of the given alarm triggers.

400 Bad Request: An error occurred while processing the request. The response message contains more information about the error.

Resolution: Check the response message for more information

401 Unauthorized: Authentication failed due to missing or invalid credentials.

Resolution: Check possible resolutions for this issue under the title “Authorization and license“

403 Forbidden: The request was valid, but the server is refusing action due to permissions. The most likely reason is a missing or invalid license.

Resolution: Check possible resolutions for this issue under the title “Authorization and license“

404 Not found: The given object is not found. This error can occur when giving an invalid alarm trigger ID or when the alarm configuration for the given trigger is not found.

Resolution: Check the alarm trigger ID and the alarm configuration

500 Internal Server Error: An unexpected error occurred on the server.

Resolution: Check the response message for more information

Examples

Providing examples helps users understand how to utilize the API effectively. Below are examples of API calls and their expected responses:

Example 1: Get Triggers
Request
GET /recorder/externalalarmtriggers HTTP/1.1
Host: [VMS Server Address]
Authorization: Digest username="admin", realm="VMS", nonce="...", uri="/recorder/externalalarmtriggers", response="..."
License: [Your License Key]

Response
HTTP/1.1 200 OK

[
  {
    "id": "da3f305f-49ec-4457-8813-b6439b62b264",
    "name": "Trigger 1",
    "triggerType": "0",
    "channelStart": "-1",
    "channelEnd": "-1"
  }
  // More triggers...
]

Example 2: Add Triggers
Request
POST /recorder/externalalarmtriggers HTTP/1.1
Host: [VMS Server Address]
Authorization: Digest username="admin", realm="VMS", nonce="...", uri="/recorder/externalalarmtriggers", response="..."
License: [Your License Key]
Content-Type: application/json

[
  {
    "id": "new-guid-identifier",
    "name": "Trigger Name",
    "triggerType": "1",
    "channelStart": "0",
    "channelEnd": "2"
  }
]

Response
HTTP/1.1 200 OK

{
  "operation": "1",  // 1 - add
  "hasErrors": false,
  "results": [
    {
      "id": "new-guid-identifier",
      "result": "Success"
    }
  ]
}

Example 3: Updating Triggers
Request
PUT /recorder/externalalarmtriggers HTTP/1.1
Authorization: Digest username="admin", realm="VMS", nonce="...", uri="/recorder/externalalarmtriggers", response="..."
License: [Your License Key]
Content-Type: application/json

[
  {
    "id": "existing-guid-identifier",
    "name": "Trigger Name",
    "triggerType": "1",
    "channelStart": "0",
    "channelEnd": "5"
  }
]

Response
HTTP/1.1 200 OK

{
  "operation": "2",  // 2 - update
  "hasErrors": false,
  "results": [
    {
      "id": "existing-guid-identifier",
      "result": "Success"
    }
  ]
}

Example 4: Deleting Triggers
Request
DELETE /recorder/externalalarmtriggers HTTP/1.1
Authorization: Digest username="admin", realm="VMS", nonce="...", uri="/recorder/externalalarmtriggers", response="..."
License: [Your License Key]
Content-Type: application/json

[
  "existing-guid-identifier-1",
  ...,
  "existing-guid-identifier-N"
]

Response
HTTP/1.1 200 OK

{
  "operation": "3",  // 3 - delete
  "hasErrors": false,
  "results": [
    {
      "id": "existing-guid-identifier-1",
      "result": "Success"
    },
    ...
    {
      "id": "existing-guid-identifier-N",
      "result": "Success"
    }
  ]
}

Example 5: Changing Trigger State
Request
GET /recorder/externalalarmtriggers/existing-guid-identifier?channel=1&activation=0 HTTP/1.1
Authorization: Digest username="admin", realm="VMS", nonce="...", uri="/recorder/externalalarmtriggers", response="..."
License: [Your License Key]

Response
HTTP/1.1 200 OK

Enabling secure communication (HTTPS)

The following steps have to be made to enable secure HTTPS communication on the VMS server API:

Get an SSL certificate signed by a certificate authority (CA). In the development time, self-signed certificates can be used. It is highly recommended to use certificates signed by CA; self-signed certificates should only be used during the development time. When using self-signed certificates, the certificate validation needs to be overridden on the calling party. See an example in the sample application code of how the certificate validation can be overridden.

Install the certificate in the Windows certificate store. This can be done, for example, by using the Microsoft Management Console (MMC).

The installed SSL certificate needs to be bound to the HTTP server port 8083. The port binding can be done by running the Windows Command Prompt with administrator privileges with the following command

netsh http add sslcert ipport=0.0.0.0:8083 certhash=7c92d90c37e4a5645cd22d6d6cc55fa42e0b2be1 appid={e103ea44-536f-4726-a43d-3b7cd8ef8ed4}


In this command, the "ipport" value is the IP address and port number, the "certhash" value is the SSL certificate thumbprint, and the "appid" value is a GUID that represents the application identity.

Configure the VMS Server to use HTTPS. This can be done with the following steps

Shutdown WDServer, DVRServer, and SMServer services

Enable HTTPS in the dvr.xml file by changing the ‘Https’ value to 'True'

  <HttpServer>
    <Port value="8083" />
    <Https value="True" />
    <AlarmTriggerAPI value="True" />
  </HttpServer>


Start the WDServer, DVRServer, and SMServer services

After the steps described above are done, HTTPS can be used with the API calls. See code examples from the sample application on how to call the API with HTTPS.

Troubleshooting

When calling the Alarm Triggering API HTTP endpoints, a failed response can be returned by the API. In this case, please follow the following guidelines to troubleshoot the failure reason:

Check the error details from the HTTP response

The HTTP response can contain useful information on why the HTTP call fails. Please check all the information contained in the response.

Check the VMS server log

Change the VMS server logging to the debug level first. This can be done as follows

Stop the WDServer and DVRServer in this order by using the Windows Services tool.

Navigate to the VMS server installation folder ‘C:\Program Files\DVMS\DVR’

Edit the file ‘DVRServer.exe.config’

Change the logging level from INFO to DEBUG for the RollingFileAppender as following

    <root>
      <level value="DEBUG" />
      <!--<appender-ref ref="ConsoleAppender" />-->
      <appender-ref ref="RollingFileAppender" />
    </root>


Save the file

Start WDServer and DVRServer by using the Windows Services tool

Examine the logs found in the folder 'C:\Program Files\DVMS\DVR\logs' about the user credentials validations and license key checks to see what causes the API call request to fail.

In case of authentication validation fails, API returns an unauthorized error (HTTP 401 Unauthorized). To identify the problem of an unauthorized error, the following checks can be made to find the reason for the error:

Check that the given user credentials are correct

You can check the credentials from the System Manager user settings and try to use the same credentials to log in to one of the Mirasys VMS clients (Spotter, Spotter Web, or System Manager). In case incorrect credentials are being used in the API call, use the correct credentials and try again.

Check that the VMS server has a connection to the main server

Log in to the System Manager and check from the VMS servers tab that the connection to the VMS server, which API you are using, is connected. In case the connection is disconnected, restore the connection.

Check that the license key provided in the call is included in the VMS server license

You can check the VMS server license from the System Manager system tab ‘Master license’ if it is the main server or from the named VMS server dialog under the Licenses that the license contains the license key for the API.

Additional Information
Accessing the API

Please contact the support team and we will help you get started.

Terms of Use

To use the Alarm Triggering Web API, users must comply with specific terms of use. These terms ensure that the API is used safely and responsibly. We will send you the terms of use when you contact us to access the Alarm Triggering Web API.

Next Steps

Review the API documentation and ensure you have the necessary credentials and permissions.

Configure your development environment according to the Getting Started section.

Test the API using the provided Examples to familiarize yourself with its functionality.

Check the Status and Error Codes section for troubleshooting tips.

Please contact our technical support should you require further help.

Pagination
Previous page
For Developers
Next page
SMServer HTTP API