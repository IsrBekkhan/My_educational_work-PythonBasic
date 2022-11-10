ip = input('Введите IP: ').split('.')

if len(ip) < 4:
    print('Адрес — это четыре числа, разделённые точками.')
elif len(ip) > 4:
    print('Адрес не должен состоять из более чем 4 чисел.')
else:
    for number in ip:
        if not number.isdigit():
            print(number, '— это не целое число.')
        elif int(number) > 255:
            print(number, 'превышает 255.')
    print('IP-адрес корректен.')

