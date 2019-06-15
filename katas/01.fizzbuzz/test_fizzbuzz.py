import pytest

### Step one:  Run this test through pytest to verify you have python setup with pytest

### Step two:  Uncomment the following two lines and get them to compile by updating the 
# production code in fizzbuzz.py.  Note Uncle Bob's rule that you are not allowed to write 
# any more of a unit test than is sufficient to fail; and compilation failures are failures.
# from fizzbuzz import FizzBuzz
# fizzBuzz = FizzBuzz()

class TestClass(object):
    def test_one(self):

        ### Step three:  Remove the "pass" statement and uncomment the assertion that the answer to 1 is "1".
        # This will cause a compile error.  Fix the compile error in the production code.  Write the simplest
        # code possible to make the test pass.  You might want to first return an incorrect value to verify 
        # that the test runs red (failure) when the production code is not behaving correctly.
        pass
        # assert fizzBuzz.answer(1) == "1"

### Step four:  Continue the TDD cycle (red, green, refactor) until you are satified that the code is complete.