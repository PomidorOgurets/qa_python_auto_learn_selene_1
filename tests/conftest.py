from selene import browser
from selenium import webdriver
import pytest


@pytest.fixture(scope="function", autouse=True)
def browser_settings():
    browser.config.base_url = ("https://demoqa.com/automation-practice-form")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver

    yield

    browser.quit()