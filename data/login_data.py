from base import Base


class LoginData:

    method = Base()
    login_pasword = method.register_new_courier_and_return_login_password()

    lodin_courier = {
        'login': login_pasword[0],
        'password': login_pasword[1]
    }

    login_incorect_data_password = {
        'login': login_pasword[0],
        'password': f'{login_pasword[1]} + 3'
    }

    login_incorect_data_login = {
        'login': f'{login_pasword[0]} +3',
        'password': login_pasword[1]
    }
    login_non_existent = {
        'login': 'qwerf',
        'password': '12345'
    }

    login_no_login = {
        'login': "",
        'password': '12345'
    }

    param = [
        (login_incorect_data_password, 404, 'message', 'Учетная запись не найдена'),
        (login_incorect_data_login, 404, 'message', 'Учетная запись не найдена'),
        (login_non_existent, 404, 'message', 'Учетная запись не найдена'),
        (login_no_login, 400, 'message', 'Недостаточно данных для входа')
    ]