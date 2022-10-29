amount_skates = int(input('Кол-во коньков: '))
skates_list = []
for count in range(amount_skates):
    print('Размер', count + 1, end = '')
    skates = int(input('-й пары: '))
    skates_list.append(skates)

amount_human = int(input('\nКол-во людей: '))
human_list = []
for count in range(amount_human):
    print('Размер ноги', count + 1, end = '')
    foot_size = int(input('-го человека: '))
    human_list.append(foot_size)

total_human = 0

for size in human_list:
    for skates in skates_list:
        if size <= skates:
            total_human += 1
            skates_list.remove(skates)

print('\nНаибольшее кол-во людей, которые могут взять ролики:', total_human)
