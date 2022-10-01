# Task 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# т.к. нельзя использовать строки, то придетсянемного повозиться.

from array import array


def get_int():
    while True:
        try:
            reply = int(input("Enter the number "))
            return reply
        except:
            print("Not a number... Try again")


def translate_into_binary(num):
    new_array = []
    while num > 0:
        new_array.append(num % 2)
        num //= 2
    new_array = new_array[::-1]
    for i in new_array:
        print(i, end="")


number = get_int()
translate_into_binary(number)
print(f" is a binary code of number {number}")
