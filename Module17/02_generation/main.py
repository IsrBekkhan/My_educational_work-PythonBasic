import random

N = int(input('Введите длину списка: '))
numbers_list = [random.randint(0, 10) % 5 if index % 2 != 0
                else 1
                for index in range(N)]

print(numbers_list)