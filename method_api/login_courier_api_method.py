import requests
from urls import Urls


class LoginCourierApi:

    @staticmethod
    def login_courier_request(data):
        return requests.post(Urls.BASE_URLS + Urls.COURIER_LOGIN, json = data)



