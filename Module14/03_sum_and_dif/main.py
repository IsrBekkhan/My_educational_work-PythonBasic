def summ_n(N):
    summ = 0
    while N != 0:
        res = N % 10
        summ += res
        N //= 10
    return summ
def counter(N):
    count = 0
    while N != 0:
        N //= 10
        count += 1
    return count

number = int(input('Введите число: '))
print('Сумма чисел:', summ_n(number))
print('Количество цифр в числе:', counter(number))
print('Разность суммы и количества цифр:', abs(summ_n(number) - counter(number)))

