from sonarBoothWallDetector import SonarBoothWallDetector
import pytest
import machine

EXPECTED_DISTANCE_CM = 77
DISTANCE_TOLERANCE_CM = 10
NUM_READS_TO_CHANGE_STATE = 3
trigger_pin=2
echo_pin=15

class TestSonarBoothWallDetector:

    detector = SonarBoothWallDetector(trigger_pin, echo_pin, EXPECTED_DISTANCE_CM, DISTANCE_TOLERANCE_CM, NUM_READS_TO_CHANGE_STATE)

    def test_WhenWallFoundExactThenBoothIsAvailable(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM)

        assert self.detector.isAvailable()
        assert self.detector.error == None

    def test_WhenWallBlockedByPersonThenBoothIsInUse(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(10)

        assert not self.detector.isAvailable()
        assert self.detector.error == None

    def test_WhenWallFoundWithinLowTolerance(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM - DISTANCE_TOLERANCE_CM)

        assert self.detector.isAvailable()
        assert self.detector.error == None

    def test_WhenPersonFoundWithinLowTolerance(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM - DISTANCE_TOLERANCE_CM - 1)

        assert not self.detector.isAvailable()
        assert self.detector.error == None

    def test_WhenWallFoundWithinHighTolerance(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM + DISTANCE_TOLERANCE_CM)

        assert self.detector.isAvailable()
        assert self.detector.error == None

    def test_WhenObjectFoundOutsideHighTolerance(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM + DISTANCE_TOLERANCE_CM + 1)

        assert not self.detector.isAvailable()
        assert self.detector.error == "object out of range"

    def test_WhenSonarScanError(self):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeErrorForTesting = OSError(110)

        assert not self.detector.isAvailable()
        assert self.detector.error == "Out of sonar range"

def expectedPulsesForCm(cm):
    return int(round(cm * 58.2))
