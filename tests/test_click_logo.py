import allure
from data import Urls
from locators.main_page_locator import MainPageLocators
from pages.main_page import MainPage


class TestClickLogo:

    @allure.title('Проверка перехода на главную страницу "Самоката"')
    def test_click_samokat_logo(self, driver):
        main_page = MainPage(driver, timer=10)
        main_page.open_page(Urls.ORDER_URL)
        main_page.wait_and_click_element(MainPageLocators.SAMOKAT_LOGO)
        assert main_page.driver.current_url == Urls.SCOOTER_URL, 'Не удалось перейти на главную страницу'

    @allure.title('Проверка перехода на главную страницу "Дзена"')
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver, timer=10)
        main_page.wait_and_click_element(MainPageLocators.YANDEX_LOGO)
        main_page.switch_second_browser_window(MainPageLocators.FIND_BUTTON)
        assert main_page.driver.current_url == Urls.DZEN_URL, 'Не удалось перейти на страницу Дзена'