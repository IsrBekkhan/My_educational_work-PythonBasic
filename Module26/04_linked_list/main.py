from typing import Any, Optional
from collections.abc import Iterable


class Node:
    """
    Класс узел, содержащий значение и следующий узел

    Args:
        value (Any): значение узла
        next (Node): следующий узел
    """

    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """
        Магический метод, возвращающий строку со значением узла

        :return: значение узла
        :rtype: str
        """
        return 'Node [{value}]'.format(
            value=str(self.value)
        )


class LinkedList:
    """
    Класс Связанный список, содержащий главный узел списка

    Attributes:
        head (Node): главный узел списка
        lenght (int): счётчик количества узлов в списке
        index (int): счётчик итераций для итератора
    """
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.lenght = 0
        self.index: int = -1

    def __str__(self) -> str:
        """
        Магический метод, возвращающий строку со списком значений узлов

        :return: список значений узлов
        :rtype: str
        """
        if self.head is not None:
            current = self.head
            values = [str(current.value)]

            while current.next is not None:
                current = current.next
                values.append(str(current.value))

            return '[{values}]'.format(values=' '.join(values))
        return 'LinkedList []'

    def __iter__(self) -> Iterable[Any]:
        """
        Магический метод, добавляющий итератор в данный класс

        :param: index: сбрасывает счётчик итераций
        :type: int
        """
        self.index = -1
        return self

    def __next__(self) -> (Optional[Any], StopIteration):
        """
        Магический метод, возвращащий по одному значению узлов данного класса

        :return: Any: значение узла
        :raise: StopIteration: исключение окончания итерации
        """
        while self.index < self.lenght:
            self.index += 1
            return self.get(self.index)
        raise StopIteration

    def append(self, elem: Any) -> None:
        """
        Метод, добавляющий ссылку на следующий узел

        Args:
            elem (Any): значение следующего узла
        """
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.lenght += 1

    def get(self, index: int) -> Optional[Any]:
        """
        Метод, возвращающий значение узла по индексу

        Args:
            index (int): индекс узла

        :return: Any: значение узла
        """
        cur_node = self.head
        cur_index = 0

        if self.lenght == 0 or self.lenght < index:
            raise IndexError

        while cur_node is not None:
            if cur_index == index:
                return cur_node.value
            cur_node = cur_node.next
            cur_index += 1

    def remove(self, index: int) -> None:
        """
        Метод, удаляющий узел по индексу

        Args:
            index (int): индекс узла
        """
        cur_node = self.head
        cur_index = 0
        if self.lenght == 0 or self.lenght < index:
            raise IndexError

        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.lenght -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.lenght -= 1


# Код для теста
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(0))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

for elem in my_list:
    print(elem)
