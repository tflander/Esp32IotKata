I’m hoping to avoid test-driving a bunch of socket code for implementing an HTTP server

Need WEP password for wifi-IoT so I can run upip
-- or just connect as The Forge

https://techtutorialsx.com/2017/09/01/esp32-micropython-http-webserver-with-picoweb/

import upip
upip.install('picoweb')

import picoweb
app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello world from picoweb running on the ESP32")


ImportError: no module named 'ulogging'
upip.install('ulogging')

Error installing 'ulogging': Package not found, packages may be partially installed

upip.install(‘micropython-logging’)
upip.install('logging')

import logging
log = logging.getLogger("my-logger")
