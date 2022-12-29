from re import findall


numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

car_numbers = findall(r'[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', numbers)
taxi_numbers = findall(r'[АВЕКМНОРСТУХ]{2}\d{5,6}', numbers)

print('Список номеров частных автомобилей:', car_numbers)
print('Список номеров такси:', taxi_numbers)
