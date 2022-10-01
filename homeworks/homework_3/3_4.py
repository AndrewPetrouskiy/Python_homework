# Task 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform


def get_positive_int():
    while True:
        try:
            reply = int(input("Enter a positive number ... "))
            if reply > 0:
                return reply
            else:
                print("This number isn't positive")
        except:
            print("Not a number... Try again")


def fill_array_real_numbers(num):
    new_array = []
    array = [uniform(0, 10) for i in range(num)]
    print(array)
    for i in array:
        temp = i % 1
        new_array.append(round(temp, 2))
    print(new_array)
    return new_array


def find_difference_between_max_and_min(arr):
    new_arr = sorted(arr)
    return round(new_arr[-1] - new_arr[0], 2)

# it's the second solution to this task

# def find_difference_between_max_and_min(arr):
#     max = arr[0]
#     min = arr[0]
#     for i in arr:
#         if i > max:
#             max = i
#         if i < min:
#             min = i
#     return max - min


number = get_positive_int()
array = fill_array_real_numbers(number)
difference = find_difference_between_max_and_min(array)
print(f"{difference} it's the difference between max and min value in the array")
