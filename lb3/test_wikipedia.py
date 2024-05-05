import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()


def test_wikipedia_elements(browser):
    browser.get("https://uk.wikipedia.org")

    search_input = browser.find_element_by_name("search")
    search_input.send_keys("Київ")
    search_input.send_keys(Keys.RETURN)

    assert browser.find_element_by_css_selector("img[alt='Герб Києва']").is_displayed()
    assert browser.find_element_by_xpath("//th[contains(text(), 'Населення')]").is_displayed()
    assert browser.find_element_by_xpath("//th[contains(text(), 'Температура')]").is_displayed()
    assert browser.find_element_by_link_text("Епідемія коронавірусу").is_displayed()
    assert browser.find_element_by_xpath("//th[contains(text(), 'Густина населення')]").is_displayed()
