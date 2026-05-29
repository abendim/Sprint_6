import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage



class MainPage(MainPageLocators, BasePage):


    def accordion_panel_content_text(self, header_id):
        return self.find_element(self.accordion_panel_content_locator(header_id)).text

    @allure.step('Нажать на кнопку "Создать заказ" внизу страницы')
    def click_create_order_button_on_bottom(self):
        self.find_and_click(self.create_order_button_on_bottom_locator)

    @allure.step('Нажать на кнопку "Создать заказ" в шапке страницы')
    def click_create_order_button_on_header(self):
        self.find_and_click(self.create_order_button_on_header_locator)

    @allure.step('Нажать на аккордеон с id {header_id}')
    def click_accordion_panel(self, header_id):
        element = self.driver.find_element(*self.accordion_header_locator(header_id))
        self.driver.execute_script("arguments[0].click();", element)

    def wait_accordion_header_locator(self, header_id):
        return self.wait_element_clickable(self.accordion_header_locator(header_id))

    def wait_accordion_panel_content_locator(self, header_id):
        return self.wait_element_visible(self.accordion_panel_content_locator(header_id))
    
    @allure.step('Прокрутить страницу до кнопки "Создать заказ" внизу страницы')
    def scroll_to_create_button_on_bottom(self):
        self.scroll_to_element(self.create_order_button_on_bottom_locator)

    @allure.step('Прокрутить страницу до аккордеона с id {header_id}')
    def scroll_to_accordion_panel(self, header_id):
        self.scroll_to_element(self.accordion_header_locator(header_id))

    @allure.step('Проверить текст в раскрывающемся аккордеоне с id {header_id}')
    def check_accordion_panel_text(self, header_id, expected_text):
        assert self.accordion_panel_content_text(header_id) == expected_text, f"Expected text: '{expected_text}', but got: '{self.accordion_panel_content_text(header_id)}'"