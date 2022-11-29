def validation(data):
    if not len(data) == 3:
        raise IndexError('НЕ присутствуют все три поля')

    else:
        user_name, user_email, user_age = data[0], data[1], int(data[2])
        is_alpha(user_name)
        is_email(user_email)
        is_age(user_age)


def is_alpha(name):
    if not name.isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')


def is_email(email):
    if email.find('@') == -1 or email.find('.') == -1:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')


def is_age(age):
    if not 10 < age < 99:
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')


def good_saver(data):
    with open('registrations_good.log', 'a', encoding='utf-8') as right_data:
        right_data.write(data)


def bad_saver(data, error):
    with open('registrations_bad.log', 'a', encoding='utf-8') as errors_data:
        error_message = '\t\t'.join((data.rstrip(), str(error), '\n'))
        errors_data.write(error_message)


file_name = 'registrations.txt'
with open(file_name, 'r', encoding='utf-8') as registration_data:
    for user_data in registration_data:
        try:
            validation(user_data.split())

        except (IndexError, NameError, SyntaxError, ValueError) as exc:
            bad_saver(user_data, exc)

        else:
            good_saver(user_data)

print('Проверка завершена. Результаты в файлах registrations_good.log и registrations_bad.log')
