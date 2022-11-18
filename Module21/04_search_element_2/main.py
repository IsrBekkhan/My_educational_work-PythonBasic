site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(dictonary, key, depth=None):
    if depth == 0:
        return 'При заданном уровне глубины такого ключа не найдено.'

    if key in dictonary:
        return dictonary[key]

    for struct in dictonary.values():
        if isinstance(struct, dict):
            depth = depth or None
            if depth:
                depth -= 1
            result = find_key(struct, key, depth=depth)
            if result:
                return result
    else:
        result = None

    return result


user_key = input('Введите искомый ключ: ')
is_depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()

while is_depth != 'y' and is_depth != 'n':
    print('Ошибка ввода. Повторите попытку.')
    is_depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()

if is_depth == 'y':
    user_depth = int(input('Введите максимальную глубину: '))
    total_res = find_key(site, user_key, user_depth)
elif is_depth == 'n':
    total_res = find_key(site, user_key)

if total_res:
    print('Значение ключа: ', total_res)
else:
    print('Такого ключа не найдено')