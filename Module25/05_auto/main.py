from math import radians
from math import cos
from math import sin


class Auto:
    """
    Базовый класс, описывающий автотранспорт

    Args:
        __x (int): передаётся координата 'x' местоположения автотранспорта
        __y (int): передаётся координата 'y' местоположения автотранспорта
        __route (int): передаётся направление движения (в градусах) автотранспорта
    """
    def __init__(self, x, y, route):
        self.__x = x
        self.__y = y
        self.__route = route % 360

    def to_drive(self, distance):
        """
        Метод, перемещающий транспорт в заведомо заданном направлении

        Args:
            distance (int): передаётся значение расстояния (в метрах) до точки перемещения
        """
        radian_route = radians(self.__route)
        self.__x += cos(radian_route) * distance
        self.__y += sin(radian_route) * distance

    def to_turn(self, new_route):
        """
        Сеттер для изменения направления движения автотранспорта

        Args:
            new_route (int): передаётся значение угла нового направления (в градусах) относительно оси координат
        """
        self.__route = new_route % 360

    def get_x_y(self):
        """
        Геттер для получения кортежа с значениями 'x' и 'y'

        :return: (x, y)
        :rtype: tuple
        """
        return self.__x, self.__y

    def get_route(self):
        """
        Геттер для получения значения направления движения

        :return: __route
        :rtype: int
        """
        return self.__route

    def change_x_y(self, x, y):
        """
        Сеттер для изменения местоположения автотранспорта относительно текущего

        Args:
            __x (int): передаётся координата 'x' для изменения текущего значения
            __y (int): передаётся координата 'y' для изменения текущего значения
        """
        self.__x += x
        self.__y += y


class Bus(Auto):
    """
    Класс Автобус. Родитель: Auto

    Args:
        __x (int): передаётся координата 'x' местоположения автотранспорта
        __y (int): передаётся координата 'y' местоположения автотранспорта
        __route (int): передаётся направление движения (в градусах) автотранспорта
        __passengers (int): передаётся количество пассажиров

    Attributes:
        __received_money (int): количество заработанных денег
    """
    __received_money = 0

    def __init__(self, x, y, route, passengers):
        super().__init__(x, y, route)
        self.__passengers_amount = passengers

    def come_in(self, pass_amount):
        """
        Сеттер для увеличения количества пассажиров

        Args:
            pass_amount (int): передаётся количество пассажиров
        """
        print('\nОстановка. Набрали {} пассажира(ов).'.format(pass_amount))
        self.__passengers_amount += pass_amount

    def go_out(self, pass_amount):
        """
        Сеттер для уменьшения количества пассажиров

        Args:
            pass_amount (int): передаётся количество пассажиров
        """
        print('\nОстановка. Из автобуса вышло {} пассажира(ов).'.format(pass_amount))
        self.__passengers_amount -= pass_amount

    def to_drive(self, distance):
        """
        Метод, перемещающий транспорт в заведомо заданном направлении и вычисляет количество заработанных денег
        тариф: 100 метров - 1 рубль с человека

        Args:
            distance (int): передаётся значение расстояния (в метрах) до точки перемещения
        """
        print('\nЕдем. Следующая остановка через {} метров.'.format(distance))
        radian_route = radians(self.get_route())
        new_x = cos(radian_route) * distance
        new_y = sin(radian_route) * distance
        self.change_x_y(x=new_x, y=new_y)
        self.__received_money += self.__passengers_amount * (distance / 100)

    def get_received_money(self):
        """
        Геттер для получения количества заработанных денег (в рублях)

        :return: __received_money
        :rtype: int
        """
        return self.__received_money

    def __str__(self):
        """
        Магический метод, возвращающий строку с информацией об автобусе
        """
        x, y = self.get_x_y()
        return '\nАвтобус "Москва-Сочи"\nТекущее местоположение: x = {}, y = {}\nЗаработано {} рублей'.format(
            round(x, 2), round(x, 2), self.get_received_money()
        )


# Код для теста
bus_Moscov_Sochi = Bus(x=0, y=0, route=220, passengers=100)
print(bus_Moscov_Sochi)
bus_Moscov_Sochi.to_drive(distance=1000)
print(bus_Moscov_Sochi)
bus_Moscov_Sochi.go_out(pass_amount=20)
print(bus_Moscov_Sochi)
bus_Moscov_Sochi.to_drive(distance=2000)
print(bus_Moscov_Sochi)
bus_Moscov_Sochi.come_in(pass_amount=50)
print(bus_Moscov_Sochi)
bus_Moscov_Sochi.to_turn(new_route=270)
print(bus_Moscov_Sochi)
bus_Moscov_Sochi.to_drive(distance=2000)
print(bus_Moscov_Sochi)
