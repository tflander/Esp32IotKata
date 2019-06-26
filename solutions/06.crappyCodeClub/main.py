from boothInUseLedIndicator import BoothInUseLedIndicator
from boot import apConnect, startListener
try:
    import machine
except:
    from machine_emulator import machine

try:
    import picoweb
except:
    print('picoweb module not found')
# import picoweb_stub as picoweb

from boothInUseDetector import BoothInUseDetector
 
# addr, ifconfig = wifiConnect("TheForge", "speed2VALUE!")
addr, ifconfig = apConnect("Todd Esp32")
serverSocket = startListener(addr)

app = picoweb.WebApp(__name__)

boothInUseDetector = BoothInUseDetector(trigger_pin=2, echo_pin=15, expectedDistanceCm=77, distanceTolerance=10, retriesToChangeState=3)

# distance = -1
# isOccupied = False
# candidateStateChangeCount = 0

boothInUseLedIndicator = BoothInUseLedIndicator(redLedPin = 21, greenLedPin = 22)

def measureDistance(timer):
    boothInUseDetector.sample()
    if boothInUseDetector.isAvailable():
        boothInUseLedIndicator.setAvailable()
    else:
        boothInUseLedIndicator.setOccupied()

distanceTimer = machine.Timer(0)  
distanceTimer.init(period=1000, mode=machine.Timer.PERIODIC, callback=measureDistance)

@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("'isOccupied' : " + str(boothInUseLedIndicator.redLed.value()))

globalReq = None
globalResp = None
@app.route("/sandbox")
def sandbox(req, resp):

    # >>> req
    # <picoweb.HTTPRequest object at 3ffc8ef0>
    # >>> resp
    # <uasyncio.StreamWriter <socket>>

    yield from picoweb.start_response(resp)
    yield from resp.awrite("req = {}; resp = {}".format(req.__class__, resp.__class__))

import logging
log = logging.getLogger(__name__)

app.run(debug=True, host = ifconfig[0], log=log)
