TEST_MODE = True

expectedPulseTimeForTesting = 0

# pulse_time = machine.time_pulse_us(self.echo, 1, self.echo_timeout_us)
def time_pulse_us(echoPin, one, echo_timeout_us):
    return expectedPulseTimeForTesting

class Pin:
    IN = "in"
    OUT = "out"
    pinForTesting = None
    currentState = None

    def __init__(self, pin, mode=OUT, pull=None):
        self.pinForTesting = pin

    def on(self):
        # self.currentState = "on"
        self.currentState = 1

    def off(self):
        # self.currentState = "off"
        self.currentState = 0

    def value(self, newValue=None):
        if newValue == 0:
            self.off()
        elif newValue == 1:
            self.on()
        return self.currentState

