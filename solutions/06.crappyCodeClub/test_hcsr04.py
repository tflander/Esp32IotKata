from hcsr04 import HCSR04
import esp32_machine_emulator.machine as machine

class TestHCSR04:

    def test_pulseTimeOf291IsFiveCm(self):
        machine.resetExpectationsForTesting()
        sensor = HCSR04(trigger_pin=2, echo_pin=15)
        machine.expectedPulseTimeForTesting = 291

        distance = sensor.distance_cm()
        assert distance == 5

    def test_pulseTimeoutErrorHandling(self):
        machine.resetExpectationsForTesting()
        sensor = HCSR04(trigger_pin=2, echo_pin=15)
        machine.expectedPulseTimeErrorForTesting = OSError(110)

        try:
            sensor.distance_cm()
            assert False,  "Expected error raised from distance_cm"
        except OSError as ex:
            assert ex.args[0] == 'Out of range'
