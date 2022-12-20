from math import pi
from math import sqrt


class Circle:

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def square(self):
        return round(pi * self.r**2, 2)

    def perimeter(self):
        return round(2 * pi * self.r, 2)

    def increase(self, k):
        self.r *= k

    def is_cross(self, another_circle):
        leg_1 = self.x - another_circle.x
        leg_2 = self.y - another_circle.y
        hypotenuse = sqrt(leg_1**2 + leg_2**2)
        if self.r + another_circle.r > hypotenuse:
            return True


# Код для теста
circle_1 = Circle(0, 0, 3)
circle_2 = Circle(1, -1, 5)

print('Площадь:', circle_1.square(), 'м^2')
print('Периметр:', circle_1.perimeter(), 'м')
circle_1.increase(5)
print('Круг 1 увеличен в 5 раз')
print('Площадь:', circle_1.square(), 'м^2')

if circle_1.is_cross(circle_2):
    print('Окружности пересекаются.')
else:
    print('Не пересекаются.')

