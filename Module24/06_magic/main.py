class Water:

    def __str__(self):
        return 'Вода'

    def __add__(self, other):

        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Ground):
            return Dirt()
        return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):

        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):

        if isinstance(other, Ground):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        return None


class Ground:

    def __str__(self):
        return 'Земля'

    def __add__(self, other):

        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        return None


class FifthElement:

    def __str__(self):
        return 'Пятый элемент'

    def __add__(self, other):

        if isinstance(other, Storm):
            return Water(), Air()
        elif isinstance(other, Steam):
            return Water(), Fire()
        elif isinstance(other, Dirt):
            return Water(), Ground()
        elif isinstance(other, Lightning):
            return Air(), Fire()
        elif isinstance(other, Dust):
            return Air(), Ground()
        elif isinstance(other, Lava):
            return Fire(), Ground()
        return None


class Storm:

    def __str__(self):
        return 'Шторм'

    def __add__(self, other):

        if isinstance(other, Lava):
            return FifthElement()
        return None


class Steam:

    def __str__(self):
        return 'Пар'

    def __add__(self, other):

        if isinstance(other, Dust):
            return FifthElement()
        return None


class Dirt:

    def __str__(self):
        return 'Грязь'

    def __add__(self, other):

        if isinstance(other, Lightning):
            return FifthElement()
        return None


class Lightning:

    def __str__(self):
        return 'Молния'

    def __add__(self, other):

        if isinstance(other, Dirt):
            return FifthElement()
        return None


class Dust:

    def __str__(self):
        return 'Пыль'

    def __add__(self, other):

        if isinstance(other, Steam):
            return FifthElement()
        return None


class Lava:

    def __str__(self):
        return 'Лава'

    def __add__(self, other):

        if isinstance(other, Storm):
            return FifthElement()
        return None


# Код для теста
fire = Fire()
water = Water()
lava = Lava()
storm = Storm()
fifth_element = FifthElement()

print(fire + water, lava + storm)
result = fifth_element + lava
print(*result)



