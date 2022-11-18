def sum(*args, lst=[0]):
    if len(args) == 1:
        user_values = args[0]
    else:
        user_values = args

    for i_elem in user_values:
        if isinstance(i_elem, list):
            lst[0] += sum(i_elem, lst=[0])
        else:
            lst[0] += i_elem
    return lst[0]


print('Ответ:', sum([[1, 2, [3]], [1], 3]))