from selenium.webdriver import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.base_page import *
import urls

#элементы страницы
class OrderPage(BasePage):
    #Форма "Для кого самокат"
    @allure.step("Инициализируем браузер")
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Нажимаем на 'Заказать' на главной вверху страницы")
    def go_to_order_top(self):
        self.click_element(Locators.top_order_button)

    @allure.step("Прокручиваем до кнопки 'Заказать' внизу страницы")
    def scroll_to_bottom(self):
        element = self.find_element(Locators.bottom_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Нажимаем на 'Заказать' на главной вверху страницы")
    def go_to_order_bottom(self):
        self.click_element(Locators.bottom_order_button)

    @allure.step("Дожидаемся видимости кнопки 'Заказать' внизу страницы")
    def wait_for_bottom_button_visible(self):
        self.wait_for_element_visible(Locators.bottom_order_button)

    @allure.step("Прокручиваем до блока с вопросами и ответами")
    def scroll_to_accordeon(self):
        element = self.find_element(Locators.faq_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Убеждаемся, что доскроллили до блока с вопросами и ответами")
    def wait_for_accordeon_in_view(self):
        self.wait_for_element_visible(Locators.faq_1)

    @allure.step("Ждём появления всплывающего окна 'Хотите оформить заказ?'")
    def wait_for_popup1(self):
        self.wait_for_element_visible(Locators.order_confirm_header)

    @allure.step("Нажимаем 'Да' во всплывающем окне")
    def click_yes(self):
        self.click_element(Locators.order_confirm_yes_button)

    def popup_click_yes(self):
        self.wait_for_popup1()
        self.click_yes()

    @allure.step("Ждём появления всплывающего окна с номером заказа")
    def wait_for_popup2(self):
        self.wait_for_element_visible(Locators.order_created_header)

    @allure.step("Кликаем на 'Посмотреть статус' для перехода к странице статуса заказа")
    def click_to_see_order_page(self):
        self.click_element(Locators.go_to_order_button)

    def popup_go_to_order(self):
        self.wait_for_popup2()
        self.click_to_see_order_page()

    @allure.step("Ждём, пока нужный заголовок станет видимым")
    def wait_until_receiver_form_visible(self):
        self.wait_for_element_visible(Locators.receiver_header)

    @allure.step("Заполняем поле 'Имя'")
    def fill_in_name(self):
        self.enter_text(Locators.name_field, "Юнги")

    @allure.step("Заполняем поле 'Фамилия'")
    def fill_in_surname(self):
        self.enter_text(Locators.surname_field, "Мин")

    @allure.step("Заполняем поле 'Адрес'")
    def fill_in_address(self):
        self.enter_text(Locators.address_field, "Бойцовая улица, 24с1")

    @allure.step("Выбираем станцию метро")
    def click_metro_station(self):
        self.click_element(Locators.metro_station_field)
        self.click_element(Locators.metro_station_button)

    @allure.step("Вводим номер телефона")
    def fill_in_phone_number(self):
        self.enter_text(Locators.phone_field, "+79999999999")

    @allure.step("Кликаем на 'Далее'")
    def click_continue(self):
        self.click_element(Locators.continue_button)

    @allure.step("Заполняем форму 'Для кого самокат'")
    def fill_in_receiver_form(self):
        self.wait_until_receiver_form_visible()
        self.fill_in_name()
        self.fill_in_surname()
        self.fill_in_address()
        self.click_metro_station()
        self.fill_in_phone_number()
        self.click_continue()


    @allure.step("Ждём, пока нужный заголовок станет видимым")
    def wait_until_rent_form_visible(self):
        self.wait_for_element_visible(Locators.rent_header)

    @allure.step("Заполняем дату")
    def fill_in_date(self):
        self.enter_text(Locators.date_field, "31.12.2024")

    @allure.step("Прожимаем Enter после ввода даты")
    def press_enter_date(self):
        self.enter_text(Locators.date_field, Keys.ENTER)

    @allure.step("Выбираем длительность аренды")
    def pick_duration(self):
        self.click_element(Locators.rent_time_field)
        self.wait_for_element_visible(Locators.rent_picker)
        self.click_element(Locators.rent_picker)

    @allure.step("Выбираем чёрный цвет самоката")
    def pick_colour_black(self):
        self.click_element(Locators.scooter_colour_black)

    @allure.step("Выбираем серый цвет самоката")
    def pick_colour_grey(self):
        self.click_element(Locators.scooter_colour_grey)

    @allure.step("Нажимаем 'Заказать'")
    def click_order_at_rent_details(self):
        self.click_element(Locators.order_button)


    @allure.step("Заполняем форму 'Про аренду'")
    def fill_in_rent_form(self):
        self.wait_until_rent_form_visible()
        self.fill_in_date()
        self.press_enter_date()
        self.pick_duration()
        self.pick_colour_black()
        self.click_order_at_rent_details()


    @allure.step("Проверяем, что мы на странице с трекингом заказа")
    def wait_for_tracking_page(self):
        return self.wait_for_element_visible(Locators.cancel_button)

    @allure.step("Кликаем по слову 'Яндекс' в логотипе")
    def yandex_click(self):
        self.click_element(Locators.ya_logo)

    @allure.step("Кликаем по слову 'Самокат' в логотипе")
    def scooter_click(self):
        self.click_element(Locators.scooter_logo)


    @allure.step("Проверяем, что мы на странице с трекингом заказа")
    def wait_for_tracking_page(self):
        return self.wait_for_element_visible(Locators.cancel_button)


    @allure.step("Проверка url")
    def check_url_samokat(self):
        expected_url = urls.MAIN_URL
        assert self.driver.current_url == expected_url

    @allure.step("Дожидаемся видимости иконки 'лупа' на экране, чтобы убедиться, что мы на странице 'Дзена'")
    def wait_for_dzen_logo_visible(self):
        self.wait_for_element_visible(Locators.yandex_search_logo)

    @allure.step("Дожидаемся видимости текста")
    def check_icon_dzen(self):
        assert self.driver.find_element(Locators.dzen_icon) == Locators.dzen_icon
