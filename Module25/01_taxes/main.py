class Property:
    """
    Базовый класс, описывающий объект имущества.

    Args:
        __worth (int): стоимость имущества в рублях
    """
    def __init__(self, worth):
        self.__worth = worth

    def __str__(self):
        """
        Магический метод, возвращающий вид имущества

        :return: вид имущества
        :rtype: str
        """
        return self.__class__.__name__

    def tax(self):
        """
        Метод, вычисляющий величину налога на имущество

        :return: величина налога в рублях
        :rtype: int
        """
        pass

    def get_worth(self):
        """
        Геттер для получения смоимости

        :return: __worth
        :rtype: int
        """
        return self.__worth


class Apartment(Property):
    """
    Класс Квартира. Родитель: Property

    Args:
    __worth (int): стоимость имущества в рублях
    """
    def __str__(self):
        return 'Квартира'

    def tax(self):
        """
        Метод, вычисляющий величину налога на имущество

        :return: величина налога в рублях
        :rtype: int
        """
        return round(self.get_worth() / 1000, 2)


class Car(Property):
    """
    Класс Машина. Родитель: Property

    Args:
    __worth (int): стоимость имущества в рублях
    """
    def __str__(self):
        return 'Машина'

    def tax(self):
        """
        Метод, вычисляющий величину налога на имущество

        :return: величина налога в рублях
        :rtype: int
        """
        return round(self.get_worth() / 200, 2)


class CountryHouse(Property):
    """
    Класс Загородный дом. Родитель: Property

    Args:
    __worth (int): стоимость имущества в рублях
    """
    def __str__(self):
        return 'Загородный дом'

    def tax(self):
        """
        Метод, вычисляющий величину налога на имущество

        :return: величина налога в рублях
        :rtype: int
        """
        return round(self.get_worth() / 500, 2)


def input_user_data():
    """
    Функция, принимающая данные от пользователя для формирования классов.
    :returns: классы имущества
    :rtype: class
    """
    apartment_worth = int(input('Введите cтоимость квартиры: '))
    apartment_car = int(input('Введите cтоимость машины: '))
    apartment_country_house = int(input('Введите cтоимость загородного дома: '))

    return Apartment(apartment_worth), Car(apartment_car), CountryHouse(apartment_country_house)


def tax_calculator(*args):
    """
    Функция, для вычисления суммы общего налога на имущество

    :param args: классы имущества
    :return: cумма общего налога
    :rtype: int
    """
    total_tax_result = 0

    for apartment in args:
        total_tax_result += apartment.tax()
        print('\nВид имущества: {}\nНалог: {} рублей'.format(
            apartment, apartment.tax()
        ))

    return total_tax_result


def check_cash(cash, tax):
    """
    Функция, для проверки достаточности денег на оплату налога

    :param cash: сумма денег собственника
    :param tax: сумма налога
    """
    if tax > cash:
        print('\nНедостаточно денег для выплаты налога.\nТребуется еще {} рублей'.format(
            tax - cash
        ))
    else:
        print('\nИтоговая сумма налога:', tax, 'рублей.')


total_cash = int(input('Введите количество имеющихся денег: '))
user_apartment, user_car, user_country_house = input_user_data()
total_tax = tax_calculator(user_apartment, user_car, user_country_house)
check_cash(total_cash, total_tax)
