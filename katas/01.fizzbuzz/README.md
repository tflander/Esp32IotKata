# FizzBuzz

The purpose of this Kata is to verify the development environment for test-driving Python.  A future Kata will verify the environment to test-drive MicroPython on the ESP32.

This may also be an introduction to Python and/or an introduction to test driving software.  If this is your first time doing Python, you might want to look at some Python tutorials on the internet.  Simarly, if this is your first time doing test-driven development (TDD), you might want to do the same.

If this is your first time using pytest (it was for me), you might want to read up on it.  You are also free to look in the solution folder to learn.  It's not cheating, it's learning.  You can always repeat the kata without referring to the solution.

Install python3, pytest and any other necessary dependencies.  TODO: should there be a series of steps here, or 
should this kata emphasize hacking skills?

I use Visual Studio Code for Python development.  You are free to set up your environment as you choose.  I also have the pytest Extension installed for Visual Studio Code.  You are free to run pytest however you want.

Write a method or function that takes a number, and returns the number as a string with the following exceptions:

- For each multiple of 3, print "Fizz" instead of the number. 
- For each multiple of 5, print "Buzz" instead of the number. 
- For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

Be sure to follow the rules of TDD per Uncle Bob:

 - You are not allowed to write any production code unless it is to make a failing unit test pass.
 - You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.
 - You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

