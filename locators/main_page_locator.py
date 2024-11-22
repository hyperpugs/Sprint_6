from selenium.webdriver.common.by import By


class MainPageLocators:

    COOKIE_BUTTON = By.ID, 'rcc-confirm-button'  # кнопка принятия куки
    ORDER_BUTTON_HEADER = By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"  # кнопка "Заказать" сверху страницы
    ORDER_BUTTON_FOOTER = By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"  # кнопка "Заказать" снизу страницы
    SAMOKAT_LOGO = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'  # лого самоката
    YANDEX_LOGO = By.CLASS_NAME, 'Header_LogoYandex__3TSOI'  # лого яндекса

    FIND_BUTTON = By.XPATH, './/button[text() = "Найти"]'  # кнопка "Найти" на странице Дзена

    LAST_QUESTION = By.XPATH, '//div[@id = "accordion__heading-7"]'  # последний вопрос

    @staticmethod
    def get_question_button(question_number):  # метод формирует локатор для вопроса
        return By.ID, f'accordion__heading-{question_number}'

    @staticmethod
    def get_question_answer(question_answer):  # метод формирует локатор для ответа
        return By.ID, f'accordion__panel-{question_answer}'