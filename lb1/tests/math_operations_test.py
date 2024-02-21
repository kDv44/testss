import unittest
from math_operations import addition, subtraction, multiplication, division


class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(3, 4), 7)
        self.assertEqual(addition(-3, 4), 1)
        self.assertEqual(addition(3.5, 2.5), 6)

    def test_subtraction(self):
        self.assertEqual(subtraction(3, 4), -1)
        self.assertEqual(subtraction(-3, 4), -7)
        self.assertEqual(subtraction(3.5, 2.5), 1)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 4), 12)
        self.assertEqual(multiplication(-3, 4), -12)
        self.assertEqual(multiplication(3.5, 2.5), 8.75)

    def test_division(self):
        self.assertEqual(division(8, 4), 2)
        self.assertEqual(division(-8, 4), -2)
        self.assertEqual(division(10, 3), 10 / 3)
        self.assertRaises(ValueError, division, 10, 0)


if __name__ == '__main__':
    unittest.main()
