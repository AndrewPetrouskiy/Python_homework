# Task 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.


from random import randint


def get_positive_int() -> int:
    while True:
        try:
            reply = int(input("Enter how many elements must be in the list ... "))
            if reply > 0:
                return reply
            else:
                print("This number isn't positive")
        except:
            print("Not a number... Try again")

def fill_list(num: int) -> list:
    return [randint(-100 , 100) for i in range(num)]


def find_max_value(array: list) -> list:
    return [array[i] for i in range(1, len(array)) if array[i] > array[i - 1]]

source_list = fill_list(get_positive_int())
print(source_list)
sorted_list = find_max_value(source_list)
print(sorted_list)


