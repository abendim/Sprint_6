from selenium.webdriver.common.by import By


class MainPageLocators:

    create_order_button_on_bottom_locator = [By.XPATH, '//div[@class="Home_RoadMap__2tal_"]//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    create_order_button_on_header_locator = [By.XPATH, '//div[@class="Header_Nav__AGCXC"]//button[@class="Button_Button__ra12g"]']


    def accordion_header_locator(self, header_id):
        return (By.XPATH, f'//*[@id="accordion__heading-{header_id}"]')

    def accordion_panel_content_locator(self, header_id):
        return (By.XPATH, f'//*[@id="accordion__panel-{header_id}"]//p')
    