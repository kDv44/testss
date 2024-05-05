from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = '**\\selenium\\chromedriver_114.0.5735.90.exe'

options = webdriver.ChromeOptions()
options.binary_location = "**\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument("--start-maximized")

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
        await driver.find_element(By.CSS_SELECTOR, 'a[href="/product_details/2"]').click()

        await driver.wait(until.element_located((By.CSS_SELECTOR, '.btn.btn-default.cart')), 10).click()
        await driver.wait(until.element_located((By.CSS_SELECTOR, '.modal-content')), 5)

        await driver.sleep(1.5)
        await driver.find_element(By.CSS_SELECTOR, '.modal-content a[href="/view_cart"]').click()

        await driver.wait(until.element_located((By.CSS_SELECTOR, '.btn.btn-default.check_out')), 5)
        product_name = await driver.find_element(By.CSS_SELECTOR, '.cart_description a').text
        product_price = await driver.find_element(By.CSS_SELECTOR, '.cart_total_price').text
        print("Product in cart:", product_name)
        print("Price of product:", product_price)

        if product_name == "Men Tshirt" and product_price.strip() == "Rs. 400":
            print("Test Passed: Product name and price are correct.")
        else:
            print("Test Failed: Incorrect product name or price.")

        await driver.get('https://automationexercise.com/product_details/2')
        await driver.wait(until.element_located((By.CSS_SELECTOR, '.btn.btn-default.cart')), 10).click()
        await driver.wait(until.element_located((By.CSS_SELECTOR, '.modal-content')), 5)

        await driver.sleep(1.5)
        await driver.find_element(By.CSS_SELECTOR, '.modal-content a[href="/view_cart"]').click()
        await driver.sleep(1.5)
        await driver.wait(until.element_located((By.CSS_SELECTOR, '.btn.btn-default.check_out')), 5)

        total = await driver.find_element(By.CSS_SELECTOR, '.cart_total_price').text
        print("Total for 2 items:", total)

        if total.strip() == "Rs. 800":
            print("Test Passed: Total price is correct for 2 items.")
        else:
            print("Test Failed: Total price is incorrect.")
    except Exception as e:
        print('An error occurred:', e)
    finally:
        print('Everything is fine here, exiting.')


await run_test()
