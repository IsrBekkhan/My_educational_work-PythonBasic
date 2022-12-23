from typing import Callable
from functools import wraps


def callback(user_data: str) -> Callable:
    def checker(func: Callable) -> Callable:

        @wraps(func)
        def wrapped_func(*args, **kwargs) -> str:
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


app = {'//': example}

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')