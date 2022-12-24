from typing import Callable
from functools import wraps


def check_permission(user: str) -> Callable:
    def checker(func: Callable) -> Callable:
        """
        Декоратор, добавляющий проверку доступа пользователя
        к вызываемой (декорируемой) функции.
        """
        @wraps(func)
        def wrapped_func() -> None:
            try:
                if user in user_permissions:
                    func()
                else:
                    raise PermissionError('У пользователя {} недостаточно прав, чтобы выполнить функцию {}.'.format(
                        user, func.__name__
                    ))
            except PermissionError as exp:
                print(exp)
        return wrapped_func
    return checker


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    """
    Функция, удаляющий сайт.
    """
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    """
    Функция, добавляющий комментарий.
    """
    print('Добавляем комментарий')


delete_site()
add_comment()
