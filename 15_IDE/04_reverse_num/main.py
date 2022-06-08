def turn_numbers1(N):
    number = 0
    main_part = round(N, 1) // 1
    while main_part > 0:
     rest = main_part % 10
     main_part = main_part // 10
     number = number * 10
     number = number + rest
    return number


def turn_numbers2(N):
    number2 = 0
    residual_part = round(N - (N // 1), 2) * 100
    while residual_part > 0:
     rest = (round((N - (N // 1)), 2) * 100) % 10
     residual_part = residual_part // 10
     number2 = number2 + rest
     number2 = round(number2 * 10 - 0.1, 0)
     number2 = number2 / 100 - 0.01
    return number2


N1 = float(input("Введите первое вещественное число: "))
N2 = float(input("Введите второе вещественное число: "))


reverse_N1 = turn_numbers1(N1) + turn_numbers2(N1)
print("1ое число наоборот: ", reverse_N1)


reverse_N2 = turn_numbers1(N2) + turn_numbers2(N2)
print("2ое число наоборот: ", reverse_N2)


summ_reversed_num = reverse_N1 + reverse_N2
print("Сумма: ", summ_reversed_num)


