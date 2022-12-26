from typing import Callable
from functools import wraps
app = dict()


def callback(user_data: str) -> Callable:
    """
    Декоратор, добавляющий экземпляр фукции в словарь по ключу пользователя.
    """
    def checker(func: Callable) -> Callable:
        app[user_data] = func

        @wraps(func)
        def wrapped_func(*args, **kwargs) -> None:
            return func()
        return wrapped_func
    return checker


@callback('//')
def example() -> str:
    """
    Тестовая функция, для проверки работы декоратора.
    """
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
