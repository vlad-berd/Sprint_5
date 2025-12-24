from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *
from locators import Locators


class TestConstructorMenuNavigation:
    
    def test_navigate_to_sauces_section_success(self, driver):
        """Проверка перехода к разделу 'Соусы'"""
        driver.get(BASE_URL)

        driver.find_element(*Locators.TAB_SAUCES).click()
        section_text = driver.find_element(*Locators.SECTION_SELECTED_CONSTRUCTOR).text

        assert section_text == "Соусы"
    
    def test_navigate_to_toppings_section_success(self, driver):
        """Проверка перехода к разделу 'Начинки'"""
        driver.get(BASE_URL)

        driver.find_element(*Locators.TAB_TOPPINGS).click()
        section_text = driver.find_element(*Locators.SECTION_SELECTED_CONSTRUCTOR).text

        assert section_text == "Начинки"
    
    def test_navigate_to_breads_section_success(self, driver):
        """Проверка перехода к разделу 'Булки'"""
        driver.get(BASE_URL)
        driver.find_element(*Locators.TAB_SAUCES).click()

        driver.find_element(*Locators.TAB_BREADS).click()
        is_text_in_element = WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(Locators.SECTION_SELECTED_CONSTRUCTOR, "Булки"))

        assert is_text_in_element == True
