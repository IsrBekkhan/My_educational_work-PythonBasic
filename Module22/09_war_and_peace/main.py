import zipfile


def unzip(archive):
    zfile = zipfile.ZipFile(archive, 'r')

    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
    zfile.close()


def letters_counter(user_file):
    if user_file.endswith('.zip'):
        unzip(user_file)
        user_file = ''.join((user_file[:-3], 'txt'))
    input_data = open(user_file, 'r', encoding='utf-8')
    letters_dict = dict()

    for string in input_data:
        for letter in string:
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                if letter.isalpha():
                    letters_dict[letter] = 1

    input_data.close()
    return letters_dict


def sorter_func(dictonary):
    sorted_values = sorted(dictonary.values(), reverse=True)
    sorted_dict = dict()

    for value in sorted_values:
        for key in dictonary:
            if dictonary[key] == value:
                sorted_dict[key] = value
                break


    return sorted_dict


def printer(dictonary):
    print('+{:-^19}+'.format('+'))
    print('|{: ^9}|{: ^9}|'.format('буква', 'частота'))
    print('+{:-^19}+'.format('+'))
    for letter, count in dictonary.items():
        print('|{: ^9}|{: ^9}|'.format(letter, count))
    print('+{:-^19}+'.format('+'))


file_name = 'voyna-i-mir.zip'
result = letters_counter(file_name)
result = sorter_func(result)
printer(result)