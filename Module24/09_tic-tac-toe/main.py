class Cell:

    def __init__(self, cell_index):
        self.index = cell_index


class Board:

    def __init__(self):
        self.cells = [Cell(index) for index in range(1, 10)]

    def take_cell(self, cell_index, player):
        the_cell = self.cells[cell_index - 1]
        the_cell.index = player.flag

    def is_busy(self, cell_index):
        the_cell = self.cells[cell_index - 1]

        if isinstance(the_cell.index, str):
            return True


class Player:

    def __init__(self, name, flag):
        self.name = name
        self.choices = set()
        self.flag = flag


def motion(player_object):
    while True:
        answer = int(input('\n{}, на которую клетку ходите? Ваш флаг - ({})\n(Введите число от 1 до 9) '.format(
            player_object.name, player_object.flag
        )))

        if answer < 1 or answer > 9:
            print('Ошибка ввода. Повторите попытку.')
        elif board.is_busy(answer):
            print('Ошибка. Выбранная клетка уже занята. Выберите другую.')
        else:
            board.take_cell(answer, player_object)
            player_object.choices.add(answer)
            break


def print_result(class_object):
    count = 0
    for row in range(3):
        for col in range(count, count + 3):
            cell = class_object.cells[col]
            print(cell.index, end='\t')
        print()
        count += 3


def is_win(player_object):
    if {1, 2, 3} <= player_object.choices:
        return True
    if {4, 5, 6} <= player_object.choices:
        return True
    if {7, 8, 9} <= player_object.choices:
        return True

    if {1, 4, 7} <= player_object.choices:
        return True
    if {2, 5, 8} <= player_object.choices:
        return True
    if {3, 6, 9} <= player_object.choices:
        return True

    if {1, 5, 9} <= player_object.choices:
        return True
    if {3, 5, 7} <= player_object.choices:
        return True


player_1 = Player('Игрок 1', 'x')
player_2 = Player('Игрок 2', 'o')
board = Board()

try:
    while True:
        for player in player_1, player_2:
            print_result(board)
            motion(player)

            if is_win(player):
                print_result(board)
                print('\nВыиграл {}!'.format(player.name))
                raise ValueError('Игра окончена!')

except ValueError as exc:
    print(str(exc))
