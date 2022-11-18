def move(n, x, y):
    if n == 1:
        print(f'Переложить диск 1 со стержня номер {x} на стержень номер {y}')
    else:
        temp = 6 - x - y
        move(n - 1, x, temp)
        print(f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
        move(n - 1, temp, y)


disс_amount = int(input('Введите количество дисков: '))
x = 1
y = 3
move(disс_amount, x, y)