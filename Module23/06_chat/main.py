def watch_chat():
    with open('chat_list.txt', 'r', encoding='utf-8') as view_messages:
        messages = view_messages.readlines()
        print(''.join(messages))


def send_message():
    user_message = input('Введите сообщение: ')
    with open('chat_list.txt', 'a', encoding='utf-8') as add_message:
        add_message.write('[{name}]: {message}\n'.format(
            name=user_name,
            message=user_message))


user_name = input('Введите имя: ')

while True:
    print('\nВыберите действие:\n'
          '1. Посмотреть текущий текст чата.\n'
          '2. Отправить сообщение.')

    choice = input()
    while not choice in ('1', '2'):
        choice = input('Ошибка ввода. Повторите попытку.')

    try:
        if choice == '1':
            watch_chat()

        elif choice == '2':
            send_message()

    except FileNotFoundError:
        print('Нет сообщений.')
    except PermissionError:
        print('Сервер перегружен. Повторите попытку.')


