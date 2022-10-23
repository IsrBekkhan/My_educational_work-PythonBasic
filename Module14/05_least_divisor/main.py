def lcd(number):
    for numbers in range(2, number + 1):
         if number % numbers == 0:
             res = numbers
             print('Наименьший делитель, отличный от единицы:', res)
             break

number = int(input('Введите число: '))
while number <= 1:
    number = int(input('Неверный ввод. Введите число больше 1: '))
lcd(number)
