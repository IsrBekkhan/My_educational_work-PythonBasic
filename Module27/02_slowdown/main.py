from time import sleep
from functools import wraps
from typing import Callable


def delay(func: Callable) -> Callable:
    """
    Декоратор, добавляющий задержку (3 секунды) в декорируемую функцию.
    """
    @wraps(func)
    def wrapped_func(*args) -> None:
        print('Программа выполняется. Подождите 3 секунд...')
        sleep(3)
        return func(*args)

    return wrapped_func


@delay
def squares_sum(x: int) -> int:
    """
    Фунция нахождения суммы квадратов
    для каждого N от 0 до x

    Args:
        x (int): конечное число

    :return: int: сумма квадратов
    """
    return sum([number**2 for number in range(x)])


print(squares_sum(50))
