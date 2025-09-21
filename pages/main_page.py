import sys 
sys.path.append('..')
import allure
from locators.main_page_locators import MainPageLocators
from ..pages.base_page import BasePage

class MainPage(BasePage):

    def __init__(self, main_page):
        self.driver = main_page

    @allure.step('Переход на страницу заказа путем клика на кнопку "Заказать" в хедере страницы') 
    def click_button_up(self, main_page):
        main_page.find_element(*MainPageLocators.button_up).click()

    @allure.step('Переход на страницу заказа путем клика на кнопку "Заказать" вв футере страницы') 
    def click_button_down(self, main_page):
        main_page.find_element(*MainPageLocators.button_down).click()

    @allure.step('Клик на стрелочку вопросов в разделе "Вопросы о важном')
    def questions_click(self, main_page):   
        main_page.find_element(*MainPageLocators.QUESTIONS).click()

    @allure.step('Клик на логотип "Яндекс"')
    def logo_yandex_click(self, main_page):   
        main_page.find_element(*MainPageLocators.logo_yandex).click()

    @allure.step('Получение ответов на вопросы в разделе "Вопросы о важном" на главной странице "Яндекс.Самокат')
    def get_answers(self, main_page):
        main_page.fint_element(*MainPageLocators.ANSWERS).text()