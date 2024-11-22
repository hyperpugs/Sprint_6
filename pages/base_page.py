
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:
    URL = None
    WAIT_TIME = 5
    LOGO_SCOOTER = (By.XPATH, ".//a[contains(@class,'LogoScooter')]")
    LOGO_YANDEX = (By.XPATH, ".//a[contains(@class,'LogoYandex')]")
    BUTTON_ORDER_IN_HEADER = (By.XPATH, ".//div[contains(@class,'Header')]//button[contains(text(),'Заказать')]")

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def _modify_locator(locator, variable):
        method, locator = locator
        locator = locator.format(variable)

        return method, locator

    def _open_the_page(self):
        self.driver.get(self.URL)

    def _wait_and_find_element(self, locator):
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def _wait_and_click_on_element(self, something_locator):
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.element_to_be_clickable(something_locator))
        self.driver.find_element(*something_locator).click()

    def _wait_of_url_changing(self):
        current_url = self.driver.current_url
        WebDriverWait(self.driver, self.WAIT_TIME).until(EC.url_changes(current_url))

    def _go_to_element(self, element):
        element = self._wait_and_find_element(element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажать на кнопку "Заказать" в футере')
    def click_on_order_button_in_header(self):
        self._wait_and_click_on_element(self.BUTTON_ORDER_IN_HEADER)

    @allure.step('Нажать на лого "Самокат" ')
    def click_on_logo_scooter(self):
        self._wait_and_click_on_element(self.LOGO_SCOOTER)

    @allure.step('Нажать на лого "Яндекс" ')
    def click_on_logo_yandex(self):
        self._wait_and_click_on_element(self.LOGO_YANDEX)

    def _set_value_to_field(self, field_locator, value):
        self._wait_and_click_on_element(field_locator)
        self._wait_and_find_element(field_locator).send_keys(value)

        actual_value = self._wait_and_find_element(field_locator).get_attribute('value')
        assert value == actual_value, (f"Значение в поле не совпадает введенному. Ожидаемое значение {value}, "
                                       f"фактическое - {actual_value}")

    def _press_enter_in_field(self, field_locator):
        self.driver.find_element(*field_locator).send_keys(Keys.RETURN)

    @allure.step('Проверка перехода на страницу оформления заказа')
    def check_is_it_order_page(self):
        assert EC.url_contains('order'), f'Переход не на страницу оформления заказа'

    @allure.step('Проверка перехода на страницу оформления заказа')
    def check_is_it_main_page(self):
        from pages.main_page import MainPage
        assert EC.url_to_be(MainPage.URL), f'Переход не на главную страницу'

    @allure.step('Проверка перехода на страницу Дзена')
    def check_is_it_dzen_page(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        self._wait_of_url_changing()
        assert EC.url_contains('dzen.ru'), "Переход не на страницу дзена"