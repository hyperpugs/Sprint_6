from pages.base_page import *
from locators import *

class DzenPage(BasePage):
    @allure.step("Инициализируем браузер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Дожидаемся видимости логотипа 'дзена' на экране, чтобы убедиться, что мы на странице 'Дзена'")
    def wait_for_dzen_logo_visible(self):
        self.wait_for_element_visible(DzenLocators.yandex_search_logo)
