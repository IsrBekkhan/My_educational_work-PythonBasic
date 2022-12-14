from os import path, sep, walk
from collections.abc import Iterable


def gen_files_path(dir: str, path: str = path.abspath(sep)) -> Iterable[tuple]:
    result: tuple = walk(top=path, topdown=True, onerror=None, followlinks=False)

    for elem in result:
        direct_path = elem[0]
        direct_names = elem[1]
        files_list = elem[2]

        if dir in direct_names:
            print('\n\nПапка {} найдена в директории {}\n\n'.format(
                dir, direct_path
            ))
        if len(files_list) != 0:
            yield direct_path, files_list


user_dir = 'Module21'
user_path = 'C:\\Users\Bekkhan\PycharmProjects'
dir_tuple = gen_files_path(dir=user_dir, path=user_path)

for elem in dir_tuple:
    print(elem)
