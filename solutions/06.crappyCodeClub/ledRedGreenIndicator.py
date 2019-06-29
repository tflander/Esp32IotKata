try:
    import machine
except:
    import esp32_machine_emulator.machine as machine

class LedRedGreenIndicator:
    
    def __init__(self, greenLedPin, redLedPin):
        self.greenLed = machine.Pin(greenLedPin, machine.Pin.OUT)
        self.redLed = machine.Pin(redLedPin, machine.Pin.OUT)

    def green(self):
        self.greenLed.on()
        self.redLed.off()

    def red(self):
        self.greenLed.off()
        self.redLed.on()
