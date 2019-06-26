from hcsr04 import HCSR04

class BoothInUseDetector:
    
    def __init__(self, trigger_pin, echo_pin, expectedDistanceCm, distanceTolerance, retriesToChangeState):
        # self.objectDetector = SonarBoothObjectDetector(trigger_pin=trigger_pin, echo_pin=echo_pin,expectedDistanceCm=expectedDistanceCm,distanceTolerance=distanceTolerance)
        self.retriesToChangeState = retriesToChangeState
        self.currentState = False
        self.sampleCount = 0
        self.sonar = HCSR04(trigger_pin, echo_pin)
        self.expectedDistanceCm = expectedDistanceCm
        self.distanceTolerance = distanceTolerance
        self.error = None

    def isAvailable(self):
        return self.currentState

    def sample(self):

        candidateStateChange = self.singleScan()

        # TODO: replace with debug logging
        # print(self.sampleCount, candidateStateChange, self.currentState)

        if(candidateStateChange == self.currentState):
            self.sampleCount = 0
            # print("resetting")
        else:
            self.sampleCount = self.sampleCount + 1
            if self.sampleCount >= self.retriesToChangeState:
                self.currentState = candidateStateChange
                # print("stateChange triggered")
        return candidateStateChange

    def singleScan(self):

        try:
            distanceCm = int(round(self.sonar.distance_cm()))
        except OSError as ex:
            if ex.args[0] == 'Out of range':
               self.error = 'Out of sonar range'
               return False

        isAvailable = distanceCm >= self.expectedDistanceCm - self.distanceTolerance and distanceCm <= self.expectedDistanceCm + self.distanceTolerance

        self.error = None
        if distanceCm > self.expectedDistanceCm + self.distanceTolerance:
            self.error = "object out of range"

        return isAvailable
