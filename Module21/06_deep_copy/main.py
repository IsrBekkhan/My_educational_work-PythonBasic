import json


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def deep_copy(plagiat_name, original):
    temp_dict = dict()

    for key, value in original.items():

        if isinstance(value, dict):
            value = deep_copy(plagiat_name, value)

        else:
            word_list = value.split()

            if 'телефон' in word_list:
                change_index = word_list.index('телефон')
                word_list[change_index] = plagiat_name

            elif 'iphone' in word_list:
                change_index = word_list.index('iphone')
                word_list[change_index] = plagiat_name

            value = ' '.join(word_list)

        temp_dict[key] = value
    return temp_dict


plagiat_struct = dict()

amount = int(input('Сколько сайтов: '))
for _ in range(amount):
    site_name = input('\nВведите название продукта для нового сайта: ')
    plagiat_struct[f'Сайт для {site_name}'] = deep_copy(site_name, site)

    for key, value in plagiat_struct.items():
        print(f'\n{key}:\nsite = ', json.dumps(value, sort_keys=True, indent=4, ensure_ascii=False))


