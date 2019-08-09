# MicroPython Firmware

## Why MicroPython?

### MicroPython Advantages over C/C++

 - **Ease of programming**.  This translates into real cost savings as code gets developed quicker.
 - **Memory management / Garbage Collection**.  Common C/C++ code problems such as memory leaks and buffer overruns are eliminated, resulting in more time spend coding functionality and less time debugging.
 - **The REPL**.  The MicroPython ecosystem gives you the ability to do command-line interaction with the hardware.  This allows you to quickly explore library functionality interactivly, allowing you to develop working code faster.  It also encourages good code design, because your code needs to be well organized in order to be useful using a command-line tool.
 - **Fast Build Cycle**.  Rather than building and uploading binary files, you just upload source code.  Not only do you have zero build time, but the source code is an order of magnitude smaller and faster to upload.
 - **Popular In General**.  While C/C++ continues to dominate embedded systems, Python is a more popular language for computer science students.  It's also the fastest growing non-C/C++ language used for embedded systems.
 - **Fast Enough Runtime**.  Because Python is interpreted, you are not likely to achive the blazing speed of native code compiled from C/C++.  In the IoT relm, however, your speed bottle-necks are not likely to be on-chip processing.  They are far more likely to be related to network traffic and actuator response (how fast hardware can respond to commands).
 - **Maturing Ecosytem**. Advancements such as CPython and JIT compilers are beginning to close the gap between C speed and Python speed.  

### C/C++ Advantages over MicroPython

 - **Quick Start Up**.  You can install the Arduino ecosystem and flash code on devices out-of-the-box.  No need to load special firmware.
 - **Blazing Speed**.  Natively compiled code is almost always going to execute faster than interpreted code.
 - **Real Time Predictability**. Since programmers are responsible for memory management, there are no unpredictible garbage collection cycles.
 - **Popular In Embedded Systems**.  Until relatively recently, C/C++ was the only choice for embedded system programming.  It remains by far the most popular choice today.
 - **Good Enough Serial Monitoring**. While you don't get the power of a Python REPL, you can interact with the device using a serial monitor. 

## Background
The ESP-32 dev boards come ready to upload binary code out-of-the-box.  You can create binary code using the Arduino ecosystem or a C/C++ compiler.  We are using MicroPython, so we need special firmware that includes the micropython ecosystem.

There are many MicroPython firmware builds, and you are free to build your own.  There are two common ones.  You can almost always use the official MicroPython [ESP-32 Firmware](http://micropython.org/download). 

To find this link, google `esp32 micropython firmware`

Scroll down or search for `Firmware for ESP32 boards`

The official MicroPython firmware is like the Arduino libraries.  They design goal is not to fully expose the capabilities of the ESP-32, but rather to provide some cross-compatibility between chips in order to make your code portable.

To fully support the ESP-32 chip using MicroPython, you can play with [LoBo MicroPython for ESP-32](https://loboris.eu/forum/index.php)

LoBo is built on the official MicroPython firmware for ESP-32, but adds capabilities found in the ESP-IDF libraries.

ESP-IDF is the official development framework for the ESP-32.  If you are using C/C++, you can use ESP-IDF as an alternative to the Arduino libraries to fully exploit the capabilities of the chip.

