"""
The purpose of this module is to emulate the machine module of the ESP32 chip.  The primary reason to 
emulate the chip is for test-driving code (TDD).

Firmware version: esp32-20190610-v1.11-37-g62f004ba4
"""
import time
EMULATION_MODE = True

__version__ = '0.0.0'
__author__ = 'Todd Flanders https://github.com/tflander/Esp32IotKata'
__license__ = "Apache License 2.0. https://www.apache.org/licenses/LICENSE-2.0"

expectedPulseTimeForTesting = 0
expectedPulseTimeErrorForTesting = None

def resetExpectationsForTesting():
    global expectedPulseTimeForTesting, expectedPulseTimeErrorForTesting
    expectedPulseTimeForTesting = 0
    expectedPulseTimeErrorForTesting = None

# TODO: understand unknownParameter
def time_pulse_us(echoPin, unknownParameter, echo_timeout_us):
    global expectedPulseTimeErrorForTesting
    if expectedPulseTimeErrorForTesting is not None:
        raise expectedPulseTimeErrorForTesting
    return expectedPulseTimeForTesting

def sleep_us(delayUs):
    pass

time.sleep_us = sleep_us

class Pin:
    IN = "in"
    OUT = "out"
    pinForTesting = None
    currentState = None

    def __init__(self, pin, mode=OUT, pull=None):
        self.pinForTesting = pin

    def on(self):
        # self.currentState = "on"
        self.currentState = 1

    def off(self):
        # self.currentState = "off"
        self.currentState = 0

    def value(self, newValue=None):
        if newValue == 0:
            self.off()
        elif newValue == 1:
            self.on()
        return self.currentState

