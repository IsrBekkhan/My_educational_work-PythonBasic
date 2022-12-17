from husband import *


class Child(Husband):

    def __str__(self):
        return 'Ребёнок - {}'.format(self.name)

    def to_eat(self, house):
        if house.food >= 10:
            house.food -= 10
            house.food_eaten += 10
            self.satiety_grade += 1
            print('{} кушает.'.format(self))
            return True

    def to_sleep(self):
        self.satiety_grade -= 10
        print('{} спит.'.format(self))

    def to_work(self):
        pass

    def life_day(self, house):

        if self.satiety_grade <= 10:
            if not self.to_eat(house):
                self.to_sleep()

        elif self.happiness_grade <= 10:
            self.to_play()
        else:
            self.to_sleep()
