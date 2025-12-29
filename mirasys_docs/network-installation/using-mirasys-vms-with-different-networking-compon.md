# Using Mirasys VMS With Different Networking Components | Mirasys Help Center

Source: https://documentation.mirasys.com/network-installation/networkinstallation/using-mirasys-vms-with-different-networking-compon

Using Mirasys VMS With Different Networking Components

When building a Mirasys VMS system, usability, security issues and the need to contact system components outside of surveillance sites are extremely important factors to be considered.
When contacting the system with a System Manager application from outside of a closed network, a VPN (Virtual Private Network) or an effective firewall are good alternatives.

IP Addressing

Devices communicating over an IP network identify each other through their IP addresses.
An IP address is a unique identifier on a given network that signifies a networking device’s interface.
Addresses within a closed network are arbitrary, but larger networks have addresses that are either in constant use or are reserved for an organizational entity’s use.
An IP address is made of a group of octets and a subnet mask.

IPv4 addresses use four octets (groups of eight bits, so 32 bits), some of which are reserved to indicate the network a host is in, and the non-reserved bits are used by the host.
An IPv4 address format allows addresses from 0.0.0.0 to 255.255.255.255, and the subnet is indicated by a prefix /N, where N indicates the number of bits reserved for the network portion of the address, ranging 8-32. The subnet mask is an expanded presentation of the prefix and can range from 255.255.255.255 to 255.0.0.0.

The smaller the number on the subnet mask, the more hosts are allowed on its network.
In a subnet, the first address (e.g. 192.168.1.0/24) is always the network address and the last address (e.g. 192.168.1.255/24) is the broadcast address.
All addresses between these can be assigned to hosts, e.g. in a /24 subnet, the final octet for a host’s address ranges from 1 to 254.

IPv6 addresses use sixteen octets in eight hexadecimal pairs (total of 128 bits), with some reserved to indicate a host’s network.
The address format allows addresses from 0::0 to ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff, with any octet pairs marked as 0 between other pairs omitted in a written address.
The subnet is prefixed /N, where N indicates the number of bits reserved for the network portion of the address, ranging from 4-to 128
The subnet is marked with the octet pairs included in the networking segment followed by the prefix. e.g. the subnet for address 200f:0db8:ab00:0000:0000:000:4567:8901/48 (written 200f:0db8:ab00::4567:8901), has a subnet notation of 200f:0db8:ab00::/48.

IPv6 is meant to counteract Internet address exhaustion, as it allows 2128 (c. 3,40x1038) addresses, significantly more than the 232 (4,3x109) in IPv4.
However, networked monitoring systems are usually smaller and closed to other network traffic either through physical isolation or address translation, so IPv4 is used for ease and simplicity of configuration and use without fear of address exhaustion.
IP addresses are also classed to make their subnetting easier.
In general, the relationship between potential unique addresses in a network, and the total potential number of unique sub-networks supported is a decision well beyond a surveillance system.

The three most common network classes are limited as follows:

Class A ranges from 0.0.0.0/8 to 127.255.255.255/8

The first octet is reserved for subnets (NNNN.HHHH.HHHH.HHHH)

128 subnets of 16 777 214 host addresses

Class B ranges from 128.0.0.0/16 to 191.255.255.255/16

The first two octets are reserved for subnets (NNNN.NNNN.HHHH.HHHH)

16 384 subnets of 65 534 host addresses

Class C ranges from 192.0.0.0/24 to 223.255.255.255/24

The first three octets reserved for subnets (NNNN.NNNN.NNNN.HHHH)

2 097 152 subnets of 254 host addresses.

IP addresses or Hostnames for the older versions of Mirasys VMS 

