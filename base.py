import random
import string

import allure
import requests


class Base:

    @allure.step('Генерация рандомных данных.')
    def generate_random_word(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @allure.step('Создание курьера и возврат данных регистраций в виде списка.')
    def register_new_courier_and_return_login_password(self):
        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = self.generate_random_word(10)
        password = self.generate_random_word(10)
        first_name = self.generate_random_word(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)

        # возвращаем список
        return login_pass

