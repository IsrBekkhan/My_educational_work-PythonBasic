def calculating_math_func(data):
    result = 1

    if data in factorials_dict:
        result = factorials_dict[data]

    else:

        if len(factorials_dict) != 0:
            begin_num = len(factorials_dict) + 1
            dict_keys = list(factorials_dict)
            result = factorials_dict[dict_keys[-1]]

        else:
            begin_num = 1

        for index in range(begin_num, data + 1):
            result *= index
            factorials_dict[index] = result

        result = factorials_dict[data]

    result /= data ** 3
    result = result ** 10
    return result


factorials_dict = dict()
while True:
    user_num = int(input('Введите число: '))
    if user_num == 0:
        break
    print('Результат', calculating_math_func(user_num))