from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from locators import *
import allure
from selenium.common import NoSuchElementException

class BasePage:
    @allure.step("Инициализируем браузер")
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Открываем нужный URL")
    def navigate (self, url):
        self.driver.get(url)

    @allure.step("Ищем нужный элемент")
    def find_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Ищем нужные элементы")
    def find_elements(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Кликаем по нужному элементу")
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Заполняем поле нужным значением")
    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step("Ждём, пока элемент станет видимым")
    def wait_for_element_visible(self, locator, timeout = 30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Переключаемся на открывшуюся вкладку")
    def switch_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

    @allure.step("Соглашаемся с куками, чтобы они не перекрывали элемент")
    def cookie_close(self):
        try:
            close_button = self.find_element(Locators.cookie_button)
            close_button.click()
        except NoSuchElementException:
            pass

    @allure.step("Дожидаемся видимости иконки 'лупа' на экране, чтобы убедиться, что мы на странице 'Дзена'")
    def wait_for_dzen_logo_visible(self):
        self.wait_for_element_visible(Locators.yandex_search_logo)

