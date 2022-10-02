# Task 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
from random import randint


def get_positive_int():
    while True:
        try:
            reply = int(input("Enter how many elements must be in list "))
            if reply > 0:
                return reply
            else:
                print("This number isn't positive")
        except:
            print("Not a number... Try again")


def fill_array(num):
    array = []
    for i in range(num):
        array.append(randint(-10, 10))
    return array


def get_unique_numbers(array):
    unique = []
    for i in array:
        if array.count(i) > 1:
            continue
        else:
            unique.append(i)
    return unique


number = get_positive_int()
array = fill_array(number)
unique_numbers = get_unique_numbers(array)
print(f"{unique_numbers} are the unique elements in list {array}")
