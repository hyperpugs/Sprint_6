import urls
import pytest
from pages.order_page import *
from locators import *
from selenium import webdriver
from selenium.webdriver.firefox import webdriver


class TestFaq:
    driver = None

    @allure.title("Проверяем, что раскрываются все пункты в блоке вопросов и ответов")
    @pytest.mark.parametrize("question, answer",
                             [
                                 [Locators.faq_1, Locators.faq_text_1],
                                 [Locators.faq_2, Locators.faq_text_2],
                                 [Locators.faq_3, Locators.faq_text_3],
                                 [Locators.faq_4, Locators.faq_text_4],
                                 [Locators.faq_5, Locators.faq_text_5],
                                 [Locators.faq_6, Locators.faq_text_6],
                                 [Locators.faq_7, Locators.faq_text_7],
                                 [Locators.faq_8, Locators.faq_text_8]
                             ])
    def test_questions_and_answers_block(self, question, answer, driver):
        faq = OrderPage(driver)
        faq.navigate(urls.MAIN_URL)
        faq.scroll_to_accordeon()
        faq.wait_for_accordeon_in_view()
        faq.click_element(question)
        result = faq.wait_for_element_visible(answer)
        assert result.is_displayed()
