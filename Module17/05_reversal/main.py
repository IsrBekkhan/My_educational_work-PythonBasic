text = input('Введите строку: ')
reverse_text = text[::-1]

start_index = text.index('h')
end_index = reverse_text.index('h')

reverse_piece = text[len(text) - 1 - end_index - 1:start_index:-1]

print('Развёрнутая последовательность между первым и последним h:', reverse_piece)







