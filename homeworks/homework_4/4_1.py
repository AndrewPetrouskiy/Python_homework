# Task 1. Вычислить число c заданной точностью d
from decimal import Decimal


def get_number():
    while True:
        try:
            reply = input("Enter the number ")
            if float(reply):
                return reply
        except:
            print("Not a number... Try again")


def precision_of_number():
    while True:
        try:
            reply = int(input("Enter the number what the precision of the number must be "))
            if reply > 0:
                return "1." + "0" * reply
            else:
                print("This number isn't positive")
        except:
            print("Not a number... Try again")


print(Decimal(get_number()).quantize(Decimal(precision_of_number())))
