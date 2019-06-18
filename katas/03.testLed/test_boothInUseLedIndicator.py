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

    def test_whenOccupiedThenTurnRedOnAndTurnGreenOff(self):
        pass
        # hint: look at the machine_stub.py file to see how you can assert on the pin states

    def test_whenAvailableThenTurnRedOffAndTurnGreenOn(self):
        pass
