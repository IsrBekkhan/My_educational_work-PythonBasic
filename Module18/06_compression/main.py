text = input('Введите строку: ')
text_list = []
count = 1

for index in range(1, len(text)):
    if text[index] == text[index - 1]:
        count += 1

        if index + 1 == len(text):
            text_list.append(text[index])
            text_list.append(str(count))
            break

    elif text[index] != text[index - 1]:
        text_list.append(text[index - 1])
        text_list.append(str(count))
        count = 1

        if index + 1 == len(text):
            text_list.append(text[index])
            text_list.append(str(count))
            break

print('\nЗакодированная строка:', ''.join(text_list))
