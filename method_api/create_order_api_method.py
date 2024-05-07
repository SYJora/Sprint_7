import requests

from urls import Urls


class CreateOrder:

    @staticmethod
    def create_order(data):
        return requests.post(Urls.BASE_URLS + Urls.CREATE_ORDER, json = data)

    @staticmethod
    def get_list_order():
        return requests.get(Urls.BASE_URLS + Urls.CREATE_ORDER)

