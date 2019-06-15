import pytest

from fizzbuzz import FizzBuzz
fizzBuzz = FizzBuzz()

class TestFizzBuzz(object):

    def test_one(self):
        assert fizzBuzz.answer(1) == "1"

    def test_two(self):
        assert fizzBuzz.answer(2) == "2"

    def test_three(self):
        assert fizzBuzz.answer(3) == "Fizz"

    def test_five(self):
        assert fizzBuzz.answer(5) == "Buzz"

    def test_six(self):
        assert fizzBuzz.answer(6) == "Fizz"

    def test_ten(self):
        assert fizzBuzz.answer(10) == "Buzz"

    def test_fifteen(self):
        assert fizzBuzz.answer(15) == "FizzBuzz"

    def test_thirty(self):
        assert fizzBuzz.answer(30) == "FizzBuzz"
