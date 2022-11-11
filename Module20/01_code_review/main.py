students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def get_info(dict):
    all_interest = list()
    surnames_length = 0

    for value in dict.values():
        all_interest.extend(value['interests'])
        surnames_length += len(value['surname'])

    return all_interest, surnames_length


pairs_ID_age = [(ID, data['age']) for ID, data in students.items()]
print('Список пар "ID студента — возраст":', pairs_ID_age)

interest_list, surnames_length = get_info(students)
print('Полный список интересов всех студентов:', interest_list)
print('Общая длина всех фамилий студентов:', surnames_length)

