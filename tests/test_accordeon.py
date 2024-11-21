from selenium.webdriver.firefox import webdriver
from pages.order_page import *
import pytest
from locators.order_page_locator import *

class TestLandingAccordeon:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title("Проверяем, что раскрываются все пункты в блоке вопросов и ответов")
    @pytest.mark.parametrize("question, answer",
                             [
                                 [OrderPageLocators.accordeon_1, OrderPageLocators.accordeon_text_1],
                                 [OrderPageLocators.accordeon_2, OrderPageLocators.accordeon_text_2],
                                 [OrderPageLocators.accordeon_3, OrderPageLocators.accordeon_text_3],
                                 [OrderPageLocators.accordeon_4, OrderPageLocators.accordeon_text_4],
                                 [OrderPageLocators.accordeon_5, OrderPageLocators.accordeon_text_5],
                                 [OrderPageLocators.accordeon_6, OrderPageLocators.accordeon_text_6],
                                 [OrderPageLocators.accordeon_7, OrderPageLocators.accordeon_text_7],
                                 [OrderPageLocators.accordeon_8, OrderPageLocators.accordeon_text_8]
                             ])
    def test_questions_and_answers_block(self, question, answer):
        main = OrderPage(self.driver)
        main.navigate(links.MAIN_URL)
        main.scroll_to_accordeon()
        main.wait_for_accordeon_in_view()
        main.click_element(question)
        result = main.wait_for_element_visible(answer)
        assert result.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()