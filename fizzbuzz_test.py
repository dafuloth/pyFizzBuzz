import fizzbuzz
import unittest

class Test_FizzBuzz(unittest.TestCase):
  def test_fizzbuzz(self):
    self.assertEqual(fizzbuzz.Fizzbuzz(15), "FizzBuzz")
    self.assertEqual(fizzbuzz.Fizzbuzz(9), "Fizz")
    self.assertEqual(fizzbuzz.Fizzbuzz(10), "Buzz")
    self.assertEqual(fizzbuzz.Fizzbuzz(11), 11)
    