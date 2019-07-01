from hcsr04UltrasonicDistanceSensor import Hcsr04UltrasonicDistanceSensor

class BoothOccupancyDetector:
    
    def __init__(self, triggerPin, echoPin, wallDistanceCm, tolaranceCm):
        self.sensor = Hcsr04UltrasonicDistanceSensor(triggerPin=triggerPin, echoPin=echoPin)
        self.wallDistanceCm = wallDistanceCm
        self.tolaranceCm = tolaranceCm

    def findWall(self):
        distance = self.sensor.distanceCm()
        return distance >= self.wallDistanceCm - self.tolaranceCm