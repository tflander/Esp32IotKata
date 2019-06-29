try:
    import machine
except:
    import esp32_machine_emulator.machine as machine

from hcsr04UltrasonicDistanceSensor import Hcsr04UltrasonicDistanceSensor
from ledRedGreenIndicator import LedRedGreenIndicator
from boot import apConnect, startListener

# addr, ifconfig = wifiConnect("TheForge", "speed2VALUE!")
addr, ifconfig = apConnect("Todd Esp32")
serverSocket = startListener(addr)


EXPECTED_DISTANCE_CM = 77
DISTANCE_TOLERANCE_CM = 10
NUM_READS_TO_CHANGE_STATE = 3

ledIndicator = LedRedGreenIndicator(greenLedPin=22, redLedPin=21)

try:
    import picoweb
except:
    import picoweb_stub as picoweb

app = picoweb.WebApp(__name__)

sensor = Hcsr04UltrasonicDistanceSensor(triggerPin=2, echoPin=15)

distance = -1
isOccupied = False
candidateStateChangeCount = 0

def measureDistance(timer):
    global distance, isOccupied, candidateStateChangeCount
    candidateDistance = -1
    while candidateDistance < 0 or candidateDistance > EXPECTED_DISTANCE_CM + DISTANCE_TOLERANCE_CM:
        candidateDistance = sensor.distanceCm()
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
        ledIndicator.red()
    else:
        ledIndicator.green()

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
log = logging.getLogger(__name__)

app.run(debug=True, host = ifconfig[0], log=log)
