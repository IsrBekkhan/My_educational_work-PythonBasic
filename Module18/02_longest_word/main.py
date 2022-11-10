text = input('Введите строку: ').split()
length_word = [len(word) for word in text]
print('Самое длинное слово:', text[length_word.index(max(length_word))])
print('Длина этого слова:', max(length_word))