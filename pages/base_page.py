import sys 
sys.path.append('..')
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver):
        self.driver = driver
                
    @allure.step('Ожидание загрузки  страницы заказа сайта "Яндекс.Самокат"- "Для кого самокат?"')
    def load_order_page_for_whom(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.next)
        )

    @allure.step('Ожидание загрузки  страницы заказа сайта "Яндекс.Самокат"- "Про аренду"')
    def load_order_page_rent(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.back)
        )

    @allure.step('Ожидание загрузки  страницы заказа сайта "Яндекс.Самокат"- "Хотите оформить заказ?"')
    def load_order_page_make_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.yes_button)
        )
           

    @allure.step('Ожидание загрузки  страницы завершения заказа сайта "Яндекс.Самокат"')
    def load_page_confirm_order(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.order_made)
        )

    @allure.step('Скролл до элемента на главной странице "Яндекс.Самокат"')
    def scroll_to_element(self):
        element = self.driver.find_element(*MainPageLocators.main_questions)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание загрузки главной страницы')
    def wait_for_main_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://qa-scooter.praktikum-services.ru/")
        )
    
       

       