class Human:
    satiety_grade = 30
    happiness_grade = 100

    def __init__(self, name):
        self.name = name

    def to_eat(self):
        if our_house.food >= 30:
            our_house.food -= 30
            our_house.food_eaten += 30
            self.satiety_grade += 1
            print('{} кушает.'.format(self))
            return True

    def pet_cat(self):
        self.happiness_grade += 5
        self.satiety_grade -= 10
        print('{} гладит кота.'.format(self))

    def life_day(self):
        pass

    def is_alive(self):

        if self.satiety_grade < 0:
            print('{} умер от голода.'.format(self.name))
            our_house.tenants.remove(self)

        if self.happiness_grade < 10:
            print('{} умер от депрессии.'.format(self.name))
            our_house.tenants.remove(self)

    def day_happiness(self):
        if our_house.dirt > 90:
            self.happiness_grade -= 10


class Husband(Human):

    def __str__(self):
        return 'Муж - {}'.format(self.name)

    def to_play(self):
        self.happiness_grade += 20
        self.satiety_grade -= 10
        print('{} гоняет в игрушки.'.format(self))

    def to_work(self):
        self.satiety_grade -= 10
        our_house.cash += 150
        our_house.money_earned += 150
        print('{} работает в поте лица.'.format(self))

    def life_day(self):

        if self.satiety_grade <= 30:
            if not self.to_eat():
                self.to_work()

        elif self.happiness_grade <= 10:
            self.to_play()
        else:
            self.to_work()


class Wife(Human):

    def __str__(self):
        return 'Жена - {}'.format(self.name)

    def buy_products(self):
        if our_house.cash >= 20:
            our_house.cash -= 20
            our_house.food += 10
            our_house.cat_food += 10
            self.satiety_grade -= 10
            print('{} покупает продукты.'.format(self))

    def buy_fur_coat(self):
        if our_house.cash >= 350:
            our_house.cash -= 350
            our_house.bought_fur_coats += 1
            self.happiness_grade += 60
            self.satiety_grade -= 10
            print('{} покупает шубу.'.format(self))

    def clean_house(self):
        if our_house.dirt >= 100:
            our_house.dirt -= 100
        else:
            our_house.dirt = 0
        self.satiety_grade -= 10
        print('{} убирается в доме.'.format(self))

    def life_day(self):

        if self.satiety_grade <= 30:
            if not self.to_eat():
                self.buy_products()

        elif our_house.dirt > 90:
            self.clean_house()
        elif self.happiness_grade <= 10:
            self.buy_fur_coat()
        else:
            self.buy_products()


class Cat(Human):

    def __str__(self):
        return 'Кот - {}'.format(self.name)

    def to_eat(self):
        if our_house.cat_food >= 10:
            our_house.cat_food -= 10
            self.satiety_grade += 2
            print('{} кушает.'.format(self))
            return True

    def to_sleep(self):
        self.satiety_grade -= 10
        print('{} спит.'.format(self))

    def tear_wallpaper(self):
        our_house.dirt += 5
        self.satiety_grade -= 10
        print('{} дерёт обои.'.format(self))

    def pet_cat(self):
        pass

    def day_happiness(self):
        pass

    def is_alive(self):

        if self.satiety_grade < 0:
            print('{} умер от голода.'.format(self.name))
            our_house.tenants.remove(self)

    def life_day(self):

        if self.satiety_grade <= 10:
            if not self.to_eat():
                self.tear_wallpaper()

        elif self.happiness_grade <= 10:
            self.tear_wallpaper()
        else:
            self.to_sleep()


class Child(Husband):

    def __str__(self):
        return 'Ребёнок - {}'.format(self.name)

    def to_sleep(self):
        self.satiety_grade -= 10
        print('{} спит.'.format(self))

    def to_work(self):
        pass

    def life_day(self):

        if self.satiety_grade <= 10:
            if not self.to_eat():
                self.to_sleep()

        elif self.happiness_grade <= 10:
            self.to_play()
        else:
            self.to_sleep()


class House:
    cash = 100
    food = 50
    cat_food = 30
    dirt = 0
    tenants = []
    money_earned = 0
    food_eaten = 0
    bought_fur_coats = 0

    def house_pollution(self):
        self.dirt += 5


def day_in_house():

    for creature in our_house.tenants:
        creature.life_day()
        creature.is_alive()
        our_house.house_pollution()
    return 1


husband = Husband('Вася')
wife = Wife('Оля')
child = Child('Алёша')
cat_1 = Cat('Пушок')
cat_2 = Cat('Том')
cat_3 = Cat('Ленивец')

our_house = House()
our_house.tenants = [
    husband, wife, child,
    cat_1, cat_2, cat_3
]


total_days = 0
while total_days < 365:
    print('\nДень {}-й:'.format(total_days + 1))

    if len(our_house.tenants) > 0:
        total_days += day_in_house()
    else:
        print('\nВ доме прожито {} дней.'.format(total_days))
        print('Все жильцы в доме умерли.')
        print('Заработано денег: {} рублей \nСъедено еды: {}\nКуплено шуб: {} штук'.format(
            our_house.money_earned, our_house.food_eaten, our_house.bought_fur_coats
        ))
        break
else:
    print('\nВ доме прожито 365 дней.\nЖильцы:', end=' ')
    for human in our_house.tenants:
        print(human, end='; ')
