import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()


def test_architectural_landmarks_count(browser):
    browser.get("https://example.com/architectural_landmarks")

    landmarks_list = browser.find_elements_by_css_selector(".architectural-landmark")
    assert len(landmarks_list) > 20
