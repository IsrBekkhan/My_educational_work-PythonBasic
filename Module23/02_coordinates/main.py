import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return round(x / y, 4)


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return round(y / x, 4)


res1 = None
res2 = None
file_name = 'coordinates.txt'
file_2 = open('result.txt', 'w', encoding='utf-8')
try:
    with open(file_name, 'r') as file:
        for line in file:
            nums_list = line.split()
            try:
                res1 = f(int(nums_list[0]), int(nums_list[1]))
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                error_message = None
            except ZeroDivisionError:
                error_message = 'Ошибка деления на ноль.'
                print(error_message)
            number = random.randint(0, 100)

            if error_message:
                file_2.write(error_message)
            else:
                my_list = sorted([str(res1), str(res2), str(number)])
                file_2.write(' '.join(my_list))
            file_2.write('\n')

except FileNotFoundError:
    print(f'Файл {file_name} не найден.')
except PermissionError:
    print('Отказано в доступе к файлу.')
finally:
    file_2.close()
    print("Операция завершена. Результаты в файле 'result.txt'")