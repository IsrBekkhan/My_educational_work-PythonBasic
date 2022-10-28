shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

component = input('Название детали: ')
count_components = 0
total_price = 0
for index in range(len(shop)):
        if component == shop[index][0]:
                count_components += 1
                total_price += shop[index][1]

print('Кол-во деталей —', count_components)
print('Общая стоимость —', total_price)

