from pages.base_page import *
from locators import *

class OrderCreatedPage(BasePage):
    @allure.step("Инициализируем браузер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ждём появления всплывающего окна с номером заказа")
    def wait_for_popup2(self):
        self.wait_for_element_visible(OrderCreatedPopupLocators.order_created_header)

    @allure.step("Кликаем на 'Посмотреть статус' для перехода к странице статуса заказа")
    def click_to_see_order_page(self):
        self.click_element(OrderCreatedPopupLocators.go_to_order_button)

    def popup_go_to_order(self):
        self.wait_for_popup2()
        self.click_to_see_order_page()