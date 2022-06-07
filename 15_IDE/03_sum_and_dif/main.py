def func_summa(N):
 summa = 0
 while N > 0:
  num = N % 10
  summa = summa + num
  N = N // 10
 print('Сумма чисел:', summa)
 return summa

def func_count(N):
 count = 0
 while N > 0:
  count += 1
  N //= 10
 print('Количество цифр в числе:', count)
 return count


def res(summa, count):
 res = summa - count
 print('Разность суммы и количества цифр:', res)

N = int(input('Введите число: '))

summa = func_summa(N)
count = func_count(N)
res(summa, count)
