from random import randint


class Student:

    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

    def av_grade(self): # 1/2 Для теста функции сортировки.
        return sum(self.grades) / len(self.grades)


def add_data(names_list):
    new_list = list()

    for name in names_list:
        group = randint(1, 10)
        grades = [randint(1, 5) for _ in range(5)]
        new_list.append(Student(name, group, grades))

    return new_list


def data_sorter(user_data):

    for i_min in range(len(user_data)):
        for curr in range(i_min, len(user_data)):
            min_value = sum(user_data[i_min].grades)/len(user_data[i_min].grades)
            curr_value = sum(user_data[curr].grades)/len(user_data[curr].grades)

            if curr_value < min_value:
                user_data[curr], user_data[i_min] = user_data[i_min], user_data[curr]


def printer(user_list):
    for data in user_list:
        print(data.name, '-',
              data.av_grade()) # 2/2 Для теста функции сортировки.


students_names = [
                'Панов Ярослав', 'Чехова Алина',
                'Ли Степан', 'Нагиев Артём',
                'Брежнева Мария', 'Михайлов Стас',
                'Дрокин Дмитрий', 'Ян Алексей',
                'Волочкова Ольга', 'Бузова Вика'
]

student_data = add_data(students_names)
data_sorter(student_data)
printer(student_data)


