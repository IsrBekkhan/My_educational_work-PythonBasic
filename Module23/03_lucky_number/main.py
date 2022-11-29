import random


def check_luck(exit_number=7):
    random_number = random.randint(1, 13)
    if exit_number == random_number:
        raise ValueError('Вас постигла неудача!')


def numbers_saver(number):
    with open('out_file.txt', 'a') as number_list:
        number_list.write(str(number))
        number_list.write('\n')


total_sum = 0

while total_sum <= 777:
    try:
        new_number = int(input('Введите число: '))
    except ValueError:
        print('Введено значение нечислового типа')
        continue

    try:
        check_luck()
    except ValueError as exc:
        print(exc)
        break

    numbers_saver(new_number)
    total_sum += new_number
else:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
