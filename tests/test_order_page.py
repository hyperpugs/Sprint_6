import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderFormPage
class TestSmoke:
    @allure.title('Проверка оформления заказа с помощью кнопки в шапке сайта и переходы по лого')
    @allure.description('Проверяем оформления заказа по кнопке "Заказать" в шапке сайта, '
                        'проверяем переход на главную страницу «Самоката» с помощью логотипа «Самокат», '
                        'проверяем переход на главную страницу Дзена с помощью логотипа Яндекса')
    @pytest.mark.parametrize('data', [
        ["Дмитрий", "Иванов", "пр. Мира 2", "Лубянка", "77007009858", "02.10.2024", "сутки", "black",
         "Как получится"],
        ["Марго", "Иванова", "ул. Чекистов 5г", "Красные Ворота", "72888406506", "11.11.2024", "двое суток", "grey",
         "Утром"]])
    def test_order_button_in_footer_and_logo(self, driver, data):
        base_page = MainPage(driver)
        base_page.open_the_page()
        base_page.click_on_order_button_in_header()
        base_page.check_is_it_order_page()
        order_form_page = OrderFormPage(driver)
        order_form_page.place_order(*data)
        order_form_page.check_order_is_placed()
        base_page.click_on_logo_scooter()
        base_page.check_is_it_main_page()
        base_page.click_on_logo_yandex()
        base_page.check_is_it_dzen_page()

    @allure.title('Проверка оформления заказа с помощью кнопки в центре сайта и переходы по лого')
    @allure.description('Проверяем оформления заказа по кнопке "Заказать" в центре сайта, '
                        'проверяем переход на главную страницу «Самоката» с помощью логотипа «Самокат», '
                        'проверяем переход на главную страницу Дзена с помощью логотипа Яндекса')
    @pytest.mark.parametrize('data', [
        ["Иван", "Иванов", "ул. Старовиленская 10а", "Черкизовская", "74561234567", "26.10.2024", "четверо суток",
         "black", "Вечером"],
        ["Алина", "Игнатова", "пл. Свободы 2а", "Сокольники", "76146399170", "21.10.2024", "пятеро суток", "grey",
         "К 14:00"]])
    def test_order_button_in_middle_and_logo(self, driver, data):
        base_page = MainPage(driver)
        base_page.open_the_page()
        base_page.click_on_order_button_in_middle()
        base_page.check_is_it_order_page()
        order_form_page = OrderFormPage(driver)
        order_form_page.place_order(*data)
        order_form_page.check_order_is_placed()
        base_page.click_on_logo_scooter()
        base_page.check_is_it_main_page()
        base_page.click_on_logo_yandex()
        base_page.check_is_it_dzen_page()