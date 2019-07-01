This is the first kata where we test-drive by emulating hardware.  We want to create a class that wraps the two LEDs from the previous kata (green and red).  This class represents the availability of a phone booth in The Forge.  We will turn on the green LED only when the booth is available, and will turn on the red LED only when the booth is occupied.  This class will have methods set the state of the phone booth: setAvailable() and setOccupied().

This kata requires that you install the [esp32-machine-emulator package](https://pypi.org/project/esp32-machine-emulator/) from PyPi.

The author of this kata is also the author of the esp32-machine-emulator package.  Take a look at the [source code](https://github.com/tflander/esp32-machine-emulator) for the esp32-machine-emulator package.  The solution for this kata is the (LED Pin-Out Example)[https://github.com/tflander/esp32-machine-emulator/blob/master/exampleTest/test_ledPinOutExample.py]

You can also look in the kata solutions folder.
