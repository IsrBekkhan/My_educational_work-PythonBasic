from husband import *
from wife import *
from cat import *
from house import *
from child import *


def day_in_house(house):

    for creature in house.tenants:
        creature.life_day(house)
        creature.is_alive(house)
        house.house_pollution()
    return 1


def print_resume(house, days):
    print('\nВ доме прожито {} дней.'.format(days))

    if len(house.tenants) == 0:
        print('Все жильцы в доме умерли.')
    else:
        for human in our_house.tenants:
            print(human, end='; ')

    print('Заработано денег: {} рублей \nСъедено еды: {}\nКуплено шуб: {} штук'.format(
        house.money_earned, house.food_eaten, house.bought_fur_coats
    ))


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

    if len(our_house.tenants) > 0:
        print('\nДень {}-й:'.format(total_days + 1))
        total_days += day_in_house(our_house)
    else:
        print_resume(our_house, total_days)
        break
else:
    print_resume(our_house, total_days)
