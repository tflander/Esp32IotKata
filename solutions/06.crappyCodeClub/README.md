# Crappy Code Club Refactoring Excercise

##Refactoring decisions

`hcsr04.py` - I didn't author this code, so I'm not going to clean or test protect it.  I would do so if I find the code is buggy or needs to be extended.  For now, I'll leave it alone.

low-level networking code - functions `wifiConnect()`, `apConnect()`, `startListener()` - I'm going to just move them to `boot.py` for now.  It seems this is boilerplate code that doesn't belong in `main.py`.

The code for the green and red led is the same code that we test-drove in a previous kata.  Let's re-use the test-driven code and delete the duplication.