import random

team_1 = [round(random.uniform(0, 10), 2) for _ in range(10)]
team_2 = [round(random.uniform(0, 10), 2) for _ in range(10)]

team_3 = [team_1[index] if team_1[index] > team_2[index]
          else team_2[index]
          for index in range(10)]

print('Первая команда:', team_1)
print('Вторая команда:', team_2)
print('Победители тура:', team_3)