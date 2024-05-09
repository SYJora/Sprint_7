import allure
import requests
from urls import Urls


class LoginCourierApi:

    @staticmethod
    @allure.step('Отправка метода post на логирование курьера в систему.')
    def login_courier_request(data):
        return requests.post(Urls.BASE_URLS + Urls.COURIER_LOGIN, json = data)



