import allure
import pytest
from pages.main_page import MainPage
from data import TestData
from Sprint_6.conftest import driver

class TestMainPage:
    @allure.title('Проверка ответов на вопросы в разделе "Вопросы о важном"')
    @allure.description('Проверка корректности текста ответов при клике на вопросы')
    @pytest.mark.parametrize('question_number, expected_answer', 
                             TestData.test_data_question_answers)
    def test_questions_answers(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_questions_section()
        main_page.click_question(question_number)
        actual_answer = main_page.get_answer_text(question_number)
        assert actual_answer == expected_answer, \
            f"Текст ответа не совпадает. Ожидалось: {expected_answer}, Получено: {actual_answer}"
