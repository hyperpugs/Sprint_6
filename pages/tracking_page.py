from pages.base_page import *

class TrackingPage(BasePage):
    @allure.step("Инициализируем браузер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверяем, что мы на странице с трекингом заказа")
    def wait_for_tracking_page(self):
        return self.wait_for_element_visible(TrackingPageLocators.cancel_button)

    @allure.step("Кликаем по слову 'Яндекс' в логотипе")
    def yandex_click(self):
        self.click_element(TrackingPageLocators.ya_logo)

    @allure.step("Кликаем по слову 'Самокат' в логотипе")
    def scooter_click(self):
        self.click_element(TrackingPageLocators.scooter_logo)
