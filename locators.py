from selenium.webdriver.common.by import By


class BasePageLocator:
    cookie_accept = [By.XPATH, ".//button[text()='да все привыкли']"]
    logo_button = [By.XPATH, ".//img[@alt='Yandex']/parent::a"]
    order_status_button = [By.XPATH, ".//button[text()='Статус заказа']"]
    scooter_logo = (By.XPATH, ".//a[contains(@class, 'LogoScooter')]")

class YandexHomePage:
    top_order_button = [By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"]
    bottom_order_button = [By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"]
    FAQ_button = [By.XPATH, ".//div[@class='accordion__button']"]
    FAQ_answers = [By.CSS_SELECTOR, ".accordion__panel > p"]
    order_status_button = [By.XPATH, ".//button[text()='Статус заказа']"]

    @staticmethod
    def FAQ_question(question_number):
        return [By.XPATH, f".//div[@class='accordion__button' and @id='accordion__heading-{question_number}']"]

    @staticmethod
    def FAQ_answer(answer_number):
        return [By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{answer_number}']/p"]

class YandexOrderPage:
    first_name_input = [By.XPATH, ".//input[contains(@placeholder,'Имя')]"]
    last_name_input = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"]
    address_input = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]"]
    metro_input = [By.XPATH, ".//input[contains(@placeholder,'метро')]"]

    @staticmethod
    def METRO_HINT_BUTTON(metro_name: str):
        return [By.XPATH, f".//div[text()='{metro_name}']/parent::button"]

    telephone_number = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]"]
    next_button = [By.XPATH, ".//button[text()='Далее']"]
    back_button = [By.XPATH, ".//button[text()='Назад']"]
    date_field = [By.XPATH, ".//input[contains(@placeholder,'Когда')]"]
    rental_period = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    rental_period_list = [By.XPATH, ".//div[@class='Dropdown-option']"]
    color = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]
    comment_for_courier = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]
    order_button = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]
    accept_button = [By.XPATH, ".//button[text()='Да']"]
    order_info = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]
    status_button = [By.XPATH, ".//button[text()='Посмотреть статус']"]

