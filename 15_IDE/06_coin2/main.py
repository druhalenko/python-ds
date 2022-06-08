def find_monetka(c1, c2, r):
 if c1 <= r and c2 <= r:
  print('Монетка где-то рядом')
 else:
  print('Монетки рядом нет')

print('Введите координаты монетки: ')
x = float(input("Введите x: "))
y = float(input("Введите y: "))
r = int(input("Введите радиус : "))

find_monetka(x, y, r)
