import allure
from pages.home_page import HomePage
from configs.urls import YANDEX_HOME_PAGE, ORDER_PAGE, DZEN_HOME_PAGE, YANDEX_CAPTCHA_PAGE, MAIN_PAGE


@allure.epic('Main page')
@allure.parent_suite('Домашняя страница')
@allure.suite('Header')
class TestYandexHomePage:

    @allure.feature('Переход к форме оформления заказа из Домашней страницы')
    @allure.story('Переход к оформлению заказа по кнопке "Заказать"')
    @allure.title('Нажатия на кнопку "Заказать" вверху страницы')
    @allure.description('Проверка, что по верхней кнопки "Заказать",'
                        'осуществляеется переход к форме оформеления заказа')
    def test_click_top_order_button(self, driver):
        yandex_home_page = HomePage(driver)
        yandex_home_page.go_to_site()
        yandex_home_page.click_cookie_accept()
        yandex_home_page.click_top_order_button()
        assert yandex_home_page.current_url() == ORDER_PAGE

    @allure.feature('Переход к форме оформление заказа из Домашней страницы')
    @allure.story('Переход к оформлению заказа по кнопке "Заказать" из блока "Как это работает"')
    @allure.title('Нажатие на кнопку "Заказать" внизу страницы.')
    @allure.description('Проверка, что по верхней кнопки "Заказать",'
                        'осуществляеется переход к форме оформеления заказа')
    def test_click_bottom_order_button(self, driver):
        yandex_home_page = HomePage(driver)
        yandex_home_page.go_to_site()
        yandex_home_page.click_cookie_accept()
        yandex_home_page.click_bottom_order_button()

        assert yandex_home_page.current_url() == ORDER_PAGE

    @allure.feature('Переход на страницу "ЯндексДзен" из Домашней страницы')
    @allure.story("Редирект на страницу ЯндексДзен по кнопке logo")
    @allure.title('При нажатии на лого "Яндекс Самокат" происходит редирект на страницу "ЯндексДзен"')
    @allure.description('Проверка, что по логотипу "Яндекс Самокат",'
                        'осуществляеется успешный редирект на страницу "ЯндексДзен"')
    def test_click_logo_button(self, driver):
        yandex_home_page = HomePage(driver)
        yandex_home_page.go_to_site()
        yandex_home_page.click_cookie_accept()
        yandex_home_page.click_yandex_button()
        yandex_home_page.switch_window(1)
        yandex_home_page.wait_url_until_not_about_blank()
        current_url = yandex_home_page.current_url()

        assert (YANDEX_HOME_PAGE in current_url) or (DZEN_HOME_PAGE in current_url) or (YANDEX_CAPTCHA_PAGE in current_url)

    @allure.feature('Нажатие на лого "Самокат" с домашней страницы"')
    @allure.story('При нажатии на лого "Самокат" URL адрес не меняется')
    @allure.title('Остаемся на домашней странице')
    @allure.description('Проверка успешного открытия и перехода на домашнюю страницу после клика на логотип Самокат')
    def test_click_scooter_logo(self, driver):
        yandex_home_page = HomePage(driver)
        yandex_home_page.go_to_site()
        yandex_home_page.click_cookie_accept()
        yandex_home_page.click_scooter_button()
        current_url = yandex_home_page.current_url()
        assert MAIN_PAGE == current_url