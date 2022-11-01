violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
favorite = []
amount = int(input('Сколько песен выбрать? '))

for count in range(amount):
    print('Название', count + 1, end = '')
    name = input('-й песни: ')
    existance = True
    for index in range(len(violator_songs)):
        if name == violator_songs[index][0]:
            favorite.append(violator_songs[index])
            existance = False
            break
    if existance:
        print('Такой песни нет в списке.')

duration = 0
for index in range(len(favorite)):
    duration += favorite[index][1]

print('\nОбщее время звучания песен:', duration, 'минуты')