# Note: ignore the error "Unable to import machine" for now.  This happens because the machine module exists 
# only on the ESP32 chip, and not in the local programming environment (in my case, Visual Studio Code).
# We will fix this error in a future kata.  For now, be assured (and verify) that the inport error does not 
# occur when the code is uploaded to the ESP32
import machine

greenLed = machine.Pin(22, machine.Pin.OUT)
redLed = machine.Pin(21, machine.Pin.OUT)
