from pages.base_page import *
from locators import *

class OrderConfirmPage(BasePage):
    @allure.step("Инициализируем браузер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ждём появления всплывающего окна 'Хотите оформить заказ?'")
    def wait_for_popup1(self):
        self.wait_for_element_visible(OrderConfirmPopupLocators.order_confirm_header)

    @allure.step("Нажимаем 'Да' во всплывающем окне")
    def click_yes(self):
        self.click_element(OrderConfirmPopupLocators.order_confirm_yes_button)

    def popup_click_yes(self):
        self.wait_for_popup1()
        self.click_yes()