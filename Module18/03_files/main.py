symbols = '@№$%^&\*()'
file_name = input('Название файла: ')

if file_name[0] in symbols:
    print('Ошибка: название начинается на один из специальных символов.')
elif not file_name.endswith('.txt') or file_name.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')