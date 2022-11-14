message = input('Сообщение: ')
temp = ''
reverse_message = ''

for letter in message:

    if letter.isalpha():
        temp = letter + temp

    else:
        reverse_message += temp
        reverse_message += letter
        temp = ''

print('Новое сообщение: ', reverse_message)
