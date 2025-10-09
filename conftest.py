import pytest
import allure
from selenium import webdriver
from urls import *


@pytest.fixture
def driver():
    with allure.step("Инициализировать браузер Firefox и развернуть на весь экран"):
        driver=webdriver.Firefox()
        driver.get("https://qa-scooter.praktikum-services.ru/")
    with allure.step('Открытие главной страницы сайта "Яндекс.Самокат"'):
        driver.maximize_window()
    with allure.step('Ожидание загрузки главной страницысайта "Яндекс.Самокат"'):
        driver.implicitly_wait(10)
    yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()
