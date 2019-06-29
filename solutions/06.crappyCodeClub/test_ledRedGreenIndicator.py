from ledRedGreenIndicator import LedRedGreenIndicator

indicator = LedRedGreenIndicator(greenLedPin = 5, redLedPin = 6)

def test_ledPinsCreated():
    assert indicator.greenLed.pinForTesting == 5
    assert indicator.redLed.pinForTesting == 6

def test_green():
    indicator.green()
    assert indicator.greenLed.currentStateForTesting == 1
    assert indicator.redLed.currentStateForTesting == 0

def test_red():
    indicator.red()
    assert indicator.greenLed.currentStateForTesting == 0
    assert indicator.redLed.currentStateForTesting == 1
