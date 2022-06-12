from Homework5 import get_info_from_file

lst1 = get_info_from_file("Polynom1.txt")
lst2 = get_info_from_file("Polynom2.txt")
print(lst1)
for i in range(len(lst1)):
    if lst1[i] == "+":
        print(lst1[i-1])
