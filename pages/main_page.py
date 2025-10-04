import sys
sys.path.append('..')
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from .base_page import BasePage
from pages.order_page import OrderPage
from selenium import webdriver

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на страницу заказа путем клика на кнопку "Заказать" в хедере страницы') 
    def click_button_up(self):
        self.driver.find_element(*MainPageLocators.button_up).click()

    @allure.step('Переход на страницу заказа путем клика на кнопку "Заказать" в футере страницы') 
    def click_button_down(self):
        self.driver.find_element(*MainPageLocators.button_down).click()

    @allure.step('Клик по кнопке Заказать в зависимости от типа кнопки заказать')
    def click_order_button(self, button_type):
        if button_type == "top":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(MainPageLocators.button_up)
            ).click()
        else:  
            element = self.driver.find_element(*MainPageLocators.button_down)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(MainPageLocators.button_down)
            ).click()

    @allure.step('Клик на вопрос по номеру {question_index}')
    def click_question(self, question_index):
        index = question_index - 1
        question_locator = MainPageLocators.QUESTIONS[index]
        
        question = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(question_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()

    @allure.step('Получение текста ответа на вопрос {question_index}')
    def get_answer_text(self, question_index):
        index = question_index - 1
        answer_locator = MainPageLocators.ANSWERS[index]
        
        answer_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(answer_locator)
        )
        return answer_element.text

    @allure.step('Получить текущий дескриптор окна')
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    
    @allure.step('Клик на логотип "Яндекс"')
    def click_yandex_logo(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.logo_yandex)
        ).click()

    @allure.step('Переключение на новое окно и проверка URL')
    def switch_to_window_and_check_url(self, expected_url):
        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > 1
        )
        
        current_window = self.driver.current_window_handle
        for window in self.driver.window_handles:
            if window != current_window:
                self.driver.switch_to.window(window)
                break
        
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(expected_url)
        )
        return self.driver.current_url
    
    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    