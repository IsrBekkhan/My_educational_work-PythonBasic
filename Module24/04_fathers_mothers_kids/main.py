from random import randint


class Parent:

    def __init__(self, name='Алина', age=20, kids=1):
        self.name = name
        self.age = age
        self.kids = {
            kid_names_list[index - 1]: Kid(kid_names_list[index - 1], randint(0, self.age - 16))
            for index in range(kids)
        }

    def personal_info(self):
        print('Имя - {};\nВозраст - {};'.format(
            self.name, self.age
        ))
        print('Дети -', end=' ')
        for name in self.kids:
            print(name, end='; ')
        print()

    def calm_down_kid(self, kid_name):
        self.kids[kid_name].stillness_status = 0

    def feed_kid(self, kid_name):
        self.kids[kid_name].hanger_status += 1
        self.kids[kid_name].stillness_status += 1


class Kid:
    hanger_status = 0
    stillness_status = 0

    def __init__(self, name='Noname', age=3):
        self.name = name
        self.age = age

    def hanger_status_info(self):
        hanger_dict = {-1: 'Голодный', 0: 'Сытый', 1: 'Переедание'}
        print(hanger_dict[self.hanger_status])

    def stillness_status_info(self):
        stillness_dict = {-1: 'Агрессивный', 0: 'Спокойный', 1: 'Печальный'}
        print(stillness_dict[self.stillness_status])


kid_names_list = [
                'Стёпа', 'Гена',
                'Артём', 'Оля',
                'Мария', 'Слава',
                'Вика', 'Катя',
                'Ира', 'Петя'
]

# Код для теста
family_1 = Parent('Алёна', 25, 5)
family_1.personal_info()
print('\nПокормили Гену')
family_1.feed_kid('Гена')
family_1.kids['Гена'].hanger_status_info()
family_1.kids['Гена'].stillness_status_info()
print('\nУспокоили Гену')
family_1.calm_down_kid('Гена')
family_1.kids['Гена'].hanger_status_info()
family_1.kids['Гена'].stillness_status_info()


