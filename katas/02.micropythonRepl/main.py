try:
    # this works if we are running code on-chip
    import machine
except:
    # this works if we are testing on a dev workstation.  
    # if the import fails, pip install esp32-machine-emulator
    import esp32_machine_emulator.machine as machine

greenLed = machine.Pin(22, machine.Pin.OUT)
redLed = machine.Pin(21, machine.Pin.OUT)
