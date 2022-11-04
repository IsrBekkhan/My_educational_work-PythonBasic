message = input('Сообщение: ').split()
marks = ('.', ',', '!', '?')
reverse_message = []

for word in message:
    if word.endswith(marks):
        word_list = list(word)
        remarked_word = ''.join([''.join(word_list[-1:]), ''.join(word_list[:-1])])
        reverse_message.append(remarked_word[::-1])
    else:
        reverse_message.append(word[::-1])

print('\nНовое сообщение:', ' '.join(reverse_message))