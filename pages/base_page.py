import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вызов URL')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('ожидание элемента {locator}')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу {locator} с предварительным ожиданием')
    def click_on_element(self, locator):
        self.wait_element(locator).click()

    @allure.step('Клик по элементу {locator}, без ожидания')
    def click_on_element1(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввод текста {set_text}  в элемент {locator}')
    def set_text_to_element(self, locator, set_text):
        self.wait_element(locator).send_keys(set_text)

    @allure.step('Получение текста элемента {locator}')
    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Переход в конец страницы')
    def scroll_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Создание локатора через форматирование')
    def create_locator(self, locator, num):
        return (locator[0], locator[1].format(num))

    @allure.step('Установка значения Метро')
    def set_metro(self, locator, set_text):
        element = self.wait_element(locator)
        element.send_keys(set_text)
        element.send_keys(Keys.DOWN)
        element.send_keys(Keys.ENTER)
