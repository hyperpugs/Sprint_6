import allure
import pytest

from data_for_test import URL_ORDER_PAGE, URL_STATUS_PAGE, ORDER_GOOD, SET_FOR_ORDER
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.feature('Страница заказа')
    @allure.title('Проверка формы заказа')
    @allure.description('Заказ самоката. Нужно проверить весь флоу позитивного сценария с двумя наборами данных '
                        'Нажать кнопку «Заказать». Заполнить форму заказа.Проверить, '
                        'что появилось всплывающее окно с сообщением об успешном создании заказа.,так же проверяется '
                        'переход к просмотру заказа')
    @pytest.mark.parametrize('data_set_first, data_set_second', SET_FOR_ORDER)
    def test_order(self, driver, data_set_first, data_set_second):
        order_page = OrderPage(driver)
        order_page.get_url(URL_ORDER_PAGE)
        order_page.click_on_element(HomePageLocators.BUTTON_COOKIES)
        order_page.fill_first_page(*data_set_first)
        order_page.click_on_element1(OrderPageLocators.BUTTON_NEXT)
        order_page.fill_second_page(*data_set_second)
        order_page.click_on_element(HomePageLocators.BUTTON_ORDER_SECOND)
        order_page.click_on_element(OrderPageLocators.BUTTON_YES)
        order_page.wait_element(OrderPageLocators.TEXT_GOOD_ORDER)
        assert ORDER_GOOD in order_page.get_text_from_element(OrderPageLocators.TEXT_GOOD_ORDER)
        order_page.click_on_element(OrderPageLocators.WATCH_STATUS)
        assert URL_STATUS_PAGE in driver.current_url