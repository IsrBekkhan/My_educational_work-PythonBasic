from random import choice


class Unit:
    health = 100

    def __init__(self, name):
        self.name = name

    def kick(self, enemy):
        enemy.health -= 20


def fight(attacker, enemy):
    attacker.kick(enemy)
    print('{} ударил игрока {}(здоровье - {}).'.format(
        attacker.name, enemy.name, enemy.health
    ))

    if enemy.health <= 0:
        print('{} одержал победу!'.format(attacker.name))
        return True


warrior_1 = Unit('Воин 1')
warrior_2 = Unit('Воин 2')

while True:
    attacker = choice((warrior_1, warrior_2))
    if attacker == warrior_1:
        if fight(attacker, warrior_2):
            break
    else:
        if fight(attacker, warrior_1):
            break

print('Бой окончен.')

