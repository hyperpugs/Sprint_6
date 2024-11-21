from selenium.webdriver.common.by import By

class OrderPageLocators():
    top_order_button = [By.XPATH, "//button[@class='Button_Button__ra12g'][contains(.,'Заказать')]"]

    bottom_order_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][contains(.,'Заказать')]"]

    # Раскрывашки в "Вопросах о важном"
    accordeon_1 = [By.CSS_SELECTOR, "#accordion__heading-0"]
    accordeon_2 = [By.CSS_SELECTOR, "#accordion__heading-1"]
    accordeon_3 = [By.CSS_SELECTOR, "#accordion__heading-2"]
    accordeon_4 = [By.CSS_SELECTOR, "#accordion__heading-3"]
    accordeon_5 = [By.CSS_SELECTOR, "#accordion__heading-4"]
    accordeon_6 = [By.CSS_SELECTOR, "#accordion__heading-5"]
    accordeon_7 = [By.CSS_SELECTOR, "#accordion__heading-6"]
    accordeon_8 = [By.CSS_SELECTOR, "#accordion__heading-7"]

    # Текст под раскрывашкой
    accordeon_text_1 = [By.CSS_SELECTOR, "#accordion__panel-0 > p:nth-child(1)"]
    accordeon_text_2 = [By.CSS_SELECTOR, "#accordion__panel-1 > p:nth-child(1)"]
    accordeon_text_3 = [By.CSS_SELECTOR, "#accordion__panel-2 > p:nth-child(1)"]
    accordeon_text_4 = [By.CSS_SELECTOR, "#accordion__panel-3 > p:nth-child(1)"]
    accordeon_text_5 = [By.CSS_SELECTOR, "#accordion__panel-4 > p:nth-child(1)"]
    accordeon_text_6 = [By.CSS_SELECTOR, "#accordion__panel-5 > p:nth-child(1)"]
    accordeon_text_7 = [By.CSS_SELECTOR, "#accordion__panel-6 > p:nth-child(1)"]
    accordeon_text_8 = [By.CSS_SELECTOR, "#accordion__panel-7 > p:nth-child(1)"]



class ReceiverFormLocators:

    receiver_header = [By.XPATH, "//div[@class='Order_Header__BZXOb'][contains(.,'Для кого самокат')]"] #Заголовок "Для кого самокат"

    name_field = [By.XPATH, "//input[@placeholder='* Имя']"] #Поле "Имя"

    surname_field = [By.XPATH, "//input[@placeholder='* Фамилия']"] #Поле "Фамилия"

    address_field = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"] #Поле "Адрес"

    metro_station_field = [By.XPATH, "//input[@placeholder='* Станция метро']"] #Поле "Станция метро"

    metro_station_button = [By.XPATH, "//button[contains(.,'Преображенская площадь')]"] #Кнопка со станцией метро

    phone_field = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"] #Поле "Телефон"

    continue_button = [By.CSS_SELECTOR, ".Button_Middle__1CSJM"] #Кнопка "Далее"

    cookie_button = [By.CSS_SELECTOR, "#rcc-confirm-button"] #Кнопка "да все привыкли"


class RentDetailsLocators:

    rent_header = [By.XPATH, "//div[@class='Order_Header__BZXOb'][contains(.,'Про аренду')]"] #Заголовок "Про аренду"

    date_field = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"] #Поле "Когда привезти самокат"

    rent_time_field = [By.XPATH, "//div[@class='Dropdown-placeholder'][contains(.,'* Срок аренды')]"] #Поле "Срок аренды"

    rent_picker = [By.XPATH, "(//div[@class='Dropdown-option'])[3]"] #Кнопка в раскрывашке

    scooter_colour_black = [By.XPATH, "//label[@for='black']"] #Чекбокс с цветом
    scooter_colour_grey = [By.XPATH, "//label[@for='grey']"] #Чекбокс с цветом

    order_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][contains(.,'Заказать')]"] #Кнопка заказать внизу страницы

class OrderConfirmPopupLocators:

    order_confirm_header = [By.XPATH, "//div[contains(.,'Хотите оформить заказ?')]"] #Всплывашка с подтверждением

    order_confirm_yes_button = [By.XPATH, "//button[contains(.,'Да')]"] #Кнопка "Да"

class OrderCreatedPopupLocators:

    order_created_header = [By.XPATH, "//div[contains(.,'Заказ оформлен')]"] #Всплывашка с номером

    go_to_order_button = [By.XPATH, "//button[contains(.,'Посмотреть статус')]"] #Кнопка "Посмотреть статус"

class TrackingPageLocators:

    cancel_button = [By.CSS_SELECTOR, "button.Button_Button__ra12g:nth-child(14)"] #Кнопка "Отменить заказ"

    ya_logo = [By.XPATH, "//img[@alt='Yandex']"] #Лого "Яндекс"

    scooter_logo = [By.XPATH, "//img[@alt='Scooter']"] #Лого "Самокат"

class DzenLocators:
    yandex_search_logo = [By.XPATH, "//div[1]/a/svg[2]/use"]