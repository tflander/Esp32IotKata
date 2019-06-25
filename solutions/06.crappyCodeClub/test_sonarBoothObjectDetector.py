from sonarBoothObjectDetector import SonarBoothObjectDetector
import pytest
import esp32_machine_emulator.machine as machine

EXPECTED_DISTANCE_CM = 77
DISTANCE_TOLERANCE_CM = 10
trigger_pin=2
echo_pin=15

class TestSonarBoothObjectDetector:

    detector = SonarBoothObjectDetector(trigger_pin, echo_pin, EXPECTED_DISTANCE_CM, DISTANCE_TOLERANCE_CM)

    def test_WhenWallFoundExactThenBoothIsAvailable(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM)

        assert self.detector.isObjectDetected()
        assert self.detector.error == None

    def test_WhenWallBlockedByPersonThenBoothIsInUse(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(10)

        assert not self.detector.isObjectDetected()
        assert self.detector.error == None

    def test_WhenWallFoundWithinLowTolerance(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM - DISTANCE_TOLERANCE_CM)

        assert self.detector.isObjectDetected()
        assert self.detector.error == None

    def test_WhenPersonFoundWithinLowTolerance(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM - DISTANCE_TOLERANCE_CM - 1)

        assert not self.detector.isObjectDetected()
        assert self.detector.error == None

    def test_WhenWallFoundWithinHighTolerance(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM + DISTANCE_TOLERANCE_CM)

        assert self.detector.isObjectDetected()
        assert self.detector.error == None

    def test_WhenObjectFoundOutsideHighTolerance(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM + DISTANCE_TOLERANCE_CM + 1)

        assert not self.detector.isObjectDetected()
        assert self.detector.error == "object out of range"

    def test_WhenSonarScanError(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeErrorForTesting = OSError(110)

        assert not self.detector.isObjectDetected()
        assert self.detector.error == "Out of sonar range"

def expectedPulsesForCm(cm):
    return int(round(cm * 58.2))
