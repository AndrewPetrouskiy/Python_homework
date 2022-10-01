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
