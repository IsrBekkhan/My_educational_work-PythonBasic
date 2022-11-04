first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')

shift = second_str.index(first_str[:1])
shifted_second = ''.join([second_str[shift:], second_str[:shift]])

if shifted_second.startswith(first_str):
    print(f'\nПервая строка получается из второй со сдвигом {shift}.')
else:
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')