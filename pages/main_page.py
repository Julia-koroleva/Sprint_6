import sys
sys.path.append('..')
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from .base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на страницу заказа путем клика на кнопку "Заказать" в хедере страницы') 
    def click_button_up(self):
        self.driver.find_element(*MainPageLocators.button_up).click()

    @allure.step('Переход на страницу заказа путем клика на кнопку "Заказать" в футере страницы') 
    def click_button_down(self):
        self.driver.find_element(*MainPageLocators.button_down).click()

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


    @allure.step('Клик на логотип "Яндекс"')
    def logo_yandex_click(self):   
        self.driver.find_element(*MainPageLocators.logo_yandex).click()

   