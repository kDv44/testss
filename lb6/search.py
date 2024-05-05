from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import unittest


class GoogleSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.headless = True
        cls.driver = webdriver.Firefox(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_google_logo_present(self):
        self.driver.get('https://www.google.com')
        logo = self.driver.find_element(By.ID, 'hplogo')
        self.assertTrue(logo.is_displayed())

    def test_search_button_visible_and_clickable(self):
        search_button = self.driver.find_element(By.NAME, 'btnK')
        self.assertTrue(search_button.is_displayed())
        self.assertTrue(search_button.is_enabled())


if __name__ == '__main__':
    unittest.main()
