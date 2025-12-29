# Network Optimization | Mirasys Help Center

Source: https://documentation.mirasys.com/mirasys-vms-admin-guide/V9.9/network-optimization-1

Network Optimization

TruCast can be used to reduce network load in specific scenarios.

The load reduction mainly occurs when the server is located off-site (remote) and the viewing client is on-site (local to the cameras).

An example scenario 1, we have two sites where the recording is off-site, and the viewing client is on-site. In the following diagram, the viewing is done without TruCast, and the video goes first to the server and then from the server to the viewing client.

In this solution, the traffic between the two sites is increased.

If the stream is consumed directly from the camera with TruCast, the traffic between the two sites is reduced.

An example scenario 2, there are cameras on two sites and viewing clients on two sites.

For the Site 2 user, the use of TruCast makes more sense for the on-site cameras.

The user can choose to use TruCast for all cameras or only for the on-site cameras.

For the Site 1 user, the use of TruCast only reduces the amount of traffic from the server to the nearest network connection.

Users have complete control over which cameras are using TruCast and which cameras are viewed typically.

The setting is memorized for each camera and each user and saved to Spotter layouts.

Pagination
Previous page
Supported Cameras
Next page
Multistreaming and TruCast for Network Optimization and Storage