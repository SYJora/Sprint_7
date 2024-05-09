from base import Base


class CreateCourier:

    method = Base()
    login = method.generate_random_word(10)
    password = method.generate_random_word(10)
    first_name = method.generate_random_word(10)


    courier_new = {
        'login': login,
        'password': password,
        'firstName': first_name
    }

    courier_same_login = courier_new

    courier_no_login = {
        'login': ' ',
        'password': '1234',
        'firstName': 'smith'
    }

    param = [
        (courier_new, 201, 'ok', True),
        (courier_same_login, 409, 'message', 'Этот логин уже используется. Попробуйте другой.'),
        (courier_no_login, 409, 'message', 'Этот логин уже используется. Попробуйте другой.')
    ]