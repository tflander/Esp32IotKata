import pytest
from boothInUseDetector import BoothInUseDetector
import esp32_machine_emulator.machine as machine

class TestBoothInUseDetector:

    TRIGGER_PIN=1
    ECHO_PIN=2
    EXPECTED_DISTANCE_CM=10
    DISTANCE_TOLERANCE = 3
    RETRIES_TO_CHANGE_STATE = 4
    SAMPLE_INTERVAL_MS = 300

    @pytest.fixture
    def boothInUseDetector(self):
        return BoothInUseDetector(
            trigger_pin = self.TRIGGER_PIN, 
            echo_pin = self.ECHO_PIN, 
            expectedDistanceCm = self.EXPECTED_DISTANCE_CM, 
            distanceTolerance = self.DISTANCE_TOLERANCE, 
            retriesToChangeState = self.RETRIES_TO_CHANGE_STATE, 
            sampleIntervalMs = self.SAMPLE_INTERVAL_MS
        )

    def test_initialStateIsOccupied(self, boothInUseDetector):
        assert not boothInUseDetector.isAvailable()

    def test_boothDetectorCreatesObjectDetector(self, boothInUseDetector):
        assert boothInUseDetector.expectedDistanceCm == self.EXPECTED_DISTANCE_CM
        assert boothInUseDetector.distanceTolerance == self.DISTANCE_TOLERANCE
        assert boothInUseDetector.retriesToChangeState == self.RETRIES_TO_CHANGE_STATE
        assert boothInUseDetector.sampleIntervalMs == self.SAMPLE_INTERVAL_MS
        assert not boothInUseDetector.objectDetector == None
        sonar = boothInUseDetector.objectDetector.sonar
        assert sonar.trigger.pinForTesting == self.TRIGGER_PIN
        assert sonar.echo.pinForTesting == self.ECHO_PIN

    def test_stateDoesNotChangeWhenSonarDetectsWallExactly(self, boothInUseDetector):
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(self.EXPECTED_DISTANCE_CM)
        assert not boothInUseDetector.isAvailable()


def expectedPulsesForCm(cm):
    return int(round(cm * 58.2))
