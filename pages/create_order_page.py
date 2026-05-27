from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CreateOrderPage(BasePage):

    order_create_title_text = [By.XPATH, '//div[@class="Order_Content__bmtHS"]/div[text()="Для кого самокат"]']
    order_create_input_name = [By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and contains(@placeholder, "Имя")]']
    order_create_input_surname = [By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and contains(@placeholder, "Фамилия")]']
    order_create_input_address = [By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and contains(@placeholder, "Адрес: куда привезти заказ")]']
    order_create_input_metro_station = [By.XPATH, '//input[@class="select-search__input" and contains(@placeholder, "Станция метро")]']
    order_create_input_phone = [By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and contains(@placeholder, "Телефон: на него позвонит курьер")]']
    order_create_next_page_button = [By.XPATH, '//div[@class="Order_NextButton__1_rCA"]/button[text()="Далее"]']
    order_create_date_dropdown = [By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and contains(@placeholder, "Когда привезти самокат")]']
    order_create_rental_period_dropdown = [By.XPATH, '//div[@class="Dropdown-placeholder" and contains(text(), "Срок аренды")]']
    order_create_color_checkbox_black = [By.ID, 'black']
    order_create_color_checkbox_grey = [By.ID, 'grey']
    order_create_comment_input = [By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and contains(@placeholder, "Комментарий для курьера")]']
    order_create_button = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Заказать")]']
    order_create_details_page_title = [By.XPATH, "//div[@class='Order_Header__BZXOb' and contains(text(), 'Про аренду')]"]
    order_create_confirm_order_button = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Да")]']
    order_create_success_create_message = [By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ" and contains(text(), "Заказ оформлен")]']
    order_create_check_created_order_status = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Посмотреть статус")]']
    order_create_cancel_order_button = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i" and text()="Отменить заказ"]']

    def __init__(self, driver):
        super().__init__(driver)


    def get_order_create_metro_station(self, metro_station_index):
        return [By.XPATH, f'//div[@class="select-search__select"]//li[@data-index="{metro_station_index}"]/button']
    
    def get_order_create_date(self, date_index):
        return [By.XPATH, f'//div[@class="react-datepicker"]//div[@class="react-datepicker__day react-datepicker__day--00{date_index}"]']
    
    def get_order_create_rental_period(self, rental_period_text):
        return [By.XPATH, f'//div[@class="Dropdown-menu"]//div[@class="Dropdown-option" and text()="{rental_period_text}"]']
    
    @allure.step('Ввести имя: {name}')
    def set_create_order_name(self, name):
        self.driver.find_element(*self.order_create_input_name).send_keys(name)

    @allure.step('Ввести фамилию: {surname}')
    def set_create_order_surname(self, surname):
        self.driver.find_element(*self.order_create_input_surname).send_keys(surname)

    @allure.step('Ввести адрес: {address}')
    def set_create_order_address(self, address):
        self.driver.find_element(*self.order_create_input_address).send_keys(address)

    @allure.step('Кликнуть на кнопку выбора станции метро')
    def click_create_order_metro_station(self):
        self.driver.find_element(*self.order_create_input_metro_station).click()

    @allure.step('Выбрать станцию метро с индексом: {metro_station_index}')
    def set_create_order_metro_station(self, metro_station_index):
        self.driver.find_element(*self.get_order_create_metro_station(metro_station_index)).click()

    @allure.step('Ввести телефон: {phone}')
    def set_create_order_phone(self, phone):
        self.driver.find_element(*self.order_create_input_phone).send_keys(phone)

    @allure.step('Кликнуть на кнопку "Далее" для перехода на страницу деталей заказа')
    def click_create_order_next_page_button(self):
        self.driver.find_element(*self.order_create_next_page_button).click()

    def wait_create_order_metro_station_list(self, metro_station_index):
        return WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.get_order_create_metro_station(metro_station_index)))

    def wait_create_order_date_dropdown(self):
        return WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.order_create_date_dropdown))
    
    def wait_create_order_title_text(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.order_create_title_text))
    
    def wait_create_order_details_page_title(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.order_create_details_page_title))
    
    @allure.step('Кликнуть на кнопку выбора даты заказа')
    def click_create_order_date_dropdown(self):
        self.driver.find_element(*self.order_create_date_dropdown).click()

    @allure.step('Выбрать дату заказа с индексом: {date_index}')
    def set_create_order_date(self, date_index):
        self.driver.find_element(*self.get_order_create_date(date_index)).click()

    @allure.step('Кликнуть на кнопку выбора срока аренды')
    def click_create_order_rental_period_dropdown(self):
        self.driver.find_element(*self.order_create_rental_period_dropdown).click()

    @allure.step('Выбрать срок аренды: {rental_period_text}')
    def set_create_order_rental_period(self, rental_period_text):
        self.driver.find_element(*self.get_order_create_rental_period(rental_period_text)).click()

    @allure.step('Выбрать цвет самоката: черный')
    def click_create_order_color_checkbox_black(self):
        self.driver.find_element(*self.order_create_color_checkbox_black).click()

    @allure.step('Выбрать цвет самоката: серый')
    def click_create_order_color_checkbox_grey(self):
        self.driver.find_element(*self.order_create_color_checkbox_grey).click()

    @allure.step('Ввести комментарий для курьера: {comment}')
    def set_create_order_comment(self, comment):
        self.driver.find_element(*self.order_create_comment_input).send_keys(comment)

    @allure.step('Кликнуть на кнопку "Заказать" для создания заказа')
    def click_create_order_button(self):
        self.driver.find_element(*self.order_create_button).click()

    def wait_create_order_confirm_order_button(self):
        return WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.order_create_confirm_order_button))
    
    def wait_create_order_success_create_message(self):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.order_create_success_create_message))
    
    @allure.step('Кликнуть на кнопку подтверждения заказа')
    def click_create_order_confirm_order_button(self):
        self.driver.find_element(*self.order_create_confirm_order_button).click()
    
    def check_create_order_success_create_message(self):
        actual_text = self.driver.find_element(*self.order_create_success_create_message).text
        assert 'Заказ оформлен' in actual_text, f"Expected text: Заказ оформлен, but got: {actual_text}"

    @allure.step('Кликнуть на кнопку "Посмотреть статус" для проверки статуса созданного заказа')
    def click_create_order_check_created_order_status(self):
        self.driver.find_element(*self.order_create_check_created_order_status).click()

    def wait_create_order_cancel_order_button(self):
        return WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.order_create_cancel_order_button))

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

    

