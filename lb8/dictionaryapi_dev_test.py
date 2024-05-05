import requests
import unittest


class DictionaryAPIDevTest(unittest.TestCase):

    def test_get_examples_of_usage_for_english_words(self):
        words = ['apple', 'banana', 'cat', 'dog', 'elephant']
        for word in words:
            response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}')
            data = response.json()
            self.assertTrue(response.status_code == 200)
            self.assertTrue('meanings' in data)
            self.assertIsInstance(data['meanings'], list)


if __name__ == '__main__':
    unittest.main()
