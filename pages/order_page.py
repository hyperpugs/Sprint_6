from pages.base_page import *

#элементы страницы
class OrderPage(BasePage):
    #Форма "Для кого самокат"
    @allure.step("Инициализируем браузер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажимаем на 'Заказать' на главной вверху страницы")
    def go_to_order_top(self):
        self.click_element(OrderPageLocators.top_order_button)

    @allure.step("Прокручиваем до кнопки 'Заказать' внизу страницы")
    def scroll_to_bottom(self):
        element = self.find_element(OrderPageLocators.bottom_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Нажимаем на 'Заказать' на главной вверху страницы")
    def go_to_order_bottom(self):
        self.click_element(OrderPageLocators.bottom_order_button)

    @allure.step("Дожидаемся видимости кнопки 'Заказать' внизу страницы")
    def wait_for_bottom_button_visible(self):
        self.wait_for_element_visible(OrderPageLocators.bottom_order_button)

    @allure.step("Прокручиваем до блока с вопросами и ответами")
    def scroll_to_accordeon(self):
        element = self.find_element(OrderPageLocators.accordeon_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Убеждаемся, что доскроллили до блока с вопросами и ответами")
    def wait_for_accordeon_in_view(self):
        self.wait_for_element_visible(OrderPageLocators.accordeon_1)


