import allure
from locators.main_page_locator import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажать на вопрос внизу страницы')
    def click_to_question(self, number):
        click_question = MainPageLocators.get_question_button(number)
        self.click_to_cookies()
        self.scroll_to_element(click_question)

        self.wait_and_find_element(click_question)
        self.wait_and_click_element(click_question)

    @allure.title('Прокрутка до последнего вопроса на странице')
    def scroll_to_last_question(self):
        self.scroll_to_element(MainPageLocators.LAST_QUESTION)