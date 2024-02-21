import unittest
from array_utils import sum_array, filter_positive_numbers, filter_negative_numbers


class TestArrayUtils(unittest.TestCase):

    def setUp(self):
        self.test_array = [-2, -1, 0, 1, 2]

    def test_sum_array(self):
        self.assertEqual(sum_array(self.test_array), 0)

    def test_filter_positive_numbers(self):
        self.assertEqual(filter_positive_numbers(self.test_array), [1, 2])

    def test_filter_negative_numbers(self):
        self.assertEqual(filter_negative_numbers(self.test_array), [-2, -1])


if __name__ == '__main__':
    unittest.main()
