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






#============================== Teacher's solution==============================================


# 4. * Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
#      Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform


def list_rand_nums(count: int):
    list_nums = []
    if count <= 0:
        print("Negative value of the number of numbers!")
        return [0.0]

    for i in range(count):
        list_nums.append(round(uniform(1, count), 2))
    return list_nums


def dif_max_min(list_nums: list):
    num_max = num_min = list_nums[0] % 1

    for k in range(1, len(list_nums)):
        num = round(list_nums[k] % 1, 2)
        if num > num_max:
            num_max = num
        elif num < num_min:
            num_min = num

    result = round(num_max - num_min, 2)
    print(f"Min: {num_min}, Max: {num_max}. Difference: {result}")
    return result


all_list = list_rand_nums(int(input("Number of numbers: ")))
print(all_list)
print(dif_max_min(all_list))