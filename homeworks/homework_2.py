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