from human import Human


class Husband(Human):

    def __str__(self):
        return 'Муж - {}'.format(self.name)

    def to_play(self):
        self.happiness_grade += 20
        self.satiety_grade -= 10
        print('{} гоняет в игрушки.'.format(self))

    def to_work(self, house):
        self.satiety_grade -= 10
        house.cash += 150
        house.money_earned += 150
        print('{} работает в поте лица.'.format(self))

    def life_day(self, house):

        if self.satiety_grade <= 30:
            if not self.to_eat(house):
                self.to_work(house)

        elif self.happiness_grade <= 10:
            self.to_play()
        else:
            self.to_work(house)
