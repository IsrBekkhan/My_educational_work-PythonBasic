import math
def scaner(x, y, r):
    hypotenus = math.sqrt(x**2 + y**2)
    if hypotenus > r:
        print('Монетки в области нет')
    else:
        print('Монетка где-то рядом')

print('Введите координаты монетки:')
coord_X = float(input('X: '))
coord_Y = float(input('Y: '))
radius = float(input('Введите радиус: '))
scaner(coord_X, coord_Y, radius)
