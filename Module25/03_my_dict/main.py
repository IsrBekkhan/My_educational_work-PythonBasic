class MyDict(dict):
    """
    Класс MyDict. Родитель: dict

    """
    def get(self, key):
        """
        Метод, возвращающий значение в словаре по его ключу
        если ключа нет в словаре - возвращает 0.

        :return: значение в словаре
        или
        :return int: 0
        """
        if key in self:
            return self[key]
        return 0


# Код для теста
my_dict = MyDict()
my_dict[1] = 'Один'
my_dict[2] = 'Два'
my_dict[3] = 'Три'

print(my_dict.get(1))
print(my_dict.get(4))
