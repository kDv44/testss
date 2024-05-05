import requests
import unittest


class BankHolidaysTest(unittest.TestCase):

    def test_get_bank_holidays(self):
        response = requests.get('https://www.gov.uk/bank-holidays.json')
        data = response.json()
        self.assertTrue(response.status_code == 200)
        self.assertIsInstance(data['EnglandAndWales'], dict)
        self.assertIsInstance(data['Scotland'], dict)
        self.assertIsInstance(data['NorthernIreland'], dict)

    def test_get_easter_date(self):
        response = requests.get('https://www.gov.uk/bank-holidays.json')
        data = response.json()
        easter_date = next(
            event['date'] for event in data['EnglandAndWales']['events'] if event['title'] == 'Easter Monday')
        self.assertTrue(response.status_code == 200)
        self.assertIsInstance(easter_date, str)


if __name__ == '__main__':
    unittest.main()
