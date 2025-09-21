import pytest
import allure
from selenium import webdriver

main_site = "https://qa-scooter.praktikum-services.ru/"
order_site = "https://qa-scooter.praktikum-services.ru/order"
dzen = "https://dzen.ru/"

@pytest.fixture
def driver():
    with allure.step("Инициализировать браузер Firefox и развернуть на весь экран"):
        driver = webdriver.Firefox()
        driver.maximize_window()
    yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()

@pytest.fixture
def main_page(driver):
    with allure.step(f"Перейти на главную страницу: {main_site}"):
        driver.get(main_site)
    return driver

@pytest.fixture
def order_page(driver):
    with allure.step(f"Перейти на страницу заказа: {order_site}"):
        driver.get(order_site)
    return driver

@pytest.fixture
def main_page_locators():
    from locators.main_page_locators import MainPageLocators
    return MainPageLocators

@pytest.fixture
def order_page_locators():
    from locators.order_page_locators import OrderPageLocators
    return OrderPageLocators