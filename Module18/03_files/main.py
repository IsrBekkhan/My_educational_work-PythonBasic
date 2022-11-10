symbols = '@№$%^&\*()'
file = input('Название файла: ')

for symbol in symbols:
    if file.startswith(symbol):
        print('Ошибка: название начинается на один из специальных символов.')
        break

if not file.endswith('.txt') or file.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')