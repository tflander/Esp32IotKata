import pytest
try:
    import machine
except:
    import esp32_machine_emulator.machine as machine

from boothInUseLedIndicator import BoothInUseLedIndicator

class TestPinTransitions(object):

    def test_pinValuesSetOnInit(self):
        boothInUseLedIndicator = BoothInUseLedIndicator(redLedPin=1, greenLedPin=2)
        assert boothInUseLedIndicator.redLed.pinForTesting == 1
        assert boothInUseLedIndicator.greenLed.pinForTesting == 2

    def test_whenOccupiedThenTurnRedOnAndTurnGreenOff(self):
        boothInUseLedIndicator = BoothInUseLedIndicator(redLedPin=1, greenLedPin=2)
        boothInUseLedIndicator.setOccupied()
        assert boothInUseLedIndicator.greenLed.currentStateForTesting == 0
        assert boothInUseLedIndicator.redLed.currentStateForTesting == 1

    def test_whenAvailableThenTurnRedOffAndTurnGreenOn(self):
        boothInUseLedIndicator = BoothInUseLedIndicator(redLedPin=1, greenLedPin=2)
        boothInUseLedIndicator.setAvailable()
        assert boothInUseLedIndicator.greenLed.currentStateForTesting == 1
        assert boothInUseLedIndicator.redLed.currentStateForTesting == 0
