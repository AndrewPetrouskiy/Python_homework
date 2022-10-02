# Task 4.* Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.

from random import randint, choices


# тут мы и проверяем на 0 и на отрицательные числа, чтобы не выдавать список.
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


def fill_array(number):
    array = []
    for i in reversed(range(0, number+1)):
        k = randint(0, 10)
        if k == 0:
            continue
        elif i == 0:
            array.append(f"{k}")
        else:
            array.append(f"{k}*x^{i}")
            temp = choices("+-", k=1)
            array.append("".join(temp))
    array.append("= 0")
    return array

for i in range(3):
    number = get_positive_int()
    array = fill_array(number)
    with open("polynom.txt", "a", encoding="utf-8") as text:
        text.write(f"{' '.join(array)}\n")
