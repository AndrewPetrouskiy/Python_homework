# Task 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import randint , sample


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

# def fill_array(num):
#     array = sample(range(num), num)
#     print(array)
#     return array


#делал не через sample, потому что через sample меньше разнообразие чисел
def fill_array(num):
    array = [randint(-10, 10) for i in range(num)]
    print(array)
    return array


def find_sum_in_odd_positions(array):
    return sum(array[::2])


number = get_positive_int()
array = find_sum_in_odd_positions(fill_array(number))
print(f"The sum all odd-numbered elements in array equals {array}")



#============================== Teacher's solution==============================================


# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая найдёт сумму элементов списка,
#    стоящих на нечётных позициях(не индексах).

from random import sample


def list_rand_nums(count: int):
    if count < 0:
        print("Negative value of the number of numbers!")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums


def sum_odd_pos(list_nums: list):
    sum_nums = 0
    for k in range(0, len(list_nums), 2):
        sum_nums += list_nums[k]
    return sum_nums


all_list = list_rand_nums(int(input("Number of numbers: ")))
print(all_list)
print(sum_odd_pos(all_list))
