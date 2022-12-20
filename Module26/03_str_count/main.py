from os import path, sep, walk
from collections.abc import Iterable


def gen_py_files(path: str = path.abspath(sep)) -> Iterable[tuple]:
    result = walk(top=path, topdown=True, onerror=None, followlinks=False)
    total_strings = 0

    for elem in result:
        files_list = elem[2]

        for file_object in files_list:

            if file_object.endswith('.py'):

                try:
                    with open(file_object, 'r', encoding='utf-8') as python_file:

                        for string in python_file:

                            if len(string.rstrip()) != 0:

                                if not '#' in string:
                                    total_strings += 1
                except FileNotFoundError:
                    pass
    yield total_strings


user_path = 'C:\\Users\Bekkhan\PycharmProjects'
dir_tuple = gen_py_files(path=user_path)

for elem in dir_tuple:
    print('Количество строк:', elem)
