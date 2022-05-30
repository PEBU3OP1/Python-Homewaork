# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#
# Пример:
#
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# def summa_nechetnyh(spisok):
#     i = 1
#     summa = 0
#     while i < len(spisok):
#         summa += spisok[i]
#         i += 2
#     return summa
#
# print(summa_nechetnyh([2, 3, 5, 9, 3, 4, 5]))

# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Если остается 1 элемент без пары - умножаем его самого на себя.
#
# Пример:
#
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
# import math
# def proizved_par (spisok):
#     new_list = []
#     for i in range(math.ceil(len(spisok)/2)):
#         new_list.append(spisok[i]*spisok[-i-1])
#     return new_list
#
# print(proizved_par([2, 3, 4, 5, 6]))


# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# def subtraction_max_min (spisok):
#     for i in range(len(spisok)):
#         spisok[i] = round(float(spisok[i]) - int(spisok[i]), 3)
#     spisok.sort()
#     res = spisok[-1] - spisok[0]
#     return res
#
# print(subtraction_max_min([1.1, 1.2, 3.1, 5.2, 10.01, 0.001]))