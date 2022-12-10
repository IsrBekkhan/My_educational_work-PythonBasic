class Person:
    """
    Базовый класс, описывающий человека

    Args:
        __name (str): передаётся имя человека
        __surname (str): передаётся фамилия человека
        __age (int): передаётся возраст человека
    """
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        """
        Магический метод, возвращающий строку с информацией о человеке
        """
        return 'Должность: {}\nИмя: {}\nФамилия: {}\nВозраст: {}'.format(
            self.__class__.__name__, self.__name, self.__surname, self.__age
        )


class Employee(Person):
    """
    Класс Employee. Родитель: Person
    """
    def get_salary(self):
        """
        Метод, возвращающий значение зарплаты.
        должен быть переопределён и доработан в дочерних классах
        """
        pass


class Manager(Employee):
    """
    Класс Manager. Родитель: Employee

    Attributes:
        __salary (int): величина зарплаты менеджера
    """
    __salary = 13000

    def get_salary(self):
        """
        Метод, возвращающий величину зарплаты

        :return: __salary
        :rtype: int
        """
        return self.__salary


class Agent(Employee):
    """
    Класс Agent. Родитель: Employee

    Attributes:
        __sales_volume (int): объем продаж
    """
    __sales_volume = 1000

    def get_salary(self):
        """
        Метод для вычисления и возвращения величины зарплаты.

        :return: зарплата, определённая как оклад 5000 + 5% от объёма продаж (__sales_volume)
        :rtype: int
        """
        return 5000 + (self.__sales_volume / 100) * 5

    def set_sales_volume(self, amount):
        """
        Метод, увеличивающий величину объема продаж.

        :param amount: количество проданных товаров
        :type amount: int
        """
        self.__sales_volume += amount


class Worker(Employee):
    """
    Класс Worker. Родитель: Employee

    Attributes:
        __worked_hours (int): количество отработанных часов
    """
    __worked_hours = 160

    def get_salary(self):
        """
        Метод для вычисления и возвращения величины зарплаты.

        :return: величина зарплаты, определённая как 100 * число отработанных часов (__worked_hours)
        :rtype: int
        """
        return 100 * self.__worked_hours

    def set_worked_hours(self, amount):
        """
        Метод, увеличивающий число отработанных часов.

        :param amount: число отработанных часов
        :type amount: int
        """
        self.__worked_hours += amount


def to_print(employers):
    """
    Функция, для вывода на экран информации о работнике и величины его зарплаты
    """
    for index, employee in enumerate(employers_list):
        print('\nСотрудник №{}.\n{}\nЗаработная плата: {}'.format(
            index + 1, employee, employee.get_salary()
        ))


employers_list = [
    Manager(name='Таня', surname='Онегина', age='28'),
    Manager(name='Вика', surname='Сельникова', age='29'),
    Manager(name='Антон', surname='Субботников', age='26'),
    Agent(name='Джеймс', surname='Бонд', age='38'),
    Agent(name='Джесон', surname='Борн', age='30'),
    Agent(name='Эдуардо', surname='Саламанка', age='45'),
    Worker(name='Петя', surname='Петров', age='19'),
    Worker(name='Вася', surname='Курочкин', age='20'),
    Worker(name='Гена', surname='Ленин', age='19'),
]

to_print(employers_list)
