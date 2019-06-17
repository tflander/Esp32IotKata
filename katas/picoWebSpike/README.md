I’m hoping to avoid test-driving a bunch of socket code for implementing an HTTP server

Need WEP password for wifi-IoT so I can run upip

https://techtutorialsx.com/2017/09/01/esp32-micropython-http-webserver-with-picoweb/

import upip
upip.install('picoweb')

import picoweb
app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello world from picoweb running on the ESP32")

