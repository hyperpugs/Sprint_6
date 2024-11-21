from pages.base_page import *

class ReceiverFormPage(BasePage):

    @allure.step("Инициализируем браузер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ждём, пока нужный заголовок станет видимым")
    def wait_until_receiver_form_visible(self):
        self.wait_for_element_visible(ReceiverFormLocators.receiver_header)

    @allure.step("Заполняем поле 'Имя'")
    def fill_in_name(self):
        self.enter_text(ReceiverFormLocators.name_field, "Юнги")

    @allure.step("Заполняем поле 'Фамилия'")
    def fill_in_surname(self):
        self.enter_text(ReceiverFormLocators.surname_field, "Мин")

    @allure.step("Заполняем поле 'Адрес'")
    def fill_in_address(self):
        self.enter_text(ReceiverFormLocators.address_field, "Бойцовая улица, 24с1")

    @allure.step("Выбираем станцию метро")
    def click_metro_station(self):
        self.click_element(ReceiverFormLocators.metro_station_field)
        self.click_element(ReceiverFormLocators.metro_station_button)

    @allure.step("Вводим номер телефона")
    def fill_in_phone_number(self):
        self.enter_text(ReceiverFormLocators.phone_field, "+79999999999")

    @allure.step("Кликаем на 'Далее'")
    def click_continue(self):
        self.click_element(ReceiverFormLocators.continue_button)

    @allure.step("Заполняем форму 'Для кого самокат'")
    def fill_in_receiver_form(self):
        self.wait_until_receiver_form_visible()
        self.fill_in_name()
        self.fill_in_surname()
        self.fill_in_address()
        self.click_metro_station()
        self.fill_in_phone_number()
        self.click_continue()