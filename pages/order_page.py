import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    driver = None

    @allure.step('Заполнение первой страницы заказа')
    def fill_first_page(self, name, last_name, address, metro, phone):
        self.set_text_to_element(OrderPageLocators.FIELD_INPUT_NAME, name)
        self.set_text_to_element(OrderPageLocators.FIELD_INPUT_LAST_NAME, last_name)
        self.set_text_to_element(OrderPageLocators.FIELD_INPUT_ADDRESS, address)
        self.click_on_element(OrderPageLocators.FIELD_INPUT_METRO)
        self.set_metro(OrderPageLocators.COMBOBOX_METRO, metro)
        self.set_text_to_element(OrderPageLocators.FIELD_INPUT_PHONE, phone)

    @allure.step('Заполнение второй страницы заказа')
    def fill_second_page(self, date, period, color, comment):
        self.click_on_element(OrderPageLocators.FIELD_DATE)

        format_locator = self.create_locator(OrderPageLocators.CHANGE_DAY, date)
        self.click_on_element(format_locator)

        self.click_on_element(OrderPageLocators.FIELD_PERIOD)

        format_locator = self.create_locator(OrderPageLocators.FIELD_PERIOD_DROP_DOWN_OPTION, period)
        self.click_on_element(format_locator)

        format_locator = self.create_locator(OrderPageLocators.FIELD_COLOR, color)
        self.click_on_element(format_locator)

        self.set_text_to_element(OrderPageLocators.FIELD_COMMENT, comment)