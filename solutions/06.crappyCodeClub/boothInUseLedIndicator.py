try:
    import machine
except:
    import esp32_machine_emulator.machine as machine

class BoothInUseLedIndicator:

    def __init__(self, redLedPin, greenLedPin):
        self.greenLed = machine.Pin(greenLedPin, machine.Pin.OUT)
        self.redLed = machine.Pin(redLedPin, machine.Pin.OUT)
        self.occupied = True

    def setOccupied(self):
        self.greenLed.off()
        self.redLed.on()
        self.occupied = True

    def setAvailable(self):
        self.greenLed.on()
        self.redLed.off()
        self.occupied = False

    def isOccupied(self):
        return self.occupied

