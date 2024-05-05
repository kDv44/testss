import requests
import unittest


class CurrencyAPITest(unittest.TestCase):

    def test_get_available_currencies(self):
        response = requests.get('https://api.fawazahmed0.me/currency/list')
        data = response.json()
        self.assertTrue(response.status_code == 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['currencies'], list)

    def test_get_exchange_rate_euro_to_other_currencies(self):
        response = requests.get('https://api.fawazahmed0.me/currency/convert/EUR')
        data = response.json()
        self.assertTrue(response.status_code == 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['rates'], dict)

    def test_get_exchange_rate_euro_to_dollar(self):
        response = requests.get('https://api.fawazahmed0.me/currency/convert/EUR/USD')
        data = response.json()
        self.assertTrue(response.status_code == 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['rate'], float)

    def test_get_non_existing_currency(self):
        response = requests.get('https://api.fawazahmed0.me/currency/convert/ABC')
        self.assertTrue(response.status_code == 404)


if __name__ == '__main__':
    unittest.main()
