import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls
from locators.order_page_locator import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.title('Выбор станции из выпадающего списка')
    def click_to_dropdown(self, locator):
        self.wait_and_click_element(OrderPageLocators.STATION_INPUT)
        self.wait_and_click_element(locator)

    @allure.title('Переход на страницу заказа')
    def go_to_order(self, button):
        self.scroll_to_element(button)
        self.wait_and_find_element(button)
        self.wait_and_click_element(button)
        self.assert_url_change(Urls.SCOOTER_URL)

    @allure.title('Заполнение данных для оформления заказа')
    def fill_order(self, params, station):
        self.wait_and_send_keys(OrderPageLocators.NAME_INPUT, params[0])
        self.wait_and_send_keys(OrderPageLocators.SURNAME_INPUT, params[1])
        self.wait_and_send_keys(OrderPageLocators.ADDRESS_INPUT, params[2])
        self.click_to_dropdown(station)
        self.wait_and_send_keys(OrderPageLocators.PHONE_INPUT, params[3])
        self.wait_and_click_element(OrderPageLocators.NEXT_BUTTON)
        self.wait_and_click_element(OrderPageLocators.DELIVERY_DATE_INPUT)
        self.wait_and_click_element(params[4])
        self.wait_and_click_element(OrderPageLocators.RENTAL_TIME_INPUT)
        self.wait_and_click_element(params[5])
        self.wait_and_click_element(params[6])
        self.wait_and_send_keys(OrderPageLocators.COMMENT_INPUT, params[7])
        self.wait_and_click_element(OrderPageLocators.ORDER_BUTTON_COMPLETE)

    @allure.title('Ожидание смены адреса')
    def assert_url_change(self, url):
        WebDriverWait(self.driver, self.timer).until(EC.url_changes(url))