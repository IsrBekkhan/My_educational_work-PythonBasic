from typing import List
from functools import reduce

if __name__ == '__main__':
    floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

    print(list(map(lambda f_num: round(f_num**3, 3), floats)))
    print(list(filter(lambda name: len(name) >= 5, names)))
    print(reduce(lambda a, b: a * b, numbers))



