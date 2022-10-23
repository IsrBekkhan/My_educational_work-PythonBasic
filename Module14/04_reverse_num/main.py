def revers_int(number):
    num_int = int(number)
    count_calc = num_int
    count = 0
    res = 0

    while count_calc != 0:
        count_calc //= 10
        count += 1

    for amount in range(1, count + 1):
        last_num = num_int % 10
        res += last_num * 10 ** (count - amount)
        num_int //= 10

    return res

def revers_float(number):
    num_float = round(number % 1, 14)
    count = 0

    while num_float != 0:
        count += 1
        num_float = round(num_float * 10 % 1, 14)
    number = int(round(number % 1, 14) * 10**count)
    res = revers_int(number) * 10**(-count)

    return res

num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
num_1_rev = revers_int(num_1) + revers_float(num_1)
num_2_rev = revers_int(num_2) + revers_float(num_2)

print('\nПервое число наоборот:', num_1_rev)
print('Второе число наоборот:', num_2_rev)
print('Сумма:', num_1_rev + num_2_rev)


