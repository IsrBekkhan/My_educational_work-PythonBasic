def tpl_sort(tuple_combination):
    for value in tuple_combination:
        if str(value).isalpha():
            return tuple_combination
    return tuple(sorted(list(tuple_combination)))

print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))

