from hcsr04 import HCSR04

class SonarBoothObjectDetector:
        
    def __init__(self, trigger_pin, echo_pin, expectedDistanceCm, distanceTolerance):
        self.sonar = HCSR04(trigger_pin, echo_pin)
        self.expectedDistanceCm = expectedDistanceCm
        self.distanceTolerance = distanceTolerance
        self.error = None

    def isObjectDetected(self):

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
