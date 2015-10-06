class Settings:
    class Test:
        MERCHANT_ID = '002020000000001'
        SECRET_KEY = MERCHANT_ID + '_KEY1'
        URL = 'https://payment-webinit.simu.omnikassa.rabobank.nl/paymentServlet'
    URL = 'https://payment-webinit.omnikassa.rabobank.nl/paymentServlet'
    VERSION = 'HP_1.0'


class Currency:
    EURO = '978'


class ResponseCode:
    SUCCESS = '00'
