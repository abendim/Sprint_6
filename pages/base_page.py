from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


class BasePage:

    create_order_button_on_bottom_locator = [By.XPATH, '//div[@class="Home_RoadMap__2tal_"]//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    create_order_button_on_header_locator = [By.XPATH, '//div[@class="Header_Nav__AGCXC"]//button[@class="Button_Button__ra12g"]']
    scooter_logo_locator = [By.XPATH, '//img[@alt="Scooter" and contains(@src, "scooter.svg")]']
    yandex_logo_locator = [By.XPATH, '//img[@alt="Yandex" and contains(@src, "ya.svg")]']
    cookie_confirm_button_locator = [By.ID, 'rcc-confirm-button']

    def __init__(self, driver):
        self.driver = driver

    def accordion_header_locator(self, header_id):
        return (By.XPATH, f'//*[@id="accordion__heading-{header_id}"]')

    def accordion_panel_content_locator(self, header_id):
        return (By.XPATH, f'//*[@id="accordion__panel-{header_id}"]//p')
    
    def accordion_panel_content_text(self, header_id):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.accordion_panel_content_locator(header_id))
        ).text

    @allure.step('Нажать на кнопку "Создать заказ" внизу страницы')
    def click_create_order_button_on_bottom(self):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.create_order_button_on_bottom_locator)
        ).click()

    @allure.step('Нажать на кнопку "Создать заказ" в шапке страницы')
    def click_create_order_button_on_header(self):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.create_order_button_on_header_locator)
        ).click()

    @allure.step('Проверить отображение логотипа самоката')
    def wait_scooter_logo_displayed(self):
        return self.driver.find_element(*self.scooter_logo_locator).is_displayed()
    
    @allure.step('Нажать на кнопку логотипа Яндекса')
    def click_scooter_logo(self):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.scooter_logo_locator)
        ).click()

    @allure.step('Нажать на кнопку логотипа Самоката')
    def click_yandex_logo(self):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.yandex_logo_locator)
        ).click()

    @allure.step('Нажать на аккордеон с id {header_id}')
    def click_accordion_panel(self, header_id):
        element = self.driver.find_element(*self.accordion_header_locator(header_id))
        self.driver.execute_script("arguments[0].click();", element)

    def wait_accordion_header_locator(self, header_id):
        return WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.accordion_header_locator(header_id))
        )

    def wait_accordion_panel_content_locator(self, header_id):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.accordion_panel_content_locator(header_id))
        )
    
    @allure.step('Прокрутить страницу до кнопки "Создать заказ" внизу страницы')
    def scroll_to_create_button_on_bottom(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.create_order_button_on_bottom_locator))

    def scroll_to_create_button_on_header(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.create_order_button_on_header_locator))

    @allure.step('Прокрутить страницу до аккордеона с id {header_id}')
    def scroll_to_accordion_panel(self, header_id):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.accordion_header_locator(header_id)))

    @allure.step('Нажать на кнопку подтверждения куки')
    def click_cookie_confirm_button(self):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.cookie_confirm_button_locator)
        ).click()

    def check_accordion_panel_text(self, header_id, expected_text):
        actual_text = self.accordion_panel_content_text(header_id)
        assert actual_text == expected_text, f"Expected text: '{expected_text}', but got: '{actual_text}'"

    def check_scooter_logo_click_page(self,expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Expected URL: '{expected_url}', but got: '{actual_url}'"

    def check_yandex_logo_click_page(self):
        WebDriverWait(self.driver, 5).until(
            lambda d: len(d.window_handles) >= 2
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains("yandex.ru"))
        actual_url = self.driver.current_url
        assert "yandex.ru" in actual_url, f"Expected yandex.ru, but got: '{actual_url}'"
