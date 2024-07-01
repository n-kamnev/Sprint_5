from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellaBurgersLocators
from data import StellaBurgerTestData
import urls


class TestTransitionFromToConstructor:
    def test_transition_click_button_constructor(self, driver):
        """Проверка перехода по клику на «Конструктор»"""
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.AUTH_EMAIL_INPUT).send_keys(StellaBurgerTestData.AUTH_EMAIL)
        driver.find_element(*StellaBurgersLocators.AUTH_PASSWORD_INPUT).send_keys(StellaBurgerTestData.AUTH_PASSWORD)
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellaBurgersLocators.COLLECT_BURGER_TEXT))
        expected_url = driver.current_url
        assert expected_url == urls.MAIN_PAGE_URL

    def test_transition_click_logo(self, driver):
        """Проверка перехода по клику на логотип Stellar Burgers"""
        driver.find_element(*StellaBurgersLocators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.AUTH_EMAIL_INPUT).send_keys(StellaBurgerTestData.AUTH_EMAIL)
        driver.find_element(*StellaBurgersLocators.AUTH_PASSWORD_INPUT).send_keys(StellaBurgerTestData.AUTH_PASSWORD)
        driver.find_element(*StellaBurgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.PERSONAL_CABINET_BUTTON).click()
        driver.find_element(*StellaBurgersLocators.LOGO_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(StellaBurgersLocators.COLLECT_BURGER_TEXT))
        expected_url = driver.current_url
        assert expected_url == urls.MAIN_PAGE_URL
