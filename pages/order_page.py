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


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввод тестовых данных для заказа самоката "Для кого самокат"')
    def for_whom_form_fullfill(self, test_data):
        self.driver.find_element(*OrderPageLocators.name).send_keys(test_data[0])
        self.driver.find_element(*OrderPageLocators.surname).send_keys(test_data[1])
        self.driver.find_element(*OrderPageLocators.address).send_keys(test_data[2])
        self.driver.find_element(*OrderPageLocators.metro).send_keys(test_data[3])
        self.driver.find_element(*OrderPageLocators.phone).send_keys(test_data[4])

    @allure.step('Ввод тестовых данных для заказа самоката на странице заказа самоката "Про аренду"')
    def order_specifics_fulfill(self, test_data):
        self.driver.find_element(*OrderPageLocators.date).send_keys(test_data[5])
        self.driver.find_element(*OrderPageLocators.rental_period).send_keys(test_data[6])
        self.driver.find_element(*OrderPageLocators.black_samocat).send_keys()

    @allure.step('Клик на кнопку "Далее" после заполнения формы "Для кого замокат"')
    def click_button_next(self):
        self.driver.find_element(*OrderPageLocators.next).click()

    @allure.step('Клик на кнопку "Заказать" после заполнения формы "Про аренду"')
    def click_button_order(self):
        self.driver.find_element(*OrderPageLocators.order).click()

    @allure.step('Клик на кнопку "Да" на странице подтверждения заказа')
    def click_button_yes(self):
        self.driver.find_element(*OrderPageLocators.yes_button).click()

    @allure.step('Клик на логотип "Самокат" на странице заказа самоката')
    def click_logo_samocat(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.logo_samocat)
        ).click()