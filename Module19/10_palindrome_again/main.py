def is_poly(word):
    char_dict = {}
    for i_sym in word:
        char_dict[i_sym] = char_dict.get(i_sym, 0) + 1

    odd_count = 0
    for value in char_dict.values():
        if value % 2 != 0:
            odd_count += 1

    return odd_count <= 1


word = input('Введите строку: ')

if is_poly(word):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
