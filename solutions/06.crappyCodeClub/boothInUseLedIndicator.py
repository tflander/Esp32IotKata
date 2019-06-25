try:
    import machine
except:
    import esp32_machine_emulator.machine as machine

class BoothInUseLedIndicator:

    greenLed = None
    redLed = None

    def __init__(self, redLedPin, greenLedPin):
        self.greenLed = machine.Pin(greenLedPin, machine.Pin.OUT)
        self.redLed = machine.Pin(redLedPin, machine.Pin.OUT)

    def setOccupied(self):
        self.greenLed.off()
        self.redLed.on()

    def setAvailable(self):
        self.greenLed.on()
        self.redLed.off()
