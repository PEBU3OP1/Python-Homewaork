# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# import random
# def polynomial(k):
#     polynominal = f" {str(random.randint(0, 100))} * (x ** {str(k)})"
#     for i in range(k-1, 0, -1):
#         polynominal = polynominal + f" + {str(random.randint(0, 100))} * (x ** {str(i)})"
#     polynominal = polynominal + f" + {random.randint(0, 100)}"
#     polynominal = polynominal.replace("x ** 1", "x")
#     print(polynominal)
# polynomial(4)

# def polynomial(k):
#     polynom = [x for x in range(k, 0, -1)]
#     polynom = list(map(lambda x: f"{random.randint(0, 100)} * (x ** {str(x)})", polynom))
#     polynom = (" + ".join(polynom)).replace("x ** 1", "x") + " + " + str(random.randint(0, 100))
#
#     return polynom
#
# print(polynomial(10))