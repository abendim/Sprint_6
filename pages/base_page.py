from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from locators.base_page_locators import BasePageLocators 


class BasePage(BasePageLocators):

    def __init__(self, driver):
        self.driver = driver
    
    def find_and_click(self, locator):
        self.find_element(locator).click()

    def find_and_send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def wait_element_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))
    
    def wait_element_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step('Нажать на кнопку логотипа Яндекса')
    def click_scooter_logo(self):
        self.find_and_click(self.scooter_logo_locator)

    @allure.step('Нажать на кнопку логотипа Самоката')
    def click_yandex_logo(self):
        self.find_and_click(self.yandex_logo_locator)

    @allure.step('Нажать на кнопку подтверждения куки')
    def click_cookie_confirm_button(self):
        self.find_and_click(self.cookie_confirm_button_locator)

    @allure.step('Проверить отображение страницы главной страницы при клике на логотип самоката')
    def check_scooter_logo_click_page(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url
    
    @allure.step('Проверить отображение страницы Яндекса при клике на логотип Яндекса')
    def check_yandex_logo_click_page(self):
        actual_url = self.driver.current_url
        assert "yandex.kz" in actual_url

    def wait_to_new_yandex_window_opened(self, timeout=5):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, timeout).until(EC.url_contains("yandex.kz"))

