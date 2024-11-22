import allure
import pytest
from configs.test_data import YandexHomePageFAQ
from pages.main_page import HomePage
from locators import YandexHomePage


@allure.epic('Main page')
@allure.parent_suite('Домашняя страница')
@allure.suite('FAQ')
class TestYandexFAQ:
    @allure.feature('Вопрос/ответ на Домашней страницы')
    @allure.story('При нажатии на вопрос в разделе "Вопросы о важном" раскрывается ответ.')
    @allure.title('При нажатии на вопрос раскрывается ответ ')
    @allure.description('Проверка что при нажатии на вопрос, '
                        'данный вопрос открывается и текст в нем соответствует выводу')
    @pytest.mark.parametrize(
        "question,answer,expected_answer",
        [
            (0, 0, YandexHomePageFAQ.ANS_1),
            (1, 1, YandexHomePageFAQ.ANS_2),
            (2, 2, YandexHomePageFAQ.ANS_3),
            (3, 3, YandexHomePageFAQ.ANS_4),
            (4, 4, YandexHomePageFAQ.ANS_5),
            (5, 5, YandexHomePageFAQ.ANS_6),
            (6, 6, YandexHomePageFAQ.ANS_7),
            (7, 7, YandexHomePageFAQ.ANS_8),
        ]
    )
    def test_questions_page_click_show_answer(self, driver, question, answer, expected_answer):
        yandex_home_page = HomePage(driver)
        yandex_home_page.go_to_site()
        yandex_home_page.click_cookie_accept()
        yandex_home_page.click_question(question_number=question)
        answer = yandex_home_page.find_element(YandexHomePage.FAQ_answer(answer_number=answer))

        assert answer.is_displayed() and answer.text == expected_answer