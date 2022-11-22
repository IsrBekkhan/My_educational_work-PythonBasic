def get_info(user_file):
    norm = 0
    norm_get = False
    scores_dict = dict()

    input_data = open(user_file, 'r', encoding='utf-8')

    for value in input_data:

        if not norm_get:
            norm = int(value)
            norm_get = True

        else:
            player_score = value.split()
            if int(player_score[2]) > norm:
                cut_name = ' '.join((''.join((player_score[1][0], '.')), player_score[0]))
                scores_dict[cut_name] = player_score[2]

    input_data.close()
    return scores_dict


def dict_sorter(dictonary):
    sorted_values = sorted(dictonary.values(), reverse=True)
    sorted_dictonary = dict()

    for value in sorted_values:
        for key in dictonary:
            if dictonary[key] == value:
                sorted_dictonary[key] = value
                break

    return sorted_dictonary


def upload_info(dictonary):
    output_data = open('second_tour.txt', 'w', encoding='utf-8')
    output_data.write('2\n')

    count = 1

    for name, scores in dictonary.items():
        position = ''.join((str(count), ')'))
        output_data.write(' '.join((position, name, scores, '\n')))
        count += 1

    output_data.close()
    print('Результат в файле second_tour.txt')


file_name = 'first_tour.txt'
best_results = get_info(file_name)
sorted_dict = dict_sorter(best_results)
upload_info(sorted_dict)
