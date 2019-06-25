from sonarBoothObjectDetector import SonarBoothObjectDetector
import pytest
import esp32_machine_emulator.machine as machine

EXPECTED_DISTANCE_CM = 77
DISTANCE_TOLERANCE_CM = 10
trigger_pin=2
echo_pin=15

class TestSonarBoothObjectDetector:

    @pytest.fixture
    def detector(self):
        machine.resetExpectationsForTesting()
        return SonarBoothObjectDetector(trigger_pin, echo_pin, EXPECTED_DISTANCE_CM, DISTANCE_TOLERANCE_CM)

    def test_WhenWallFoundExactThenBoothIsAvailable(self, detector):
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM)

        assert detector.isObjectDetected()
        assert detector.error == None

    def test_WhenWallBlockedByPersonThenBoothIsInUse(self, detector):
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(10)

        assert not detector.isObjectDetected()
        assert detector.error == None

    def test_WhenWallFoundWithinLowTolerance(self, detector):
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM - DISTANCE_TOLERANCE_CM)

        assert detector.isObjectDetected()
        assert detector.error == None

    def test_WhenPersonFoundWithinLowTolerance(self, detector):
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM - DISTANCE_TOLERANCE_CM - 1)

        assert not detector.isObjectDetected()
        assert detector.error == None

    def test_WhenWallFoundWithinHighTolerance(self, detector):
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM + DISTANCE_TOLERANCE_CM)

        assert detector.isObjectDetected()
        assert detector.error == None

    def test_WhenObjectFoundOutsideHighTolerance(self, detector):
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM + DISTANCE_TOLERANCE_CM + 1)

        assert not detector.isObjectDetected()
        assert detector.error == "object out of range"

    def test_WhenSonarScanError(self, detector):
        machine.expectedPulseTimeErrorForTesting = OSError(110)

        assert not detector.isObjectDetected()
        assert detector.error == "Out of sonar range"

def expectedPulsesForCm(cm):
    return int(round(cm * 58.2))
