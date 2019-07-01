from boothOccupancyDetector import BoothOccupancyDetector
import esp32_machine_emulator.machine as machine

WALL_DISTANCE = 70
TOLARANCE = 10
def test_init():
    detector = BoothOccupancyDetector(triggerPin=5, echoPin=6, wallDistanceCm=WALL_DISTANCE, tolaranceCm=TOLARANCE)
    assert detector.sensor.echo.pinForTesting == 6
    assert detector.sensor.trigger.pinForTesting == 5
    assert detector.wallDistanceCm == WALL_DISTANCE
    assert detector.tolaranceCm == TOLARANCE

def test_findsWallExactly():
    detector = BoothOccupancyDetector(triggerPin=5, echoPin=6, wallDistanceCm=WALL_DISTANCE, tolaranceCm=TOLARANCE)
    machine.resetExpectationsForTesting()
    machine.expectedPulseTimeForTesting = cmToPulse(WALL_DISTANCE)
    assert detector.findWall()

def test_findsWallFailsWhenBlockedByPerson():
    detector = BoothOccupancyDetector(triggerPin=5, echoPin=6, wallDistanceCm=WALL_DISTANCE, tolaranceCm=TOLARANCE)
    machine.resetExpectationsForTesting()
    machine.expectedPulseTimeForTesting = cmToPulse(WALL_DISTANCE - TOLARANCE - 1)
    assert not detector.findWall()

def cmToPulse(distanceCm):
    return int(round(distanceCm * 2 * 29.1))