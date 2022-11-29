import os


def rare_letter_func(file_path):
    alphavet = 'abcdefghijklmnopqrstuvwxyz'
    input_file = open(file_path, 'r')
    text = input_file.read().lower()
    min_count = len(text)
    rare_letter_temp = ''

    for letter in alphavet:
        if letter in text:
            if text.count(letter) < min_count:
                min_count = text.count(letter)
                rare_letter_temp = letter
    input_file.close()

    return rare_letter_temp


strings = 0
words = 0
letters = 0

abs_path = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))
input_data = open(abs_path, 'r')

for string in input_data:
    strings += 1
    words_list = string.split()
    words += len(words_list)

    for word in words_list:
        letters += len(word)

input_data.close()
rare_letter = rare_letter_func(abs_path)

print('Количество букв в файле:', letters)
print('Количество слов в файле:', words)
print('Количество строк в файле:', strings)
print('Наиболее редкая буква:', rare_letter)