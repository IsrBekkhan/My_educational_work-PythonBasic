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
    rev_calc = num_float
    count = 0

    while num_float != 0:
        count += 1
        num_float = round(num_float * 10 % 1, 14)

    res = 0
    for amount in range(1, count + 1):
        res += (round(rev_calc * 10 // 1, 14)) * 10**(amount - 1)
        rev_calc = round(rev_calc * 10 % 1, 14)
    res /= 10**count

    return res

num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
num_1_rev = revers_int(num_1) + revers_float(num_1)
num_2_rev = revers_int(num_2) + revers_float(num_2)

print('\nПервое число наоборот:', round(num_1_rev, 2))
print('Второе число наоборот:', round(num_2_rev, 2))
print('Сумма:', num_1_rev + num_2_rev)


