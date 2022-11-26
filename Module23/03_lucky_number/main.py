import random

total_sum = 0
try:
    with open('out_file.txt', 'w') as number_list:
        while total_sum <= 777:
            new_number = int(input('Введите число: '))
            random_number = random.randint(1, 13)
            exit_number = 7
            if exit_number == random_number:
                raise Exception
            number_list.write(str(new_number))
            number_list.write('\n')
            total_sum += new_number

    print('Вы успешно выполнили условие для выхода из порочного цикла!')
except Exception:
    print('Вас постигла неудача!')