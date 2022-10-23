begin_year = int(input('Введите первый год: '))
finish_year = int(input('Введите второй год: '))
print('\nГоды от', begin_year, 'до', finish_year, 'с тремя одинаковыми цифрами:')
for years in range(begin_year, finish_year + 1):
    for numbers in str(years):
        count = 0
        if numbers == str(years // 1000):
            count += 1
        if numbers == str(years // 100 % 10):
            count += 1
        if numbers == str(years // 10 % 10):
            count += 1
        if numbers == str(years % 10):
            count += 1
        if count >= 3:
            print(years)
            break