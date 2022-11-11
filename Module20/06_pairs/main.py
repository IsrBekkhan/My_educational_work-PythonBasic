import random
origin_list = [random.randint(0, 10) for _ in range(10)]
print('Оригинальный список:', origin_list)

# Способ 1:
print('Новый список:', [(origin_list[index], origin_list[index + 1]) for index in range(0, 10, 2)])


# # Способ 2:
# new_list = []
#
# for index, value in enumerate(origin_list):
#
#     if not index % 2 == 1:
#         pair = (origin_list[index], origin_list[index + 1])
#         new_list.append(pair)
#
# print('Новый список:', new_list)


# # Способ 3:
# origin_1 = [origin_list[index] for index in range(0, 10, 2)]
# origin_2 = [origin_list[index] for index in range(1, 11, 2)]
# new_list = list(zip(origin_list, origin_2))
#
# print('Новый список:', new_list)

