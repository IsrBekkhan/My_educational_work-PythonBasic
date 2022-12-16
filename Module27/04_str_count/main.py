from typing import Callable
from functools import wraps


def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """
    @wraps(func)
    def wrapped_func(*args, **kwargs) -> Callable:
        wrapped_func.counter += 1
        result = func(*args, **kwargs)
        print('Фунция {} была вызвана {} раз.'.format(
            func.__name__, wrapped_func.counter
        ))
        return result

    wrapped_func.counter = 0
    return wrapped_func


@counter
def test() -> None:
    print('ТЕСТ')


test()
test()
test()
