amount = int(input('Количество стран: '))
country_dict = dict()
rus_counter_list = ['Первый', 'Второй', 'Третий']

for count in range(amount):
    country_cities = input(f'{count + 1}-я страна: ').split()
    country_dict[country_cities[0]] = country_cities[1:]

for count in range(3):
    find = False
    state = input(f'\n{rus_counter_list[count]} город: ')

    for key in country_dict:

        if state in country_dict[key]:
            print(f'Город {state} расположен в стране {key}')
            find = True

    if not find:
        print(f'По городу {state} данных нет')
