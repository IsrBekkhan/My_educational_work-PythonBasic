def slicer(tuple_comb, rand_elem):

    if not rand_elem in tuple_comb:
        return tuple()

    begin_tuple = None
    end_tuple = None
    is_begin = True

    for key, value in enumerate(tuple_comb):

        if value == rand_elem and is_begin:
            begin_tuple = key
            is_begin = False

        elif value == rand_elem and not is_begin:
            end_tuple = key + 1
            break

    return tuple(tuple_comb[begin_tuple:end_tuple])

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))