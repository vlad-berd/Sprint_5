from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *
from locators import Locators
from data import Credentials, ExpectedValueConstructorPage as EVCP, ExpectedValueLoginPage as EVLP


class TestLoginWithExistingCredentials:

    def test_login_success(self, driver):
        """Проверка аунтефикации пользователя."""
        driver.get(LOGIN_URL)
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        result_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON)).text

        assert result_text == EVCP.text_order_button
        assert driver.current_url == BASE_URL

class TestCheckingLoginButtons:

    def test_click_log_in_account_button_on_main_page_redirects_to_login_success(self, driver):
        """Проверка перехода на страницу Login по кнопке 'Войти в аккаунт' на главной."""
        driver.get(BASE_URL)

        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        result_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON)).text

        assert result_text == EVLP.text_link_login
        assert driver.current_url == LOGIN_URL

    def test_click_personal_cabinet_button_redirects_to_login_success(self, driver):
        """Проверка перехода на страницу Login по кнопке 'Личный Кабинет'."""
        driver.get(BASE_URL)

        driver.find_element(*Locators.PERSONAL_CABINET_BUTTON).click()
        result_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON)).text

        assert result_text == EVLP.text_link_login
        assert driver.current_url == LOGIN_URL
    
    def test_click_log_in_via_button_registration_form_redirects_to_login_success(self, driver):
        """Проверка перехода на страницу Login через кнопку в форме регистрации."""
        driver.get(REGISTER_URL)

        driver.find_element(*Locators.LINK_LOGIN).click()
        result_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON)).text

        assert result_text == EVLP.text_link_login
        assert driver.current_url == LOGIN_URL
    
    def test_click_log_in_button_in_password_recovery_redirects_to_login_success(self, driver):
        """Проверка перехода на страницу Login через кнопку в форме восстановления пароля."""
        driver.get(FORGOT_PASSWORD_URL)

        driver.find_element(*Locators.LINK_LOGIN).click()
        result_text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON)).text

        assert result_text == EVLP.text_link_login
        assert driver.current_url == LOGIN_URL
