# Web Access Point

Let's start looking at some real IoT functionality.  We will create a web server on the ESP32 and connect to it using a browser.

We have two choices on how to connect the web server.  We can connect it as a station on a network through a router, or we can create a network access point and attach the web sever to the new network.

The advantage of connecting as a station is that you get the internet capabilites of the network, so you can access external web services as allowed by your network.  The disadvantage is that the device has to be able to connect to a router, so it will stop working when the device goes out of range or the network is unavailable.

The advantage of connecting as an access point is that the network and webserver are running on the same chip, so it will always be available as long as the chip is powered.  The disadvantage is that anyone who connects exclusivly to this network is not going to be able to connect to the web.

It's possible to have the ESP32 running as an access point and as a station at the same time.  For now, let's keep it simple and run as an access point.

## Stubbing
The network module is only on-chip, so we stub it for testing.  The socket module is available for testing, but running the production code fails because I don't have permission to open a new IPv4 TCP socket on port 80 for my PowerMac.  I have some test detection code in the production code, so I import a socket stub instead of the real socket module if I'm in test mode.

TODO:  This would be a really good kata for stubbing before introducing mocking