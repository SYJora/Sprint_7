import allure
import requests

from urls import Urls


class CreateCourierApi:

    @staticmethod
    @allure.step('Отправка метода post на регистрацию курьера.')
    def create_courier_post(data):
        return requests.post(Urls.BASE_URLS + Urls.CREATE_COURIER, json=data)