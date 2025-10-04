import sys 
sys.path.append('..')
import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_6.data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from Sprint_6.data import TestData
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Ввод тестовых данных для заказа самоката "Для кого самокат"')
    def for_whom_form_fullfill(self, test_data):
        self.driver.find_element(*OrderPageLocators.name).send_keys(test_data['name'])
        self.driver.find_element(*OrderPageLocators.surname).send_keys(test_data['surname'])
        self.driver.find_element(*OrderPageLocators.address).send_keys(test_data['address'])
        self.select_metro_station(test_data['metro']) 
        self.driver.find_element(*OrderPageLocators.phone).send_keys(test_data['phone'])

    @allure.step('Ввод тестовых данных для заказа самоката на странице заказа самоката "Про аренду"')
    def order_specifics_fulfill(self, test_data):
        self.driver.find_element(*OrderPageLocators.rental_period).click()
        self.driver.find_element(*OrderPageLocators.date).send_keys(test_data['date'])
        self.select_rental_period(test_data['period'])
        if test_data.get('color') == 'black':
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(OrderPageLocators.black_samocat)
        ).click()
        else:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(OrderPageLocators.gray_samocat)
        ).click()
        if test_data.get('message'):
            self.driver.find_element(*OrderPageLocators.message).send_keys(test_data['message'])


    @allure.step('Выбор периода аренды')
    def select_rental_period(self, period):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.rental_period)
        )
        self.driver.execute_script("arguments[0].click();", dropdown)
    
        period_locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']")
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(period_locator)
        )
        self.driver.execute_script("arguments[0].click();", option)

    @allure.step('Клик на кнопку "Далее" после заполнения формы "Для кого замокат"')
    def click_button_next(self):
        self.driver.find_element(*OrderPageLocators.next).click()

    @allure.step('Клик на кнопку "Заказать" после заполнения формы "Про аренду"')
    def click_button_order(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()


    @allure.step('Клик на кнопку "Да" на странице подтверждения заказа')
    def click_button_yes(self):
        self.driver.find_element(*OrderPageLocators.yes_button).click()

    @allure.step('Клик на логотип "Самокат" на странице заказа самоката')
    def click_logo_samocat(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.logo_samocat)
        ).click()

    @allure.step('Выбор на странице заказа типа самоката "Серая безысходность"')
    def click_samocat_type(self):
        self.driver.find_element(*OrderPageLocators.gray_samocat).click()
    
    @allure.step('Отображение сообщения об успешном оформлении заказа')
    def is_success_message_displayed(self):
        return self.driver.find_element(*OrderPageLocators.order_made).is_displayed()
    
    @allure.step('Получение текста сообщения об успехе')
    def get_success_message_text(self):
        return self.driver.find_element(*OrderPageLocators.order_made).text
    
    @allure.step('Выбор станции метро')
    def select_metro_station(self, station_name):
        self.driver.find_element(*OrderPageLocators.metro).click()
        dropdown_list = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "select-search__select"))
        )
        station_locator = (By.XPATH, f".//*[contains(text(), '{station_name}')]")
        WebDriverWait(dropdown_list, 15).until(
            EC.element_to_be_clickable(station_locator)
        ).click()

        @allure.step('Клик на выпадающий список периода аренды')
        def click_rental_period(self):
            self.driver.find_element(*OrderPageLocators.rental_period)
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(OrderPageLocators.rental_period)
            )
            self.driver.execute_script("arguments[0].click();", element)