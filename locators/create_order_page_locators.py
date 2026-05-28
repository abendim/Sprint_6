from selenium.webdriver.common.by import By


class CreateOrderPageLocators:
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
    order_create_comment_input = [By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN" and contains(@placeholder, "Комментарий для курьера")]']
    order_create_button = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Заказать")]']
    order_create_details_page_title = [By.XPATH, "//div[@class='Order_Header__BZXOb' and contains(text(), 'Про аренду')]"]
    order_create_confirm_order_button = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Да")]']
    order_create_success_create_message = [By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ" and contains(text(), "Заказ оформлен")]']
    order_create_check_created_order_status = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Посмотреть статус")]']



    def get_order_create_metro_station(self, metro_station_index):
        return [By.XPATH, f'//div[@class="select-search__select"]//li[@data-index="{metro_station_index}"]/button']
    
    def get_order_create_date(self, date_index):
        return [By.XPATH, f'//div[@class="react-datepicker"]//div[@class="react-datepicker__day react-datepicker__day--00{date_index}"]']
    
    def get_order_create_rental_period(self, rental_period_text):
        return [By.XPATH, f'//div[@class="Dropdown-menu"]//div[@class="Dropdown-option" and text()="{rental_period_text}"]']