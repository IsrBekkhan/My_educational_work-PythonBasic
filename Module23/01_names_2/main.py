def letters_counter(string):
    amount = len(string.rstrip())

    if amount < 3:
        raise SyntaxError('Ошибка: в {number}-м имени меньше 3-x букв: {name}'.format(
                            number=count + 1, name=name.rstrip()))
    return amount


def add_log(error_message):
    with open('errors.log', 'a', encoding='utf-8') as save_log:
        save_log.write(str(error_message))
        save_log.write('\n')


letters_amount = 0

with open('people.txt', 'r', encoding='utf-8') as input_names:
    for count, name in enumerate(input_names):
        try:
            letters_amount += letters_counter(name)
        except SyntaxError as exc:
            letters_amount += len(name.rstrip())
            print(exc)
            add_log(exc)

    print('Общее количество символов:', letters_amount)