amount = int(input('Введите количество заказов: '))
order_dict = dict()

for count in range(amount):
    order = input(f'{count + 1}-й заказ: ').split()

    if order[0] in order_dict:
        order_dict[order[0]].update({})

        if order[1] in order_dict[order[0]]:
            order_dict[order[0]][order[1]] += int(order[2])
        else:
            order_dict[order[0]][order[1]] = int(order[2])

    else:
        order_dict[order[0]] = {}

        if order[1] in order_dict[order[0]]:
            order_dict[order[0]][order[1]] += int(order[2])
        else:
            order_dict[order[0]][order[1]] = int(order[2])
print()

for key in sorted(order_dict):
    print(f'{key}:')
    for j_key in sorted(order_dict[key]):
        print(f'\t\t{j_key}: {order_dict[key][j_key]}')



