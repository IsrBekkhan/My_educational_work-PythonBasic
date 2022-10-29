numbers_list_1 = []
numbers_list_2 = []

for count in range(3):
    print('Введите', count + 1, end = '')
    number = int(input('-е число для первого списка: '))
    numbers_list_1.append(number)

for count in range(7):
    print('Введите', count + 1, end = '')
    number = int(input('-е число для второго списка: '))
    numbers_list_2.append(number)

print('\nПервый список:', numbers_list_1)
print('Второй список:', numbers_list_2)

numbers_list_1.extend(numbers_list_2)
new_list = []

for value in numbers_list_1:
    if new_list.count(value) == 0:
        new_list.append(value)

print('\nНовый первый список с уникальными элементами:', new_list)

