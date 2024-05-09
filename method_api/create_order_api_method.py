import allure
import requests

from urls import Urls


class CreateOrder:

    @staticmethod
    @allure.step('Отправка метода post на создание заказов.')
    def create_order(data):
        return requests.post(Urls.BASE_URLS + Urls.CREATE_ORDER, json = data)

    @staticmethod
    @allure.step('Отправка метода get на получение списка заказов.')
    def get_list_order():
        return requests.get(Urls.BASE_URLS + Urls.CREATE_ORDER)

