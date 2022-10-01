# Task 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


from random import randint, sample


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


def find_multiply_numbers(array):
    index = -1
    new_array = []
    len_arr = len(array)
    if len(array) % 2 == 1:
        for i in range(len_arr):
            if i == len_arr // 2:
                new_array.append(array[i])
                break
            else:
                new_array.append(array[i] * array[index])
                index -= 1
    else:
        for i in range(len_arr):
            if i == len_arr // 2:
                break
            else:
                new_array.append(array[i] * array[index])
                index -= 1
    return new_array


number = get_positive_int()
array = fill_array(number)
multiply_numbers = find_multiply_numbers(array)
print(f"{multiply_numbers} is multiply of two elements of array as the multiply is the first and last elements and etc.")
