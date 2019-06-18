import network
import socket
import machine
from hcsr04 import HCSR04

EXPECTED_DISTANCE_CM = 77
DISTANCE_TOLERANCE_CM = 10
NUM_READS_TO_CHANGE_STATE = 3

def wifiConnect(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, password)
    print('waiting for connection...')
    while not sta_if.isconnected():
        pass

    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    return addr, sta_if.ifconfig()

def apConnect(ssid):
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True) 
    ap_if.config(essid=ssid)
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    return addr, ap_if.ifconfig()

def startListener(addr):
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    return s

# addr, ifconfig = wifiConnect("TheForge", "speed2VALUE!")
addr, ifconfig = apConnect("Todd Esp32")
serverSocket = startListener(addr)
greenLed = machine.Pin(22, machine.Pin.OUT)
redLed = machine.Pin(21, machine.Pin.OUT)

import picoweb
app = picoweb.WebApp(__name__)

sensor = HCSR04(trigger_pin=2, echo_pin=15)

distance = -1
isOccupied = False
candidateStateChangeCount = 0

def measureDistance(timer):
    global distance, isOccupied, candidateStateChangeCount
    candidateDistance = -1
    while candidateDistance < 0 or candidateDistance > EXPECTED_DISTANCE_CM + DISTANCE_TOLERANCE_CM:
        candidateDistance = sensor.distance_cm()
        # print('retrying...')

    distance = candidateDistance
    candiateIsOccupied = candidateDistance < EXPECTED_DISTANCE_CM - DISTANCE_TOLERANCE_CM
    if(candiateIsOccupied):
        if not isOccupied:
            if candidateStateChangeCount < NUM_READS_TO_CHANGE_STATE:
                candidateStateChangeCount = candidateStateChangeCount + 1
            else:
                candidateStateChangeCount = 0
                isOccupied = True
    else:
        if isOccupied:
            if candidateStateChangeCount < NUM_READS_TO_CHANGE_STATE:
                candidateStateChangeCount = candidateStateChangeCount + 1
            else:
                candidateStateChangeCount = 0
                isOccupied = False

    if(isOccupied):
        greenLed.off()
        redLed.on()
    else:
        greenLed.on()
        redLed.off()

distanceTimer = machine.Timer(0)  
distanceTimer.init(period=1000, mode=machine.Timer.PERIODIC, callback=measureDistance)

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("'isOccupied' : " + str(isOccupied))

@app.route("/debug")
def debug(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Distance = {} cm; isOccupied = {}; candidateStateChangeCount = {}".format(str(distance), isOccupied, candidateStateChangeCount))

import logging
log = logging.getLogger("my-logger")

app.run(debug=True, host = ifconfig[0], log=log)
