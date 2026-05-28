from selenium.webdriver.common.by import By


class BasePageLocators:


    scooter_logo_locator = [By.XPATH, '//img[@alt="Scooter" and contains(@src, "scooter.svg")]']
    yandex_logo_locator = [By.XPATH, '//img[@alt="Yandex" and contains(@src, "ya.svg")]']
    cookie_confirm_button_locator = [By.ID, 'rcc-confirm-button']
