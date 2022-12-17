from human import *


class Cat(Human):

    def __str__(self):
        return 'Кот - {}'.format(self.name)

    def to_eat(self, house):
        if house.cat_food >= 10:
            house.cat_food -= 10
            self.satiety_grade += 2
            print('{} кушает.'.format(self))
            return True

    def to_sleep(self):
        self.satiety_grade -= 10
        print('{} спит.'.format(self))

    def tear_wallpaper(self, house):
        house.dirt += 5
        self.satiety_grade -= 10
        print('{} дерёт обои.'.format(self))

    def pet_cat(self):
        pass

    def day_happiness(self):
        pass

    def is_alive(self, house):

        if self.satiety_grade < 0:
            print('{} умер от голода.'.format(self.name))
            house.tenants.remove(self)

    def life_day(self, house):

        if self.satiety_grade <= 10:
            if not self.to_eat(house):
                self.tear_wallpaper(house)

        elif self.happiness_grade <= 10:
            self.tear_wallpaper(house)
        else:
            self.to_sleep()
