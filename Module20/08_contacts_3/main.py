def add_contact():
    new_contact = input('Введите имя и фамилию нового контакта (через пробел): ').split()
    if tuple(new_contact) in phone_book:
        print('Такой человек уже есть в контактах.')
    else:
        phone = input('Введите номер телефона: ')
        phone_book[tuple(new_contact)] = phone


def search_contact():
    is_find = False
    search = input('Введите фамилию для поиска: ').title()
    for name, phone in phone_book.items():
        if name[1].startswith(search):
            print(name[0], name[1], phone)
            is_find = True
    if not is_find:
        print('Данный человек отсутствует в контактах.')


phone_book = dict()

while True:
    print('Введите номер действия:\n 1. Добавить контакт\n 2. Найти человека')
    choice = int(input())

    while choice != 1 and choice != 2:
        choice = int(input('Ошибка ввода. Повторите попытку: '))

    if choice == 1:
        add_contact()

    elif choice == 2:
        search_contact()

    print('Текущий словарь контактов:', phone_book)