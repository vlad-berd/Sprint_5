import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from curl import *
from locators import Locators
from data import Credentials

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--windows-size=1600,900")
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    """Фикстура для аунтефикации пользователя."""
    driver.get(LOGIN_URL)
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    return driver
