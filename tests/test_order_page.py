
import urls
from selenium.webdriver.firefox import webdriver
from pages.order_page import *


class TestOrder:
    driver = None

    @allure.title("Проверка создания заказа и перехода на главную по клику на 'Самокат' в логотипе")
    def test_click_scooter(self, driver):
        home_page = OrderPage(driver)
        home_page.navigate(urls.MAIN_URL)
        home_page.cookie_close()
        home_page.go_to_order_top()
        home_page.fill_in_receiver_form()
        home_page.fill_in_rent_form()
        home_page.popup_click_yes()
        home_page.popup_go_to_order()
        home_page.wait_for_tracking_page()
        order_created = home_page.wait_for_tracking_page()
        assert order_created.is_displayed()
        home_page.scooter_click()
        home_page.check_url_samokat()


    @allure.title("Проверка создания заказа и перехода на 'Дзен' по клику на 'Яндекс' в логотипе")
    def test_click_yandex(self, driver):
        home_page = OrderPage(driver)
        home_page.navigate(urls.MAIN_URL)
        home_page.cookie_close()
        home_page.scroll_to_bottom()
        home_page.wait_for_bottom_button_visible()
        home_page.go_to_order_bottom()
        home_page.fill_in_receiver_form()
        home_page.fill_in_rent_form()
        home_page.popup_click_yes()
        home_page.popup_go_to_order()
        home_page.yandex_click()
        home_page.switch_tab()
        home_page.check_icon_dzen()
