import random

stick_amount = int(input('Количество палок: '))
shot_amount = int(input('Количество бросков: '))
stick_list = [stick for stick in range(1, stick_amount + 1)]

for shot in range(shot_amount):
    L_stick = 0
    R_stick = -1

    while L_stick >= R_stick:
        L_stick = random.randint(1, stick_amount)
        R_stick = random.randint(1, stick_amount)

    print('Бросок', shot + 1, end = '')
    print('. Сбиты палки с номера', L_stick, 'по номер', R_stick, end = '')
    print('.')

    for index in range(L_stick, R_stick + 1):
        stick_list[index - 1] = '.'

stick_picture = ''
for index in stick_list:
    if index != '.':
        stick_picture += 'I'
    else:
        stick_picture += '.'

print('\nРезультат:', stick_picture)


