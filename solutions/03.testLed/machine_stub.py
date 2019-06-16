class machine:
    
    class Pin:
        IN = "in"
        OUT = "out"
        pinForTesting = None

        def __init__(self, pin, dir):
            self.pinForTesting = pin

        def on(self):
            pass

        def off(self):
            pass
            