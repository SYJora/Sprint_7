import allure
import pytest

from data.create_courier_data import CreateCourier
from method_api.courier_api_method import CreateCourierApi


class TestCreateCourier:

    @allure.title("Проверка создания курьера.")
    @allure.description("Проверка хеппи паса создания курьера и реакция системы на отсутствия обязательных данных.")
    @pytest.mark.parametrize('param', CreateCourier.param)
    def test_create_courier(self, param):
        data, code, massage, text = param
        res_request = CreateCourierApi.create_courier_post(data)
        assert res_request.status_code == code and res_request.json()[massage] == text


