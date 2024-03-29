# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# import random
# def guarantee_not_zero():
#     a = random.randint(0, 100)
#     while a == 0:
#         a = random.randint(0, 100)
#     return a
#
#
# def polynomial(k):
#     polynominal = f" {str(guarantee_not_zero())} * (x ** {str(k)})"
#     for i in range(k-1, 0, -1):
#         polynominal = polynominal + f" + {str(guarantee_not_zero())} * (x ** {str(i)})"
#     polynominal = polynominal + f" + {guarantee_not_zero()} = 0"
#     polynominal = polynominal.replace("x ** 1", "x")
#     print(polynominal)
#
# polynomial(4)


# def polynomial(k):
#     polynom = [x for x in range(k, 0, -1)]
#     polynom = list(map(lambda x: f"{random.randint(1, 100)} * (x ** {str(x)})", polynom))
#     polynom = (" + ".join(polynom)).replace("x ** 1", "x") + " + " + str(random.randint(1, 100)) + " = 0"
#
#     return polynom
#
# print(polynomial(4))

# Это 3 интерпретация задачи 33 с проверкой для ген 0. Извините)))
# def polynomial(k):
#     rnd = random.randint(0, 100)
#     if rnd:
#         polynominal = f" {str(rnd)} * (x ** {str(k)})"
#     else:
#         polynominal = ""
#
#     for i in range(k-1, 0, -1):
#         rnd = random.randint(0, 100)
#         if rnd:
#             if polynominal == "":
#                 polynominal = polynominal + f" {str(rnd)} * (x ** {str(i)})"
#             else:
#                 polynominal = polynominal + f" + {str(rnd)} * (x ** {str(i)})"
#         else:
#             pass
#     rnd = random.randint(0, 100)
#     if rnd:
#         polynominal = polynominal + f" + {rnd} = 0"
#     else:
#         pass
#     polynominal = polynominal.replace("x ** 1", "x")
#     print(polynominal)
#
# polynomial(4)


# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

# def get_info_from_file():
#     data = open("Homework 5.txt", 'r')
#     list_from_data = data.read()
#     list_from_data = list(map(int, list_from_data.split()))
#     data.close()
#     return list_from_data
#
# def get_back_missing_digit(data):
#     for i in range(len(data)-1):
#         if data[i + 1] - data[i] > 1:
#             data.insert(i+1, data[i]+1)
#             print(f"Не хватает {data[i]+1}")
#             return data
# print(get_back_missing_digit(get_info_from_file()))


# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# from collections import Counter
# def get_unique_el(lst):
#     count = Counter(lst)
#     return [x for x in lst if count.get(x) == 1]
#
# print(get_unique_el([1, 2, 3, 5, 1, 5, 3, 10, 10, 12, 14]))