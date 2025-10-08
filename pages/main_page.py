import sys
sys.path.append('..')
import allure
from locators.main_page_locators import MainPageLocators
from .base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на страницу заказа путем клика на кнопку "Заказать" в хедере страницы')
    def click_button_up(self):
        self.driver.find_element(*MainPageLocators.button_up).click()

    @allure.step('Клик по кнопке Заказать в зависимости от типа кнопки заказать')
    def click_order_button(self, button_type):
        if button_type == "top":
            self.click_element(MainPageLocators.button_up)
        else: 
            self.scroll_to_element(MainPageLocators.button_down)
            self.click_element(MainPageLocators.button_down)

    @allure.step('Клик на вопрос по номеру {question_index}')
    def click_question(self, question_index):
        index = question_index - 1
        question_locator = MainPageLocators.QUESTIONS[index]
        question = self.wait_for_element_to_be_clickable(question_locator)
        self.scroll_to_specific_element(question)
        question.click()

    @allure.step('Получение текста ответа на вопрос {question_index}')
    def get_answer_text(self, question_index):
        index = question_index - 1
        answer_locator = MainPageLocators.ANSWERS[index]
        return self.get_element_text(answer_locator)

    @allure.step('Клик на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.logo_yandex)

    @allure.step('Переключение на новое окно и проверка URL')
    def switch_to_window_and_check_url(self, expected_url):
        self.wait_for_multiple_windows()
        self.switch_to_new_window()
        self.wait_for_url_contains(expected_url)
        return self.get_current_url()

    