from .base_page import BasePage
from locators.create_order_page_locators import CreateOrderPageLocators
import allure

class CreateOrderPage(BasePage, CreateOrderPageLocators):
    
    @allure.step('Ввести имя: {name}')
    def set_create_order_name(self, name):
        self.find_and_send_keys(self.order_create_input_name, name)

    @allure.step('Ввести фамилию: {surname}')
    def set_create_order_surname(self, surname):
        self.find_and_send_keys(self.order_create_input_surname, surname)

    @allure.step('Ввести адрес: {address}')
    def set_create_order_address(self, address):
        self.find_and_send_keys(self.order_create_input_address, address)

    @allure.step('Кликнуть на кнопку выбора станции метро')
    def click_create_order_metro_station(self):
        self.find_and_click(self.order_create_input_metro_station)

    @allure.step('Выбрать станцию метро с индексом: {metro_station_index}')
    def set_create_order_metro_station(self, metro_station_index):
        self.find_and_click(self.get_order_create_metro_station(metro_station_index))

    @allure.step('Ввести телефон: {phone}')
    def set_create_order_phone(self, phone):
        self.find_and_send_keys(self.order_create_input_phone, phone)

    @allure.step('Кликнуть на кнопку "Далее" для перехода на страницу деталей заказа')
    def click_create_order_next_page_button(self):
        self.find_and_click(self.order_create_next_page_button)

    def wait_create_order_metro_station_list(self, metro_station_index):
        self.wait_element_clickable(self.get_order_create_metro_station(metro_station_index))
    
    def wait_create_order_title_text(self):
        self.wait_element_visible(self.order_create_title_text)
    
    def wait_create_order_details_page_title(self):
        self.wait_element_visible(self.order_create_details_page_title)
    
    @allure.step('Кликнуть на кнопку выбора даты заказа')
    def click_create_order_date_dropdown(self):
        self.find_and_click(self.order_create_date_dropdown)

    @allure.step('Выбрать дату заказа с индексом: {date_index}')
    def set_create_order_date(self, date_index):
        self.find_and_click(self.get_order_create_date(date_index))

    @allure.step('Кликнуть на кнопку выбора срока аренды')
    def click_create_order_rental_period_dropdown(self):
        self.find_and_click(self.order_create_rental_period_dropdown)

    @allure.step('Выбрать срок аренды: {rental_period_text}')
    def set_create_order_rental_period(self, rental_period_text):
        self.find_and_click(self.get_order_create_rental_period(rental_period_text))

    @allure.step('Выбрать цвет самоката: черный')
    def click_create_order_color_checkbox_black(self):
        self.find_and_click(self.order_create_color_checkbox_black)

    @allure.step('Ввести комментарий для курьера: {comment}')
    def set_create_order_comment(self, comment):
        self.find_and_send_keys(self.order_create_comment_input, comment)

    @allure.step('Кликнуть на кнопку "Заказать" для создания заказа')
    def click_create_order_button(self):
        self.find_and_click(self.order_create_button)

    def wait_create_order_confirm_order_button(self):
        self.wait_element_clickable(self.order_create_confirm_order_button)
    
    def wait_create_order_success_create_message(self):
        self.wait_element_visible(self.order_create_success_create_message)
    
    @allure.step('Кликнуть на кнопку подтверждения заказа')
    def click_create_order_confirm_order_button(self):
        self.find_and_click(self.order_create_confirm_order_button)
    
    @allure.step('Проверить отображение сообщения об успешном создании заказа')
    def check_create_order_success_create_message(self):
        assert self.find_element(self.order_create_success_create_message) and 'Заказ оформлен' in self.find_element(self.order_create_success_create_message).text

    def create_order_scooter_rent(self, name, surname, address, phone, metro_station_index, date_index, rental_period_text, comment):
        self.wait_create_order_title_text()
        self.set_create_order_name(name)
        self.set_create_order_surname(surname)
        self.set_create_order_address(address)
        self.click_create_order_metro_station()
        self.wait_create_order_metro_station_list(metro_station_index)
        self.set_create_order_metro_station(metro_station_index)
        self.set_create_order_phone(phone)
        self.click_create_order_next_page_button()
        self.wait_create_order_details_page_title()
        self.click_create_order_date_dropdown()
        self.set_create_order_date(date_index)
        self.click_create_order_rental_period_dropdown()
        self.set_create_order_rental_period(rental_period_text)
        self.click_create_order_color_checkbox_black()
        self.set_create_order_comment(comment)
        self.click_create_order_button()

    

