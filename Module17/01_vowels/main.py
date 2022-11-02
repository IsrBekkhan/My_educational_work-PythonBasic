text = input('Введите текст: ')
all_vowels = 'ауоыиэяюёе'
vowels_list = [letter for letter in text if all_vowels.count(letter) > 0]

print('\nСписок гласных букв:', vowels_list)
print('Длина списка:', len(vowels_list))