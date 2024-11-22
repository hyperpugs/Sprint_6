import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderFormPage(BasePage):
    URL = 'https://qa-scooter.praktikum-services.ru/order'
    ORDER_HEADER_FOR_WHO = (By.XPATH, ".//div[contains(text(),'Для кого')]")
    ORDER_HEADER_RENTAL = (By.XPATH, ".//div[contains(text(),'Про аренду')]")
    FIELD_FIRST_NAME = (By.XPATH, ".//input[contains(@placeholder, 'Имя')]")
    FIELD_LAST_NAME = (By.XPATH, ".//input[contains(@placeholder, 'Фамилия')]")
    FIELD_ADDRESS = (By.XPATH, ".//input[contains(@placeholder, 'Адрес')]")
    FIELD_SUBWAY_STATION = (By.XPATH, ".//input[contains(@placeholder, 'метро')]")
    STATION_LOCATOR = (By.XPATH, ".//div[contains(text(), '{0}')]")
    FIELD_PHONE_NUMBER = (By.XPATH, ".//input[contains(@placeholder, 'Телефон')]")
    BUTTON_NEXT = (By.XPATH, ".//button[contains(text(), 'Далее')]")
    FIELD_DELIVERY_DATE = (By.XPATH, ".//input[contains(@placeholder, 'Когда привезти')]")
    FIELD_RENTAL_TIME = (By.XPATH, ".//div[contains(@class, 'Dropdown-placeholder')]")
    FIELD_COMMENTS = (By.XPATH, ".//input[contains(@placeholder, 'Комментарий')]")
    BUTTON_ORDER = (By.XPATH, ".//button[contains(@class, 'Middle') and contains(text(), 'Заказать')]")
    CONFIRM_HEADER = (By.XPATH, ".//div[contains(@class, 'ModalHeader')]")
    BUTTON_ACCEPT_ORDER = (By.XPATH, ".//button[contains(text(),'Да')]")
    CONFIRMED_HEADER = (By.XPATH, ".//div[contains(text(),'оформлен')]")
    BUTTON_STATUS_ORDER = (By.XPATH, './/button[contains(text(),"статус")]')
    STATUS_ORDER = (By.XPATH, ".//div[contains(@class,'Content')]")
    CHECK_BOX = (By.ID, '{0}')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Заполнить поле "Имя" ')
    def set_first_name(self, first_name):
        self._set_value_to_field(self.FIELD_FIRST_NAME, first_name)

    @allure.step('Заполнить поле "Фамилия" ')
    def set_last_name(self, last_name):
        self._set_value_to_field(self.FIELD_LAST_NAME, last_name)

    @allure.step('Заполнить поле "Адрес" ')
    def set_address(self, address):
        self._set_value_to_field(self.FIELD_ADDRESS, address)

    @allure.step('Заполнить поле "Станция метро" ')
    def set_subway_station(self, station_name):
        self._wait_and_click_on_element(self.FIELD_SUBWAY_STATION)

        station = self._modify_locator(self.STATION_LOCATOR, station_name)
        self._go_to_element(station)
        self._wait_and_click_on_element(station)

        assert station_name in self._wait_and_find_element(self.FIELD_SUBWAY_STATION).get_attribute('value'), \
            "Отображается неверная станция"

    @allure.step('Заполнить поле "Телефон" ')
    def set_phone_number(self, phone_number):
        self._set_value_to_field(self.FIELD_PHONE_NUMBER, phone_number)

    @allure.step('Нажать на кнопку "Далее" ')
    def click_on_button_next(self):
        self._wait_and_click_on_element(self.BUTTON_NEXT)

    @allure.step('Проверка перехода в раздел "Про аренду" при оформлении заказа')
    def check_is_it_section_about_rental(self):
        assert self._wait_and_find_element(self.ORDER_HEADER_RENTAL).is_displayed(), \
            "Оформление не перешло на раздел 'Про аренду' "

    @allure.step('Заполнить раздел "Для кого самокат" ')
    def set_section_for_who(self, first_name, last_name, address, subway_station, phone_number):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_subway_station(subway_station)
        self.set_phone_number(phone_number)
        self.click_on_button_next()
        self.check_is_it_section_about_rental()

    @allure.step('Заполнить поле "Когда привезти самокат" ')
    def set_delivery_date(self, date):
        self._set_value_to_field(self.FIELD_DELIVERY_DATE, date)
        self._press_enter_in_field(self.FIELD_DELIVERY_DATE)

    @allure.step('Заполнить поле "Срок аренды" ')
    def set_rental_time(self, rental_time):
        self._wait_and_click_on_element(self.FIELD_RENTAL_TIME)

        rental_time_locator = (By.XPATH, f".//div[contains(@class, 'Dropdown') and contains(text(), '{rental_time}')]")
        self._go_to_element(rental_time_locator)
        self._wait_and_click_on_element(rental_time_locator)

        assert rental_time in self._wait_and_find_element(self.FIELD_RENTAL_TIME).text

    @allure.step('Выбрать чекбокс "Цвет самоката" ')
    def set_color(self, color):
        check_box = self._modify_locator(self.CHECK_BOX, color)
        self._wait_and_click_on_element(check_box)

        assert self._wait_and_find_element(check_box).is_selected(), "Чекбокс не выбирается"

    @allure.step('Заполнить комментарий')
    def set_comments(self, comments):
        self._set_value_to_field(self.FIELD_COMMENTS, comments)

    @allure.step('Нажать на кнопку "Заказать" ')
    def click_on_button_order(self):
        self._wait_and_click_on_element(self.BUTTON_ORDER)

    @allure.step('Проверка перехода в окно подтверждения заказа')
    def check_is_it_confirm_alert(self):
        assert self._wait_and_find_element(self.CONFIRM_HEADER).is_displayed(), 'Окно подтверждения заказа не появилось'

    @allure.step('Нажать на кнопку "Да" ')
    def click_on_button_accept_order(self):
        self._wait_and_click_on_element(self.BUTTON_ACCEPT_ORDER)

    @allure.step('Проверка перехода в окно подтверждения заказа')
    def check_is_it_confirmed_alert(self):
        assert self._wait_and_find_element(self.CONFIRMED_HEADER).is_displayed(), \
            'Окно подтвержденного заказа не появилось'

    @allure.step('Заполнить раздел "Про аренду" ')
    def set_section_about_rental(self, date, rental_time, color, comments):
        self.set_delivery_date(date)
        self.set_rental_time(rental_time)
        self.set_color(color)
        self.set_comments(comments)
        self.click_on_button_order()
        self.check_is_it_confirm_alert()
        self.click_on_button_accept_order()
        self.check_is_it_confirmed_alert()

    @allure.step('Оформить заказ ')
    def place_order(self, first_name, last_name, address, subway_station, phone_number, date, rental_time, color,
                    comments):
        self.set_section_for_who(first_name, last_name, address, subway_station, phone_number)
        self.set_section_about_rental(date, rental_time, color, comments)

    @allure.step('Нажать на кнопку "Посмотреть статус" ')
    def click_on_button_status_order(self):
        self._wait_and_click_on_element(self.BUTTON_STATUS_ORDER)

    @allure.step('Проверка оформился ли заказ ')
    def check_order_is_placed(self):
        self.click_on_button_status_order()

        assert self._wait_and_find_element(self.STATUS_ORDER).is_displayed(), "Заказ оформлен "