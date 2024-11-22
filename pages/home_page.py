import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    driver = None

    @allure.step('Нажатие на элемент - {locator}')
    def click_questions(self, locator):
        self.click_on_element(locator)

    @allure.step('Получение {num} ответа')
    def check_answer(self, num):
        question = self.create_locator(HomePageLocators.QUESTION_N, num)
        answer = self.create_locator(HomePageLocators.ANSWER_N, num)
        self.click_on_element(question)
        self.wait_element(answer)
        return self.get_text_from_element(answer)