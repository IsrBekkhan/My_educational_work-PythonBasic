from typing import TextIO


class File:
    """
    Контекст-менеджер, для работы с файлами.

    Args:
        file_name (str): имя файла с расширением
    """

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.file_object = None

    def __enter__(self) -> TextIO:
        """
        Магический метод, для подготовки объекта файлового типа.

        :return: объект файлового типа
        """
        try:
            self.file_object = open(self.file_name, 'r', encoding='utf-8')
        except FileNotFoundError:
            self.file_object = open(self.file_name, 'w', encoding='utf-8')
            pass

        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        Магический метод, для завершения работы с объектом файлового типа.

        :return: bool
        """
        self.file_object.close()
        return True


with File('test.txt') as test:
    file_object = test
    print(type(file_object))
