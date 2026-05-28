from pages.create_order_page import CreateOrderPage
import pytest
from urls import MAIN_PAGE
import allure
from pages.main_page import MainPage


class TestCreateOrderRentScooter:

    @allure.title('Проверка создания заказа на аренду самоката через кнопку в шапке сайта')
    @pytest.mark.parametrize("name, surname, address, phone, metro_station_index, date_index, rental_period_text, comment", \
                             [("Иван", "Иванов", "ул. Ленина, 1", "89991234567", 0, 1, "сутки", "Позвоните за час")])
    def test_create_order_header_button(self, driver, name, surname, address, phone, metro_station_index, date_index, rental_period_text, comment,):
        create_order_page = CreateOrderPage(driver)
        main_page = MainPage(driver)
        create_order_page.click_cookie_confirm_button()
        main_page.click_create_order_button_on_header()
        create_order_page.wait_create_order_title_text()
        create_order_page.create_order_scooter_rent(name, surname, address, phone, metro_station_index, date_index, rental_period_text, comment)
        create_order_page.wait_create_order_confirm_order_button()
        create_order_page.click_create_order_confirm_order_button()
        create_order_page.wait_create_order_success_create_message()
        create_order_page.check_create_order_success_create_message()
    

    @allure.title('Проверка создания заказа на аренду самоката через кнопку внизу сайта')
    @pytest.mark.parametrize("name, surname, address, phone, metro_station_index, date_index, rental_period_text, comment", \
                             [("Макс", "Максов", "ул. Пушкина, 1", "77777777777", 5, 7, "сутки", "Позвоните за час")])
    def test_create_order_bottom_button(self, driver, name, surname, address, phone, metro_station_index, date_index, rental_period_text, comment ):
        create_order_page = CreateOrderPage(driver)
        main_page = MainPage(driver)
        create_order_page.click_cookie_confirm_button()
        main_page.click_create_order_button_on_bottom()
        create_order_page.wait_create_order_title_text()
        create_order_page.create_order_scooter_rent(name, surname, address, phone, metro_station_index, date_index, rental_period_text, comment)
        create_order_page.wait_create_order_confirm_order_button()
        create_order_page.click_create_order_confirm_order_button()
        create_order_page.wait_create_order_success_create_message()
        create_order_page.check_create_order_success_create_message()


    @allure.title('Проверка возврата на главную страницу при клике на логотип самоката в шапке сайта')
    def test_create_order_return_to_main_page(self, driver):
        create_order_page = CreateOrderPage(driver)
        main_page = MainPage(driver)
        create_order_page.click_cookie_confirm_button()
        main_page.click_create_order_button_on_header()
        create_order_page.wait_create_order_title_text()
        create_order_page.click_scooter_logo()
        create_order_page.check_scooter_logo_click_page(MAIN_PAGE)


    @allure.title('Проверка открытия страницы Яндекса при клике на логотип Яндекса в шапке сайта')
    def test_create_order_open_yandex_page(self, driver):
        create_order_page = CreateOrderPage(driver)
        main_page = MainPage(driver)
        create_order_page.click_cookie_confirm_button()
        main_page.click_create_order_button_on_header()
        create_order_page.wait_create_order_title_text()
        create_order_page.click_yandex_logo()
        create_order_page.wait_to_new_yandex_window_opened()
        create_order_page.check_yandex_logo_click_page()