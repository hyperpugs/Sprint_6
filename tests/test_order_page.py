import allure
import pytest
from data import OrderData
from locators.order_page_locator import OrderPageLocators
from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Оформление заказа по кнопке сверху/снизу страницы')
    @pytest.mark.parametrize(OrderData.PARAM, OrderData.DATA)
    def test_order(self, driver, data, station, button):
        order_page = OrderPage(driver, timer=10)
        order_page.click_to_cookies()
        order_page.go_to_order(button)
        order_page.fill_order(data, station)

        order_page.wait_and_click_element(OrderPageLocators.YES_BUTTON)

        assert 'Заказ оформлен' in order_page.wait_and_find_element(OrderPageLocators.ORDER_MODAL_WINDOW).text, \
            'Заказ не оформлен :('