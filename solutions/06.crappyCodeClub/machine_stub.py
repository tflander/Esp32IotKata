class machine:
    
    class Pin:
        IN = "in"
        OUT = "out"
        pinForTesting = None
        currentState = None

        def __init__(self, pin, dir):
            self.pinForTesting = pin

        def on(self):
            self.currentState = "on"

        def off(self):
            self.currentState = "off"
            