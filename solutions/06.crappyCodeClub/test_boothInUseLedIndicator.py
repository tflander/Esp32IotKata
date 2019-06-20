import pytest
import machine

from boothInUseLedIndicator import BoothInUseLedIndicator

class TestPinTransitions(object):

    # TODO: do I really need this test?
    def test_pinValuesSetOnInit(self):
        boothInUseLedIndicator = BoothInUseLedIndicator(redLedPin=1, greenLedPin=2)
        assert boothInUseLedIndicator.redLed.pinForTesting == 1
        assert boothInUseLedIndicator.greenLed.pinForTesting == 2

    def test_whenOccupiedThenTurnRedOnAndTurnGreenOff(self):
        boothInUseLedIndicator = BoothInUseLedIndicator(redLedPin=1, greenLedPin=2)
        boothInUseLedIndicator.setOccupied()
        assert boothInUseLedIndicator.greenLed.currentState == 0
        assert boothInUseLedIndicator.redLed.currentState == 1

    def test_whenAvailableThenTurnRedOffAndTurnGreenOn(self):
        boothInUseLedIndicator = BoothInUseLedIndicator(redLedPin=1, greenLedPin=2)
        boothInUseLedIndicator.setAvailable()
        assert boothInUseLedIndicator.greenLed.currentState == 1
        assert boothInUseLedIndicator.redLed.currentState == 0
