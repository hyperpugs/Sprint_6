import re
from locators import YandexOrderPage as Locators
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

    @allure.step('Ввод имени')
    def input_first_name(self, first_name: str):
        return self.find_element(Locators.first_name_input).send_keys(first_name)

    @allure.step('Ввод фамилии')
    def input_last_name(self, last_name: str):
        return self.find_element(Locators.last_name_input).send_keys(last_name)

    @allure.step('Ввод адреса')
    def input_address(self, address: str):
        return self.find_element(Locators.address_input).send_keys(address)

    @allure.step('Выбор метро')
    def choose_metro(self, metro_name: str):
        self.find_element(Locators.metro_input).click()
        return self.find_element(Locators.METRO_HINT_BUTTON(metro_name)).click()

    @allure.step('Ввод номера телефона')
    def input_telephone_number(self, telephone_number: str):
        return self.find_element(Locators.telephone_number).send_keys(telephone_number)

    @allure.step('Перейти на следующий этап')
    def go_next(self):
        return self.find_element(Locators.next_button).click()

    @allure.step('Ввод даты')
    def input_date(self, date: str):
        return self.find_element(Locators.date_field).send_keys(date)

    @allure.step('Выбор срока аренды')
    def choose_rental_period(self, option: int):
        self.find_element(Locators.rental_period).click()
        return self.find_elements(Locators.rental_period_list)[option].click()

    @allure.step('Выбор цвета')
    def choose_color(self, option: int):
        return self.find_elements(Locators.color)[option].click()

    @allure.step('Комментарий для курьера')
    def input_comment(self, comment_text):
        return self.find_element(Locators.comment_for_courier).send_keys(comment_text)

    @allure.step('Нажать "Заказать"')
    def click_order(self):
        return self.find_element(Locators.order_button).click()

    @allure.step('Подтвердить заказ')
    def click_accept_order(self):
        return self.find_element(Locators.accept_button).click()

    @allure.step('Вычитать номер заказа')
    def get_order_number(self):
        about_order_text = self.find_element(Locators.order_info).text
        return ''.join(re.findall('[0-9]', about_order_text))

    @allure.step('Перейти к статусу заказа')
    def click_go_to_status(self):
        return self.find_element(Locators.status_button).click()

    @allure.step('Заполнить данные на этапе "Для кого самокат"')
    def fill_user_data(self, data_set: dict):
        self.input_first_name(data_set['first_name'])
        self.input_last_name(data_set['last_name'])
        self.input_address(data_set['address'])
        self.choose_metro(data_set['metro_name'])
        self.input_telephone_number(data_set['telepthone_number'])

    @allure.step('Заполнить данные на этапе "Про аренду"')
    def fill_rent_data(self, data_set: dict):
        self.input_date(data_set['date'])
        self.choose_rental_period(data_set['rental_period'])
        for option in data_set['color']:
            self.choose_color(option)
        self.input_comment(data_set['comment_for_courier'])