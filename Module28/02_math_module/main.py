from math import pi


class MyMath:
    """
    Класс, содержащий методы для математических вычислений.
    """

    @classmethod
    def circle_len(cls, radius: int) -> int:
        """
        Метод, для вычисления длины окружности.

        Args:
            radius (int): радиус окружности
        :return int: длина окружности
        """
        return 2 * pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> int:
        """
        Метод, для вычисления площади окружности.

        Args:
            radius (int): радиус окружности
        :return int: площадь окружности
        """
        return pi * radius ** 2

    @classmethod
    def sphere_sq(cls, radius: int) -> int:
        """
        Метод, для вычисления площади поверхности сферы.

        Args:
            radius (int): радиус окружности
        :return int: площадь поверхности сферы
        """
        return 4 * pi * radius ** 2

    @classmethod
    def square_sq(cls, side: int) -> int:
        """
        Метод, для вычисления площади квадрата.

        Args:
            side (int): длина стороны
        :return int: площадь квадрата
        """
        return side ** 2

    @classmethod
    def cube_volume(cls, side: int) -> int:
        """
        Метод, для вычисления объёма куба.

        Args:
            side (int): длина стороны
        :return int: объём куба
        """
        return side ** 3

    @classmethod
    def cube_area_sq(cls, side: int) -> int:
        """
        Метод, для вычисления площади поверхности куба.

        Args:
            side (int): длина стороны
        :return int: площадь поверхности куба
        """
        return side ** 3


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
