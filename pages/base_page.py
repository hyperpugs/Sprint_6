import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"
    SCOOTER_IMG = (By.XPATH, ".//img[contains(@src,'scooter.png')]")
    HOME_PAGE_DIV = (By.XPATH, ".//div[contains(@class,'HomePage')]")
    FOOTER = (By.XPATH, ".//div[contains(@class,'FourPart')]")
    QUESTION = (By.XPATH, ".//div[contains(@id, 'heading-{0}')]")
    ANSWER = (By.XPATH, ".//div[contains(@id, 'panel-{0}')]")

    BUTTON_ORDER_IN_MIDDLE = (By.XPATH, ".//div[contains(@class,'FinishButton')]//button")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть страницу сайта "Яндекс.Самокат"')
    def open_the_page(self):
        self._open_the_page()

    @allure.step('Скролл страницы к футеру')
    def go_to_the_footer(self):
        self._go_to_element(self.FOOTER)

    @allure.step('Открыть страницу "Яндекс.Самокат" и скролл к футору')
    def open_the_the_page_and_go_to_the_footer(self):
        self._open_the_page()
        self.go_to_the_footer()

    @allure.step('Нажать на соответствующий вопрос')
    def click_on_question(self, variable):
        question_locator = self._modify_locator(self.QUESTION, variable)
        self._wait_and_click_on_element(question_locator)

    @allure.step('Нажать на кнопку "Заказать" в центре')
    def click_on_order_button_in_middle(self):
        self._go_to_element(self.BUTTON_ORDER_IN_MIDDLE)
        self._wait_and_click_on_element(self.BUTTON_ORDER_IN_MIDDLE)

    @allure.step('Проверка соответствия текста ответа')
    def check_text_answer_of_question(self, variable, expected_answer):
        answer_locator = self._modify_locator(self.ANSWER, variable)
        actual_answer = self._wait_and_find_element(answer_locator).text

        assert expected_answer == actual_answer, f'Ожидаемый ответ {expected_answer}, фактический — f{actual_answer}'