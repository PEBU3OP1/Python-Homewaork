# 34. Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.


# from Homework5 import get_info_from_file
# from Homework5 import polynomial
# from Homework5 import working_with_files
#
# lst1 = get_info_from_file("Polynom1.txt")
# lst2 = get_info_from_file("Polynom2.txt")
#
# def replacing1(lst):
#     rate_polynom= []
#     for i in lst:
#         if i != "+" and i != "0" and i != "=":
#             i = i.replace("*(x**2)","")
#             i = i.replace("*(x)","")
#             rate_polynom.append(i)
#     return rate_polynom
#
# def summ_of_polynom(lst1, lst2):
#     lst1 = list(map(int, lst1))
#     lst2 = list(map(int, lst2))
#     result = list(map(sum, zip(lst1, lst2)))
#     return result
#
#
#
#
# working_with_files("Result.txt", "w", polynomial(summ_of_polynom(replacing1(lst1), replacing1(lst2))))


# 39, если не делали. Подумать над обработкой пользовательского ввода

# def sweets_game (sweets):
#     current_user = 1
#     print(f"Осталось конфет: {sweets}")
#     while sweets != 0:
#
#         while True:
#             user_sweets = input(f"Игрок {current_user}: введите количество конфет ")
#             if not user_sweets.isdigit():
#                 print("Только цифры!")
#                 continue
#             if int(user_sweets) not in range (1, 29) or int(user_sweets) > sweets:
#                 print("Количество неправильно!")
#                 continue
#             else:
#                 user_sweets = int(user_sweets)
#                 break
#
#         sweets = sweets - user_sweets
#         print(f"Осталось конфет: {sweets}")
#         if current_user == 1:
#             current_user = 2
#         else:
#             current_user = 1
#
#
#     print(f"Выиграл: Игрок {current_user}")
# sweets_game(50)
