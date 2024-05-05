from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

async def test_google_home_page():
    firefox_options = Options()
    firefox_options.headless = True
    driver = webdriver.Firefox(options=firefox_options)

    try:
        driver.get('https://www.google.com')

        driver.find_element(By.ID, 'hplogo')

        driver.find_element(By.NAME, 'q')

        driver.find_element(By.NAME, 'btnK')

        try:
            driver.find_element(By.NAME, 'btnSearch')
            print('Test 4 passed, button found')
        except:
            print('Test 4 failed, button not found')

        driver.find_element(By.NAME, 'btnI')

        title = driver.title
        if title == "Google Search":
            print('Test 6 passed, correct title')
        else:
            raise Exception('Test 6 failed, incorrect title')

    except Exception as e:
        print('An error occurred:', e)
    finally:
        driver.quit()
        print('Test completed, browser closed.')

await test_google_home_page()
