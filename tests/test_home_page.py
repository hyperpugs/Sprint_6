import pytest
import allure

from data_for_test import QUESTION_ANSWER, URL_HOME_PAGE, URL_ORDER_PAGE, URL_YANDEX_PAGE
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage

@allure.feature('Домашняя страница')
class TestHomePage:
    QUESTION_N = [0, 1, 2, 3, 4, 5, 6, 7]
    BUTTONS = [HomePageLocators.BUTTON_ORDER_FIRST, HomePageLocators.BUTTON_ORDER_SECOND]


    @allure.title('Проверка ответов в разделе Вопросы о важном')
    @allure.description('Выпадающий список в разделе «Вопросы о важном». Нужно проверить: когда нажимаешь на '
                        'стрелочку, открывается соответствующий текст. ')
    @pytest.mark.parametrize('num', QUESTION_N)
    def test_click_questions_about_main(self, driver, num):
        home_page = HomePage(driver)
        home_page.get_url(URL_HOME_PAGE)
        home_page.click_on_element(HomePageLocators.BUTTON_COOKIES)
        home_page.scroll_end()
        assert home_page.check_answer(num) == QUESTION_ANSWER[num][1]

    @allure.feature('Домашняя страница')
    @allure.title('Проверка двух кнопок Заказать')
    @allure.description('Проверить точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу')
    @pytest.mark.parametrize('button_order', BUTTONS)
    def test_check_button_order(self, driver, button_order):
        home_page = HomePage(driver)
        home_page.open(URL_HOME_PAGE)
        home_page.click_cookies_button()
        home_page.click_button(button_order)

        assert home_page.is_on_order_page(), "Не удалось перейти на страницу заказа"

    @allure.feature('Домашняя страница')
    @allure.title('Проверка клика на логотип Самокат')
    @allure.description('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_logo_scooter_click(driver):
        home_page = HomePage(driver)
        home_page.open(URL_ORDER_PAGE)
        home_page.click_scooter_logo()
        home_page.assert_current_url(URL_HOME_PAGE)

    @allure.feature('Домашняя страница')
    @allure.title('Проверка клика на логотип Yandex')
    @allure.description('Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная '
                        'страница Дзена')
    def test_logo_yandex_clock(self, driver):
        home_page = HomePage(driver)
        home_page.get_url(URL_ORDER_PAGE)
        home_page.click_on_element(HomePageLocators.LOGO_YANDEX)
        home_page.wait_for_new_window_to_open()
        home_page.switch_to_latest_window()
        home_page.wait_element(HomePageLocators.DZEN)

        actual_url = home_page.get_current_url()
        assert URL_YANDEX_PAGE == actual_url, f"Expected URL: {URL_YANDEX_PAGE}, but got: {actual_url}"