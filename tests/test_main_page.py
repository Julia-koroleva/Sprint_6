import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('..')
import allure
import pytest
from locators.main_page_locators import MainPageLocators
from ..pages.main_page import MainPage
from Sprint_6.conftest import driver
from Sprint_6.data import *

class TestMainPage():
    @allure.title('Проверка раздела "Вопросы о важном')
    @allure.description('Проверка появления корректного ответа при нажатии на вопросы в разделе "Вопросы о важном" на главной странице "Яндекс.Самокат"')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_question_answers)
    def test_main_page_questions_answers(self, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.load_main_page()
        main_page.scroll_to_element()
        main_page.questions_click(question_number)
        main_page.load_questions_answers(expected_answer)
        assert main_page.get_answers(question_number) == expected_answer

