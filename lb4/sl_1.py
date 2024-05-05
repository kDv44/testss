from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_driver_path = '**\\selenium\\chromedriver_114.0.5735.90.exe'

options = Options()

options.binary_location = "**\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')

def run_test():
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    try:
        driver.get('https://automationexercise.com/')
        driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()
        WebDriverWait(driver, 5).until(EC.title_is('Automation Exercise - Signup / Login'))

        driver.find_element(By.NAME, 'email').send_keys('test_mail')
        driver.find_element(By.NAME, 'password').send_keys('test_pass', Keys.RETURN)

        WebDriverWait(driver, 5).until(EC.title_is('Automation Exercise'))

        user_name = driver.find_element(By.CSS_SELECTOR, '#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(10) > a > b').text
        print("User:", user_name)
        if 'Andrii' not in user_name:
            raise AssertionError("User's name does not match the expected.")

    except Exception as e:
        print('An error occurred:', e)
    finally:
        print('Everything is fine here, exiting.')

run_test()
