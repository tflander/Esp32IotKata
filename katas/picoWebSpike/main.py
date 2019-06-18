import network
import socket

def wifiConnect(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, password)
    print('waiting for connection...')
    while not sta_if.isconnected():
        pass
    # print('network config:', sta_if.ifconfig())

    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    return addr, sta_if.ifconfig()


def startListener(addr):
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    print('listening on', addr)
    return s

addr, ifconfig = wifiConnect("TheForge", "speed2VALUE!")
serverSocket = startListener(addr)

import picoweb
app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello world from picoweb running on the ESP32")

import logging
log = logging.getLogger("my-logger")

app.run(debug=True, host = ifconfig[0], log=log)
