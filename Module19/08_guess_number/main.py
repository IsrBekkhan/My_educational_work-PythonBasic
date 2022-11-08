import random

N = int(input('Введите максимальное число: '))
numbers_set = {str(number) for number in range(1, N + 1)}
secret_number = str(random.randint(1, 10))

while True:
    question = input('\nНужное число есть среди вот этих чисел: ').lower().split()
    question_set = set(question)
    if question[0] == 'помогите!':
        break

    elif secret_number in question_set:
        print('Ответ Артёма: Да')
        numbers_set.intersection_update(question_set)

    else:
        print('Ответ Артёма: Нет')
        numbers_set.difference_update(question_set)

print('Артём мог загадать следующие числа:', ' '.join(numbers_set))

