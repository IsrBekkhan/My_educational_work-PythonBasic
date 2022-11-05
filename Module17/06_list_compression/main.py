import random

amount = int(input('Количество чисел в списке: '))
number_list = [random.randint(0, 2) for _ in range(amount)]

print('\nСписок до сжатия:', number_list)

for _ in range(number_list.count(0)):
    number_list.remove(0)
    number_list.append(0)

print('Список после перестановки нулей:', number_list)

for _ in range(number_list.count(0)):
    number_list.remove(0)

print('Список после сжатия:', number_list)