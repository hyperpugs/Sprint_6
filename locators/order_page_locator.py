from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_INPUT = By.CSS_SELECTOR, 'input[placeholder="* Имя"]'
    SURNAME_INPUT = By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]'
    ADDRESS_INPUT = By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]'
    PHONE_INPUT = By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]'
    STATION_INPUT = By.CSS_SELECTOR, "input[placeholder='* Станция метро']"
    STATION_BOULEVARD = By.XPATH,  ".//div[text()='Бульвар Рокоссовского']"
    STATION_SOKOLNIKI = By.XPATH, ".//div[text()='Сокольники']"

    NEXT_BUTTON = By.XPATH, './/button[text() = "Далее"]'

    DELIVERY_DATE_INPUT = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    DELIVERY_DATE_1 = By.XPATH, ".//div[text()='20']"  # 20 число
    DELIVERY_DATE_2 = By.XPATH, ".//div[text()='21']"  # 21 число

    RENTAL_TIME_INPUT = By.XPATH, ".//div[contains(@class, 'Dropdown-placeholder')]"  # выбор срока аренды
    RENT_TIME_1 = By.XPATH, ".//div[text() = 'двое суток']"
    RENT_TIME_2 = By.XPATH, ".//div[text() = 'трое суток']"

    BLACK_COLOR = By.XPATH, ".//label[@for='black']"  # черный цвет в чек-боксе
    GREY_COLOR = By.XPATH, ".//label[@for='grey']"  # серый цвет в чек-боксе

    COMMENT_INPUT = By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]'

    ORDER_BUTTON_COMPLETE = By.XPATH, './/button[text()="Назад"]/parent::div/button[text()="Заказать"]'

    YES_BUTTON = By.XPATH, './/button[text() = "Да"]'

    ORDER_MODAL_WINDOW = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'  # модальное окно заказа