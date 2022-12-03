from random import randint


class Human:
    satiety = 50

    def __init__(self, name='Noname'):
        self.name = name

    def eat(self):
        if House().food > 0:
            print('{} кушает.'.format(self.name))
            self.satiety += 15
            House().food -= 30
        else:
            print('{} умер.\nПричина смерти: голод.'.format(self.name))
            House().tenants.remove(self)

    def work(self):
        print('{} работает.'.format(self.name))
        self.satiety -= 15
        House().cash += 40
        if self.satiety <= 0:
            print('{} умер.\nПричина смерти: доработался.'.format(self.name))
            House().tenants.remove(self)

    def play(self):
        print('{} играет.'.format(self.name))
        self.satiety -= 30
        if self.satiety <= 0:
            print('{} умер.\nПричина смерти: доигрался.'.format(self.name))
            House().tenants.remove(self)

    def buy_food(self):
        if House().cash > 0:
            print('{} покупает продукты.'.format(self.name))
            House().food += 50
            House().cash -= 50
        else:
            print('{} умер.\nПричина смерти: бедность.'.format(self.name))
            House().tenants.remove(self)


class House:
    food = 50
    cash = 0
    tenants = [Human('Вася'), Human('Федя')]


def day_of_life(human_data):
    random_number = randint(1, 6)

    if human_data.satiety < 20:
        human_data.eat()
    elif House().food < 10:
        human_data.buy_food()
    elif House().cash < 50:
        human_data.work()
    elif random_number == 1:
        human_data.work()
    elif random_number == 2:
        human_data.eat()
    else:
        human_data.play()


total_days = 0
while total_days < 365:
    print('\nДень {}-й:'.format(total_days + 1))
    if len(House().tenants) > 0:
        for human in House().tenants:
            day_of_life(human)
        total_days += 1
    else:
        print('\nВ доме прожито {} дней.'.format(total_days))
        print('Все жильцы в доме умерли.')
        break
else:
    print('\nВ доме прожито 365 дней.\nЖильцы:', end=' ')
    for human in House().tenants:
        print(human.name, end=' ')