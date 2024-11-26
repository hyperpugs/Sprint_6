from selenium.webdriver.common.by import By

class LocatorsBase:
    LOGO_SCOOTER = (By.XPATH, ".//a[contains(@class,'LogoScooter')]")
    LOGO_YANDEX = (By.XPATH, ".//a[contains(@class,'LogoYandex')]")
    BUTTON_ORDER_IN_HEADER = (By.XPATH, ".//div[contains(@class,'Header')]//button[contains(text(),'Заказать')]")

class LocatorsMain:
    URL = "https://qa-scooter.praktikum-services.ru/"
    SCOOTER_IMG = (By.XPATH, ".//img[contains(@src,'scooter.png')]")
    HOME_PAGE_DIV = (By.XPATH, ".//div[contains(@class,'HomePage')]")
    FOOTER = (By.XPATH, ".//div[contains(@class,'FourPart')]")
    QUESTION = (By.XPATH, ".//div[contains(@id, 'heading-{0}')]")
    ANSWER = (By.XPATH, ".//div[contains(@id, 'panel-{0}')]")
    BUTTON_ORDER_IN_MIDDLE = (By.XPATH, ".//div[contains(@class,'FinishButton')]//button")

class LocatorsOrder:
    URL = 'https://qa-scooter.praktikum-services.ru/order'
    ORDER_HEADER_FOR_WHO = (By.XPATH, ".//div[contains(text(),'Для кого')]")
    ORDER_HEADER_RENTAL = (By.XPATH, ".//div[contains(text(),'Про аренду')]")
    FIELD_FIRST_NAME = (By.XPATH, ".//input[contains(@placeholder, 'Имя')]")
    FIELD_LAST_NAME = (By.XPATH, ".//input[contains(@placeholder, 'Фамилия')]")
    FIELD_ADDRESS = (By.XPATH, ".//input[contains(@placeholder, 'Адрес')]")
    FIELD_SUBWAY_STATION = (By.XPATH, ".//input[contains(@placeholder, 'метро')]")
    STATION_LOCATOR = (By.XPATH, ".//div[contains(text(), '{0}')]")
    FIELD_PHONE_NUMBER = (By.XPATH, ".//input[contains(@placeholder, 'Телефон')]")
    BUTTON_NEXT = (By.XPATH, ".//button[contains(text(), 'Далее')]")
    FIELD_DELIVERY_DATE = (By.XPATH, ".//input[contains(@placeholder, 'Когда привезти')]")
    FIELD_RENTAL_TIME = (By.XPATH, ".//div[contains(@class, 'Dropdown-placeholder')]")
    FIELD_COMMENTS = (By.XPATH, ".//input[contains(@placeholder, 'Комментарий')]")
    BUTTON_ORDER = (By.XPATH, ".//button[contains(@class, 'Middle') and contains(text(), 'Заказать')]")
    CONFIRM_HEADER = (By.XPATH, ".//div[contains(@class, 'ModalHeader')]")
    BUTTON_ACCEPT_ORDER = (By.XPATH, ".//button[contains(text(),'Да')]")
    CONFIRMED_HEADER = (By.XPATH, ".//div[contains(text(),'оформлен')]")
    BUTTON_STATUS_ORDER = (By.XPATH, './/button[contains(text(),"статус")]')
    STATUS_ORDER = (By.XPATH, ".//div[contains(@class,'Content')]")
    CHECK_BOX = (By.ID, '{0}')
    rental_time_locator = (By.XPATH, f".//div[contains(@class, 'Dropdown') and contains(text(), 'четверо')]")