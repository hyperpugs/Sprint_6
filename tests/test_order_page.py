
import allure
import pytest
from pages.main_page import MainPage
from pages.order_form_page import OrderFormPage


class TestSmoke:
    @allure.title('Проверка оформления заказа с помощью кнопки в шапке сайта и переходы по лого')
    @allure.description('Проверяем оформления заказа по кнопке "Заказать" в шапке сайта, '
                        'проверяем переход на главную страницу «Самоката» с помощью логотипа «Самокат», '
                        'проверяем переход на главную страницу Дзена с помощью логотипа Яндекса')
    @pytest.mark.parametrize('data', [
        ["Михаил", "Иванов", "пр. Независимости 116", "Аэропорт", "77007009858", "01.09.2024", "сутки", "black",
         "После обеда"],
        ["Татьяна", "Петрова", "ул. Сурганова 2в", "Международная", "72888406506", "10.10.2024", "двое суток", "grey",
         "C утра"]])
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
        ["Александр", "Волков", "ул. Старовиленская 10а", "Римская", "74544862860", "05.09.2024", "шестеро суток",
         "black", "Вечером"],
        ["Анна", "Смирнова", "пл. Свободы 2а", "Балтийская", "76146399170", "19.09.2024", "семеро суток", "grey",
         "К 15:00"]])
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