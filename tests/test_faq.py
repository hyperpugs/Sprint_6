import allure
import pytest
from data import QuestionData
from pages.main_page import MainPage
from locators.main_page_locator import MainPageLocators


class TestQuestion:

    @allure.title('Раздел "Вопросы о важном"')
    @pytest.mark.parametrize(QuestionData.PARAM, QuestionData.VALUE)
    def test_question(self, driver, number, expected_answer):

        main_page = MainPage(driver, timer=10)
        main_page.scroll_to_last_question()
        main_page.click_to_question(number)
        answer = main_page.wait_and_find_element(MainPageLocators.get_question_answer(number))

        assert answer.text == expected_answer, 'Ответ на вопрос не совпадает с ожидаемым'