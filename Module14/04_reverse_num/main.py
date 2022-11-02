def revers_int(number):
    num_int = ''
    for digit in number:
        if digit != '.':
            num_int = digit + num_int
        else:
            break

    return num_int


def revers_float(number):
    num_float = ''
    point = False
    for digit in number:
        if digit == '.':
            point = True
        elif point:
            num_float = digit + num_float

    return num_float


num_1 = input('Введите первое число: ')
num_2 = input('Введите второе число: ')

num_1_rev = revers_int(num_1) + '.' + revers_float(num_1)
num_2_rev = revers_int(num_2) + '.' + revers_float(num_2)

print('\nПервое число наоборот:', float(num_1_rev))
print('Второе число наоборот:', float(num_2_rev))
print('Сумма:', float(num_1_rev) + float(num_2_rev))


