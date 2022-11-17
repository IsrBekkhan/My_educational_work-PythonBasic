def printer(start, num):
    if start == num:
        print(num)
        return
    print(start)
    printer(start + 1, num)


num = int(input('Введите num: '))
start = 1
printer(start, num)