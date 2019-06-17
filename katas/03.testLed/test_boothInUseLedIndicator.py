import pytest
from mock import Mock, patch

# Remember the previous kata where the "import machine" statement was red.  This was becuase the machine module
# exists only on the ESP32, and we are test-driving software on a computer.  There may be a better solution,
# but here I have a machine stub module that will be imported if we fail to import the real one.  The stub has
# no behavior, but has the hardware interfaces that I want to mock for the tests.
try:
    import machine
except:
    from machine_stub import machine

# Note: since this is a test that always runs off-chip, I know that I always want machine_stub.  The try/except
# is a hint for writing the production code.

## Step one: un-comment and make green
# from boothInUseLedIndicator import BoothInUseLedIndicator

### Step three: test drive the behavior of boothInUseLedIndicator.
class TestPinTransitions(object):

    # Note: this is a really stupid test, but I've provided it as a clue to writing the BoothInUseLedIndicator
    # class.  The above monkeypatching code for the boothInUseLedIndicator fixture provides the same clues,
    # but the code doesn't fail, so I'm providing a test that will fail until the prodution code is stubbed
    # with the necessary attributes and classes
    def test_hasExpectedAttributesAndMethods(self):
        pass
        # realBoothIndicator = BoothInUseLedIndicator(redLedPin=1, greenLedPin=2)

        # def attributeExists(attributeName, expectedType):
        #     attr = getattr(realBoothIndicator, attributeName)
        #     return hasattr(realBoothIndicator, attributeName) and not callable(attr) and isinstance(attr, machine.Pin)

        # def methodExists(methodName):
        #     return hasattr(realBoothIndicator, methodName) and callable(getattr(realBoothIndicator, methodName))

        # assert attributeExists('greenLed', machine.Pin)
        # assert attributeExists('redLed', machine.Pin)
        # assert methodExists('setOccupied')
        # assert methodExists('setAvailable')

    def test_whenOccupiedThenTurnRedOnAndTurnGreenOff(self):
        pass
        # hint: look at the machine_stub.py file to see how you can assert on the pin states

    def test_whenAvailableThenTurnRedOffAndTurnGreenOn(self):
        pass
