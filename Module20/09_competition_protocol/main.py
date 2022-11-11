amount = int(input('Сколько записей вносится в протокол? '))
while amount < 3:
    amount = int(input('Ошибка ввода: введите количество записей больше 2: '))
print('Записи (результат и имя):')
protocol = dict()

for count in range(amount):
    record = input(f'{count + 1}-я запись: ').split()

    protocol_temp = protocol.copy()
    for key, score in protocol_temp.items():
        if record[1] in key:
            if int(record[0]) > int(score):
                protocol[key] = record[0]
                protocol[(count + 1, record[1])] = protocol.pop(key)
    protocol[(count + 1, record[1])] = record[0]

print('\nИтоги соревнований:')
for place in range(3):
    maximum = 0
    name = tuple()
    for info, score in protocol.items():
        if int(score) > int(maximum):
            maximum = score
            name = info
    print(f'{place + 1}-е место. {name[1]} ({maximum})')
    protocol.pop(name)