import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *
from locators import Locators
from data import ExpectedValueConstructor as EVC


class TestConstructorMenuNavigation:
    
    @pytest.mark.parametrize("tab, expected_value", [(Locators.TAB_SAUCES, EVC.text_tab_sauces), (Locators.TAB_TOPPINGS, EVC.text_tab_toppings)])
    def test_section_navigation_success(self, driver, tab, expected_value):
        """Проверка переходов между разделами"""
        driver.get(BASE_URL)

        driver.find_element(*tab).click()
        section_text = driver.find_element(*Locators.SECTION_SELECTED_CONSTRUCTOR).text

        assert section_text == expected_value
    
    def test_navigate_to_breads_section_success(self, driver):
        """Проверка перехода к разделу 'Булки'"""
        driver.get(BASE_URL)
        driver.find_element(*Locators.TAB_SAUCES).click()

        driver.find_element(*Locators.TAB_BREADS).click()
        is_text_in_element = WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(Locators.SECTION_SELECTED_CONSTRUCTOR, EVC.text_tab_breads))

        assert is_text_in_element == True
