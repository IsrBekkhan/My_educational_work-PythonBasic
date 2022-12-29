from re import findall


phone_numbers = ['9999999999', '999999-999', '99999x9999']
rus_counter = ['первый', 'второй', 'третий']


for index, number in enumerate(phone_numbers):
    if findall(r'[89]\d{9}', number) == [number]:
        print(rus_counter[index], 'номер: всё в порядке')
    else:
        print(rus_counter[index], 'номер: не подходит')
