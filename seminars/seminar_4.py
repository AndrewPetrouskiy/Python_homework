# Task 1. Задайте строку из набора чисел. Напишите программу,
# #    которая покажет большее и меньшее число.
# #    В качестве символа-разделителя используйте пробел.

# new_string = input(" Enter the string from numbers with spaces ")

def check_correct_num(list_string):
    for i in list_string:
        if not i.replace("-", "").isdigit():
            return []
        return list_string


# print(check_correct_num(input().split))

def min_sum(val):
    art = check_correct_num(val)

    if art:
        return min(art, key=int), max(art, key=int)
    else:
        return []


print(min_sum(input().split()))


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
#    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
#    Уравнения и корни запишите в файл.


# from math import sqrt
# from random import randint



# a = randint(-100, 100)
# b = randint(-100, 100)
# c = randint(-100, 100)




# d = b ** 2 - 4 * a * c
# with open("temp.txt", "a", encoding="utf-8") as text:
#     text.write(f"{a}*x^2 + {b}*x + {c}\n")
#     if d > 0 and a:
#         x1 = (-b + sqrt(d)) / (2 * a)
#         x2 = (-b - sqrt(d)) / (2 * a)
#         text.write(f"x1 = {x1} , x2 = {x2}\n")
#     elif d == 0:
#         x = -b / (2 * a)
#         text.write(f"{x}\n")
#     else:
#         text.write("Корней нет\n")





# Task 3. Задайте два числа. Напишите программу, которая найдёт
# #    НОК (наименьшее общее кратное) этих двух чисел.

# from math import gcd
#
# def nok(first, second):
#     return (first * second) // gcd(first , second)
#
# a = int(input("a = "))
# b = int(input("b = "))
#
# print(nok(a, b))
#