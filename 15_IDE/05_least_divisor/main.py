def get_min_divider(a):
 min_divider = 1
 for i in range(1, a + 1):
  if a % i == 0:
   min_divider = i
  if min_divider > 1:
   break
 return min_divider

number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', get_min_divider(number))
