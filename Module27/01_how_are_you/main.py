from typing import Callable
from functools import wraps


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор, добавляющий сорняковый код в декорируемую функцию.
    """
    @wraps(func)
    def wrapped_func(*args, **kwargs) -> None:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func(*args, **kwargs)

    return wrapped_func


@how_are_you
def test() -> None:
    """
    Фукция для простого теста
    """
    print('<Тут что-то происходит...>')


@how_are_you
def squares_sum(x: int) -> int:
    """
    Фунция нахождения суммы квадратов
    для каждого N от 0 до x

    Args:
        x (int): конечное число

    :return: int: сумма квадратов
    """
    return sum([number**2 for number in range(x)])


@how_are_you
def cubes_sum(x: int) -> int:
    """
    Фунция нахождения суммы кубов
    для каждого N от 0 до x

    Args:
        x (int): конечное число

    :return: int: сумма кубов
    """
    return sum([number**3 for number in range(x)])


test()
print('Сумма квадратов:', squares_sum(100))
print('Сумма кубов:', cubes_sum(50))


