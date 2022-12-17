from typing import Callable, Any
from functools import wraps
from datetime import datetime


def logging(func: Callable) -> Callable:
    """
    Декоратор, для логирования функций
    """
    @wraps(func)
    def wrapped_func(*args) -> Any:
        print('Выполняется фунция {}.\nДокументация: {}'.format(
            func.__name__, func.__doc__))
        try:
            result = func(*args)
        except Exception as exc:
            with open('function_errors.log', 'a', encoding='utf-8') as log_file:
                log_message = ' '.join([str(datetime.now()), func.__name__,  str(exc), '\n'])
                log_file.write(log_message)
        else:
            return result

    return wrapped_func


@logging
def squares_sum(x: int) -> int:
    """
    Фунция нахождения суммы квадратов
    для каждого N от 0 до x

    Args:
        x (int): конечное число

    :return: int: сумма квадратов
    """
    return sum([number**2 for number in range(x)])


print('Результат', squares_sum(10))
