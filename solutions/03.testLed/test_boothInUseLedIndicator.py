import pytest
from mock import Mock, patch

try:
    import machine
except:
    from machine_stub import machine

@pytest.fixture
def mockGreenLedPin():
    return Mock(spec=machine.Pin)

@pytest.fixture
def mockRedLedPin():
    return Mock(spec=machine.Pin)

from boothInUseLedIndicator import BoothInUseLedIndicator

@pytest.fixture
def boothInUseLedIndicator(monkeypatch, mockGreenLedPin, mockRedLedPin):
    with patch.object(BoothInUseLedIndicator, "__init__", lambda slf, redPin, greenPin: None):
        boothInUseLedIndicator = BoothInUseLedIndicator(1, 2)
        boothInUseLedIndicator.greenLed = mockGreenLedPin
        boothInUseLedIndicator.redLed = mockRedLedPin
        return boothInUseLedIndicator

class TestPinTransitions(object):

    def test_pinValuesSetOnInit(self):
        real = BoothInUseLedIndicator(redLedPin=1, greenLedPin=2)
        assert real.redLed.pinForTesting == 1
        assert real.greenLed.pinForTesting == 2


    def test_whenOccupiedThenTurnRedOnAndTurnGreenOff(self, monkeypatch, boothInUseLedIndicator, mockGreenLedPin, mockRedLedPin):
        boothInUseLedIndicator.setOccupied()
        mockGreenLedPin.off.assert_called()
        mockRedLedPin.on.assert_called()


    def test_whenAvailableThenTurnRedOffAndTurnGreenOn(self, monkeypatch, boothInUseLedIndicator, mockGreenLedPin, mockRedLedPin):
        boothInUseLedIndicator.setAvailable()
        mockGreenLedPin.on.assert_called()
        mockRedLedPin.off.assert_called()
