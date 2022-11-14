while True:
    password = input('Придумайте пароль: ')
    count = 0

    for symbol in password:
        if symbol.isdigit():
            count += 1

    if password.islower() or len(password) < 8 or count < 3:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break