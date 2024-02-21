import unittest
from unittest.mock import MagicMock
from custom_functions import (
    contains_object,
    contains_word,
    contains_field,
    apply_callback,
    text_to_words,
    Person
)


class TestCustomFunctions(unittest.TestCase):

    def test_contains_object(self):
        self.assertTrue(contains_object([1, 2, 3], 2))
        self.assertFalse(contains_object(["a", "b", "c"], "d"))

    def test_contains_word(self):
        self.assertTrue(contains_word("hello world", "world"))
        self.assertFalse(contains_word("hello world", "python"))

    def test_contains_field(self):
        obj = Person("John", "Doe")
        self.assertTrue(contains_field(obj, "first_name"))
        self.assertFalse(contains_field(obj, "age"))

    def test_apply_callback(self):
        mock_callback = MagicMock()
        apply_callback([1, 2, 3], mock_callback)
        mock_callback.assert_any_call(1)
        self.assertEqual(mock_callback.call_count, 3)

    def test_text_to_words(self):
        mock_callback = MagicMock()
        text_to_words("hello world", mock_callback)
        mock_callback.assert_called_with(["hello", "world"])


if __name__ == '__main__':
    unittest.main()
