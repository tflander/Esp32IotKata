Here are my refactoring steps.  Yours might be quite different.

- Move the boilerplate network code to boot.py.  This allows me to focus on the real logic in main.py
- There seems to be a seam between the LED code and the rest of the code.  Let's pull the LED code into a new class:

```
class LedRedGreenIndicator:
    greenLed = machine.Pin(22, machine.Pin.OUT)
    redLed = machine.Pin(21, machine.Pin.OUT)

    def showRed(self):
        self.greenLed.off()
        self.redLed.on()

    def showGreen(self):
        self.greenLed.off()
        self.redLed.on()

ledIndicator = LedRedGreenIndicator()

```
- Now let's comment-out the class and test-drive it from scratch