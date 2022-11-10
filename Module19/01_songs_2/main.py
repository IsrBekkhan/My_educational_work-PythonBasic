violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

amount = int(input('Сколько песен выбрать? '))
total_duration = 0

for count in range(amount):
    name = input(f'Название {count + 1}-й песни: ')

    if name in violator_songs:
        total_duration += violator_songs[name]
    else:
        print('Такой песни нет в библиотеке.')

print(f'\nОбщее время звучания песен: {round(total_duration, 2)} минуты')
