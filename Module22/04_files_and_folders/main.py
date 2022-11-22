import os


def get_info(struct, files=0, directs=0, size=0):
    for substruct in os.listdir(struct):
        path = os.path.join(struct, substruct)

        if os.path.isdir(path):
            directs += 1
            result = get_info(path)
            files += result[0]
            directs += result[1]
            size += result[2]

        elif os.path.isfile(path):
            files += 1
            size += os.path.getsize(path)

    return files, directs, size


user_path = input('Путь: ')
files, directs, size = get_info(user_path)

print('Размер каталога (в Кб):', round(size / 1024, 2))
print('Количество подкаталогов:', directs)
print('Количество файлов:', files)