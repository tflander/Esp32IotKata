# Crappy Code Club Refactoring Excercise

##Refactoring decisions

`hcsr04.py` - I didn't author this code, so I'm not going to clean or test protect it.  I would do so if I find the code is buggy or needs to be extended.  For now, I'll leave it alone.

low-level networking code - functions `wifiConnect()`, `apConnect()`, `startListener()` - I'm going to just move them to `boot.py` for now.  It seems this is boilerplate code that doesn't belong in `main.py`.

The code for the green and red led is the same code that we test-drove in a previous kata.  Let's re-use the test-driven code and delete the duplication.

The function `measureDistance()` is doing a lot.  It potentially uses the timer, handles global data from the main thread, reads the sensor, handles re-try logic, decides if we might have a state change (occupied to available or available to occupied), decides if the state change is real, and flips the LEDs if the state change is real.  Let's break it up and see what we get.  Once we have a bunch of small pieces of logic, we can decide how we want to put the logic together.

First, let's separate the timer lambda definition from the function that does stuff.

Now, let's test-drive a class that detects if the state of the booth changed.  Most of the code will move to this class.  

On second thought, that's too big.  Lets make a class that wraps the sonar detector and detects if it sees the back of the wall.  It will take multiple readings to make sure it got the answer right.

Whoops!  Still too big.  We need to be able to set expectations on the hcsr04 sonar detector.  The code I downloaded from the internet doesn't even compile.  Time to do the work I was trying to avoid and make a hcrsr04 detector that can be emulated in tests.