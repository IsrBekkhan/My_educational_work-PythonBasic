def validation(data):
    try:
        if not len(data) == 3:
            raise IndexError('НЕ присутствуют все три поля')

        else:
            user_name, user_email, user_age = data[0], data[1], int(data[2])
            if not user_name.isalpha():
                raise NameError('Поле «Имя» содержит НЕ только буквы')
            elif user_email.find('@') == -1 or user_email.find('.') == -1:
                raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
            elif not 10 < user_age < 99:
                raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
    except (IndexError, NameError, SyntaxError, ValueError) as exc:
        return str(exc)


file_name = 'registrations.txt'
with open(file_name, 'r', encoding='utf-8') as registration_data:
    for user_data in registration_data:
        error = validation(user_data.split())
        if error:
            with open('registrations_bad.log', 'a', encoding='utf-8') as errors_data:
                error_message = '\t\t'.join((user_data.rstrip(), error, '\n'))
                errors_data.write(error_message)
        else:
            with open('registrations_good.log', 'a', encoding='utf-8') as right_data:
                right_data.write(user_data)

print('Проверка завершена. Результаты в файлах registrations_good.log и registrations_bad.log')
