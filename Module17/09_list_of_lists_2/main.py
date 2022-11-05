nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [nice_list[index // 9][(index // 3) % 3][index % 3] for index in range(18)]

print(new_list)
