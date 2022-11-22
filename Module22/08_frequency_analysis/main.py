def get_data(user_file):
    input_data = open(user_file, 'r', encoding='utf-8')
    text = input_data.read()
    letters_amount = 0
    letter_dictonary = dict()

    for letter in text.lower():

        if letter in letter_dictonary:
            letter_dictonary[letter] += 1
            letters_amount += 1

        else:
            if letter.isalpha():
                letter_dictonary[letter] = 1
                letters_amount += 1

    input_data.close()
    return letters_amount, letter_dictonary


def dict_sorter(user_dict):
    tuple_gen = zip(user_dict.keys(), user_dict.values())
    tuple_list = [value for value in tuple_gen]

    for i_max in range(len(tuple_list)):
        max_value = tuple_list[i_max][1]
        max_key = tuple_list[i_max][0]

        for curr in range(i_max, len(tuple_list)):
            current_value = tuple_list[curr][1]
            current_key = tuple_list[curr][0]

            if current_value > max_value:
                tuple_list[curr], tuple_list[i_max] = tuple_list[i_max], tuple_list[curr]

            elif current_value == max_value:
                if current_key < max_key:
                    tuple_list[curr], tuple_list[i_max] = tuple_list[i_max], tuple_list[curr]

    return dict(tuple_list)


def upload_data(amount, dictonary):
    output_data = open('analysis.txt', 'w', encoding='utf-8')

    for letter, count in dictonary.items():
        fraction = round(100 / amount * count / 100, 3)
        output_data.write(' '.join((letter, str(fraction), '\n')))

    output_data.close()
    print('Результат в файле analysis.txt:')


file_name = 'text.txt'
total_letters, letter_dict = get_data(file_name)
sorted_letter_dict = dict_sorter(letter_dict)
upload_data(total_letters, sorted_letter_dict)


