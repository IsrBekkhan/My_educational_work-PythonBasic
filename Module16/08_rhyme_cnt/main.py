human_amount = int(input('Кол-во человек: '))
human_list = list(range(1, human_amount + 1))
counter = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', counter, end = '')
print('-й человек')
start_number = 0

while len(human_list) != 1:
    print('\nТекущий круг людей:', human_list)
    print('Начало счёта с номера', human_list[start_number])
    exit_number = start_number + counter

    while len(human_list) < exit_number:
        exit_number -= len(human_list)

    print('Выбывает человек под номером', human_list[exit_number - 1])
    human_list.remove(human_list[exit_number - 1 ])
    start_number = exit_number
    if  len(human_list) < exit_number:
        exit_number -= len(human_list)
    start_number = exit_number - 1

print('\nОстался человек под номером', human_list[0])
