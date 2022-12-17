from human import *


class Wife(Human):

    def __str__(self):
        return 'Жена - {}'.format(self.name)

    def buy_products(self, house):
        if house.cash >= 20:
            house.cash -= 20
            house.food += 10
            house.cat_food += 10
            self.satiety_grade -= 10
            print('{} покупает продукты.'.format(self))

    def buy_fur_coat(self, house):
        if house.cash >= 350:
            house.cash -= 350
            house.bought_fur_coats += 1
            self.happiness_grade += 60
            self.satiety_grade -= 10
            print('{} покупает шубу.'.format(self))

    def clean_house(self, house):
        if house.dirt >= 100:
            house.dirt -= 100
        else:
            house.dirt = 0
        self.satiety_grade -= 10
        print('{} убирается в доме.'.format(self))

    def life_day(self, house):

        if self.satiety_grade <= 30:
            if not self.to_eat(house):
                self.buy_products(house)

        elif house.dirt > 90:
            self.clean_house(house)
        elif self.happiness_grade <= 10:
            self.buy_fur_coat(house)
        else:
            self.buy_products(house)
