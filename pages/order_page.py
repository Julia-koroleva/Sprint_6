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

class OrderPage():

    def __init__(self, order_page):
        self.driver = order_page

    @allure.step('Ввод тестовых данных для заказа самоката "Для кого самокат"')
    def for_whom_form_fullfill(self, order_page, test_data):
        order_page.find_element(*OrderPageLocators.name).send_keys(test_data[0])
        order_page.find_element(*OrderPageLocators.surname).send_keys(test_data[1])
        order_page.find_element(*OrderPageLocators.address).send_keys(test_data[2])
        order_page.find_element(*OrderPageLocators.metro).send_keys(test_data[3])
        order_page.find_element(*OrderPageLocators.phone).send_keys(test_data[4])

    @allure.step('Ввод тестовых данных для заказа самоката на странице заказа самоката "Про аренду"')
    def order_specifics_fulfill(self, order_page, test_data):
        order_page.find_element(*OrderPageLocators.date).send_keys(test_data[5])
        order_page.find_element(*OrderPageLocators.rental_period).send_keys(test_data[6])
        order_page.find_element(*OrderPageLocators.black_samocat).send_keys()

    @allure.step('Клик на кнопку "Далее" после заполнения формы "Для кого замокат"')
    def click_button_next(self, order_page):
        order_page.find_element(*OrderPageLocators.next).click()

    @allure.step('Клик на кнопку "Заказать" после заполнения формы "Про аренду"')
    def click_button_order(self, order_page):
        order_page.find_element(*OrderPageLocators.order).click()

    @allure.step('Клик на кнопку "Да" на форме "Хотите оформить заказ?"')
    def click_button_yes(self, order_page):
        order_page.find_element(*OrderPageLocators.yes_button).click()

    @allure.step('Клик на логотип "Самокат" на странице заказа самоката')
    def click_logo_samocat(self, order_page):
        order_page.find_element(*OrderPageLocators.logo_samocat).click()

