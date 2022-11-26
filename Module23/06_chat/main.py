user_name = input('Введите имя: ')
file_name = 'chat_list.txt'

while True:
    print('\nВыберите действие:\n'
          '1. Посмотреть текущий текст чата.\n'
          '2. Отправить сообщение.')

    choice = input()
    while not choice in ('1', '2'):
        choice = input('Ошибка ввода. Повторите попытку.')


    try:
        if choice == '1':
            with open(file_name, 'r', encoding='utf-8') as view_messages:
                for message in view_messages:
                    print(message.rstrip())

        elif choice == '2':
            user_message = input('Введите сообщение: ')
            with open(file_name, 'a', encoding='utf-8') as add_message:
                add_message.write('[{name}]: {message}\n'.format(
                    name=user_name,
                    message=user_message))

    except FileNotFoundError:
        print('Нет сообщений')
    except PermissionError:
        print('Отказано в доступе к файлу {title}'.format(title=file_name))


