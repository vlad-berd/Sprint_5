from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *
from helper import generate_registration_data
from locators import Locators
from data import Credentials


class TestRegistrationWithNewCredentials:

    def test_registration_success(self, driver):
        """Проверка успешной регистрации пользователя."""
        driver.get(REGISTER_URL)
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()
        result_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON)).text

        assert result_text == "Войти"
        assert driver.current_url == LOGIN_URL

    def test_registration_password_with_five_symbols_show_error_text(self, driver):
        """Проверка отображения ошибки при некорректном поле Пароля."""
        driver.get(REGISTER_URL)
        name, email, _ = generate_registration_data()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys("12345")

        driver.find_element(*Locators.REGISTER_BUTTON).click()
        result_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_REG_MESSAGE_PASSWORD)).text

        assert result_text == "Некорректный пароль"
        assert driver.current_url == REGISTER_URL

class TestCheckingCredentialsExistingAccount:

    def test_registration_failed(self, driver):
        """Проверка отображения ошибки при попытке зарегистрировать существующего пользователя."""
        driver.get(REGISTER_URL)
        driver.find_element(*Locators.NAME).send_keys(Credentials.name)
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()
        result_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ERROR_REG_MESSAGE_EXIST_USER)).text

        assert result_text == "Такой пользователь уже существует"
        assert driver.current_url == REGISTER_URL
