import os.path
from os import path, sep, walk
from collections.abc import Iterable


def gen_files_path(user_dir: str, user_path: str = path.abspath(sep)) -> Iterable[tuple]:
    result: Iterable[tuple] = walk(top=user_path, topdown=True, onerror=None, followlinks=False)

    for elem in result:
        direct_path = elem[0]
        direct_names = elem[1]
        files_list = elem[2]

        if user_dir in direct_names:
            print('\n\nПапка {} найдена в директории {}\n\n'.format(
                dir, direct_path
            ))
        if len(files_list) != 0:
            for file_object in files_list:
                yield path.join(direct_path, file_object)


dir_input = 'Module21'
path_input = 'C:\\Users\Bekkhan\PycharmProjects'
dir_tuple = gen_files_path(user_dir=dir_input, user_path=path_input)

for elem in dir_tuple:
    print(elem)
