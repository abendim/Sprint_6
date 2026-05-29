from pages.main_page import MainPage
import pytest
import allure
from data import accordion_panel_data


class TestAccordionPanelButtonText:

    @allure.title('Проверка разделов вопросы о важном')
    @pytest.mark.parametrize("header_id, expected_text", [
        ('0', accordion_panel_data[0]),
        ('1', accordion_panel_data[1]),
        ('2', accordion_panel_data[2]),
        ('3', accordion_panel_data[3]),
        ('4', accordion_panel_data[4]),
        ('5', accordion_panel_data[5]),
        ('6', accordion_panel_data[6]),
        ('7', accordion_panel_data[7]),])
    def test_accordion_panel_button_text(self, driver, header_id, expected_text):
        accordion_panel = MainPage(driver)
        accordion_panel.click_cookie_confirm_button()
        accordion_panel.wait_accordion_header_locator(header_id)
        accordion_panel.scroll_to_accordion_panel(header_id)
        accordion_panel.click_accordion_panel(header_id)
        accordion_panel.wait_accordion_panel_content_locator(header_id)
        accordion_panel.check_accordion_panel_text(header_id, expected_text)


