import sys 
sys.path.append('..')
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, main_page):
        self.driver = main_page
        
    @allure.step('Ожидание загрузки главной страницы сайта "Яндекс.Самокат"')
    def load_main_page(self, main_page):
        WebDriverWait(main_page, 10).until(
            EC.visibility_of_element_located(MainPageLocators.button_up)
        )
    
    @allure.step('Ожидание загрузки  страницы заказа сайта "Яндекс.Самокат"- "Для кого самокат?"')
    def load_order_page_for_whom(self, order_page):
        WebDriverWait(order_page, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.next)
        )

    @allure.step('Ожидание загрузки  страницы заказа сайта "Яндекс.Самокат"- "Про аренду"')
    def load_order_page_rent(self, order_page):
        WebDriverWait(order_page, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.back)
        )

    @allure.step('Ожидание загрузки  страницы заказа сайта "Яндекс.Самокат"- "Хотите оформить заказ?"')
    def load_order_page_make_order(self, order_page):
        WebDriverWait(order_page, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.yes_button)
        )

    @allure.step('Ожидание загрузки  страницы завершения заказа сайта "Яндекс.Самокат"')
    def load_page_confirm_order(self, order_page):
        WebDriverWait(order_page, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.order_made)
        )

    @allure.step('Скролл до элемента на главной странице "Яндекс.Самокат"')
    def scroll_to_element(self):
        element = self.driver.find_element(*MainPageLocators.main_questions)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание загрузки  страницы Dzen')
    def load_page_dzen(self, dzen):
        WebDriverWait(dzen, 10).until(
            EC.visibility_of_element_located(MainPageLocators.dzen_logo)
        )

    @allure.step('Ожидание загрузки ответов на вопросы на странице "Яндек.Самокат" в разделе "Вопросы о важном"')
    def load_questions_answers(self, main_page):
       WebDriverWait(main_page, 3)  