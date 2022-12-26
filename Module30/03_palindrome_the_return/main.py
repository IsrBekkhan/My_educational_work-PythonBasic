from collections import Counter


def can_be_poly(word: str) -> bool:
    """
    Функция, проверяющая возможность создания палиндром из слова.
    """
    return len(list(filter(lambda elem: elem % 2, Counter(word).values()))) < 2


if __name__ == '__main__':
    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))