The system can be configured to contact the servers through their IP address or hostname. in the new versions of Mirasys VMS (8.5 and further), only hostnames are used.
the servers must have static IP addresses configured for their network connections so that the client programs can connect to them.
Any servers set up to function as AVM Display Servers in the system should also have either static addresses or static hostnames, as the connection from the AVM operator console to the display servers is done with either the IP address or the hostname.
While servers and the AVM must have static addresses, clients with the network can be addressed with DHCP (Dynamic Host Configuration Protocol). DHCP servers are configured to provide a set pool of IP addresses, which are reserved by connected devices every time they restart. Addresses are given out on a first-come-first-serve basis. DHCP servers can also be set to reserve specific addresses for specific devices.
Cameras should also be statically addressed, and DHCP should be used only when establishing the first connection for initial configuration.
Some camera models can support zero-configuration, where a camera directly connected to a computer generates random IP addresses in the 169.254.0.0 /16 network for both devices.
This allows for an initial condition for a connection through which the camera can be configured. Consult the documentation for IP cameras to see if they support this feature.
If the system is intended to be used from outside a closed network, it is recommended to build the system using server hostnames instead of IP Addresses.
This makes it possible to contact the system from outside the local network with minimal effort. Please refer to the Mirasys VMS System Administrator’s Guide for further information on setting the server hostnames through the System Manager application.
Even if the system uses public IP Addresses, is run on a closed network, or is used through VPN, using hostnames instead of IP addresses for the system components can enhance user-friendliness and general usability.

Public IP Addresses

When using public IP Addresses with the Spotter for Windows and System Manager applications outside the local network, an IP address is required for each DVRServer and for the SMServer.
Local networks can use a private network subnet and assign addresses for devices in it to facilitate contact between them.
But these internal addresses are not congruent in a WAN environment, so public IP addresses are used on the outside of the local network to contact the devices therein.
Network edge devices, such as routers between the local network and WAN, use NAT (Network Address Translation) to translate public addresses (WAN) to private addresses (LAN) and vice versa.
Routers that run NAT take addresses on the local network (Inside) and assign WAN/Internet (Global) IP addresses to the traffic.
As far as the end-user is concerned, NAT is primarily performed in two ways by routers:

NAT Pools, where a segment of addresses is reserved and they are dynamically given to connecting inside devices on a first-come-first-serve basis for translation

Static NAT, where an inside address is statically translated to a specific global address by the server.

A more secure and efficient method of using a limited number of public IP Addresses in the system is by using the WebClient application. By providing a public IP for the GatewayServer, it is possible to access cameras in real-time and playback modes through a Java-enabled browser, the Spotter Mobile application, or custom applications based on the Gateway SDK (Software Development Kit).

Private IP Addresses

Portions of the 172.0.0.0 and 192.0.0.0 address ranges are designated for private networks. The remaining addresses are public, and routable on the global Internet.
Private networks can use IP addresses anywhere in the presented networks:

192.168.0.0/24 - 192.168.255.0/24
Class C networks, allowing 256 addresses per subnet (including network and broadcast addresses).
All subnets have the /24 prefix.

172.16.0.0/16 - 172.31.0.0/16Class B networks, allowing 65 536 addresses per subnet (including network and broadcast addresses).All subnets have the /16 prefix.

10.0.0.0/8 - 10.255.255.255/8Class A network, allowing a single 16 777 215 address subnet (including network and broadcast addresses).The subnet has the /8 prefix.

192.168.0.0/24 is the most popular private network subnet type in use, as most private subnets usually have up to 254 hosts in each, network segmentation is easy to plan and configure, and /24 subnets can be segmented into even smaller subnets as needed.

DNS For the newer versions of Mirasys VMS 

The Domain Name System (DNS) is a hierarchical and decentralized naming system for computers, services, or other resources connected to the Internet or a private network.
It translates more readily memorized hostnames to the numerical IP addresses needed for locating and identifying computer services and devices with the underlying network protocols. An often-used analogy to explain the Domain Name System is that it serves as the phone book for the Internet by translating human-friendly computer hostnames into IP addresses and vice versa. In the Mirasys VMS 8.5 and newer, the system is configured to contact the servers through hostname with the help of DNS.
This is because hostname allows the use of certificates in the VMS servers, which allows the VMS system to be protected better.
You must have a working and reachable DNS server at your disposal.
All the Mirasys servers (master, slave, AVM etc.), their hostnames and IP Addresses must be added to the DNS server configuration.
In case you don’t have any DNS servers available, there’s an option to install a DNS server from the Mirasys installation package.
It’s recommended to be used only with Windows 7 or 10 installations, Windows server installations have a built-in DNS server available.
Clients or cameras do not have to be added to the DNS. Cameras should have a static IP address, and DHCP or static IP addresses can be used with the clients.
You can optionally use DNS service and hostnames for older versions of Mirasys VMS (7 through 8.3.1) too, though IP addresses are used by default.  

Pagination
Previous page
Mirasys VMS communication
Next page
Network Connection Types