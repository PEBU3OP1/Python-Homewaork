
# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

# def Weekend (day):
#     dayoff = abs(day) % 7
#     if dayoff == 6:
#         print('Да, это суббота')
#     elif dayoff == 0:
#         print('Да, это воскресенье')
#     else:
#         print('Нет!')
#
# day = int(input('Введите день: '))
# Weekend(day)
# 2. Напишите программу, которая принимает на вход координаты точки (X и Y),
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# def Getquart (xPoint, yPoint):
#     if (xPoint > 0 and yPoint > 0):
#         return 'Первая четверть'
#     if (xPoint < 0 and yPoint > 0):
#         return 'Вторая четверть'
#     if (xPoint < 0 and yPoint < 0):
#         return 'Третья четверть'
#     if (xPoint > 0 and yPoint < 0):
#         return 'Четвертая четверть'
#     if (xPoint == 0 or yPoint == 0):
#         return 'Точка находится на оси'
# def GetValues ():
#     x = int(input('Введите координаты точки по X: '))
#     y = int(input('Введите координаты точки по Y: '))
#     return x, y
#
# x, y = GetValues()
# print(Getquart(x,y))

# 3. Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

# def GetQuartVal (quart):
#     if quart == 1:
#         return 'Первая четверть, диапапзон координат: X > 0, Y > 0'
#     if quart == 2:
#         return 'Вторая четверть, диапапзон координат: X < 0, Y > 0'
#     if quart == 3:
#         return 'Третья четверть, диапапзон координат: X < 0, Y < 0'
#     if quart == 4:
#         return 'Четвертая четверть, диапапзон координат: X > 0, Y < 0'
#     else:
#         return 'Ошибка! Значение от 1 до 4!!'
#
# x = int(input('Введите четверть: '))
# print(GetQuartVal (x))




# 4. Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.

# def Rasst2D(xA, yA, xB, yB):
#     rasst = round(((xA - xB)**2 + (yA - yB)**2)**0.5, 3)
#     return rasst
#
# xA = int(input('Введите координаты A по X: '))
# yA = int(input('Введите координаты A по Y: '))
# xB = int(input('Введите координаты B по X: '))
# yB = int(input('Введите координаты B по Y: '))
#
# print(Rasst2D(xA, yA, xB, yB))

