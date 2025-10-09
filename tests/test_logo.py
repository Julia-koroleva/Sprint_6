import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.base_page import BasePage
from Sprint_6.conftest import driver



class TestLogo:
    @allure.title('Проверка перехода на главную страницу Дзена через логотип Яндекса')
    @allure.description('При нажатии на логотип Яндекса открывается новое окно с переходом на Дзен')
    def test_new_page_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        current_url = main_page.switch_to_window_and_check_url("dzen.ru")
        assert "dzen.ru" in current_url

    @allure.title('Проверка перехода на главную страницу через логотип Самоката')
    @allure.description('Со страницы заказа при нажатии на логотип Самоката происходит переход на главную страницу')
    def test_transfer_main_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        base_page = BasePage(driver)
        main_page.click_button_up()
        main_page.load_order_page_for_whom()
        order_page.click_logo_samocat()
        base_page.wait_for_main_page()
        current_url = main_page.get_current_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/"