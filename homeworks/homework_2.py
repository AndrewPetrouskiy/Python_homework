# Task 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def find_sum_all_figures(num, len_n):
    new_num = 0
    int_num = num * 10 ** (len_n - 1)
    while int_num > 0:
        new_num += int_num % 10
        int_num //= 10
    return int(new_num)


# number = input("Enter the real number ")
# len_num = len(number)
# number = float(number)
#
# sum_all_figures = find_sum_all_figures(number, len_num)
# print(f"The sum all figures from {number} equals {sum_all_figures}")

# Task 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def find_multiply_all_numbers(num):
    ls = list()
    a = 1
    for i in range(1, num + 1):
        a *= i
        ls.append(a)
    return ls


# number = int(input("Enter the number N "))
# multiply_all_num = find_multiply_all_numbers(number)
# print(f"{multiply_all_num} it's !N all range from {number}")


# Task 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

def fill_array_with_formula(num):
    arr = list()
    a = 1
    for i in range(1, num + 1):
        a = round((1 + 1 / i) ** i)
        arr.append(a)
    return arr


def find_sum_all_figures_in_array(arr):
    sum_elements = 0
    for i in array:
        sum_elements += i
    return sum_elements


# number = int(input("Enter the number N "))
# array = fill_array_with_formula(number)
# print(array)
# sum_all_figures = find_sum_all_figures_in_array(array)
# print(sum_all_figures)

# Task 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов,
# заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).


# def fill_array(num):
#     arr = list()
#     for i in range(-num, num + 1):
#         arr.append(i)
#     return arr


def find_multiply_two_elements(arr, pos_1, pos_2):
    multiply = arr[pos_1 - 1] * arr[pos_2 - 1]
    return multiply


# position_one = int(input("Enter the first position "))
# position_two = int(input("Enter the second position "))
# number = int(input("Enter the number N "))
#
# array = fill_array(number)
# print(array)
# multiply_two_numbers = find_multiply_two_elements(array, position_one, position_two)
# print(multiply_two_numbers)


# Task 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random. 10
import random


# def fill_array(num):
#     arr = []
#     for i in range(num):
#         arr.append(i)
#     return arr

# number = int(input("Enter the length of array "))
# array = fill_array(number)
# print(array)
# sort_array = sorted(array, key=lambda *args: random.random())
# print(sort_array)





#==================================================================================================================
#===================== Teacher's solution==========================================================================



# 1. Напишите программу, которая принимает на вход вещественное число
#    и показывает сумму его цифр. Без работы с методами строк.

num = float(input())
sum_digits = 0

power = len(str(num)) - 2
num *= 10 ** power

while num:
    sum_digits += num % 10
    num //= 10

print(int(sum_digits))



# 2. Напишите программу, которая принимает на вход число N 
#    и выдает набор произведений чисел от 1 до N в виде списка. 
#    1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.

num = int(input())
sum_dig = 1

for i in range(num):
    sum_dig *= i + 1
    print(sum_dig, end=", ")



# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

num = int(input())
sum_nums = 0
list_nums = []

for i in range(1, num + 1):
    result = round((1 + 1 / i) ** i, 3)
    list_nums.append(result)
    sum_nums += result

print(list_nums)
print(sum_nums)


# 4. * Напишите программу, которая принимает на вход 2 числа.
#      Получите значение N, для пустого списка, заполните числами
#      в диапазоне [-N, N]. Найдите произведение элементов
#      на указанных позициях(не индексах).

num = int(input("Enter the value of N: "))
n_1 = int(input("Position one: "))
n_2 = int(input("Position two: "))

nums_list = list(range(-num, num + 1))

print(nums_list)
len_list = len(nums_list)

if len_list >= n_1 > 0 and len_list >= n_2 > 0:
    print(nums_list[n_1 - 1] * nums_list[n_2 - 1])
else:
    print("There are no values for these indexes!")





    # 5. **Реализуйте алгоритм перемешивания списка.
#    Без функции shuffle из модуля random.

from random import randrange

num = int(input())
nums_list = list(range(num))
res_list = []

print(nums_list)

for i in range(num):
    n_1, n_2 = randrange(num), randrange(num)
    nums_list[n_1], nums_list[n_2] = nums_list[n_2], nums_list[n_1]

print(nums_list)