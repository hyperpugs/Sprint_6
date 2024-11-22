import allure
import pytest
from data import QuestionData
from pages.main_page import MainPage


class TestFooter:
    @pytest.mark.parametrize(QuestionData.param, QuestionData.value)
    @allure.title(f'Проверка вопроса')
    @allure.description('При нажатии на вопрос открывается соответствующий текст')
    def test_question(self, driver, number, expected_result):
        base_page = MainPage(driver)
        base_page.open_the_the_page_and_go_to_the_footer()

        base_page.click_on_question(number)

        base_page.check_text_answer_of_question(number, expected_result)