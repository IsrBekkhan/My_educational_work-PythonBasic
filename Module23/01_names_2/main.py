letters_amount = 0
string_number = 0

with open('people.txt', 'r', encoding='utf-8') as input_names:
    for name in input_names:
        try:
            letters_amount += len(name.rstrip())
            string_number += 1

            if len(name.rstrip()) < 3:
                raise Exception

        except Exception:
            error_message = 'Ошибка: в {number}-м имени меньше 3-x букв: {name}'.format(
                            number=string_number, name=name.rstrip())
            print(error_message)

            with open('errors.log', 'a', encoding='utf-8') as save_log:
                save_log.write(error_message)
                save_log.write('\n')

    print('Общее количество символов:', letters_amount)