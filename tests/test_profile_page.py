import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *
from locators import Locators


class TestCheckingAccessPersonalAccount:

    def test_click_personal_account_button_redirects_personal_account_page_success(self, login):
        """Проверка перехода на страницу Личный Кабинет по клику на 'Личный кабинет'."""
        driver = login

        driver.find_element(*Locators.PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_changes(driver.current_url))

        assert driver.current_url == PROFILE_URL

class TestPersonalAccount:

    @pytest.mark.parametrize("locator_button", [Locators.CONSTRUCTOR_BUTTON, Locators.LOGO_BUTTON])
    def test_navigate_from_personal_account_to_constructor_success(self, login, locator_button):
        """Проверка перехода из личного кабинета в конструктор."""
        driver = login
        driver.find_element(*Locators.PERSONAL_CABINET_BUTTON).click()

        driver.find_element(*locator_button).click()

        assert driver.current_url == BASE_URL
    
    def test_account_logout_success(self, login):
        """Проверка выхода по кнопке 'Выйти' в личном кабинете"""
        driver = login
        driver.find_element(*Locators.PERSONAL_CABINET_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SIGNOUT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PERSONAL_CABINET_BUTTON)).click()

        assert driver.current_url == LOGIN_URL
