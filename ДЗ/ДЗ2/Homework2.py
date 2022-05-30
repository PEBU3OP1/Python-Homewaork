#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# (отсекаем минус, считаем все в плюс).
#
# Пример:
#
# 67,82 -> 23
# 0,56 -> 11

# def Sum_digtis(n):
#     summa = 0
#     for i in str(n):
#         if i.isdigit():
#             summa = summa + int(i)
#     return summa
#
#
# print(Sum_digtis(0.56))

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

# def fib(n):
#     if n in (1, 2):
#         return n
#     else:
#         return fib(n-1) * n
# n = int(input("Введите n: "))
# dictt = []
# for i in range(1, n+1):
#     dictt.append(fib(i))
# print(dictt)

