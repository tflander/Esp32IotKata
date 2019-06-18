This is the first kata where we test-drive by emulating hardware.  We want to create a class that wraps the two LEDs from the previous kata (green and red).  This class represents the availability of a phone booth in The Forge.  We will turn on the green LED only when the booth is available, and will turn on the red LED only when the booth is occupied.  This class will have methods set the state of the phone booth: setAvailable() and setOccupied().

Take a look at machine_emulator.py

```
try:
    import machine
except:
    from machine_emulator import machine
```
