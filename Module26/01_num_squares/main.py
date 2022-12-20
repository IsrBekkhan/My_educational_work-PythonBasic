from collections.abc import Iterable


class Square:
    def __init__(self, finish_number: int) -> None:
        self.__finish = finish_number
        self.__count: int = 0

    def __iter__(self) -> Iterable[int]:
        return self

    def __next__(self) -> (int, None):
        self.__count += 1

        if self.__count > self.__finish:
            raise StopIteration
        return self.__count ** 2


def square(finish_number: int) -> (Iterable[int], None):
    count: int = 0

    while not count > finish_number:
        yield count ** 2
        count += 1
    else:
        return


square_gen = (number ** 2 for number in range(1, 11))


# Код для теста
class_square = Square(10)
print('класс-итератор')

for number in class_square:
    print(number)

square_func = square(10)
print('\nфункция-генератор')

for number in square_func:
    print(number)

print('\nгенераторное-выражение')
for number in square_gen:
    print(number)