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
    #Заголовок "Для кого самокат"
    receiver_header = [By.XPATH, "//div[@class='Order_Header__BZXOb'][contains(.,'Для кого самокат')]"]

    #Поле "Имя"
    name_field = [By.XPATH, "//input[@placeholder='* Имя']"]

    #Поле "Фамилия"
    surname_field = [By.XPATH, "//input[@placeholder='* Фамилия']"]

    #Поле "Адрес"
    address_field = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]

    #Поле "Станция метро"
    metro_station_field = [By.XPATH, "//input[@placeholder='* Станция метро']"]

    #Кнопка со станцией метро
    metro_station_button = [By.XPATH, "//button[contains(.,'Преображенская площадь')]"]

    #Поле "Телефон"
    phone_field = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]

    #Кнопка "Далее"
    continue_button = [By.CSS_SELECTOR, ".Button_Middle__1CSJM"]

    #Кнопка "да все привыкли"
    cookie_button = [By.CSS_SELECTOR, "#rcc-confirm-button"]


class RentDetailsLocators:
    #Заголовок "Про аренду"
    rent_header = [By.XPATH, "//div[@class='Order_Header__BZXOb'][contains(.,'Про аренду')]"]

    #Поле "Когда привезти самокат"
    date_field = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]

    #Поле "Срок аренды"
    rent_time_field = [By.XPATH, "//div[@class='Dropdown-placeholder'][contains(.,'* Срок аренды')]"]

    #Кнопка в раскрывашке
    rent_picker = [By.XPATH, "(//div[@class='Dropdown-option'])[3]"]

    #Чекбокс с цветом
    scooter_colour_black = [By.XPATH, "//label[@for='black']"]
    scooter_colour_grey = [By.XPATH, "//label[@for='grey']"]

    #Кнопка заказать внизу страницы
    order_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'][contains(.,'Заказать')]"]

class OrderConfirmPopupLocators:
    #Всплывашка с подтверждением
    #Заголовок
    order_confirm_header = [By.XPATH, "//div[contains(.,'Хотите оформить заказ?')]"]

    #Кнопка "Да"
    order_confirm_yes_button = [By.XPATH, "//button[contains(.,'Да')]"]

class OrderCreatedPopupLocators:
    #Всплывашка с номером
    #Заголовок
    order_created_header = [By.XPATH, "//div[contains(.,'Заказ оформлен')]"]

    #Кнопка "Посмотреть статус"
    go_to_order_button = [By.XPATH, "//button[contains(.,'Посмотреть статус')]"]

class TrackingPageLocators:
    #Кнопка "Отменить заказ"
    cancel_button = [By.CSS_SELECTOR, "button.Button_Button__ra12g:nth-child(14)"]

    #Лого "Яндекс"
    ya_logo = [By.XPATH, "//img[@alt='Yandex']"]

    #Лого "Самокат"
    scooter_logo = [By.XPATH, "//img[@alt='Scooter']"]

class DzenLocators:
    yandex_search_logo = [By.CSS_SELECTOR, ".dzen-layout--collapse-button__collapseButton-z1"]