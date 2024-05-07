import allure
import pytest
from data.login_data import LoginData
from method_api.login_courier_api_method import LoginCourierApi


class TestLoginCourier:

    @allure.title("Проверка входа курьера")
    @allure.description("Проверка входа курьера в акаунт")
    def test_login_courier(self):
        response = LoginCourierApi.login_courier_request(LoginData.lodin_courier)
        assert response.status_code == 200 and response.json() is not None

    @allure.title("Проверка входа курьера с не коррекными данными")
    @allure.description("Проверяетсявход без указания пароля иили логина")
    @pytest.mark.parametrize('param', LoginData.param)
    def test_login_incorrect_password_and_login(self, param):
        data, code, massage, text = param
        response = LoginCourierApi.login_courier_request(data)
        assert response.status_code == code and response.json()[massage] == text