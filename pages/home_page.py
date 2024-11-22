import allure
from pages.base_page import BasePage
from locators import BasePageLocator
from selenium.webdriver.support.wait import WebDriverWait
from locators import YandexHomePage as Locators
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    @allure.step('Нажать на кнопку заказа в верхней части страницы')
    def click_top_order_button(self):
        return self.find_element(Locators.top_order_button).click()

    @allure.step('Нажать на кнопку заказа в нижней части страницы')
    def click_bottom_order_button(self):
        return self.find_element(Locators.bottom_order_button).click()

    @allure.step('Нажать на вопрос в "Вопросы о важном"')
    def click_question(self, question_number: int):
        a = self.find_elements(Locators.FAQ_button, 10)
        return a[question_number].click()

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))

    @allure.step('Перейти на страницу яндекса')
    def click_yandex_button(self):
        return self.find_element(BasePageLocator.logo_button).click()

    @allure.step('Нажать на логотип "Самокат"')
    def click_scooter_button(self):
        return self.find_element(BasePageLocator.scooter_logo).click()

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        return self.find_element(BasePageLocator.cookie_accept).click()