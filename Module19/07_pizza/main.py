amount = int(input('Введите количество заказов: '))
order_dict = dict()

for count in range(amount):
    order = input(f'{count + 1}-й заказ: ').split()
    customer = order[0]
    pizza_name = order[1]
    count = int(order[2])

    if customer in order_dict:

        if pizza_name in order_dict[customer]:
            order_dict[customer][pizza_name] += count
        else:
            order_dict[customer][pizza_name] = count

    else:
        order_dict[customer] = {pizza_name: count}

print()

for key in sorted(order_dict):
    print(f'{key}:')
    for j_key in sorted(order_dict[key]):
        print(f'\t\t{j_key}: {order_dict[key][j_key]}')



