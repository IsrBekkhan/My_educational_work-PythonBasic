from random import randint


class Human:
    satiety = 50

    def __init__(self, name='Noname'):
        self.name = name

    def eat(self):
        if house.food > 0:
            print('{} кушает.'.format(self.name))
            self.satiety += 30
            house.food -= 10
        else:
            print('{} умер.\nПричина смерти: голод.'.format(self.name))
            house.tenants.remove(self)

    def work(self):
        print('{} работает.'.format(self.name))
        self.satiety -= 15
        house.cash += 60
        if self.satiety <= 0:
            print('{} умер.\nПричина смерти: доработался.'.format(self.name))
            house.tenants.remove(self)

    def play(self):
        print('{} играет.'.format(self.name))
        self.satiety -= 10
        if self.satiety <= 0:
            print('{} умер.\nПричина смерти: доигрался.'.format(self.name))
            house.tenants.remove(self)

    def buy_food(self):
        if house.cash > 0:
            print('{} покупает продукты.'.format(self.name))
            house.food += 100
            house.cash -= 50
        else:
            print('{} умер.\nПричина смерти: бедность.'.format(self.name))
            house.tenants.remove(self)


class House:
    food = 50
    cash = 0
    tenants = [Human('Вася'), Human('Федя')]


def day_of_life(human_data):
    random_number = randint(1, 6)

    if human_data.satiety < 20:
        human_data.eat()
    elif house.food < 10:
        human_data.buy_food()
    elif house.cash < 50:
        human_data.work()
    elif random_number == 1:
        human_data.work()
    elif random_number == 2:
        human_data.eat()
    else:
        human_data.play()


house = House()
total_days = 0
while total_days < 365:
    print('\nДень {}-й:'.format(total_days + 1))
    if len(house.tenants) > 0:
        for human in house.tenants:
            day_of_life(human)
        total_days += 1
    else:
        print('\nВ доме прожито {} дней.'.format(total_days))
        print('Все жильцы в доме умерли.')
        break
else:
    print('\nВ доме прожито 365 дней.\nЖильцы:', end=' ')
    for human in house.tenants:
        print(human.name, end=' ')