import network
import socket
import machine

def wifiConnect(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, password)
    print('waiting for connection...')
    while not sta_if.isconnected():
        pass

    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    return addr, sta_if.ifconfig()


def startListener(addr):
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    return s

addr, ifconfig = wifiConnect("TheForge", "speed2VALUE!")
serverSocket = startListener(addr)

import picoweb
app = picoweb.WebApp(__name__)

count = 0
def incrementCount(timer):
    global count
    count = count + 1

countTimer = machine.Timer(0)  
countTimer.init(period=1000, mode=machine.Timer.PERIODIC, callback=incrementCount)


@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello world from picoweb running on the ESP32. data = %s" % str(count))

import logging
log = logging.getLogger("my-logger")

app.run(debug=True, host = ifconfig[0], log=log)
