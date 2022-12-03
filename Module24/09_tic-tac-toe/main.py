class Cell:

    def __init__(self, index):
        self.index = index
        self.cell_position = 0

    def is_vacant_cell(self):
        if self.cell_position == 0:
            return True


class Board:

    def __init__(self):
        self.cells = [Cell(index) for index in range(1, 10)]

    def take_cell(self, index, player):
        self.cells[index-1].cell_position = player.flag

    def is_vacant(self, index):

        if self.cells[index - 1].is_vacant_cell():
            return True


class Player:

    def __init__(self, name, flag):
        self.name = name
        self.choices = set()
        self.flag = flag


def motion(player):
    while True:
        answer = int(input('\n{}, на которую клетку ходите?\n(Введите число от 1 до 9) '.format(player.name)))

        if answer < 1 or answer > 9:
            print('Ошибка ввода. Повторите попытку.')
        elif Board().is_vacant(answer):
            Board().take_cell(answer, player)
            player.choices.add(answer)
            break
        else:
            print('Ошибка. Выбранная клетка уже занята. Выберите другую.')

    print(player.choices)


player_1 = Player('Игрок 1', '1')
player_2 = Player('Игрок 2', '2')

while True:
    motion(player_1)
    motion(player_2)
    for index, cell in enumerate(Board().cells):
        print(index + 1, cell.cell_position)




