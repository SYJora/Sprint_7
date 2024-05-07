import allure
import pytest

from data.order_data import OrderData
from method_api.create_order_api_method import CreateOrder



class TestMakeOrder:

    @allure.title("Проверка создания заказа")
    @allure.description("Проверка создания заказа с разными параметрами цвета")
    @pytest.mark.parametrize('param', OrderData.param)
    def test_make_order(self, param):
        response = CreateOrder.create_order(param)
        assert response.status_code == 201 and response.json() is not None

    @allure.title("Проверка возврата списка заказов")
    def test_get_list_of_order(self):
        response = CreateOrder.get_list_order()
        list_order = response.json()["orders"]
        assert response.status_code == 200 and list_order is not None