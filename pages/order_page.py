import sys 
sys.path.append('..')
import allure
from Sprint_6.data import *
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввод тестовых данных для заказа самоката "Для кого самокат"')
    def for_whom_form_fullfill(self, test_data):
        self.send_keys_to_element(OrderPageLocators.name, test_data['name'])
        self.send_keys_to_element(OrderPageLocators.surname, test_data['surname'])
        self.send_keys_to_element(OrderPageLocators.address, test_data['address'])
        self.select_metro_station(test_data['metro'])
        self.send_keys_to_element(OrderPageLocators.phone, test_data['phone'])


    @allure.step('Ввод тестовых данных для заказа самоката на странице заказа самоката "Про аренду"')
    def order_specifics_fulfill(self, test_data):
        self.click_element(OrderPageLocators.rental_period)
        self.send_keys_to_element(OrderPageLocators.date, test_data['date'])
        self.select_rental_period(test_data['period'])
        if test_data.get('color') == 'black':
            self.click_element(OrderPageLocators.black_samocat)
        else:
            self.click_element(OrderPageLocators.gray_samocat)
        if test_data.get('message'):
            self.send_keys_to_element(OrderPageLocators.message, test_data['message'])

    @allure.step('Выбор периода аренды')
    def select_rental_period(self, period):
        self.wait_and_click_via_js(OrderPageLocators.rental_period)
        period_locator = OrderPageLocators.get_period_locator(period)
        self.wait_and_click_via_js(period_locator)

    @allure.step('Клик на кнопку "Далее" после заполнения формы "Для кого замокат"')
    def click_button_next(self):
        self.click_element(OrderPageLocators.next)


    @allure.step('Клик на кнопку "Заказать" после заполнения формы "Про аренду"')
    def click_button_order(self):
        self.click_element(OrderPageLocators.order_button)

    @allure.step('Клик на кнопку "Да" на странице подтверждения заказа')
    def click_button_yes(self):
        self.click_element(OrderPageLocators.yes_button)

    @allure.step('Клик на логотип "Самокат" на странице заказа самоката')
    def click_logo_samocat(self):
        self.click_element(OrderPageLocators.logo_samocat)

    @allure.step('Отображение сообщения об успешном оформлении заказа')
    def is_success_message_displayed(self):
        return self.is_element_displayed(OrderPageLocators.order_made)

    @allure.step('Выбор станции метро')
    def select_metro_station(self, station_name):
        self.click_element(OrderPageLocators.metro)
        self.wait_for_element_visible(OrderPageLocators.dropdown_container)
        station_locator = OrderPageLocators.get_station_locator(station_name)
        self.click_element(station_locator)