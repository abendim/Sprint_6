from pages.base_page import BasePage
import pytest
import allure


class TestAccordionPanelButtonText:

    @allure.title('Проверка разделов вопросы о важном')
    @pytest.mark.parametrize("header_id, expected_text", [
        ('0', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        ('1', 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        ('2', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        ('3', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        ('4', 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        ('5', 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        ('6', 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        ('7', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')])
    def test_accordion_panel_button_text(self, driver, header_id, expected_text):
        accordion_panel = BasePage(driver)
        accordion_panel.click_cookie_confirm_button()
        accordion_panel.wait_accordion_header_locator(header_id)
        accordion_panel.scroll_to_accordion_panel(header_id)
        accordion_panel.click_accordion_panel(header_id)
        accordion_panel.wait_accordion_panel_content_locator(header_id)
        accordion_panel.check_accordion_panel_text(header_id, expected_text)


