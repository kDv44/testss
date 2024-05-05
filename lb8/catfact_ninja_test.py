import requests
import unittest


class CatFactNinjaTest(unittest.TestCase):

    def test_get_random_cat_fact(self):
        response = requests.get('https://catfact.ninja/fact')
        data = response.json()
        self.assertTrue(response.status_code == 200)
        self.assertIsInstance(data['fact'], str)

    def test_get_multiple_random_cat_facts(self):
        response = requests.get('https://catfact.ninja/facts?limit=5')
        data = response.json()
        self.assertTrue(response.status_code == 200)
        self.assertIsInstance(data['data'], list)

    def test_get_random_cat_fact_with_max_length(self):
        response = requests.get('https://catfact.ninja/fact?max_length=50')
        data = response.json()
        self.assertTrue(response.status_code == 200)
        self.assertLessEqual(len(data['fact']), 50)

    def test_check_response_headers(self):
        response = requests.get('https://catfact.ninja/fact')
        self.assertTrue(response.status_code == 200)
        self.assertIn('server', response.headers)
        self.assertIn('cache-control', response.headers)
        self.assertIn('date', response.headers)
        self.assertIsInstance(response.headers['server'], str)
        self.assertIsInstance(response.headers['cache-control'], str)
        self.assertIsInstance(response.headers['date'], str)


if __name__ == '__main__':
    unittest.main()
