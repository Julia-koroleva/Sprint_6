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
from data import TestData


class TestOrderPage:
    
    @allure.title('Проверка оформления заказа на сайте "Яндекс.Самокат"')
    @allure.description('При вводе данных в всплывающие формы на сайте осуществляется оформление заказа самоката')
    @pytest.mark.parametrize("data_set", ["set1", "set2"])
    @pytest.mark.parametrize("button_type", ["top", "bottom"])
    def test_order_page(self, driver, button_type, data_set):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_order_button(button_type)
        order_page.load_order_page_for_whom()  
        order_page.for_whom_form_fullfill(TestData.test_data[data_set])  
        order_page.click_button_next()
        order_page.load_order_page_rent()
        order_page.order_specifics_fulfill(TestData.test_data[data_set])  
        order_page.click_button_order()
        order_page.load_order_page_make_order()
        order_page.click_button_yes()
        order_page.load_page_confirm_order()
        assert order_page.is_success_message_displayed()


