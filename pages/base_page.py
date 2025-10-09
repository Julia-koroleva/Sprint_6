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

    @allure.step('Ожидание загрузки  страницы заказа сайта "Яндекс.Самокат"- "Для кого самокат?"')
    def load_order_page_for_whom(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.next)
        )


    @allure.step('Ожидание загрузки  страницы заказа сайта "Яндекс.Самокат"- "Про аренду"')
    def load_order_page_rent(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.back)
        )


    @allure.step('Ожидание загрузки  страницы заказа сайта "Яндекс.Самокат"- "Хотите оформить заказ?"')
    def load_order_page_make_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.yes_button)
        )

    @allure.step('Ожидание загрузки  страницы завершения заказа сайта "Яндекс.Самокат"')
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

    def click_element(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    def scroll_to_element(self, locator):
        element = self.wait_for_element_clickable(locator)
        self.execute_script_scroll(element)

    def scroll_to_questions_section(self):
        self.scroll_to_element(MainPageLocators.main_questions)

    def wait_for_multiple_windows(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) > 1
        )

    def switch_to_new_window(self):
        current_window = self.driver.current_window_handle
        for window in self.driver.window_handles:
            if window != current_window:
                self.driver.switch_to.window(window)
                break

    def wait_for_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part)
        )

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Визуализация элемента')
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Получение теста на визуализированном элемента')
    def get_element_text(self, locator):
        element = self.wait_for_element_visible(locator)
        return element.text
   
    @allure.step('Клик на элемент')
    def click_element(self, locator):
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()

    @allure.step('Ожидание кликабельности элемента и клик на него')
    def execute_script_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ожидание кликабельности элемента и клик на него')
    def wait_and_click_via_js(self, locator):
        element = self.wait_for_element_to_be_clickable(locator)
        self.execute_script_click(element)
 
    @allure.step('Ожидание кликабельности элемента и клик на него')
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Скролл до элемента')
    def execute_script_scroll(self, element):  
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator, timeout=10):  
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Скролл до определенного элемента элемента')
    def scroll_to_specific_element(self, element):
        self.execute_script_scroll(element)

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step('Наполнение элемента')
    def send_keys_to_element(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step('Проверка отображения элемента')
    def is_element_displayed(self, locator, timeout=10):
        try:
            element = self.wait_for_element_visible(locator, timeout)
            return element.is_displayed()
        except:
            return False

 