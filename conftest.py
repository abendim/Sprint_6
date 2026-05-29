import pytest 
from selenium import webdriver
from urls import MAIN_PAGE
import allure


@pytest.fixture(scope="function")
def driver():
    with allure.step('Открыть браузер и перейти на главную страницу'):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(MAIN_PAGE)
    yield driver
    with allure.step('Закрыть браузер'):
        driver.quit()