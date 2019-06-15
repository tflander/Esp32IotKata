# The MicroPython REPL

REPL stands for Read-Eval-Print Loop.  

Most modern programming language have a REPL.  This allows programmers to evaluate single programming statements and observe the results.  This is really handy for IoT, because you might want to run a simple command to verify that the circuit is wired properly.

The purpose of this kata is to verify your setup for a known good circuit.  You will connect to the device and flip LEDs on and off.

No programming is necessary for this kata.  You will connect to the REPL via USB, upload the program main.py, then run commands to turn the LEDs on and off.

There is nothing interesting in the solutions folder for this kata.

I have the pycom extension in Visual Studio Code to make uploading to the ESP32 easy.  It also gives me a terminal for the REPL on-chip.

After uploading main.py to the ESP32, you get two objects defined and available in the REPL: greenLed and redLed.  These objects have two methods of interest: off() and on().  You can set the LED states using any of the following commands:

greenLed.on()
greenLed.off()
redLed.on()
redLed.off()

You can also use code completion in the REPL.  Hit g-tab to see the variable for the green LED, and r-tab to see the variable for the red LED.

You can also introspect objects by typeing the object name, dot, then hitting tab.

You can also load and run other python modules in the REPL.  To list the files uploaded to the ESP32, run these commands:

import os
os.listdir()

To show the content of the main.py file you uploaded, run these commands:

f = open('main.py')
f.read()
f.close()
