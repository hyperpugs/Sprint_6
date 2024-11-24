import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    @allure.step('Открытие страницы по URL: {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Клик на логотип «Самокат»')
    def click_scooter_logo(self):
        self.click_on_element(HomePageLocators.LOGO_SCOOTER)

    @allure.step('Проверка URL текущей страницы')
    def assert_current_url(self, expected_url):
        assert self.driver.current_url == expected_url, f'Ожидался URL {expected_url}, но получен {self.driver.current_url}'

    @allure.step('Клик на кнопку - {locator}')
    def click_button(self, locator):
        self.click_on_element(locator)

    @allure.step('Клик на кнопку "Куки"')
    def click_cookies_button(self):
        self.click_on_element(HomePageLocators.BUTTON_COOKIES)

    @allure.step('Получение {num} ответа на вопрос')
    def check_answer(self, num):
        question = self.create_locator(HomePageLocators.QUESTION_N, num)
        answer = self.create_locator(HomePageLocators.ANSWER_N, num)
        self.click_on_element(question)
        self.wait_element(answer)
        return self.get_text_from_element(answer)

    @allure.step('Клик на элемент вопроса {num}')
    def click_question(self, num):
        question = self.create_locator(HomePageLocators.QUESTION_N, num)
        self.click_on_element(question)

    def wait_for_new_window_to_open(self):
        WebDriverWait(self.driver, 10).until(EC.new_window_is_opened(self.driver.window_handles))

    def switch_to_latest_window(self):
        window_after = self.driver.window_handles[-1]
        self.driver.switch_to.window(window_after)

    def get_current_url(self):
        return self.driver.current_url