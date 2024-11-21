from pages.order_confirm_page import OrderConfirmPage
from pages.order_created_page import OrderCreatedPage
from pages.order_page import *
from pages.tracking_page import *
from pages.receiver_form_page import *
from pages.rent_details_page import *
from pages.dzen_page import *


class TestOrder:
    driver = None

    @allure.title("Проверка создания заказа и перехода на главную по клику на 'Самокат' в логотипе")
    def test_click_scooter(self, driver):
        main = OrderPage(driver)
        main.navigate(links.MAIN_URL)
        main.cookie_close()
        main.go_to_order_top()
        receiver = ReceiverFormPage(driver)
        receiver.fill_in_receiver_form()
        rent = RentDetailsFormPage(driver)
        rent.fill_in_rent_form()
        popup1 = OrderConfirmPage(driver)
        popup1.popup_click_yes()
        popup2 = OrderCreatedPage(driver)
        popup2.popup_go_to_order()
        track_page = TrackingPage(driver)
        order_created = track_page.wait_for_tracking_page()
        assert order_created.is_displayed()
        track_page.scooter_click()
        expected_url = links.MAIN_URL
        assert driver.current_url == expected_url


    @allure.title("Проверка создания заказа и перехода на 'Дзен' по клику на 'Яндекс' в логотипе")
    def test_click_yandex(self, driver):
        main = OrderPage(driver)
        main.navigate(links.MAIN_URL)
        main.cookie_close()
        main.scroll_to_bottom()
        main.wait_for_bottom_button_visible()
        main.go_to_order_bottom()
        receiver = ReceiverFormPage(driver)
        receiver.fill_in_receiver_form()
        rent = RentDetailsFormPage(driver)
        rent.fill_in_rent_form()
        popup1 = OrderConfirmPage(driver)
        popup1.popup_click_yes()
        popup2 = OrderCreatedPage(driver)
        popup2.popup_go_to_order()
        track_page = TrackingPage(driver)
        order_created = track_page.wait_for_tracking_page()
        assert order_created.is_displayed()
        track_page.yandex_click()
        track_page.switch_tab()
        dzen = DzenPage(driver)
        dzen.wait_for_dzen_logo_visible()
        expected_url = links.DZEN_URL
        assert driver.current_url == expected_url