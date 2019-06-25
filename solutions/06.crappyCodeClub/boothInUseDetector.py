from sonarBoothObjectDetector import SonarBoothObjectDetector

class BoothInUseDetector:
    
    def __init__(self, trigger_pin, echo_pin, expectedDistanceCm, distanceTolerance, retriesToChangeState, sampleIntervalMs):
        self.objectDetector = SonarBoothObjectDetector(trigger_pin=trigger_pin, echo_pin=echo_pin,expectedDistanceCm=11,distanceTolerance=3)
        self.expectedDistanceCm = expectedDistanceCm
        self.distanceTolerance = distanceTolerance
        self.retriesToChangeState = retriesToChangeState
        self.sampleIntervalMs = sampleIntervalMs
        self.currentState = False
        self.sampleCount = 0

    def isAvailable(self):
        return self.currentState

    def sample(self):
        candidateStateChange = self.objectDetector.isObjectDetected()
        if(candidateStateChange == self.currentState):
            self.sampleCount = 0
        else:
            self.sampleCount = self.sampleCount + 1
            if self.sampleCount >= self.retriesToChangeState:
                self.currentState = candidateStateChange
        return candidateStateChange