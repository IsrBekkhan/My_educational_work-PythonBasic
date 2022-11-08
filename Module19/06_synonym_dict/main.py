amount = int(input('Введите количество пар слов: '))
synonyms_dict = dict()

for count in range(amount):
    pair = input(f'{count + 1}-я пара: ').lower().split(' - ')
    synonyms_dict[pair[0]] = pair[1]
    synonyms_dict[pair[1]] = pair[0]

word = input('\nВведите слово: ').lower()
while not word in synonyms_dict:
    print('Такого слова в словаре нет.')
    word = input('Введите слово: ').lower()
else:
    print('Cиноним:', synonyms_dict[word].title())
