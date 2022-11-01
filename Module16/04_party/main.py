guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке:', guests)
    event = input('Гость пришёл или ушёл? ')
    if event == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) >= 6:
            print('Прости, ' + name + ', но мест нет.')
        else:
            guests.append(name)
            print('Привет,', name + '!')
    elif event == 'ушёл':
        name = input('Имя гостя: ')
        guests.remove(name)
        print('Пока,', name + '!')
    elif event == 'Пора спать':
        break
    else:
        print('Неверный ввод. Повторите попытку.')
print('Вечеринка закончилась, все легли спать.')

