from sonarBoothObjectDetector import SonarBoothObjectDetector

class BoothInUseDetector:
    
    objectDetector = None

    def __init__(self, trigger_pin, echo_pin, expectedDistanceCm, distanceTolerance, retriesToChangeState, sampleIntervalMs):
        self.objectDetector = SonarBoothObjectDetector(trigger_pin=trigger_pin, echo_pin=echo_pin,expectedDistanceCm=11,distanceTolerance=3)
        self.expectedDistanceCm = expectedDistanceCm
        self.distanceTolerance = distanceTolerance
        self.retriesToChangeState = retriesToChangeState
        self.sampleIntervalMs = sampleIntervalMs

    def isAvailable(self):
        return False