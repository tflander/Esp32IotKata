class SonarBoothWallDetector:
    
    isAvalable = True
    sonar = None
    
    def __init__(self, trigger_pin, echo_pin, expectedDistanceCm, distanceTolerance, numReadsToChangeState):
        self.sonar = "stub"