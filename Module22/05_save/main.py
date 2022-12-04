import os.path


def saver(text, path, rename=False):
    new_file = open(path, 'w', encoding='utf-8')
    new_file.write(text)
    new_file.close()

    if rename:
        print('Файл успешно перезаписан!')
    else:
        print('Файл успешно сохранён!')


user_text = input('Введите строку: ')
save_to_path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):\n').split()
user_path = os.path.join(os.path.abspath(os.sep), *save_to_path)

while not os.path.exists(user_path):
   save_to_path = input('Ошибка ввода: такого пути не существует. Повторите попытку:\n').split()
   user_path = os.path.join(os.path.abspath(os.sep), *save_to_path)

file_name = input('Введите имя файла: ')
file_path = os.path.join(user_path, file_name, '.txt')

while os.path.exists(file_path):
    choice = input('Вы действительно хотите перезаписать файл? ').lower()

    if choice == 'да':
        saver(user_text, file_path, rename=True)
        break

    else:
        file_name = input('Введите другое название файла: ')
        file_path = os.path.join(user_path, file_name, '.txt')

else:
    saver(user_text, file_path)




