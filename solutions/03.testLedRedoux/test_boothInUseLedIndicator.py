import pytest
from machine_stub import machine

from boothInUseLedIndicator import BoothInUseLedIndicator

class TestPinTransitions(object):

    def test_pinValuesSetOnInit(self):
        boothInUseLedIndicator = BoothInUseLedIndicator(redLedPin=1, greenLedPin=2)
        assert boothInUseLedIndicator.redLed.pinForTesting == 1
        assert boothInUseLedIndicator.greenLed.pinForTesting == 2

    def test_whenOccupiedThenTurnRedOnAndTurnGreenOff(self):
        boothInUseLedIndicator = BoothInUseLedIndicator(redLedPin=1, greenLedPin=2)
        boothInUseLedIndicator.setOccupied()
        assert boothInUseLedIndicator.greenLed.currentState == "off"
        assert boothInUseLedIndicator.redLed.currentState == "on"

    def test_whenAvailableThenTurnRedOffAndTurnGreenOn(self):
        boothInUseLedIndicator = BoothInUseLedIndicator(redLedPin=1, greenLedPin=2)
        boothInUseLedIndicator.setOccupied()
        assert boothInUseLedIndicator.greenLed.currentState == "off"
        assert boothInUseLedIndicator.redLed.currentState == "on"
