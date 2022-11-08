amount = int(input('Введите количество человек: '))
human_dict = dict()

for count in range(amount - 1):
    human_name = input(f'{count + 1}-я пара: ').split()

    if human_name[1] in human_dict:
        human_dict[human_name[1]].append(human_name[0])
    else:
        human_dict[human_name[1]] = [human_name[0]]

genelogical_dict = dict()

for father in human_dict:
    find = False
    for key in human_dict:
        sons_list = human_dict[key]
        if father in sons_list:
            genelogical_dict[father] = 1 + genelogical_dict.get(key, 0)
            find = True
            break

    if not find:
        genelogical_dict[father] = 0

for father_2 in human_dict:
    sons_list_2 = human_dict[father_2]
    for son in sons_list_2:
        if not son in genelogical_dict:
            genelogical_dict[son] = 1 + genelogical_dict.get(father_2, 0)

print('\n«Высота» каждого члена семьи:')
for key in sorted(genelogical_dict):
    print(key, genelogical_dict[key])


