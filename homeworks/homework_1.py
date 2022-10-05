
# Task 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def define_day_of_the_week(num):
    if num == 6 or num == 7:
        print("it's a weekend")
    elif num > 7 or num < 1:
        print("This day of the week doesn't exist")
    else:
        print("It isn't a weekend. It's a workday")


# number = int(input("Enter the number between 1 and 7 "))
# define_day_of_the_week(number)

# Task 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not (x or y or z) == (not x and not y and not z):
#                 print(x, y, z)


# Task3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def check_quarter(x, y):
    quarter = 4
    if x > 0 and y > 0:
        quarter = 1
    elif x < 0 and y > 0:
        quarter = 2
    elif x < 0 and y < 0:
        quarter = 3
    print(f"The point is in the {quarter} quarter")


# x = int(input("Enter the X "))
# y = int(input("Enter the Y "))

# if x == 0 or y == 0:
#     print("You entered 0, you need to enter the coordinates X and Y which doesn't equal 0")
# else:
#     check_quarter(x, y)


# Task 4. Напишите программу, которая по заданному номеру четверти,показывает диапазон возможных координат точек в этой четверти (x и y)

def show_quarter(number):
    if number == 1:
        print("x > 0 & y > 0")
    if number == 2:
        print("x < 0 & y > 0")
    if number == 3:
        print("x < 0 & y < 0")
    if number == 4:
        print("x > 0 & y < 0")


# quarter = int(input("Enter the quadrant "))

# if quarter > 4 or quarter < 1:
#     print("You entered the wrond number. This quadrant doesn't exist")
# else:
#     show_quarter(quarter)


# Task 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def input_numbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        number = int(input(f"Enter the coordinate {xy[i]}: "))
        a.append(number)
    return a


def length_between_two_points(a, b):
    distance = round(((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5, 2)
    return distance


# print("Enter the coordinates' point А")
# point_A = input_numbers(2)
# print("Enter the coordinates' point В")
# point_B = input_numbers(2)

# print(length_between_two_points(point_A, point_B))



#==========================================================================================================================
#============ Teacher's answers============================================================================================

# Task 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# num = int(input())

# if 5 < num < 8:
#     print("Weekend")
# elif 0 < num < 6:
#     print("Workday")
# else:
#     print("It's not a day of the week!")


# Task 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x and not y and not z):
                print(x, y, z)


# Task3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).


x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:
    print("Error, 0 entered!")

# Task 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)

quarter = int(input())

if quarter == 1:
    print("x > 0, y > 0")
elif quarter == 2:
    print("x < 0, y > 0")
elif quarter == 3:
    print("x < 0, y < 0")
elif quarter == 4:
    print("x > 0, y < 0")
else:
    print("Error, wrong number!")


# Task 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())

print(f"{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5:0.4}")



