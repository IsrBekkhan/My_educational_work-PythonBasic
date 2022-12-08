from random import randint
from random import choice


class KillError(Exception):
    """
    Класс Убийство. Родитель: Exeption.
    При вызове возвращает исключение

    :raise: Exeption: может вызываться как одно из случайных исключений.
    """
    def __str__(self):
        return 'Убийство'


class DrunkError(Exception):
    """
    Класс Пьянство. Родитель: Exeption.
    При вызове возвращает исключение

    :raise: Exeption: может вызываться как одно из случайных исключений.
    """
    def __str__(self):
        return 'Пьянство'


class CarCrashError(Exception):
    """
    Класс Автомобильная авария. Родитель: Exeption.
    При вызове возвращает исключение

    :raise: Exeption: может вызываться как одно из случайных исключений.
    """
    def __str__(self):
        return 'Автомобильная авария'


class GluttonyError(Exception):
    """
    Класс Чревоугодие. Родитель: Exeption.
    При вызове возвращает исключение

    :raise: Exeption: может вызываться как одно из случайных исключений.
    """
    def __str__(self):
        return 'Чревоугодие'


class DepressError(Exception):
    """
    Класс Депрессия. Родитель: Exeption.
    При вызове возвращает исключение

    :raise: Exeption: может вызываться как одно из случайных исключений.
    """
    def __str__(self):
        return 'Депрессия'


class Person:
    """
    Базовый класс, описывающий буддиста.

    Attributes:
        __karma_scores (int): общее количество очков кармы
    """
    __karma_scores = 0

    def set_score(self, score):
        """
        Сеттер для увеличения количества очков кармы

        :param: __karma_scores: очки кармы
        :rtype: int
        """
        self.__karma_scores += score

    def get_score(self):
        """
        Геттер для получения текущего количества очков кармы

        :return: __karma_scores
        :rtype: int
        """
        return self.__karma_scores


def one_day():
    """
    Функция, возвращающая количество кармы от 1 до 7 или одно из исключений с вероятностью 1 к 10.

    :return: очки кармы от 1 до 7
    :rtype: int
    :raise: Exeption: возвращает одно из исключений с вероятностью 1 к 10.
    """
    if randint(1, 10) == 7:
        raise choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressError()])
    return randint(1, 7)


def log_saver(error):
    """
    Функция, для создания log-файла с перечнем исключений.

    :return: файл karma.log
    :rtype: file
    """
    with open('karma.log', 'a', encoding='utf-8') as log_file:
        message = 'день {}-й: {}\n'.format(days, error)
        log_file.write(message)


buddhist = Person()
days = 0

while True:
    days += 1
    try:
        buddhist.set_score(one_day())
    except Exception as exc:
        log_saver(exc)

    if buddhist.get_score() >= 500:
        break

print('Буддист достиг просветления!')
