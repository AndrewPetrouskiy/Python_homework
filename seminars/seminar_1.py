# Task 1

# def check_square(a, b):
#     if a == b**2:
#         print(f"number {a} is a square of number {b}")
#     elif b == a**2:
#         print(f"number {b} is a square of number {a}")
#     else:
#         print("No one number doesn't equal square another number")
#
# number_a = int(input("Enter number a "))
# number_b = int(input("Enter number b "))
#
# check_square(number_a, number_b)

# Task 2

# max_number = 0
#
# for i in range(5):
#     a = int(input("Enter the positive number"))
#     if max_number < a:
#         max_number = a
#
# print(max_number)

# Task 3

# number = int(input("Enter the number "))
# print(*list(range(-number, number)))

# Task 4

# number = float(input(("Enter the real number")))
#
# number = number * 10 % 10
#
# if number != 0:
#     print(int(number))
# else:
#     print("No")

# Task 5

# num = int(input("Enter the number "))
#
# if (num % 5 == 0 and num % 10 or num % 15) and num % 30 != 0:
#     print(f"{num} is True number")
# else:
#     print(f"{num} isn't True number")

# Task 6

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not(x == z or x <= y and z):
#                 print(x, y, z)


for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x and not y and not z):
                print(x, y, z)