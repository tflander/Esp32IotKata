Test driving an HTTP Server using socket code is educational, but painful. Let's use an established HTTP Server framework for MicroPython. PicoWeb looks like a good choice, but it's not available on the ESP32 by default.  We need to install it.

Fortunately, the MicroPython firmware comes with the package manager upip.  Upip allows you to install modules, like pip does for full-blown python.  PIP is an acronym for "PIP Installs Packages".

To install packages
```
import upip
upip.install('picoweb')
```

Unless your ESP32 is in station mode and connected to an internet-enabled router, running upip will likely result in the following error:

```
Installing to: /lib/
Error installing 'picoweb': list index out of range, packages may be partially installed
```

We need to put the ESP32 in station mode.  For convience, I created a boot.by program here to make connecting to a router via a WEP password easy.

Upload this project to your ESP32 to enable the ability to run the following commands

```
wifiConnect('TheForge, <password for TheForge>)
```

Now when you re-run the command upip.install('picoweb'), you get the following:

```
Warning: micropython.org SSL certificate is not validated
Installing picoweb 1.6 from https://files.pythonhosted.org/packages/f8/6c/7a964643277ea923a981d4e2e9cab107592f66ede424d4ea1017dfb8119b/picoweb-1.6.tar.gz
Installing micropython-uasyncio 2.0 from https://micropython.org/pi/uasyncio/uasyncio-2.0.tar.gz
Installing micropython-pkg_resources 0.2.1 from https://micropython.org/pi/pkg_resources/pkg_resources-0.2.1.tar.gz
Installing micropython-uasyncio.core 2.0 from https://micropython.org/pi/uasyncio.core/uasyncio.core-2.0.tar.gz
```

Picoweb also needs a logger.  Install one:

```
upip.install('logging')
```
