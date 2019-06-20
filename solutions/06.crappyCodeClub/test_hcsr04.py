from hcsr04 import HCSR04

class TestSomething:

    def test_something(self):
        sensor = HCSR04(trigger_pin=2, echo_pin=15)
        distance = sensor.distance_cm()
        print(distance)
