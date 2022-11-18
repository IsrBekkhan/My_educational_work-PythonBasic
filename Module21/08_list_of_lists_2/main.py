nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def unlister(user_list, new_list=[]):
    for elem in user_list:
        if isinstance(elem, list):
            new_list.extend(unlister(elem, new_list=[]))
        else:
            new_list.append(elem)
    return new_list


print(unlister(nice_list))

