friends_amount = int(input('Кол-во друзей: '))
debit_amount = int(input('Долговых расписок: '))
debit_list = []

for _ in range(friends_amount):
    debit_list.append(0)

for debit in range(debit_amount):
    print('\n' + str(debit + 1) + '-я расписка')
    to_number = int(input('Кому: '))
    from_number = int(input('От кого: '))
    amount = int(input('Сколько: '))
    debit_list[to_number - 1] -= amount
    debit_list[from_number - 1] += amount

print('\nБаланс друзей:')
for friend in range(len(debit_list)):
    print(friend + 1, end = '')
    print(':', debit_list[friend])