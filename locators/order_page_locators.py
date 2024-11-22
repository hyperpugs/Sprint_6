from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIELD_INPUT_NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    FIELD_INPUT_LAST_NAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    FIELD_INPUT_ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    FIELD_INPUT_METRO = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    COMBOBOX = [By.CLASS_NAME, 'select-search__select']
    COMBOBOX_METRO = [By.XPATH, '//input[@class="select-search__input"]']
    FIELD_INPUT_PHONE = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    BUTTON_NEXT = [By.XPATH, '//button[contains(text(),"Далее")]']
    FIELD_DATE = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    CALENDAR = [By.CLASS_NAME, "react-datepicker__month-container"]
    CHANGE_DAY = [By.XPATH, '//div[text()={} and contains(@class,"react-datepicker__day")]']
    FIELD_PERIOD = [By.CLASS_NAME, 'Dropdown-placeholder']
    FIELD_PERIOD_DROP_DOWN_OPTION = [By.XPATH, '//div[@class="Dropdown-option" and text()="{}"]']
    FIELD_COLOR = [By.ID, '{}']
    FIELD_COMMENT = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

    BUTTON_YES = [By.XPATH, './/button[text()="Да"]']

    TEXT_GOOD_ORDER = [By.XPATH, './/div[contains(@class,"Order_ModalHeader")]']
    WATCH_STATUS = [By.XPATH, './/button[text()="Посмотреть статус" and (contains(@class,"Button_Middle"))]']