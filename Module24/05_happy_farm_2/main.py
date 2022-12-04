class Potato:
    states_dict = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}
    state = 0

    def __init__(self, index):
        self.index = index

    def info(self):
        print('Картошка {} сейчас {}.'.format(
            self.index, self.states_dict[self.state]
        ))

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.info()

    def is_ripe(self):
        if self.state == 3:
            return True


class GardenPotato:

    def __init__(self, index, count=5):
        self.index = index
        self.potato_list = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for potato in self.potato_list:
            potato.grow()

    def are_all_ripe(self):
        if all([potato.is_ripe() for potato in self.potato_list]):
            print('Вся картошка созрела. Можно собирать!\n')
            return True
        else:
            print('Картошка все ещё не созрела.\n')


class Gardener:

    def __init__(self, name, garden_count=1):
        self.name = name
        self.garden_list = [GardenPotato(index) for index in range(1, garden_count + 1)]

    def look_after(self):
        while True:
            ripe_list = []
            for garden in self.garden_list:
                print('{} ухаживает за грядкой номер {}.'.format(
                    self.name, garden.index
                ))
                garden.grow_all()
                ripe_list.append(garden.are_all_ripe())
            if all(ripe_list):
                break
        self.harvest()

    def harvest(self):
        print('{} собирает созревшую картошку.'.format(
            self.name))
        potato_amount = 0

        for garden in self.garden_list:
            for potato in garden.potato_list:
                if potato.is_ripe():
                    potato_amount += 1

        print('Количество собранной картошки:', potato_amount)


Gardener('Вася', 2).look_after()