from locators.main_page_locator import MainPageLocators
from locators.order_page_locator import OrderPageLocators


class Urls:
    SCOOTER_URL = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_URL = f'{SCOOTER_URL}order'
    DZEN_URL = 'https://dzen.ru/?yredirect=true'


class QuestionData:
    PARAM = 'number, expected_answer'
    VALUE = [
        [0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
        [1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать '
            'несколько заказов — один за другим.'],
        [2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды'
            ' начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная'
            ' аренда закончится 9 мая в 20:30.'],
        [3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
        [4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        [5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без'
            ' передышек и во сне. Зарядка не понадобится.'],
        [6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        [7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']

    ]


class OrderData:
    PARAM = 'data, station, button'
    DATA = [
        [
            [
                'Иван',
                'Иванов',
                'Московская улица, 1',
                '88005553535',
                OrderPageLocators.DELIVERY_DATE_1,
                OrderPageLocators.RENT_TIME_1,
                OrderPageLocators.BLACK_COLOR,
                'Просьба уметь читать по-русски'
            ],
            OrderPageLocators.STATION_BOULEVARD,
            MainPageLocators.ORDER_BUTTON_HEADER
        ],
        [
            [
                'Петр',
                'Петров',
                'Ленинградская улица, 2',
                '88007777777',
                OrderPageLocators.DELIVERY_DATE_2,
                OrderPageLocators.RENT_TIME_2,
                OrderPageLocators.GREY_COLOR,
                'Не забудьте терминал для оплаты'
            ],
            OrderPageLocators.STATION_SOKOLNIKI,
            MainPageLocators.ORDER_BUTTON_FOOTER
        ]
    ]