import pytest
import allure
from configs.urls import ORDER_PAGE, ORDER_STATUS_PAGE
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators import YandexOrderPage
from configs.test_data import YandexOrderPageData as order_data


@allure.epic('Тестирование интерфейса страницы "Оформление заказа"')
@allure.parent_suite('Создание заказа')
class TestYandexOrderPage:
    @allure.suite('Заполнение данных на странице "Для кого самокат"')
    @allure.feature('Заполнения данных пользователя при создании заказа на этапе ввода данных')
    @allure.story('Passed проверка заполнения данных')
    @allure.title('Заполнение данных и переход с этапа "Для кого самокат" на этап "Про аренду"')
    @allure.description('Проверка, что после ввода валидных данных, '
                        'нажатии "Далее" происходит переход на следующий этап "Про аренду"')
    def test_order_page(self, driver):
        yandex_order_page = OrderPage(driver)
        yandex_order_page.go_to_site(ORDER_PAGE)
        yandex_home_page = HomePage(driver)
        yandex_home_page.click_cookie_accept()
        yandex_order_page.fill_user_data(order_data.data_sets['data_set1'])
        yandex_order_page.go_next()
        assert len(yandex_order_page.find_elements(YandexOrderPage.order_button)) > 0

    @allure.suite('Заполнение данных на странице "Про аренду"')
    @allure.feature('Заполнения данных пользователя при создании заказа на этапе ввода данных')
    @allure.story('Passed проверка заполнения данных')
    @allure.title('Заполнение данных на этапе "Про аренду" и оформление заказа')
    @allure.description('Проверка, что после ввода валидных данных, '
                        'нажатии "Далее" происходит переход на следующий этап "Про аренду"'
                        'нажатии кнопки "Заказать", открывается окно с подтверждением заказа')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_full_order_page(self, driver, data_set):
        yandex_order_page = OrderPage(driver)
        yandex_order_page.go_to_site(ORDER_PAGE)
        yandex_home_page = HomePage(driver)
        yandex_home_page.click_cookie_accept()
        yandex_order_page.fill_user_data(order_data.data_sets[data_set])
        yandex_order_page.go_next()
        yandex_order_page.fill_rent_data(order_data.data_sets[data_set])
        yandex_order_page.click_order()
        yandex_order_page.click_accept_order()
        assert len(yandex_order_page.find_elements(YandexOrderPage.order_info)) > 0

    @allure.suite('Создание заказа')
    @allure.feature('Полный путь создания заказа')
    @allure.story('Оформление заказа и просмотр страницы заказа')
    @allure.title('Оформление заказа и переход на страницу с заказм')
    @allure.description('Проверка что при успешном оформлении заказа, заказ отображается на странице "Статус заказа" ')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_with_order_status(self, driver, data_set):
        yandex_order_page = OrderPage(driver)
        yandex_order_page.go_to_site(ORDER_PAGE)
        yandex_home_page = HomePage(driver)
        yandex_home_page.click_cookie_accept()
        yandex_order_page.fill_user_data(order_data.data_sets[data_set])
        yandex_order_page.go_next()
        yandex_order_page.fill_rent_data(order_data.data_sets[data_set])
        yandex_order_page.click_order()
        yandex_order_page.click_accept_order()
        order_number = yandex_order_page.get_order_number()
        yandex_order_page.click_go_to_status()
        current_url = yandex_order_page.current_url()
        assert (ORDER_STATUS_PAGE in current_url) and (order_number in current_url)