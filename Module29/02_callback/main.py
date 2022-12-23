from typing import Callable
from functools import wraps


def callback(user_data: str) -> Callable:
    """
    Декоратор, добавляющий экземпляр фукции в словарь по ключу пользователя.
    :param user_data:
    :return:
    """
    def checker(func: Callable) -> Callable:

        @wraps(func)
        def wrapped_func(*args, **kwargs) -> None:
            app[user_data] = func
        return wrapped_func
    return checker


@callback('//')
def example() -> str:
    """
    Тестовая функция, для проверки работы декоратора.
    """
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


app = dict()
example()

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
