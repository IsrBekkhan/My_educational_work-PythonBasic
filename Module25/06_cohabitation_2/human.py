class Human:
    satiety_grade = 30
    happiness_grade = 100

    def __init__(self, name):
        self.name = name

    def to_eat(self, house):
        if house.food >= 30:
            house.food -= 30
            house.food_eaten += 30
            self.satiety_grade += 1
            print('{} кушает.'.format(self))
            return True

    def pet_cat(self):
        self.happiness_grade += 5
        self.satiety_grade -= 10
        print('{} гладит кота.'.format(self))

    def life_day(self):
        pass

    def is_alive(self, house):
        self.day_happiness(house)

        if self.satiety_grade < 0:
            print('{} умер от голода.'.format(self.name))
            house.tenants.remove(self)

        if self.happiness_grade < 10:
            print('{} умер от депрессии.'.format(self.name))
            house.tenants.remove(self)

    def day_happiness(self, house):
        if house.dirt > 90:
            print('У {} испортилось настроение.'.format(self.name))
            self.happiness_grade -= 10
