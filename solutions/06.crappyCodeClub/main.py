from boothInUseLedIndicator import BoothInUseLedIndicator
from boot import apConnect, startListener
# try:
#     import machine
# except:
#     from machine_emulator import machine
import machine

try:
    import picoweb
except:
    print('picoweb module not found')
# import picoweb_stub as picoweb

from hcsr04 import HCSR04
 
EXPECTED_DISTANCE_CM = 77
DISTANCE_TOLERANCE_CM = 10
NUM_READS_TO_CHANGE_STATE = 3

# addr, ifconfig = wifiConnect("TheForge", "speed2VALUE!")
addr, ifconfig = apConnect("Todd Esp32")
serverSocket = startListener(addr)

app = picoweb.WebApp(__name__)

sensor = HCSR04(trigger_pin=2, echo_pin=15)

distance = -1
isOccupied = False
candidateStateChangeCount = 0

boothInUseLedIndicator = BoothInUseLedIndicator(redLedPin = 21, greenLedPin = 22)
def measureDistance(timer):
    handleStateChangeIfNecessary()

def handleStateChangeIfNecessary():
    global distance, isOccupied, candidateStateChangeCount, boothInUseLedIndicator
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
        boothInUseLedIndicator.setOccupied()
    else:
        boothInUseLedIndicator.setAvailable()

distanceTimer = machine.Timer(0)  
# distanceTimer.init(period=1000, mode=machine.Timer.PERIODIC, callback=measureDistance)

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("'isOccupied' : " + str(isOccupied))

@app.route("/debug")
def debug(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Distance = {} cm; isOccupied = {}; candidateStateChangeCount = {}".format(str(distance), isOccupied, candidateStateChangeCount))

globalReq = None
globalResp = None
@app.route("/sandbox")
def sandbox(req, resp):

# >>> globalReq
# <picoweb.HTTPRequest object at 3ffc8ef0>
# >>> globalResp
# <StreamWriter <socket>>

    global globalReq
    globalReq = req
    global globalResp
    globalResp = resp
    yield from picoweb.start_response(resp)
    yield from resp.awrite("req = {}; resp = {}".format(req.__class__, resp.__class__))

import logging
log = logging.getLogger(__name__)

app.run(debug=True, host = ifconfig[0], log=log)
