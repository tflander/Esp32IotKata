from sonarBoothWallDetector import SonarBoothWallDetector
import pytest

EXPECTED_DISTANCE_CM = 77
DISTANCE_TOLERANCE_CM = 10
NUM_READS_TO_CHANGE_STATE = 3
trigger_pin=2
echo_pin=15

class TestSonarBoothWallDetector:

    def test_initalStateIsAvailable(self):
        detector = SonarBoothWallDetector(trigger_pin, echo_pin, EXPECTED_DISTANCE_CM, DISTANCE_TOLERANCE_CM, NUM_READS_TO_CHANGE_STATE)
        assert detector.isAvalable

    @pytest.mark.skip(reason="need to test drive hcsr04.py to flesh out expectaton setting")
    def test_WhenWallBlockedByPersonThenBoothIsInUse(self):
        detector = SonarBoothWallDetector(trigger_pin, echo_pin, EXPECTED_DISTANCE_CM, DISTANCE_TOLERANCE_CM, NUM_READS_TO_CHANGE_STATE)

        sonar = detector.sonar
        print(sonar)
        
        assert not detector.isAvalable        