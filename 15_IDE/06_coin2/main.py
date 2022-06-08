import math


print('Введите координаты монетки: ')
x = float(input('Введите x: '))
y = float(input('Введите y: '))
r = float(input('Введите радиус: '))


r_xy = math.sqrt(x ** 2 + y ** 2)
if r_xy <= r:
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')
