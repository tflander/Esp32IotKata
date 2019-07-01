import pytest

# Remember the previous kata where the "import machine" statement was red.  This was becuase the machine module
# exists only on the ESP32, and we are test-driving software on a computer.  There may be a better solution,
# but here I have a machine stub module that will be imported if we fail to import the real one.  The stub has
# no behavior, but has the hardware interfaces that I want to mock for the tests.
try:
    import machine
except:
    import esp32_machine_emulator.machine as machine

# Note: since this is a test that always runs off-chip, I know that I always want the machine emulator.  
# The try/except block is a hint for writing the production code.

## Step one: un-comment and make green
# from boothInUseLedIndicator import BoothInUseLedIndicator

### Step three: test drive the behavior of boothInUseLedIndicator.
class TestPinTransitions(object):

    def test_whenOccupiedThenTurnRedOnAndTurnGreenOff(self):
        pass

    def test_whenAvailableThenTurnRedOffAndTurnGreenOn(self):
        pass
