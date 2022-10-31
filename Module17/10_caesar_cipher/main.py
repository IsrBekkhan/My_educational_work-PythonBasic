alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

encrypted_letters = [' ' if letter == ' '
    else alphabet[(alphabet.index(letter) + shift) % 33]
    for letter in message]

encrypted_word = ''
for letter in encrypted_letters:
    encrypted_word += letter

print('Зашифрованное сообщение:', encrypted_word)
