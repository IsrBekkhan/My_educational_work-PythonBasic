from random import choice


class Card:

    def __init__(self, rank, lear):
        self.rank = rank
        self.lear = lear


class Deck:
    cards = []

    for lear in range(1, 5):
        for rank in range(1, 14):
            cards.append(Card(rank, lear))

    def take_from(self, card):
        self.cards.remove(card)


class Player:
    scores = 0

    def __init__(self, name):
        self.name = name
        self.having_cards = []

    def give_to(self, card):
        self.having_cards.append(card)

    def is_ace(self):
        for card in self.having_cards:
            if card.rank == 1:
                return True


def distributor(a_player, amount=1):

    for _ in range(amount):
        rand_card = choice(Deck().cards)
        Deck().take_from(rand_card)
        a_player.give_to(rand_card)
        a_player.scores += scores_calc(rand_card)

    print('{} взял карту в количестве {}.\n'.format(
        a_player.name, amount
    ))


def card_show(player):
    lears = {1: 'Червы', 2: 'Бубны', 3: 'Пики', 4: 'Трефы'}
    ranks = {1: 'Туз', 11: 'Валет', 12: 'Дама', 13: 'Король'}
    print('\nКарты в руках игрока {}:'.format(player.name))

    for index, card in enumerate(player.having_cards):
        if card.rank in ranks:
            rank = ranks[card.rank]
        else:
            rank = card.rank
        print('Карта №{}: {} {}'.format(
            index + 1, lears[card.lear], rank
        ))


def scores_calc(card):
    if card.rank in (11, 12, 13):
        return 10
    else:
        return card.rank


def scores_correct(*args):
    for player in args:
        if player.scores > 21:
            if player.is_ace():
                player.scores -= 1
                if player.scores > 21:
                    player.scores = 0
            else:
                player.scores = 0


def show_winner(player_1, player_2):
    card_show(player_2)
    if player_1.scores == player_2.scores:
        print('Ничья!')
    elif player_1.scores > player_2.scores:
        print('\nВыиграл {}. Количество очков {}'.format(player_1.name, player_1.scores))
    else:
        print('\nВыиграл {}. Количество очков {}'.format(player_2.name, player_2.scores))


user = Player('Пользователь')
computer = Player('Компьютер')

distributor(user, 2)
distributor(computer, 2)

while True:
    card_show(user)
    answer = input('\nВзять карту или остановиться?\n1 - взять, 0 - остановитсья: ')

    if answer == '1':
        distributor(user)
    elif answer == '0':
        scores_correct(user, computer)
        show_winner(user, computer)
        break
    else:
        print('Ошибка ввода. Повторите попытку')

print('Игра окончена!')
