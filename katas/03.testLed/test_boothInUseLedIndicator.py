import pytest
from mock import Mock, patch

# Remember the previous kata where the "import machine" statement was red.  This was becuase the machine module
# exists only on the ESP32, and we are test-driving software on a computer.  There may be a better solution,
# but here I have a machine stub module that will be imported if we fail to import the real one.  The stub has
# no behavior, but has the hardware interfaces that I want to mock for the tests.
try:
    import machine
    isRunningOffChip = False
except:
    from machine_stub import machine
    isRunningOffChip = True

# these test fixures represent the LED pins controlled by the booth in-use LED indicator class - the class under 
# test.  I don't have to really light up an LED, I just have to verify that the class under test sends the pin 
# signal to turn the LED on.  The class behavior is the same if I'm using a real pin on-chip or a mock pin in the 
# test environment.
@pytest.fixture
def mockGreenLedPin():
    return Mock(spec=machine.Pin)

@pytest.fixture
def mockRedLedPin():
    return Mock(spec=machine.Pin)

## Step one: un-comment and make green
# from boothInUseLedIndicator import BoothInUseLedIndicator

### Step two: Create a test fixture for the class under test.
@pytest.fixture
def boothInUseLedIndicator(monkeypatch, mockGreenLedPin, mockRedLedPin):
    pass # TODO: delete this line of code

    # The following code is tricky.  First of all, it requires that the production code have an __init__ method 
    # that takes in the GPIO numbers of the red LED pin and the green LED pin.  We don't want to have to open
    # up the code if we decide to build a circuit where the LEDs are wired to different GPIO pins.  For our 
    # circuit, we use GPIO21 for red and GPIO22 for green.  So, we would like to construct our class using this
    # bit of code in our main.py (NOT HERE!):
    #
    # boothInUseLedIndicator = BoothInUseLedIndicator(redLedPin=21, greenLedPin=22)

    # TODO: uncomment the following block.  Make green by adding an __init__() method to set the green and red pin
    # note that we expect the attributes "greenLed" and "redLed" on the class, which will be of type machine.Pin
    # (just like our mocks in the above fixtures)

    # with patch.object(BoothInUseLedIndicator, "__init__", lambda slf, redPin, greenPin: None):
    #     boothInUseLedIndicator = BoothInUseLedIndicator(None, None)
    #     boothInUseLedIndicator.greenLed = mockGreenLedPin
    #     boothInUseLedIndicator.redLed = mockRedLedPin
    #     return boothInUseLedIndicator

### Step three: test drive the behavior of boothInUseLedIndicator.
class TestPinTransitions(object):

    def test_whenOccupiedThenTurnRedOnAndTurnGreenOff(self, monkeypatch, boothInUseLedIndicator, mockGreenLedPin, mockRedLedPin):
        pass


    def test_whenAvailableThenTurnRedOffAndTurnGreenOn(self, monkeypatch, boothInUseLedIndicator, mockGreenLedPin, mockRedLedPin):
        pass
