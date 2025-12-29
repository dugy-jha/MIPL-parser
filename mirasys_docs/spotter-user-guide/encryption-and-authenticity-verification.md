# Encryption and Authenticity Verification | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-user-guide/V-9.9/encryption-and-authenticity-verification

Encryption and Authenticity Verification

The Mirasys Spotter system is designed to provide a secure and user-friendly environment for managing video recordings, including live and archived footage. Central to this system is the Spotter Player, a media player seamlessly integrated within the client application, and the Secure Export Format (SEF), a format designed for the fast and secure export of video files.

Spotter Player is built into the client application and does not require a separate installation. The user can select to have it copied with the export. It allows you to play exported media clips, archives, or storyboards and view them similarly to when using the full application and accessing recordings on a server.

Secure Export Format (SEF)

Spotter Player is always started offline, so it can only be used to open exported SEF and WMV clips and archives. The fastest export file format is SEF (Secure Export Format). It can be viewed with Spotter or Spotter Player.

The SEF format supports exported videos with subtitles, audio, and text data—authenticity-protected format. The use of digital watermarks for authenticity verification is particularly associated with the SEF2 format, which is an extension of the original SEF format with additional security and privacy features. The SEF2 format supports exported videos with subtitles, audio, and text data—authenticity-protected format, and also enables:

Protecting the video material with the password,

Software side privacy zones in the export,

Face blurring (needs to be enabled on the camera side to be included in the export) 

Mask moving objects

Encryption to safeguard exported video data

Mirasys employs robust encryption techniques to safeguard exported video data. AES encryption with a 256-bit key encrypts image data, layout data, bookmarks, and storyboard data. This selective encryption ensures that critical components of the video and its metadata are secured against unauthorized access or tampering. AES is a widely recognized encryption standard that provides a high level of security, making it suitable for protecting sensitive video data in SEF files.

SHA1 (Secure Hash Algorithm 1) is used for hashing. Hashing is converting an input (or 'message') into a fixed-size string of bytes, typically a digest that represents the original string. While SHA1 is not an encryption technique per se, it complements the encryption process by ensuring data integrity and authenticity, allowing the system to detect any alterations to the data.

The SEF data container itself is not encrypted so that the overall file structure remains accessible for system functions, such as verifying file integrity or managing file access. In contrast, the content within the container is encrypted for security.

You have the option to password-protect SEF clips during the export process. When exporting SEF clips in Spotter, you select to password-protect the clip. If password protection is selected, the password will be requested in a separate dialog. When the correct password is entered, the clip is opened.

Decryption occurs dynamically when a password-protected SEF clip is accessed in the Spotter system. For image data, decryption is performed on the fly, meaning it is decrypted in real time as it is accessed without storing decrypted data on the disk. This approach enhances security by ensuring that sensitive decrypted data is not left vulnerable on storage media. Spotter passes the password with other export parameters to Media Exporter, which encrypts the clip. Encrypted SEF clips are saved with the extension ".esef.”

Watermarking for Authenticity Verification

An essential feature of the Mirasys system is using digital watermarks to verify the authenticity of exported video material. The watermark is a digital signature confirming the video content's originality and integrity.

The Spotter system automatically verifies the authenticity of media files when they are played back using Spotter Player or Spotter. This process checks for the presence of the digital watermark to ascertain if the media file is authentic.

Upon verification, the system informs the user of the authenticity status of the media file through notifications. If the media file is authentic, a notification stating “Media file authenticity verified” is shown.




Conversely, if the media file is not authentic, the user is notified with a message stating “Media file is not authentic.”




Pagination
Previous page
Open Media
Next page
Bookmarks