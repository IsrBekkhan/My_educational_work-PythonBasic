from typing import Callable
from datetime import datetime
from time import time
from functools import wraps


def logger(func: Callable, full_name: str, date_format: str) -> Callable:
    """
    Декоратор, добавляющий дату и время работы в декорируемую функцию.
    """
    @wraps(func)
    def wrapped(*args, **kwargs) -> int:
        date_object = datetime.now()
        cur_date = date_object.strftime(date_format)
        print("- Запускается '{}'. Дата и время запуска: {}".format(
            full_name, cur_date
        ))
        start = time()
        result = func(*args, **kwargs)
        print("- Завершение '{}', время работы = {}".format(
            full_name, round(time() - start, 3)
        ))
        return result

    return wrapped


def log_methods(date: str, decorator: Callable = logger) -> Callable:
    """
    Декоратор, оборачивающий каждый метод класса
    декоратором 'logger'.
    """
    date_format = ''

    for symbol in date:
        if symbol.isalpha():
            date_format += '%' + symbol
        else:
            date_format += symbol

    @wraps(decorator)
    def wrapped(cls):

        for metod_name in dir(cls):

            if metod_name.startswith('__') is False:
                cls_metod_name = '{}.{}'.format(cls.__name__, metod_name)
                cur_metod = getattr(cls, metod_name)
                decorate_metod = decorator(cur_metod, cls_metod_name, date_format)
                setattr(cls, metod_name, decorate_metod)

        return cls

    return wrapped


@log_methods("b d Y - H:M:S")
class A:
    """
    Тестовый класс, для проверки работы декоратора.
    """
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    """
    Дочерний класс. Родитель 'A'.
    Тестовый класс, для проверки работы декоратора.
    """
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
