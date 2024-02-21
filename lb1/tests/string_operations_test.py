import unittest
from string_operations import is_palindrome, is_anagram


class TestStringOperations(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("hello"))

    def test_is_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertFalse(is_anagram("hello", "world"))


if __name__ == '__main__':
    unittest.main()
