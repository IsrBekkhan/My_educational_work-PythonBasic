text = input('Введите строку: ')
symbols_amount = len(text)
text_set = set(list(text))
unique_symbols_amount = len(text_set)

# Алгоритм решения:
# Если количество уникальных символов <= ((количества всех символов строки) + 1) // 2
# то можно сделать палиндромом

if (symbols_amount + 1) // 2 >= unique_symbols_amount:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
