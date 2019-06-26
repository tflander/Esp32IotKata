import pytest
from boothInUseDetector import BoothInUseDetector
import esp32_machine_emulator.machine as machine

class TestBoothAvailability:

    def test_initialStateIsOccupied(self, boothInUseDetector):
        assert not boothInUseDetector.isAvailable()

    def test_stateChangeWhenSonarDetectsWallExactlyEnoughTimes(self, boothInUseDetector):
        assert not boothInUseDetector.isAvailable()
        sampleUntilBoothAvailable(boothInUseDetector)
        assert boothInUseDetector.isAvailable()

    def test_stateDoesNotChangeWhenInconsistantSampling(self, boothInUseDetector):
        assert not boothInUseDetector.isAvailable()
        inconsistantSamples = [pulseValueWhenWallFound, pulseValueWhenPersonFound, pulseValueWhenWallFound, pulseValueWhenWallFound, pulseValueWhenWallFound]
        assert len(inconsistantSamples) == RETRIES_TO_CHANGE_STATE + 1
        sampleAllExpected(boothInUseDetector, inconsistantSamples)
        assert not boothInUseDetector.isAvailable()

    def test_stateDoesNotChangeWhenNotEnoughStateChangesSampled(self, boothInUseDetector):
        assert not boothInUseDetector.isAvailable()
        samples = [pulseValueWhenWallFound] * (RETRIES_TO_CHANGE_STATE - 1)
        sampleAllExpected(boothInUseDetector, samples)
        assert not boothInUseDetector.isAvailable()

    def test_boothBecomesInUseWhenWallNolongerConsistantlyFound(self, boothInUseDetector):
        sampleUntilBoothAvailable(boothInUseDetector)
        assert boothInUseDetector.isAvailable()
        samples = [pulseValueWhenPersonFound] * RETRIES_TO_CHANGE_STATE
        sampleAllExpected(boothInUseDetector, samples)
        assert not boothInUseDetector.isAvailable()

    def test_boothDetectorInit(self, boothInUseDetector):
        assert boothInUseDetector.retriesToChangeState == RETRIES_TO_CHANGE_STATE
        assert boothInUseDetector.expectedDistanceCm == EXPECTED_DISTANCE_CM
        assert boothInUseDetector.distanceTolerance == DISTANCE_TOLERANCE_CM
        sonar = boothInUseDetector.sonar
        assert sonar.trigger.pinForTesting == TRIGGER_PIN
        assert sonar.echo.pinForTesting == ECHO_PIN
        # TODO: test if anything missing


class TestSonarSampling:

    def test_candidateStateIsAvailableWhenSonarDetectsWall(self, boothInUseDetector):
        machine.expectedPulseTimeForTesting = pulseValueWhenWallFound
        candidateAvailabilityState = boothInUseDetector.sample()
        assert candidateAvailabilityState

    def test_candidateStateIsNotAvailableWhenSonarDetectsObjectAtHighTolerance(self, boothInUseDetector):
        machine.expectedPulseTimeForTesting = pulseValueWhenPersonFound
        candidateAvailabilityState = boothInUseDetector.sample()
        assert not candidateAvailabilityState

class TestSingleScan:

    def test_WhenWallFoundExactThenBoothIsAvailable(self, boothInUseDetector):
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM)

        assert boothInUseDetector.singleScan()
        assert boothInUseDetector.error == None

    def test_WhenWallBlockedByPersonThenBoothIsInUse(self, boothInUseDetector):
        machine.resetExpectationsForTesting()
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(2)

        assert not boothInUseDetector.singleScan()
        assert boothInUseDetector.error == None

    def test_WhenWallFoundWithinLowTolerance(self, boothInUseDetector):
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM - DISTANCE_TOLERANCE_CM)

        assert boothInUseDetector.singleScan()
        assert boothInUseDetector.error == None

    def test_WhenPersonFoundWithinLowTolerance(self, boothInUseDetector):
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM - DISTANCE_TOLERANCE_CM - 1)

        assert not boothInUseDetector.singleScan()
        assert boothInUseDetector.error == None

    def test_WhenWallFoundWithinHighTolerance(self, boothInUseDetector):
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM + DISTANCE_TOLERANCE_CM)

        assert boothInUseDetector.singleScan()
        assert boothInUseDetector.error == None

    def test_WhenObjectFoundOutsideHighTolerance(self, boothInUseDetector):
        machine.expectedPulseTimeForTesting = expectedPulsesForCm(EXPECTED_DISTANCE_CM + DISTANCE_TOLERANCE_CM + 1)

        assert not boothInUseDetector.singleScan()
        assert boothInUseDetector.error == "object out of range"

    def test_WhenSonarScanError(self, boothInUseDetector):
        machine.expectedPulseTimeErrorForTesting = OSError(110)

        assert not boothInUseDetector.singleScan()
        assert boothInUseDetector.error == "Out of sonar range"

    def test_VerifyErrorStateWhenDetectorNotCalled(self, boothInUseDetector):
        assert boothInUseDetector.error == None

    
def sampleAllExpected(boothInUseDetector, samples):
    machine.expectedPulseTimeForTesting = samples
    while len(machine.expectedPulseTimeForTesting) > 0:
        boothInUseDetector.sample()

def sampleUntilBoothAvailable(boothInUseDetector):
    samples = [pulseValueWhenWallFound] * RETRIES_TO_CHANGE_STATE
    sampleAllExpected(boothInUseDetector, samples)

def expectedPulsesForCm(cm):
    return int(round(cm * 58.2))

TRIGGER_PIN=1
ECHO_PIN=2
EXPECTED_DISTANCE_CM=10
DISTANCE_TOLERANCE_CM = 3
RETRIES_TO_CHANGE_STATE = 4
SAMPLE_INTERVAL_MS = 300

pulseValueWhenWallFound = expectedPulsesForCm(EXPECTED_DISTANCE_CM)
pulseValueWhenPersonFound = expectedPulsesForCm(EXPECTED_DISTANCE_CM - DISTANCE_TOLERANCE_CM - 1)

@pytest.fixture
def boothInUseDetector():
    return BoothInUseDetector(
        trigger_pin = TRIGGER_PIN, 
        echo_pin = ECHO_PIN, 
        expectedDistanceCm = EXPECTED_DISTANCE_CM, 
        distanceTolerance = DISTANCE_TOLERANCE_CM, 
        retriesToChangeState = RETRIES_TO_CHANGE_STATE
    )
