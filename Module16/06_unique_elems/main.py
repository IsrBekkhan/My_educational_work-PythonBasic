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

for index in range(len(numbers_list_1)):
    if index > len(numbers_list_1) - 1:
        break
    count = numbers_list_1.count(numbers_list_1[index])
    remove_num = numbers_list_1[index]
    for _ in range(count - 1):
        numbers_list_1.remove(remove_num)

print('\nНовый первый список с уникальными элементами:', numbers_list_1)

