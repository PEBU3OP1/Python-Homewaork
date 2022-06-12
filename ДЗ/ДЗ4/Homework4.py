# 1.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# def digits_to_bin(n):
#     result = ''
#     while n > 1:
#         result =result + str(n % 2)
#         n = n // 2
#     result = result + str(n)
#     print(result)
#
# digits_to_bin(3)

# def digits_to_bin(n):
#     n = bin(n)
#     return n[2:]
#
# print(digits_to_bin(3))

# 2.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def fibb_neg (n):
#     if n == -2:
#         return -1
#     if n == -1:
#         return 1
#     if n == 0:
#         return 0
#     else:
#         return fibb_neg(n+2) - fibb_neg(n+1)
#
# def fibb_pos (n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fibb_pos(n-2) + fibb_pos(n-1)
#
# number = int(input("ВВеди число: "))
# listt = []
#
#
# for i in range(0,(-number -1),-1):
#     listt.append(fibb_neg(i))
# listt = listt[::-1]
#
# for i in range(1, number+1):
#     listt.append(fibb_pos(i))
#
# print(listt)


# 3.Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.


# def max_min_digit(n):
#     n = list(map(int, n.split()))
#
#     return f"Максимальное значение {max(n)}, Минимальное значение {min(n)}"
#
# n = input("Введи цифры через пробел: ")
# print(max_min_digit(n))

# 4. Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# from math import gcd
# def nok(a, b):
#     nok = (a * b)//gcd(a, b)
#     return nok
#
# print(nok(10, 13))