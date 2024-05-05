from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = '**\\webdriver-manager\\selenium\\chromedriver_114.0.5735.90.exe'
options = webdriver.ChromeOptions()
webdriver.chrome.driver = chrome_driver_path


async def run_test():
    driver = webdriver.Chrome(chrome_driver_path, options=options)

    try:
        await driver.get('https://automationexercise.com/')
        await driver.sleep(30)
        await driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()

        await WebDriverWait(driver, 5).until(EC.title_is('Automation Exercise - Signup / Login'))

        await driver.find_element(By.NAME, 'email').send_keys('test_mail')
        await driver.find_element(By.NAME, 'password').send_keys('test_pass', Keys.RETURN)

        await WebDriverWait(driver, 5).until(EC.title_is('Automation Exercise'))

        user_name = await driver.find_element(By.CSS_SELECTOR,
                                              '#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(10) > a > b').text
        print("User:", user_name)
        if 'Andrii' not in user_name:
            raise AssertionError("User's name does not match the expected.")

        await driver.find_element(By.CSS_SELECTOR, 'a[href="/products"]').click()
        await driver.sleep(3)
        await driver.find_element(By.CSS_SELECTOR, 'a[href="/product_details/1"]').click()
        await driver.sleep(3)

        product_info = await driver.find_element(By.CSS_SELECTOR, '.product-information')
        product_name = await product_info.find_element(By.CSS_SELECTOR, 'h2').text
        product_price = await product_info.find_element(By.CSS_SELECTOR, 'span span').text

        print("Product Name: ", product_name)
        print("Price: ", product_price)

    except Exception as e:
        print('An error occurred:', e)
    finally:
        print('Everything is fine here, exiting.')

await run_test()
