import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()


def test_google_title(browser):
    browser.get("https://www.google.com")

    assert "Google" in browser.title


def test_google_elements(browser):
    browser.get("https://www.google.com")

    assert browser.find_element_by_id("hplogo").is_displayed()
    assert browser.find_element_by_name("q").is_displayed()
    assert browser.find_element_by_name("btnK").is_displayed()
    assert browser.find_element_by_link_text("Gmail").is_displayed()
